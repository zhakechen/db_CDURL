<template>
  <div id="register">
    <p>注册页面</p>
    <p>账号：<input type="text" v-model="username"></p>
    <p>密码：<input type="password" v-model="password"></p>
    <p>确认密码：<input type="password" v-model="password1"></p>
    <p><button v-on:click="register_user()">确认</button></p>
  </div>
</template>

<script>
export default{
  data () {
    return {
      username: '',
      password: '',
      password1: ''
    }
  },
  methods: {
    register_user: function () {
      const params = {
        'username': this.username,
        'password': this.password,
        'password1': this.password1
      }
      var url = '/app/user/register/'
      this.axios.post(url, params)
        .then(res => {
          console.log(res.data)
          if (res.data.code == 200) {
            this.$router.push('/login/')
          }
          else {
            alert(res.data.msg)
          }
        })
        .catch(err => {
          alert('no')
        })
    }
  }
}

</script>

<style>
</style>
