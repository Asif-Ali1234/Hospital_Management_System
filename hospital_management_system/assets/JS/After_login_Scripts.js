window.setTimeout(function(){
    $(".alert").fadeTo(500,0).slideUp(500,
    function(){
        $(this).remove();
    });
},2000);
$(document).ready(function () {
    $('#sidenavCollapse').on('click', function () {
        $('#sidenav').toggleClass('active');
    });
});

function showdiv()
{
  var chekyes=document.getElementById('freshers');
  var imagediv=document.getElementById('freshersdiv');
  var imagediv2=document.getElementById('experienceddiv')
  if(chekyes.checked)
  {
    imagediv.style.display="block";
    imagediv2.style.display="none";
  }
  else
  {
    imagediv.style.display="none";
    imagediv2.style.display="block";
  }
}
function display_content(a,b,c,d,e)
{
    if(a=="profilecontent"){
      document.getElementById(a).style.display="block"
    }
    else{
      document.getElementById(a).style.display='flex';
    }
    document.getElementById(b).style.display='none';
    document.getElementById(c).style.display='none';
    document.getElementById(d).style.display='none';
    document.getElementById(e).style.display='none';
}