# Vue.js project
![MQTT Broker](STICH.jpeg)
In this repo you will find a Vue.js project that uses the [Vue.js](https://vuejs.org/) framework to create a simple web application that displays a list of items and allows the user to add new items to the list.


## Requirements for the Vue project
It must install the node.js framework. To install it, you can use the following command:

```bash
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js (you may need to restart the terminal)
nvm install 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.16.0`

# verifies the right npm version is in the environment
npm -v # should print `10.8.1`
```

## How to init the Vue project
To init the Vue project, you can use the following command that create a new Vue project with the latest version of Vue.js:

```bash
npm create vue@latest
```

Whene the command is executed, you will be asked to provide the name of the project, in this example is used as name `vue-project` and other details needed to create the project. The command will create a new directory with the name of the project and will create the project inside that directory. The project will have the following structure:

```bash
vue-project/
  README.md
  node_modules/
  package.json
  public/
    index.html
  src/
    assets/
    components/
    ...
    App.vue
    main.js
```

The best answer to the questions are the following:

```bash
> npx
> create-vue


Vue.js - The Progressive JavaScript Framework

RangeError: Incorrect locale information provided

✔ Project name: … vue-project
✔ Add TypeScript? … No  
✔ Add JSX Support? … Yes
✔ Add Vue Router for Single Page Application development? … Yes
✔ Add Pinia for state management? …  Yes
✔ Add Vitest for Unit Testing? …  Yes
✔ Add an End-to-End Testing Solution? › No
✔ Add ESLint for code quality? …  Yes
✔ Add Prettier for code formatting? …  Yes
✔ Add Vue DevTools 7 extension for debugging? (experimental) …  Yes

Scaffolding project in /home/ion/vue/vue-first-run/vue-project...

Done. Now run:

  cd vue-project
  npm install
  npm run format
  npm run dev
```

Whene the project is created, you can navigate to the project directory and install the dependencies using the following command:

```bash
cd vue-project
npm install
```

## How to run the development - Vue project
To run the development fase, you can use the following command:

```bash
npm run dev
```

The command will start the development server and will open the browser with the URL `http://localhost:5173/`. And on the `http://localhost:5173/__devtools__/` there is . The development server will watch for changes in the project files and will reload the browser when a change is detected.

## How to build the Vue project
When the project is ready to be deployed, you can use the following command to build the project:

```bash
npm run build
```

The command will create a new directory called `dist` with the build files. The build files are optimized for production and are ready to be deployed to a web server.

# Examples 
There are some examples of Vue.js projects that you can use to learn more about Vue.js and how to create web applications with Vue.js. The examples are located in the [examples](examples) directory. Move to the directory and follow the instructions in the README.md file to run the examples. You can use the examples to learn more about Vue.js and how to create web applications with Vue.js.


# License
The code is available under the [MIT license](https://opensource.org/license/MIT) and linked to the [LICENSE](LICENSE) file.