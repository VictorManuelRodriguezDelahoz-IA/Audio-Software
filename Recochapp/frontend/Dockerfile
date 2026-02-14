FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# Instalamos dependencias
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]