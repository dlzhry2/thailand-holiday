<template>
    <div>
        <h1>{{photoObject.imageFileName}}</h1>
        <div v-if="loading">
            <LoadingSpinner/>
        </div>
        <div v-else class="container">
            <div class="tile-wrapper clickable">
                <div class="tile-content">
                    <div class="tile-text">
                        <img :src='`data:image/jpeg;base64,${this.photoObject.base64Image}`' :alt="this.photoObject.imageFileName"/>
                    </div>
                    <div>
                        {{this.photoObject.caption}} <br>
                        <span>Location: <a target="blank" :href="`http://maps.google.com/?q=${this.photoObject.location}`">{{this.photoObject.location}}</a></span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import LoadingSpinner from './general/LoadingSpinner.vue'

export default {
    name: 'ViewPhoto',
    components: {
        LoadingSpinner
    },
    data () {
        return {
            apiUrl: 'https://pvk066q1d9.execute-api.eu-west-2.amazonaws.com/test/rest/photos',
            photoObject: {},
            loading: false
        }
    }  ,
    async mounted () {
        this.loading = true;
        let photoResponse = await fetch(`${this.apiUrl}/${this.$route.params.key}`);
        this.photoObject = await photoResponse.json();

        this.loading = false;
    }     
};
</script>

<style scoped>
</style>
