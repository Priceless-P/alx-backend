import { createClient, print } from "redis";

const client = createClient();
const key = 'HolbertonSchools';
client.hset(key, 'Portland', 50, print);
client.hset(key, 'Seattle', 80, print);
client.hset(key, 'New York', 20, print);
client.hset(key, 'Bogota', 20, print);
client.hset(key, 'Cali', 40, print);
client.hset(key, 'Paris', 2, print);

client.hgetall(key, (err, res) => {
    if (err) {
        console.log(err);
    } else {
        console.log(res);
    };
})