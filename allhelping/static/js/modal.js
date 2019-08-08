const btnProximo = document.querySelector('#btnNext');
const btnNao = document.querySelector('#btnNo');
const btnSim = document.querySelector('#btnYes');

const inputNumber = document.querySelector('.inputNum');

const msgErr = document.querySelector('.msgError');

btnProximo.onclick = () => {
    if (inputNumber.value === "") {
        msgErr.style = "display:block";
        return;
    }
    else{
        msgErr.style = "display:none";
        let modal = document.querySelector('#modal');
        modal.classList.add('d-flex');
    }
}

btnNao.onclick = () => {
    let modal = document.querySelector('#modal');
    modal.classList.remove('d-flex');
}