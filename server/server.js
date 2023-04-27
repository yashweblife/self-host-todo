const express = require("express")
const fs = require("fs")

const app = express()
app.use(express.static('public'))

app.get('/',(req, res)=>{
    res.sendFile(__dirname+"/public/login.html")
})
app.get('/check_login',(req, res)=>{
    console.log(req.body.username)
    // res.end("<script>console.log("+req+")</script>");
    res.end();
})

const server = app.listen(8080,()=>{
    console.log("Starting Server At")
    console.log("http://localhost:" + server.address().port)
});