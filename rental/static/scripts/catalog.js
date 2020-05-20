
var catalog = [];

function loadData(){
    $.ajax({
        url: '/api/movies',
        type: 'GET',
        success: (res) => {
            console.log('from server', res);

            catalog = res.objects;

            for(let i=0;i<res.objects.length; i++){
                var movie = res.objects[i];
                displayMovie(movie);
            }
        },
        error: (errorDetail) => {
            console.log(errorDetails);
        }
    });
}
function displayMovie(movie){
    var card = 
    `

    <div class="container_details">
    <div class="card mb-3" style="max-width: 400px;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img src="${movie.image}" class="card-img" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
       <h5 class="card-title"><a href="/movie/${movie.id}">${movie.title}</a>
       </h5>
        <p class="card-text">Release Year: ${movie.release_year} <br> Price: $${movie.price}<br>In stock :${movie.in_stock}</p>
      </div>
    </div>
  </div>
  </div>

      
      
    `
    $(".catalog").append(card);

}

function init() {
  console.log("catalog page");
  loadData();
}

window.onload = init;
