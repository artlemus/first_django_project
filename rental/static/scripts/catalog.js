
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
    var tr = 
    `
    <tr>
        <td><img src='${movie.image}'></td>
        <td><a href="/movie/${movie.id}">${movie.title}</a></td>
        <td>${movie.release_year}</td>
        <td>${movie.price}</td>
        <td>${movie.in_stock}</td>
    </tr>
    `
    $(".catalog table tbody").append(tr);
}

function init() {
  console.log("catalog page");
  loadData();
}

window.onload = init;
