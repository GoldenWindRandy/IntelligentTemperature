// 封装提示框函数，重复调用，满足提示需求
const myAlert = document.querySelector('.alert')
const Flag = false
function alertFn(msg, isSuccess) {
    // 1.显示提示框
    myAlert.classList.add('show')
    //2.实现细节
    myAlert.innerText = msg
    const bgStyle = isSuccess ? 'alert-success' : 'alert-danger'
    myAlert.classList.add(bgStyle)
    //3.过2秒隐藏
    setTimeout(() => {
        myAlert.classList.remove('show')
        //提示：避免类名冲突，重置背景色
        myAlert.classList.remove(bgStyle)
    }, 2000)
}

document.querySelector('.btn-login').addEventListener('click', () => {
    // 获取用户名和密码
    const username = document.querySelector('.username').value
    const password = document.querySelector('.password').value

    // 判断长度
    if (username.length < 8 || username.length > 12 || (username[0] >= '0' && username[0] <= '9')) {
        alertFn('用户名为8-12位，且不能以数字开头', false)
        return   //阻止代码继续执行
    }
    if (password.length < 6 || password.length > 15) {
        alertFn('密码长度为6-15位', false)
        return   //阻止代码继续执行
    }

    // 基于axios提交用户名和密码
    axios({
        url: 'http://127.0.0.1:8000/user/login/',
        method: 'post',
        data: {
            username,
            password
        }
    }).then(result => {
        console.log(result)
        alertFn(result.data.reseaion, true)
        window.location.replace('func.html')
    }).catch(error => {
        console.log(result)
        //处理错误信息
        alertFn(error.response.data.reseaion, false)
    })
})
const regModalDom = document.querySelector('.register-modal')
const regModal = new bootstrap.Modal(regModalDom)
new Vue({
    el: '#app',
    data() {
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                if (this.ruleForm.checkPass !== '') {
                    this.$refs.ruleForm.validateField('checkPass');
                }
                callback();
            }
        };
        var validatePass2 = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再次输入密码'));
            } else if (value !== this.ruleForm.pass) {
                callback(new Error('两次输入密码不一致!'));
            } else {
                callback();
            }
        };
        return {
            ruleForm: {
                pass: '',
                checkPass: '',
                user: ''
            },
            rules: {
                user: [
                    // 非空
                    { required: true, message: '请输入用户名', trigger: 'blur' },
                    // 用户名必须是 1 ~ 10 位的数字字母, 同时不能以数字开头
                    { pattern: /^[a-zA-Z][a-zA-Z0-9]{7,11}$/, message: '请输入 8 ~ 12 位的数字或字母, 不能以数字开头', trigger: 'blur' }
                ],
                pass: [
                    // 非空
                    { required: true, message: '请输入密码', trigger: 'blur' },
                    { pattern: /^\S{6,15}$/, message: '请输入 6 ~ 15 位的非空字符', trigger: 'blur' },
                    { validator: validatePass, trigger: 'blur' }
                ],
                checkPass: [
                    // 非空
                    { required: true, message: '请再次输入密码', trigger: 'blur' },
                    { pattern: /^\S{6,15}$/, message: '请输入 6 ~ 15 位的非空字符', trigger: 'blur' },
                    { validator: validatePass2, trigger: 'blur' }
                ],
            }
        };
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    const username = this.ruleForm.user;
                    const password = this.ruleForm.pass;
                    axios({
                        url: 'http://hmajax.itheima.net/api/register',
                        method: 'post',
                        data: {
                            username,
                            password
                        }
                    }).then(result => {
                        alert(result.data.message)
                        this.$refs[formName].resetFields();
                        regModal.hide()
                    }).catch(error => {
                        alert(error.response.data.message)
                    })
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    }
})


