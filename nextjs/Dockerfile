FROM node:21

WORKDIR /src

COPY . .

RUN npm install --verbose

WORKDIR /src/src/prisma
RUN npx prisma generate

WORKDIR /src
RUN npm run build

CMD ["npm", "run", "start"]
