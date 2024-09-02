

<script setup>
    import { ref, onMounted } from 'vue';

    const count = ref(0);
    

    const query = ref(''); //reactive('')
    const reset = (evt) => {
      query.value = '' // clears the query
    }

    const response_text = ref('No response from backend');
    onMounted(() => {
      fetch('http://localhost:5000/status')
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        response_text.value = data;
      });
    })

    

    const new_response = ref('No clicked yet');
    const clicked = ref(false);
    const clicked_times = ref(0);
    const onClick = () => {
      fetch('http://localhost:5000/hello')
      .then((response) => response.json()) 
      .then((data) => {
        console.log(data);
        new_response.value = data.message;
      });
      clicked_times.value++;
      clicked.value = true;
      console.log(clicked.value);
    }


</script>

<template>
    <div class="test">
      <h1>This is a test page</h1>
      
      <br>
        <p>Response from backend on mount: <b>{{ response_text }}</b></p>
        <button @click="onClick">Click me</button> Clicked {{ clicked_times }} times
        <p>Response from backend on click: <b>{{ new_response }}</b></p>
      <br>
      <h2>Filter Search value</h2>
      Value is: {{ query }} 
      <br>
      <input type="text" placeholder="Filter Search" v-model="query" />
      <button @click="reset">Reset</button>
      <div v-if="clicked">
        <br>
        <img src="/STICH.jpeg" alt="image stitch" height="50%" width="50%">
        <br>
        Picture
        <br>
      </div>
    
      <br>
      <br>
      <h2>Count button value</h2>
        <button @click="count++">{{ count }}</button>
    </div>
  </template>
  
