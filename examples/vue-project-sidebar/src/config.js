// During development, process.env.NODE_ENV will be development, 
// and during production builds, it will be production. This allows you 
// to automatically pick the correct configuration based on the environment

const config = {
    development: {
      apiUrl: 'http://127.0.0.1:5000/upload',
    },
    production: {
      apiUrl: 'https://api.example.com', // Change this to your production API URL
    },
  };
  
  export default config;
  