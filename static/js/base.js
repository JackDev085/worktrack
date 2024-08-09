const cards = document.getElementsByClassName(".card")

for (let i = 0; i < cards.length; i++) {
  cards[i].addEventListener('click', function () {

    cards[i].style.backgroundColor = '#F56F16'; // Altere a cor de fundo para a cor desejada
    for (let j = 0; j < cards.length; j++) {

      if (j == i) {
        continue
      }
      cards[j].style.backgroundColor = 'transparent'; // Altere a cor de fundo para a cor desejada
    }
  });
}