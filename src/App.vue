<script>
export default {
  name: 'App',
  data: function () {
    return {
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
  <div id="app" class="page-container">
    <md-app md-mode="reveal">
      <md-app-toolbar class="md-primary" md-elevation="0">
        <md-button class="md-icon-button" @click="toggleMenu" v-if="!menuVisible">
          <md-icon>menu</md-icon>
        </md-button>
        <span class="md-title">Bauer Core Sequencing Center</span>
      </md-app-toolbar>
      <md-app-drawer :md-active.sync="menuVisible"  md-persistent="mini" >
        <md-toolbar class="md-transparent" md-elevation="0">
          <span>Navigation</span>
          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button md-dense" @click="toggleMenu">
              <md-icon>keyboard_arrow_left</md-icon>
            </md-button>
          </div>
        </md-toolbar>
        <md-list>
          <md-list-item md-expand md-expanded>
            <md-icon>polymer</md-icon>
            <span class="md-list-item-text">Bauer</span>
            <md-list slot="md-expand">
              <md-list-item to="/runs">
                <span class="md-list-item-text">Runs</span>
              </md-list-item>
            </md-list>
          </md-list-item>

          <md-list-item>
            <md-icon>send</md-icon>
            <span class="md-list-item-text">Sent Mail</span>
          </md-list-item>

          <md-list-item>
            <md-icon>delete</md-icon>
            <span class="md-list-item-text">Trash</span>
          </md-list-item>

          <md-list-item>
            <md-icon>error</md-icon>
            <span class="md-list-item-text">Spam</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>
      <md-app-content>

    <router-view/>
      </md-app-content>
    </md-app>
  </div>

</template>

<style lang="scss" scoped>
@import "./node_modules/vue-material/dist/theme/engine";
@include md-register-theme('default', (
    primary: md-get-palette-color(bluegrey, A200), // primary color
    accent: md-get-palette-color(grey, A200) // secondary color
));
@import "~vue-material/dist/components/MdButton/theme"; // Apply the Button
@import "~vue-material/dist/components/MdContent/theme"; // Apply the Content
@import "~vue-material/dist/components/MdToolbar/theme";

@import "~vue-material/dist/theme/all";
</style>
