

const words = ["Abdulhakeem Adamu","Python Developer", "Full Stack Developer"]
const introd = document.getElementById("intro-h1")
const theme = document.getElementById("theme")
const footer = document.getElementById("footer")
const toggle_btn = document.getElementById("toggle_theme_btn")

// const intro=()=>{

//     c = words.map((b)=>{
//         introd.innerHTML = words;
//     })
// }
// to change theme and toggle button
const change_theme = ()=>{
    if (toggle_btn.innerHTML == '🌙'){
        toggle_btn.innerHTML = '☀️';
        theme.style.backgroundColor="black";
        theme.style.color="white";
        footer.style.backgroundColor= '#333';
    }
    else{
        theme.style.backgroundColor="white";
        theme.style.color="black";
        toggle_btn.innerHTML = '🌙';
        footer.style.backgroundColor= '#999';
    }
    
} 

// b = intro()
