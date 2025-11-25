const userProfile = {};

userProfile.username = 'developer123';
userProfile.email = 'dev@example.com';
userProfile.age = 25;
userProfile.isLoggedIn = true;

console.log(userProfile.email);

userProfile.age = 26;

userProfile['user location'] = 'New York';

console.log(userProfile['user location']);