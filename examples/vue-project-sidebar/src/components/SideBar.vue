<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from '@/components/HelloWorld.vue'
</script>

<template>
    <div class="sidebar sidebar-narrow sidebar-dark border-end">
        <div class="sidebar-header border-bottom">
            <div class="sidebar-brand">NAV</div>
        </div>
        <ul class="sidebar-nav">
            <li class="nav-title">Nav Title</li>
            <li class="nav-item">
                <router-link class="nav-link" to="/">
                    <i class='nav-icon bx bxs-castle'></i> Home
                </router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/about">
                    <i class='nav-icon bx bxs-universal-access' ></i> About
                </router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/test">
                    <i class='nav-icon bx bx-test-tube' ></i> Test
                </router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/test-upload">
                    <i class='nav-icon bx bx-cloud-upload'></i>Test Upload
                </router-link>
            </li>
            <li class="nav-item nav-group show">
                <a class="nav-link nav-group-toggle" href="#">
                    <i class="nav-icon bx bxs-universal-access"></i> Nav dropdown
                </a>
                <ul class="nav-group-items">
                    <li class="nav-item">
                        <a class="nav-link" href="#">
                            <span class="nav-icon"><span class="nav-icon-bullet"></span></span> Nav dropdown item
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">
                            <span class="nav-icon"><span class="nav-icon-bullet"></span></span> Nav dropdown item
                        </a>
                    </li>
                </ul>
            </li>
            <li class="nav-item mt-auto">
                <a class="nav-link" href="https://coreui.io">
                    <i class="nav-icon bx bx-cloud-download"></i> Download CoreUI
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="https://coreui.io/pro/">
                    <i class='nav-icon bx bxl-product-hunt'></i> Try CoreUI
                    <strong>PRO</strong>
                </a>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
}
</style>