# Frontend Dockerfile - minimalistyczny z multi-stage build
FROM node:20-alpine AS builder

WORKDIR /app

# Kopiuj package files
COPY package.json ./
RUN npm install

# Kopiuj kod i zbuduj
COPY . .
RUN npm run build

# Production stage - serwuj z nginx
FROM nginx:alpine

# Kopiuj zbudowaną aplikację
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
