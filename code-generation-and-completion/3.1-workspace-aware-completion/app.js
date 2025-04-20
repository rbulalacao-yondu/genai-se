const express = require('express');
const app = express();
app.use(express.json());

const userRouter = require('./routes/user');
const projectRouter = require('./routes/project');

app.use('/users', userRouter);
app.use('/projects', projectRouter);

module.exports = app;
