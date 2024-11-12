<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="register">
            <input v-model="username" placeholder="Username" required />
            <input v-model="email" type="email" placeholder="Email" required />
            <input v-model="password" type="password" placeholder="Password" required />
            <button type="submit">Register</button>
        </form>
    </div>
</template>

<script>
import api from '../api';

export default {
    name: 'UserRegister',
    data() {
        return {
            username: '',
            email: '',
            password: '',
        };
    },
    methods: {
        async register() {
            try {
                const response = await api.post('register/', {
                    username: this.username,
                    email: this.email,
                    password: this.password,
                });
                console.log('User registered:', response.data);
            } catch (error) {
                console.error('Registration error:', error);
            }
        },
    },
};
</script>
