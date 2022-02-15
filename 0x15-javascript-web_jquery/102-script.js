$(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data) {
      if (data.code !== 'none') {
        $('DIV#hello').text(data.hello);
      } else {
        $('DIV#hello').text('Non-supported language');
      }
    });
  });
});
