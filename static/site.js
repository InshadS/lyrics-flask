function main() {
  $.get({
    url: 'http://127.0.0.1:5000/artists',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list +=
          `<li class="items" value=${element.id}>` + element.name + '</li>';
      });
      tag = `<ul>${list}</ul>`;
      $('div.artist').html(tag);
      console.log(data);
    },
  });
  $(document).on('click', 'li.items', function () {
    $.get({
      url: `http://127.0.0.1:5000/songs/${this.value}`,
      success: (data) => {
        list = '';
        data.forEach((element) => {
          list +=
            `<li class="song" value=${element.id}>` + element.name + '</li>';
        });
        tag = `<ul>${list}</ul>`;
        $('div.songs').html(tag);
        console.log(data);
      },
    });
  });
}
$(main);
