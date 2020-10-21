## write_up

### web
- 販売停止しちゃったね
  - http://vitamin874.pythonanywhere.com/
  - curlコマンドでUserAgentを変更しpostするとflagが出る
  `curl http://vitamin874.pythonanywhere.com/ -A admin-d people=garbage
  `
  - wizCTF{WIZ_z4QXaWKP}
  
- 星
  - https://hidden-plateau-76804.herokuapp.com/
  - cookieの値を変更しページ開きなおすとflag出る
  - wizCTF{Variable_direct_cookie}