import { createApp } from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router'
import ComingSoon from './components/ComingSoon.vue'
import HomePage from './components/HomePage.vue'
import UploadPhoto from './components/UploadPhoto.vue'
import UploadStory from './components/UploadStory.vue'
import ViewPhoto from './components/ViewPhoto.vue'
import { createStore } from 'vuex'

const store = createStore({
    state () {
      return {
        filteredImages: [],
        fullImageList: [],
        storyCount: 0
      }
    },
    mutations: {
      updateFilteredImages (state, updated) {
        state.filteredImages = updated
      }
    }
  })

const routes = [
    {
        path: '/',
        redirect: '/home'
    },
    { path: '/home', component: HomePage },
    { path: '/upload-photo', component: UploadPhoto },
    { path: '/coming-soon', component: ComingSoon },
    { path: '/photo/:key', component: ViewPhoto },
    { path: '/upload-story', component: UploadStory }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
  })

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
