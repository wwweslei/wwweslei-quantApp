// sidebar  
$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

//cards
let update = document.getElementsByClassName('small-box-footer')
for (let i = 0; i < update.length; i++) {
    update[i].addEventListener('click',() => {
        update[i].innerHTML = "updating"
    });
}

let value = document.querySelectorAll('.small-box h4');
let div = document.querySelectorAll('.small-box');
for (let i = 0; i < value.length; i++) {
    // console.log(value[i].innerHTML.slice(0, -1));
    if (value[i].innerHTML.slice(0, -1) <= -1){
        div[i].classList.remove('bg-info');
        div[i].classList.remove('bg-success');
        div[i].classList.remove('bg-warning');
        div[i].classList.add('bg-danger');
    };
    if (value[i].innerHTML.slice(0, -1) < 0 &&
        value[i].innerHTML.slice(0, -1) > -1 ){
        div[i].classList.remove('bg-info');
        div[i].classList.remove('bg-success');
        div[i].classList.remove('bg-danger');
        div[i].classList.add('bg-warning');
    };
    if (value[i].innerHTML.slice(0, -1) > 0 &&
    value[i].innerHTML.slice(0, -1) < 1) {
        div[i].classList.remove('bg-warning');
        div[i].classList.remove('bg-success');
        div[i].classList.remove('bg-danger');
        div[i].classList.add('bg-info');
    };
    if (value[i].innerHTML.slice(0, -1) >= 1){
        div[i].classList.remove('bg-danger');
        div[i].classList.remove('bg-info');
        div[i].classList.remove('bg-warning');
        div[i].classList.add('bg-success');
    };
    // console.log(value[i]);
}
