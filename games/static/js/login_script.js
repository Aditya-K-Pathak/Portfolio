if (localStorage.getItem('Aditya_Quiz_username') &&
    localStorage.getItem('Aditya_Quiz_username')){
        document.getElementById('user_name').value = 
        localStorage.getItem('Aditya_Quiz_username');
        document.getElementById('user_password').value = 
        localStorage.getItem('Aditya_Quiz_username');

        document.getElementById('submit').click();
}

const setval = () => {
    username = document.getElementById('user_name').value;
    password = document.getElementById('user_password').value;

    localStorage.setItem('Aditya_Quiz_username', username);
    localStorage.setItem('Aditya_Quiz_password', password);
}
