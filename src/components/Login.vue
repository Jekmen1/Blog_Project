<template>
    <div>
        <h2>Login</h2>
        <form @submit.prevent="login">
            <input v-model="username" placeholder="Username" required />
            <input v-model="password" type="password" placeholder="Password" required />
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
import api from '../api';

export default {
    name: 'UserLogin',
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async login() {
            try {
                const response = await api.post('token/', {
                    username: this.username,
                    password: this.password,
                });
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);
                console.log('User logged in:', response.data);
            } catch (error) {
                console.error('Login error:', error);
            }
        },
    },
};
</script>
