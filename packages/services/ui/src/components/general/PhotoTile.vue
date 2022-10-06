<template>
  <div class="tile-wrapper clickable">
    <div class="tile-content">
      <div class="tile-text">
       <img :src='`data:image/jpeg;base64,${imgBase64}`' :alt="imgName"/>
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
    }
  },
};
</script>

<style scoped>
.tile-wrapper {
  width: 300px;
  height: 300px;
  border: 1.5px solid dimgrey;
  border-radius: 25px;
  transition: 0.3s;
}

.tile-wrapper:hover {
  background-color: whitesmoke;
}

.tile-content {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.tile-title {
  padding-bottom: 20px;
  font-size: 20px;
  font-weight: bold;
}

img {
    height: 260px;
    width: 260px;
    object-fit: cover;
}
</style>
