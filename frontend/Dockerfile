# Build stage
FROM node:20-slim as build

WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies
RUN yarn install

# Copy the source code
COPY . .

# Set backend url
ENV VITE_API_BASE_URL=/

# Build the application
RUN yarn build

# Production stage
FROM nginx:stable-alpine

# Copy built files from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"] 