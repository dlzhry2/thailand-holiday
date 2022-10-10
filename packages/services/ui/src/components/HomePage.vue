<template>
  <div class="home-page">
    <div class="alert alert-success alert-dismissible fade show" role="alert" v-if="$route.query.notification === 'success'">
      <strong>Success:</strong> Your photo was added to our holiday album.
      <button type="button" class="close" data-dismiss="alert" aria-label="Close" @click="removeQueryParams">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <h1>{{ msg }}</h1>
      <div v-if="loading">
        <LoadingSpinner/>
      </div>
      <div v-else>
        <div v-if="photoList.length > 0" class="tiles">
          <PhotoTile
            v-for="photo in photoList"
            :key="photo.imageFileName + '-tile'"
            :imgBase64="photo.base64Image"
            :imgName="photo.imageFileName"
            :imgCaption="photo.caption"
            :imgLocation="photo.location"
            :navigateToPhoto="navigateToPhoto"
            class="tile"
          />
        </div>
      </div>
  </div>
</template>

<script>
import PhotoTile from './general/PhotoTile.vue'
import LoadingSpinner from './general/LoadingSpinner.vue'

export default {
  name: 'HomePage',
  components: {
    PhotoTile,
    LoadingSpinner
  },
  data () {
    return {
      msg: 'Our holiday in Thailand',
      photoList: [],
      loading: true,
      apiUrl: 'https://pvk066q1d9.execute-api.eu-west-2.amazonaws.com/test/rest/photos'
    }
  },
  watch: {
    '$store.state.filteredImages': function() {
      this.photoList = this.$store.state.filteredImages;
    }
  },
  async mounted () {
    let res = await fetch(this.apiUrl);
    const fullPhotoList = await res.json();
    
    this.photoList = await this.getAllPhotos(fullPhotoList.photos);
    this.$store.state.fullImageList = this.photoList;
    this.$store.commit('updateFilteredImages', this.photoList);
    this.loading = false
  },
  methods: {
    removeQueryParams () {
      this.$router.replace()
    },
    async fetchImage (imageKey) {
      let photoResponse = await fetch(`${this.apiUrl}/${imageKey}`);
      const parsedPhotoObject = await photoResponse.json();

      return parsedPhotoObject;
    },
    async getAllPhotos (photoKeys) {
      const allRequests = [];

      for (const key of photoKeys) {
        allRequests.push(this.fetchImage(key));
      }

      const photos = await Promise.all(allRequests);

      return photos;
    },
    navigateToPhoto (photoKey) {
      this.$router.push({
        path: `/photo/${photoKey}`
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  padding-top: 20px;
  padding-bottom: 20px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.tiles {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

.tile {
  margin-top: 10px;
}
</style>
