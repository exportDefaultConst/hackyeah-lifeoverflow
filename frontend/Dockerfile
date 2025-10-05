# Frontend Dockerfile - Node.js runtime without nginx
FROM node:20-alpine

WORKDIR /app

# Kopiuj package files
COPY package.json ./
RUN npm install

# Kopiuj kod i zbuduj
COPY . .
RUN npm run build

# Wystaw port domyślnego podglądu Vite
EXPOSE 5173

# Uruchom serwer podglądu Vite na wszystkich interfejsach
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "5173"]
