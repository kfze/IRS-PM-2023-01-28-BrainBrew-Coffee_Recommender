function checkFruity(){
    var checkbox = document.getElementById('Fruity');
    var fruitExpend = document.getElementById('fruit-expend');
    if (checkbox.checked == true){
        fruitExpend.style.visibility = 'visible';
        fruitExpend.style.display = 'block';
    }
    else {
        fruitExpend.style.visibility = 'hidden';
        fruitExpend.style.display = 'none';
    }
}
