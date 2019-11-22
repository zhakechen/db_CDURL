<template>
    <div>
      <p>文章</p>
      <ul>
        <li v-for="article in articles">{{ article.title }}</li>
      </ul>
    </div>
</template>

<script>
export default {
  data () {
    return {
      articles: '',
      token: localStorage.getItem('token')
    }
  },
  mounted: function () {
    var url = '/app/article/?token=' + this.token
    this.axios.get(url)
      .then(res => {
        if (res.data.code === 0) {
          console.log(res.data)
          this.articles = res.data.data.results
        }
        alert('11')
      })
  }
}
</script>

<style scoped>

</style>
