if (!localStorage.getItem('username')){
    document.getElementById('user_name').value = document.getElementById('username').innerHTML;
    localStorage.setItem('username', document.getElementById('username').innerHTML);
} else{
    document.getElementById('user_name').value = localStorage.getItem('username');
}