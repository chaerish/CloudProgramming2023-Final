const menuBtn=document.querySelector('.navbar_menuBtn');
const menu=document.querySelector('.navbar_menu');

menuBtn.addEventListener('click',()=>{
    menu.classList.toggle('active');
});