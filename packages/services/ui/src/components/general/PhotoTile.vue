<template>
  <div class="tile-wrapper clickable" v-on:click="navigateToPhoto(imgName)">
    <div class="tile-content">
      <div class="tile-text">
       <img :src='`data:image/jpeg;base64,${imgBase64}`' :alt="imgName"/>
      </div>
      <div class="tile-title">
        {{imgCaption}} <br>
        <span>Location: <a target="blank" :href="`http://maps.google.com/?q=${imgLocation}`">{{imgLocation}}</a></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContentTile",
  props: {
    imgBase64: {
      type: String,
      default: "Default Title",
    },
    imgName: {
      type: String,
      default: "Default Title",
    },
    imgCaption: {
      type: String,
      default: 'Default caption'
    },
    imgLocation: {
      type: String,
      default: 'Default location'
    },
    navigateToPhoto: {
      type: Function
    }
  }
};
</script>

<style scoped>
.tile-wrapper {
  width: 300px;
  height: 360px;
  border: 1.5px solid dimgrey;
  border-radius: 25px;
  transition: 0.3s;
}

.tile-wrapper:hover {
  background-color: whitesmoke;
  cursor: pointer;
}

.tile-content {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.tile-title {
  padding-top: 15px;
  padding-bottom: 15px;
  font-size: 15px;
  font-family: Arial, Helvetica, sans-serif;
}

img {
    height: 260px;
    width: 260px;
    object-fit: cover;
}
img:hover {
  cursor: auto;
}

span {
  font-size: 12px;
}

a {
  font-size: 12px;
}
</style>
