<template>
    <div>
        <nav class="navbar navbar-stickytop navbar-expand-lg navbar-light bg-light">
            <a id="main" class="navbar-brand" href="/#/home">Thailand 2k22</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-nav-bar" aria-controls="main-nav-bar" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="main-nav-bar">
                <ul class="navbar-nav mr-auto">
                    <li :class="$router.path === '/home' ? 'nav-item active' : 'nav-item'">
                        <a class="nav-link" href="/#/home">Home</a>
                    </li>
                    <li :class="$router.path === '/upload=photo' ? 'nav-item active' : 'nav-item'">
                        <a class="nav-link" href="/#/upload-photo">Upload photo</a>
                    </li>
                    <li :class="$router.path === '/coming-soon' ? 'nav-item active' : 'nav-item'">
                        <a class="nav-link" href="/#/coming-soon">Coming Soon</a>
                    </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" v-model="searchTerm">
                    <button class="btn btn-outline-success my-2 my-sm-0" @click="search" @keydown.enter="search">Search</button>
                </form>
            </div>
        </nav>
    </div>
</template>

<script>

export default {
    name: 'Main-Header',
    data () {
        return {
            searchTerm: ''
        }
    },
    methods: {
        search (event) {
            event.preventDefault();

            const results = this.$store.state.fullImageList.filter(this.containsString)
            this.$store.commit('updateFilteredImages', results)
        },
        containsString (imageObject) {
            const searchTerm = this.searchTerm.toLowerCase()
            if (
                imageObject.caption.toLowerCase().includes(searchTerm) ||
                imageObject.imageFileName.toLowerCase().includes(searchTerm) ||
                imageObject.location.toLowerCase().includes(searchTerm)
            ) {
                return true;
            }

            return false;
        }
    }
};
</script>

<style>
#main {
    font-size: 30px;
}
a {
    font-size: 20px;
}
button {
    font-size: 20px;
}
input {
    font-size: 20px
}
</style>
