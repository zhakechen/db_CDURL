<template>
  <div id="login">
    <p>用户名：<input type="text" v-model="username"></p>
    <p>密码<input type="password" v-model="password"></p>
    <p><button v-on:click="login_user()">登录</button></p>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login_user: function () {
      const params = {
        'username': this.username,
        'password': this.password
      }
      var url = '/app/user/login/'
      this.axios.post(url, params)
        .then(res => {
          if (res.data.code === 200) {
            var token = res.data.data.token
            localStorage.setItem('token', token)
            this.$router.push('/register')
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
