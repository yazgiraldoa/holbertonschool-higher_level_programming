$(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';

  function translate () {
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data) {
      if (data.code !== 'none') {
        $('DIV#hello').text(data.hello);
      } else {
        $('DIV#hello').text('Non-supported language');
      }
    });
  }

  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});
