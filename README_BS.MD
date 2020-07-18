# Prikupiti oglase za posao **python.org/jobs**

Ova aplikacija prikazuje kako se na jednostavan način mogu prikupiti podaci sa neke web stranice.

U primjeru je korištena _python.org_ kao izvor podataka.

Svaka web stranice ima tri osnovne komponente (taga) **html**, **head**, **body**

Primjer osnovne strukture _.html_ dokumenta:

```
<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p>This is an example paragraph. Anything in the <strong>body</strong> tag will appear on the page, just like this <strong>p</strong> tag and its contents.</p>
  </body>
</html>
```

Sadžaj strnice se uvijek nalazi unuar _body_ taga. Kako je organizovan sadržaj unutar _body_ taga zavisi od svake stranice zasebno. 

U ovom primjeru bit će pokazana organizacije _python.org/jobs_ stranice. Dijelovi koji su nepotrebni biti će izostavljeni.

Organizacija _python.org/jobs_ stranice:

![Organizacija](img/jobsOrganisation.png)

Trenutno nas zanima samo sadržaj pa ćemo zanemariti ostalo.

Slika ispod pokazuje ogranizaciju **body** taga
![Body tag organisation](img/bodyOrganisation.png)

u ovom slučju nas **scripts** tag ne zanima pa ćemo ga zanemariti. Pored **scripts**  taga na istom nivou nalazi se `<div id="touchnav-wraper>"`, pa ćemo zaviriti unutar njega da vidimo šta se nalazi.

![Touchnav wraper](img/touchnav-wraper.png)

Kao što se može vidjeti na slici iznad unutar ovog taga se nali sada nekoliko novih. Kada se dođe mišem na svaki od ovih tagova, dio stranice koji odgovara ovom tgagu biti će označen. Kao na primjer:

![Footer](img/footer.png)

Na slici iznad smo došli mišem na footer i on nam je označen, međutim unutar footera se ne nalze informacije koje mi tražimo pa ga možemo ignorisati.

Nama je potreba sadržaj stranice pa ćemo doći preko taga koji ima `id="content"`.

![Content](img/content.png)

Dolaskom pokazivačem miša iznad taga `<div id="content">` označen je dio dokumenta u kojem se nalazi sadržaj od interesa. 

U narednom koraku je potrebno pogledati šta se nalazi unutar `<div id="content">` taga.

![Content tag](img/content_tag.png)

Sada je već potrbno dobro obratiti pažnju na sadržaj ovog tga.

Prvo što je bitno prikupljanje traženih podataka jeste `<ol class="list-recent-jobs list-row-contaner menu">...</ol>` tag.

Unutar ovog taga nalazi se lista sa objavljenim oglasima za posao (u ovoj listi se nalaze svi traženi podaci).

I druga stvar koju je bitno odma spomenuti jeste
`<ul class="pagination menu"...</ul>`.
Unutar ovog taga nalaze se lista stranice (broj stranice u podnožju). Kao što je prikazano na slici ispd.

![Brojevi stranice](img/pageNumbers.png)

Budući da ima veliki broj oglasa i oni su podijeljeni u nekoliko stranica korištenjem linka za **Next** ići se na sljedeću stranicu.

Procedura je sljedeća:
1. Pokupiti podatke iz svih postavljenih oglasa.
2. Otići na link next kako bi se prešlo na sljedeću stranicu koja sadrži oglse

Ova pocedura se ponavlja sve dok se ne prođe kroz sve stranice.

## Lista sa oglasima