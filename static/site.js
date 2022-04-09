function main() {
  $.get({
    url: 'http://127.0.0.1:5000/api/artists',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list +=
          `<li class="items" value=${element.id}>` + element.name + '</li>';
      });
      tag = `<ul type='square'>${list}</ul>`;
      $('div.artist').html(tag);
      console.log(data);
    },
  });
  $(document).on('click', 'li.items', function () {
    $.get({
      url: `http://127.0.0.1:5000/api/songs/${this.value}`,
      success: (data) => {
        list = '';
        data.forEach((element) => {
          list += `<li class="song" id=${element.id}>` + element.name + '</li>';
        });
        tag = `<ul type='square'>${list}</ul>`;
        $('div.songs').html(tag);
        console.log(data);
      },
    });
  });
  $(document).on('click', 'li.song', function () {
    $.get({
      url: `http://127.0.0.1:5000/api/songs/${this.value}/lyrics/${this.id}`,
      success: (data) => {
        lyric = `<pre><p>${data}</p></pre>`;
        $('div.lyric').html(lyric);
        console.log(data);
      },
    });
  });
  $(document).on('click', 'li.items', function () {
    $('li.items.active').removeClass('active');
    $(this).addClass('active');
  });
  $(document).on('click', 'li.song', function () {
    $('li.song.active').removeClass('active');
    $(this).addClass('active');
  });
}

$(main);
