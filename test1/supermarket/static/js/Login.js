!function (a) { "function" == typeof define && define.amd ? define(["jquery"], a) : "object" == typeof exports ? a(require("jquery")) : a(jQuery) }(function (a) { function b(a) { return h.raw ? a : encodeURIComponent(a) } function c(a) { return h.raw ? a : decodeURIComponent(a) } function d(a) { return b(h.json ? JSON.stringify(a) : String(a)) } function e(a) { 0 === a.indexOf('"') && (a = a.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, "\\")); try { return a = decodeURIComponent(a.replace(g, " ")), h.json ? JSON.parse(a) : a } catch (b) { } } function f(b, c) { var d = h.raw ? b : e(b); return a.isFunction(c) ? c(d) : d } var g = /\+/g, h = a.cookie = function (e, g, i) { if (void 0 !== g && !a.isFunction(g)) { if (i = a.extend({}, h.defaults, i), "number" == typeof i.expires) { var j = i.expires, k = i.expires = new Date; k.setTime(+k + 864e5 * j) } return document.cookie = [b(e), "=", d(g), i.expires ? "; expires=" + i.expires.toUTCString() : "", i.path ? "; path=" + i.path : "", i.domain ? "; domain=" + i.domain : "", i.secure ? "; secure" : ""].join("") } for (var l = e ? void 0 : {}, m = document.cookie ? document.cookie.split("; ") : [], n = 0, o = m.length; o > n; n++) { var p = m[n].split("="), q = c(p.shift()), r = p.join("="); if (e && e === q) { l = f(r, g); break } e || void 0 === (r = f(r)) || (l[q] = r) } return l }; h.defaults = {}, a.removeCookie = function (b, c) { return void 0 === a.cookie(b) ? !1 : (a.cookie(b, "", a.extend({}, c, { expires: -1 })), !a.cookie(b)) } });
        var code;
        function login(){
                //clickChange();不应该在这里进行clickchange
                $('.fright').click(function () {

                });
                var c = $('.textcode').val();
                if (c === '') {
                    alert('请输入验证码');
                    return -1;
                }
                else if(code !== c.toLowerCase()) {
                    alert(code);
                    alert('验证码错误');
                    clickChange();
                    $('#verificationCode').val("");
                    return 1;
                }
                clickChange();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            if(document.getElementById('user_id').value===''||document.getElementById('pass').value==='')
            {
                alert('用户名或者密码不能为空');
            }

            else
            {
                //还必须使用value，因为val只能用在表单元素上
                var name=document.getElementById('user_id').value;
                //alert('hwq');
                var pwd=document.getElementById('pass').value;
                $.ajax({
                    'type':'post',
                    'url':'/login_submit/',
                    'data':{csrfmiddlewaretoken:token,username:name,password:pwd},
                    success:function(result){
                        //后台传数据到js中，我们要用JSON进行parse解析
                        var data=JSON.parse(result);
                        if(data["result"]==='成功'){
                            //应该要跳转到相应的用户界面
                            //alert(data["result"]);
                            //window.location.href='{%url ''%}';
                            //localStorage.setItem('the_cookie','value');
                            localStorage.setItem('username',document.getElementById('user_id').value);
                            localStorage.setItem('password',document.getElementById('pass').value);
                            window.location.href="/user_index/";
                        }
                        else{
                            //流程打通了
                            alert(data["result"]);
                            reset();
                        }
                    }
                });
            }
        }
        function back(){
            window.location.href="/home/";//这样也可以呢，通过reverse反向查找
        }
        function reset(){
            document.getElementById("user_id").value="";
            document.getElementById("pass").value="";
        }
        function register_new() {
            //点击注册按钮进行跳转
            window.location.href = "/register_new/";
        }

        function forget(){
            window.location.href = "/change_pass/";
        }

/*生成4位随机数*/
function rand() {
    var str = "abcdefghijklmnopqrstuvwxyz0123456789";
    var arr = str.split("");
    var validate = "";
    var ranNum;
    for (var i = 0; i < 4; i++) {
        ranNum = Math.floor(Math.random() * 36); //随机数在[0,35]之间
        validate += arr[ranNum];
    }
    return validate;
}
/*干扰线的随机x坐标值*/
function lineX() {
    var ranLineX = Math.floor(Math.random() * 80);
    return ranLineX;
}
/*干扰线的随机y坐标值*/
function lineY() {
    var ranLineY = Math.floor(Math.random() * 34);
    return ranLineY;
}
function clickChange() {
    var mycanvas = document.getElementById('mycanvas');
    var cxt = mycanvas.getContext('2d');
    cxt.fillStyle = '#fff';
    cxt.fillRect(0, 0, 80, 34);
    /*生成干扰线10条*/
    for (var j = 0; j < 3; j++) {
        cxt.strokeStyle = randomColor(0, 255);
        cxt.beginPath(); //若省略beginPath，则每点击一次验证码会累积干扰线的条数
        cxt.moveTo(lineX(), lineY());
        cxt.lineTo(lineX(), lineY());
        cxt.lineWidth = 0.5;
        cxt.closePath();
        cxt.stroke();
    }
    cxt.fillStyle = 'red';
    cxt.font = 'bold 20px Arial';
    code = rand();
    cxt.fillText(code, 25, 25); //把rand()生成的随机数文本填充到canvas中
}
function randomColor(min, max) {
    var r = randomNum(min, max);
    var g = randomNum(min, max);
    var b = randomNum(min, max);
    return "rgb(" + r + "," + g + "," + b + ")";
}
function randomNum(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}
/*点击验证码更换*/
mycanvas.onclick = function (e) {
    e.preventDefault(); //阻止鼠标点击发生默认的行为
    clickChange();
};
