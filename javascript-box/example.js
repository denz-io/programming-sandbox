const user = { username: 'yourname.123', friends: 12, };

const users = [
  { username: 'yourname.123', friends: 12, },
  { username: 'yourname.123', friends: 12, },
  { username: 'yourname.123', friends: 12, },
];

users.forEach(res => {
   console.log(res.username);
   console.log(res.friends);
});
