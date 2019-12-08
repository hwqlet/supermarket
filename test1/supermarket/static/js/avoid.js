function avoid(){
    if(document.referrer==""){
        alert('请先登录，小东西');
        window.location.href="/home/";
    }
}
avoid();