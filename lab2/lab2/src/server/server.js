import express from 'express';
import basicAuth from 'express-basic-auth';
import ReactDOM from "react-dom/server";
import {indexTemplate} from "./indexTemplate";
import {App} from "../App";

const app = express();
const PORT = process.env.PORT || 3000;

app.use("/static", express.static("./dist/client"));
app.use(basicAuth({
  realm: 'Web.',
  challenge: true,
  users: { 'admin': 'pwd001' }
}));

app.get("*", (req, res) => {
  res.send(indexTemplate(ReactDOM.renderToString(App())));
})

app.listen(PORT, () => {
  console.log("Server started on port http://localhost:3000");
})
