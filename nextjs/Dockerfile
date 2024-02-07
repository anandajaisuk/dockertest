FROM node:21

WORKDIR /src

# Copy everything from the current directory into the container's /src directory
COPY . .

# Install dependencies
RUN npm install

# Change directory to src/prisma and generate Prisma client
WORKDIR /src/src/prisma
RUN npx prisma generate

# Change back to the parent directory
WORKDIR /src

# Set the default command to run when the container starts
CMD ["npm", "run", "build"]