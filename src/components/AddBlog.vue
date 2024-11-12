<template>
  <div>
    <h2>Add New Blog Post</h2>
    <form @submit.prevent="addBlog">
      <input v-model="title" placeholder="Title" required />
      <textarea v-model="description" placeholder="Description" required></textarea>
      <input type="file" @change="onFileChange" />
      <select v-model="category">
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
      </select>
      <input v-model="tags" placeholder="Tags (comma separated)" />
      <button type="submit">Add Blog Post</button>
    </form>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'AddBlog',
  data() {
    return {
      title: '',
      description: '',
      category: null,
      tags: '',
      main_image: null,
      categories: []
    };
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await api.get('categories/');
        this.categories = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    },
    onFileChange(event) {
      this.main_image = event.target.files[0];
    },
    async addBlog() {
      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('main_image', this.main_image);
      formData.append('category', this.category);
      this.tags.split(',').forEach(tag => formData.append('tags', tag.trim()));

      try {
        const response = await api.post('blogs/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log('Blog post added:', response.data);
        this.$router.push('/blogs');
      } catch (error) {
        console.error('Error adding blog post:', error);
      }
    }
  },
  mounted() {
    this.fetchCategories();
  }
};
</script>
