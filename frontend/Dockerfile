FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install ALL dependencies (including react-scripts)
RUN npm ci --legacy-peer-deps

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Set environment to development
ENV NODE_ENV=development

# Start app
CMD ["npm", "start"]