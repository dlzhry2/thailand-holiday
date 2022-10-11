<template>
    <div>
        <h1>Upload Story</h1>
        <div v-if="loading">
            <LoadingSpinner/>
        </div>
        <div v-else class="container">
            <form>
                <div class="form-group">
                    <input type="file" class="form-control-file" id="exampleFormControlFile1" accept="video/*" @change="retrieveVideoBytes">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="authToken">
                    <small v-if="error" id="error" class="form-text text-muted">{{error}}</small>
                </div>
                <button class="btn btn-primary" @click="submitVideo">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import LoadingSpinner from './general/LoadingSpinner.vue'

export default {
    name: 'UploadStory',
    components: {
        LoadingSpinner
    },
    data () {
        return {
            authToken: '',
            videoString: '',
            error: '',
            loading: false
        }
    },
    methods: {
        async retrieveVideoBytes (event) {
            if (!event.target || !event.target.files) {
                console.log('Something went wrong')
                return
            }

            const uploadedFile = event.target.files[0];

            const reader = new FileReader();

            reader.addEventListener("load", () => {
                this.videoString = reader.result;
            }, false);

            if (uploadedFile) {
                reader.readAsDataURL(uploadedFile);
            }
        },
        async submitVideo (e) {
            e.preventDefault();
            this.error = ''
            this.loading = true
            const requestPayload = {
                imageName: `z_story_${this.$store.state.storyCount + 1}.webm`,
                location: '',
                caption: '',
                base64Image: this.videoString.split(',')[1]
            }

            const response = await fetch('https://pvk066q1d9.execute-api.eu-west-2.amazonaws.com/test/rest/photos', {
                method: 'POST',
                headers: {
                    'x-thai-api-token': this.authToken
                },
                body: JSON.stringify(requestPayload)
            });

            if (response.status === 200) {
                this.$router.push({
                    path: '/home',
                    query: {
                        notification: 'story-success'
                    }
                })
            }

            // For now, this is the only failure we will handle
            if (response.status === 403) {
                this.error = 'Oops, the password you provided was incorrect'
            }

            this.loading = false
        }
    }
};
</script>

<style scoped>
h1 {
  padding-top: 20px;
  padding-bottom: 20px;
}
.container {
    display: flex;
}
.form-group {
    padding-top: 5px;
    padding-bottom: 5px;
}
form {
    margin: auto;
}
form label {
    font-size: 25px;
}
small {
    color: red !important;
}
</style>
