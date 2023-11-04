var submit_form = document.getElementById('signupForm')
var pass =  document.getElementById('signup_password_input')
var re_pass =  document.getElementById('signup_repassword_input')
var v = document.getElementById('v')
function submit_event(event){
    event.preventDefault();
    console.log('===' )
    if (pass.value === re_pass.value){
        submit_form.submit();
    }
    else{
        event.preventDefault();
        v.innerText = 'password does not match'
    }
}