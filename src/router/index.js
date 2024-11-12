import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '../components/Login.vue';
import UserRegister from '../components/Register.vue';
import AddBlog from '../components/AddBlog.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: UserLogin },
  { path: '/register', component: UserRegister },
  { path: '/add-blog', component: AddBlog },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
