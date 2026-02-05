const express=require('express');
const app=express();

app.get("/",(req,res)=>{
    res.send("<h1>Hello from home page</h1>")
});
app.get("/about",(req,res)=>{
    res.send("<h1>Hello from About page</h1>")
});

app.get("/contactus",(req,res)=>{
res.send("<h1>Hello from Contact us page</h1>")
});

app.listen(4000,()=>{console.log("Server working and listening!!")});