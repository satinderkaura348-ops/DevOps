#!/bin/bash

sudo apt-get update 
sudo apt-get install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

echo "<h1> This is to confirm if shell script worked and nginx installed</h1>" | sudo tee /var/www/html/index.html
