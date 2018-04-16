/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#">Lab 7</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
          </li>
          
          <li class="nav-item active">
            <router-link class="nav-link" to="/upload-form/">Upload Form <span class="sr-only">(current)</span></router-link>
          </li>
        </ul>
      </div>
    </nav>
    `
});

Vue.component('app-footer', {
    template: `
    <footer>
        <div class="container">
            <p>Copyright &copy; Flask Inc.</p>
        </div>
    </footer>
    `
});


const Form = Vue.component('upload-form', {
     template: `
        <div class="upload">

        <h2>Upload</h2>

        <div class="form-inline d-flex justify-content-center">

            <form id="uploadForm"  @submit.prevent="uploadPhoto" method="POST" enctype="multipart/form-data">

                <div>

                <div for="msg">Description: </div> </br>    <textarea class="form-control" rows="5"  cols="50" id="msg" name="description"></textarea><br></br>

                <input type="file" name="upload"/></br>

                </div></br>

                <button class="btn btn-success" type="submit">Upload</button>

            </form>

        </div>

        </div>

    `,
 
methods: {
    uploadPhoto: function(){
        let uploadForm = document.getElementById('uploadForm');
        let form_data = new FormData(uploadForm); 
        console.log(form_data);
        fetch("/api/upload", {method: 'POST',body: form_data, headers: {'X-CSRFToken': token},credentials: 'same-origin'} ).then(function (response) {
            return response.json();
        }).then(function (jsonResponse) {
            // display a success message
            console.log(jsonResponse);
            }).catch(function (error) {
                console.log(error);
                });
    } 
}
})


const Home = Vue.component('home', {
   template: `
    <div class="jumbotron">
        <h1>Lab 7</h1>
        <p class="lead">In this lab we will demonstrate VueJS working with Forms and Form Validation from Flask-WTF.</p>
    </div>
   `,
    data: function() {
       return {}
    }
});

// Define Routes
const router = new VueRouter({
    routes: [
        { path: "/", component: Home },
        { path: "/upload-form/", component: Form }
    ]
});

// Instantiate our main Vue Instance
let app = new Vue({
    el: "#app",
    router
});