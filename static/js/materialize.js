// Materialize CSS Init Functions

//collapsible navbar 
$(document).ready(function () {
   $('select').material_select();
   $(".button-collapse").sideNav();
   $('.sidenav').sideNav();
});

// for HTML5 "required" attribute
$(document).ready(function () {
   $('select').material_select();
   $("select[required]").css({
      display: "inline",
      height: 0,
      padding: 0,
      width: 0
   });
});
// EasyPaginate
$('#easyPaginate').easyPaginate({
   paginateElement: 'li',
   elementsPerPage: 5,
   effect: 'climb'
});

// $('#easyPaginate_').easyPaginate({
//    paginateElement: 'div',
//    elementsPerPage: 6,
//    effect: 'climb'
// });