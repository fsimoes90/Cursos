var listaFilmes = [
    'https://www.hostfilmes.com/wp-content/uploads/2016/08/Escola-de-Rock-Dublado.jpg',
    'https://br.web.img3.acsta.net/pictures/16/08/16/17/39/022521.jpg',
    'https://image.tmdb.org/t/p/w1280/ybQSBSrINtjWsJQ6Ih8sva8HlEZ.jpg',
    'https://is1-ssl.mzstatic.com/image/thumb/Video/2a/13/8b/mzi.nzdqmufo.jpg/268x0w.jpg',
    'https://images-na.ssl-images-amazon.com/images/I/813dE2pH7XL._AC_SL1417_.jpg'
  ];
  
  var nomesFilmes = [
    'Escola do Rock',
    'A chegada',
    'Aranhaverso',
    '10 Coisas que eu odeio em você',
    'Matrix'
  ];
  
  var i = 0;
  while (i < listaFilmes.length) {
    if (listaFilmes[i].endsWith('.jpg')) {
      document.write('<img src=' + listaFilmes[i] + '>');
      document.write('<p style="color: white;">' + nomesFilmes[i] + '</p>');
    }
    i++;
  }
  