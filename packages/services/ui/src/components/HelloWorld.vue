<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <img v-if="photoList.length > 0" :alt="photoList[0].imageFileName" :src="`data:image/jpeg;base64,${photoList[0].base64Image}`">
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      photoList: []
    }
  },
  async mounted () {
    let photoResponse = await fetch('https://pvk066q1d9.execute-api.eu-west-2.amazonaws.com/test/rest/photos');
    const fullPhotoList = await photoResponse.json();
    
    this.photoList = fullPhotoList.photos;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
