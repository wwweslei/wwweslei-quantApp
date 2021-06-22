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