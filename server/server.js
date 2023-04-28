const express = require("express")
const fs = require("fs")

const app = express()
app.use(express.static('public'))
app.set('view engine', 'ejs');
app.get('/',(req, res)=>{
    res.sendFile(__dirname+"/public/login.html")
})

app.get('/check_login',(req, res)=>{
    const {username, password} = req.query;
    console.log({username, password})
    if(username == "yash" && password == "1234"){
        res.sendFile(__dirname+"/public/index.html", {username: username})
    }else{
        res.sendFile(__dirname+"/public/user_not_found.html")
    }
})

const server = app.listen(8080,()=>{
    console.log("Starting Server At")
    console.log("http://localhost:" + server.address().port)
});