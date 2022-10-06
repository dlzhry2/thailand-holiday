<template>
    <div>
        <h1>Upload Photo</h1>
        <div v-if="loading">
            <LoadingSpinner/>
        </div>
        <div v-else class="container">
            <form>
                <div class="form-group">
                    <input type="file" class="form-control-file" id="exampleFormControlFile1" accept=".jpg,.jpeg,.bmp,.png" @change="retrievePhotoBytes">
                </div>
                <div class="form-group">
                    <label for="exampleInputEmail1">Photo title</label>
                    <input type="text" class="form-control" id="exampleInputEmail1" placeholder="Enter title" maxlength="240" v-model="imageName" autocomplete="off">
                </div>
                <div class="form-group">
                    <label for="exampleInputEmail1">Location</label>
                    <input type="text" class="form-control" id="exampleInputEmail1" placeholder="Enter location" maxlength="300" v-model="location" autocomplete="off">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="authToken">
                    <small v-if="error" id="error" class="form-text text-muted">{{error}}</small>
                </div>
                <div class="form-group">
                    <label for="exampleFormControlTextarea1">Caption</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" maxlength="240" v-model="caption" autocomplete="off"></textarea>
                </div>
                <button class="btn btn-primary" @click="submitPhoto" :disabled="!caption || !location || !imageName">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import LoadingSpinner from './general/LoadingSpinner.vue'

export default {
    name: 'UploadPhoto',
    components: {
        LoadingSpinner
    },
    data () {
        return {
            caption: '',
            authToken: '',
            location: '',
            imageName: '',
            imageString: '',
            error: '',
            loading: false
        }
    },
    methods: {
        retrievePhotoBytes (event) {
            if (!event.target || !event.target.files) {
                console.log('Something went wrong')
                return
            }

            const uploadedFile = event.target.files[0]

            this.imageName = uploadedFile.name

            const reader = new FileReader();

            reader.addEventListener("load", () => {
                this.imageString = reader.result;
            }, false);

            if (uploadedFile) {
                reader.readAsDataURL(uploadedFile);
            }
        },
        async submitPhoto (e) {
            e.preventDefault();
            this.error = ''
            this.loading = true
            const requestPayload = {
                imageName: this.imageName,
                location: this.location,
                caption: this.caption,
                base64Image: this.imageString.split(',')[1]
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
                        notification: 'success'
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
