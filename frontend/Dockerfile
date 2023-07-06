# Use an official Node.js image as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install the project dependencies
RUN npm ci --silent

# Copy the entire project to the container
COPY . .

# Build the React app
RUN npm run build

# Expose the port that the application will be served on
EXPOSE 3000

# Set the entrypoint command to serve the React app
CMD ["npm", "start"]
