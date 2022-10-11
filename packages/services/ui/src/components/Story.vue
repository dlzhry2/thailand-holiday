<template>
  <div>
      <video controls width="400" v-on:ended="updateVideoSource" ref="videoContainer">
            <source ref="videoObjOne" :src="`data:video/webm;base64,${videoByteList[videoIdx]}`"
                    type="video/webm">

            <source ref="videoObjTwo" :src="`data:video/mp4;base64,${videoByteList[videoIdx]}`"
                    type="video/mp4">
        </video>
  </div>
</template>

<script>
export default {
  name: "UserStory",
  props: {
    storyList: {
      type: Array
    }
  },
  data () {
      return {
          videoByteList: [],
          videoIdx: 0
      }
  },
  mounted () {
      if (this.storyList.length < 1) {
          return;
      }

      for (const video of this.storyList) {
          this.videoByteList.push(video.base64Image);
      }
  },
  methods: {
      updateVideoSource () {
          if (this.videoIdx + 1 < this.storyList.length) {
              this.videoIdx = this.videoIdx + 1;
          } else if (this.videoIdx + 1 === this.storyList.length) {
              this.videoIdx = 0;
          }

          this.$refs.videoObjOne.src = `data:video/mp4;base64,${this.videoByteList[this.videoIdx]}`;
          this.$refs.videoObjTwo.src = `data:video/mp4;base64,${this.videoByteList[this.videoIdx]}`;

          this.$refs.videoContainer.load();
          this.$refs.videoContainer.play();
      }
  }
};
</script>

<style scoped>
</style>
