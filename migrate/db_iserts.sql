USE jufisTube;
INSERT INTO `jufistube`.`genero`
(`nome_genero`,
`icone`,
`cor`)

VALUES
("rock", "", "red"),
("trap", "", "blue"),
("MPB", "", "#FACADA");

INSERT INTO `jufistube`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)

VALUES
("2zdiniz",
"03:30",
"faixa amarela",
"https://cdn-images.dzcdn.net/images/cover/c77e5c5fd4586f3ef42b6492fbf7de76/0x1900-000000-80-0-0.jpg",
"trap"),

("Charlie brown jr",
"03:40",
"é quente",
"https://i.scdn.co/image/ab67616d0000b2735e7cb9ed84348b98973c823f",
"rock"),

("gal costa",
"3:20",
"eternamente",
"https://cdn-images.dzcdn.net/images/cover/8baa68597787aa5333ece18b5f389693/1900x1900-000000-80-0-0.jpg",
"MPB");