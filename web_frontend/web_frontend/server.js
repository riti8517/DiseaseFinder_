const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors({
    origin: "*"
}));

app.get('/', (req,res)=> {
    res.send("CORS issue ressolved");
})

const port = 8080;
app.listen(port, () => console.log(`Server started on port ${port}`))
