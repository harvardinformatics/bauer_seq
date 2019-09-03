<script>
export default {
  name: 'App',
  data: function () {
    return {
      drawer: null,
      menuVisible: true,
      expandSub: true
    }
  },
  methods: {
    toggleMenu () {
      this.menuVisible = !this.menuVisible
    }
  }
}

</script>
<template>
  <v-app id="inspire">
      <v-navigation-drawer v-model="drawer" fixed app>
        <v-list dense>
        <v-list-tile :to="{name:'analysis'}">
            <v-list-tile-action>
                <v-icon>home</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
                <v-list-tile-title>
                    Home
                </v-list-tile-title>
            </v-list-tile-content>
        </v-list-tile>
        <v-list-tile :to="{name:'runs'}">
            <v-list-tile-action>
                <v-icon>polymer</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
                <v-list-tile-title>
                    Runs
                </v-list-tile-title>
            </v-list-tile-content>
        </v-list-tile>
        <v-list-tile :to="{name:'analysis'}">
            <v-list-tile-action>
                <v-icon>input</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
                <v-list-tile-title>
                    Analysis
                </v-list-tile-title>
            </v-list-tile-content>
        </v-list-tile>
        </v-list>
    </v-navigation-drawer>
    <v-toolbar color="primary" fixed app>
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title>Bauer Sequencing Core</v-toolbar-title>
    </v-toolbar>
    <v-content>
        <v-container fluid>
            <router-view></router-view>
        </v-container>
    </v-content>
    <v-footer color="secondary" app>
        <span class="white--text">2018 The Presidents and Fellows of Harvard College.</span>
    </v-footer>
  </v-app>
</template>
