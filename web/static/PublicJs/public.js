function ajax_response(url,method,data) {
    /**
     * 函数编写人：丁志颖
     * 
     * 作用：
     *      Django框架中用来发送表单的验证请求
     **/
    if (method == 'post') {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        console.log(csrftoken);
        axios({
            url:url,
            method:method,
            // x-www-form-urlencoded
            headers: {'X-CSRFToken': csrftoken,"Content-Type":"application/x-www-form-urlencoded"},
            data:{
                "data":JSON.stringify(field)
            }
        }).then(res => {
            return res.data
        }).catch(error => {
            return error.response.dataa;
        })
    } else {
        axios({
            url:url,
            method:method,
            // headers: {'X-CSRFToken': csrftoken,"Content-Type":"application/x-www-form-urlencoded"},
            params:{
                'params':data
            }
        }).then(res => {
            return res.data;
        }).catch(error => {
            return error.response.dataa;
        })
    }
}