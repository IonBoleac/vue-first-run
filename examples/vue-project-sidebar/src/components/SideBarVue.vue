<script setup>
    import { CSidebar, CSidebarBrand, CSidebarHeader, CSidebarNav, CNavTitle, CNavItem, CIcon } from '@coreui/vue';
</script>

<template>
    <CSidebar narrow>
        <CSidebarHeader class="border-bottom">
            <CSidebarBrand>CUI</CSidebarBrand>
        </CSidebarHeader>
        <CSidebarNav>
            <CNavTitle>Nav Title</CNavTitle>
            <CNavItem href="#">
            <CIcon  customClassName="nav-icon" icon="cil-speedometer"/>
            </CNavItem>
            <CNavItem href="#">
            <CIcon  customClassName="nav-icon" icon="cil-speedometer"/>
            </CNavItem>
            <CNavItem href="https://coreui.io">
            <CIcon customClassName="nav-icon" icon="cil-cloud-download" />
            </CNavItem>
            <CNavItem href="https://coreui.io/pro/">
            <CIcon customClassName="nav-icon" icon="cil-layers" />
            </CNavItem>
        </CSidebarNav>
    </CSidebar>
</template>