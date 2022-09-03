window.setTimeout(function () {
    $(".alert").fadeTo(500, 0).slideUp(500,
        function () {
            $(this).remove();
        });
}, 2000);
bool=true
function reveal(x) {
    x.classList.toggle("fa-eye-slash");
    if (bool) {
        document.getElementById('newpwd').type = 'text';
        document.getElementById('newpwd').focus()
        bool = false;
    }
    else {
        document.getElementById('newpwd').type = 'password';
        document.getElementById('newpwd').focus()
        bool = true;
    }
}

function checkfocus(id){
    //var ele=document.getElementById(id)
    if(!id.checkValidity()){
        id.style.border="3px solid red"
        id.nextElementSibling.style.color="red"
        id.nextElementSibling.style.transform="translateY(-25px)"
        id.nextElementSibling.style.fontSize="0.9em"
        id.nextElementSibling.style.left="10px"
        id.nextElementSibling.style.fontWeight="700"
    }
    else{
        id.style.border="1px solid coral"
        id.nextElementSibling.style.color="coral"
    }
}