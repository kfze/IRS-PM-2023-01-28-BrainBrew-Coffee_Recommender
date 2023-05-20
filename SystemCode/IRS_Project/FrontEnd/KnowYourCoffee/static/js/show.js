var aBtn = document.querySelectorAll('.pos');
var aDivQ = document.querySelectorAll('.q');
var oHForms = document.querySelector('.forms-title');
var oDivContent = document.querySelector('.q-content');
for(var i = 0; i < aBtn.length; i++){
    
    aBtn[i].onclick = function(){
        var index = this.dataset['index'];
        aDivQ[index*1+1].classList.add('a4');
        aDivQ[index].style.opacity = '0';
        if(index == 2){
            oHForms.classList.remove('d-none');
            aDivQ[3].style.position = 'static';
            oDivContent.style.height = '900px';
        }
    }
}