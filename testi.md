Johdanto
========

Käyttäjän huomioiminen suunnittelussa
=====================================

Ohjelmistot tarjoavat käyttäjälleen tietyn rajapinnan, jota käyttää.
Käyttäjän suorittaessa tehtäviä sovelluksen avulla, käyttäjä ja systeemi
ovat jatkuvassa vuorovaikutuksessa keskenään. Ohjelmistotuotannossa
järjestelmä nähdään kuitenkin herkästi kokoelmana toiminnallisuuksia.
Nämä toiminnallisuudet ja niihin liittyvät käsitteet pyritään
mallintamaan loogisesti ja teknisesti järkevällä tavalla.
Sovellusarkkitehti pyrkii abstraktoimaan käsitteet ja toiminnallisuudet
koneen käsittelytapaan sopivaan malliin. Tämä saattaa luoda käyttäjälle
vieraita rinnastuksia. Esimerkiksi yrityksellä ja henkilöllä voi
molemmilla olla nimi ja osoite, mutta käyttäjän mielessä näillä ei ole
mitään tekemistä toistensa kanssa, kun taas järjestelmässä ne voivat
olla periytetty samasta kantaluokasta. Toisaalta käyttäjän mielikuvissa
lähellä toisiaan olevilla käsitteillä ei järjestelmän kannalta ole
välttämättä muuta yhteistä kuin sijainti. Jos järjestelmän ja käyttäjien
vuorovaikutukseen ei kiinnitetä huomiota, järjestelmät suunnitellaan
tyypillisesti toteuttamaan kasa toimintoja ja vaikka tämä lähestymistapa
voi olla insinöörityön näkökulmasta tehokas, tehokkuus saavutetaan usein
järjestelmän käyttäjien kustannuksella \[Interaction design -beoynd
human-computer interaction\].

Ihmisen ja tietokoneen välinen vuorovaikutus (HCI) on osa suurempaa
kokonaisuutta \[Interaction design -beoynd human-computer interaction\],
jonka juuret juontavat tehdastyön tehokkuuden parantamisen tutkimiseen
1900 -luvun alussa <span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Grudin, 2012)", "formattedCitation": "(Grudin, 2012)", "previouslyFormattedCitation": "(Grudin, 2012)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "page": "1-40", "title": "A Moving Target \u2014 The Evolution of Human-Computer Interaction", "type": "article-journal", "issued": {"date-parts": [["2012"]]}, "author": [{"family": "Grudin", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Jonathan"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=7dc85ae6-9127-4956-afc8-74c9adff0fb7"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RND2EcUoHni6f"></span>Ihmisen
ja tietokoneen välinen vuorovaikutus (HCI) on osa suurempaa
kokonaisuutta \[Interaction design -beoynd human-computer interaction\],
jonka juuret juontavat tehdastyön tehokkuuden parantamisen tutkimiseen
1900 -luvun alussa (Grudin, 2012)⁠. Ihmisen ja tietokoneen välisen
vuorovaikutuksen tutkimisen tarve alkoi kasvaa tietokoneiden siirtyessä
80-luvulla yhä enemmän suuren, kouluttamattoman yleisön käytettäväksi
<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Grudin, 2012)", "formattedCitation": "(Grudin, 2012)", "previouslyFormattedCitation": "(Grudin, 2012)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "page": "1-40", "title": "A Moving Target \u2014 The Evolution of Human-Computer Interaction", "type": "article-journal", "issued": {"date-parts": [["2012"]]}, "author": [{"family": "Grudin", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Jonathan"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=7dc85ae6-9127-4956-afc8-74c9adff0fb7"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDxXPtIKjw98"></span>Ihmisen
ja tietokoneen välinen vuorovaikutus (HCI) on osa suurempaa
kokonaisuutta \[Interaction design -beoynd human-computer interaction\],
jonka juuret juontavat tehdastyön tehokkuuden parantamisen tutkimiseen
1900 -luvun alussa <span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Grudin, 2012)", "formattedCitation": "(Grudin, 2012)", "previouslyFormattedCitation": "(Grudin, 2012)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "page": "1-40", "title": "A Moving Target \u2014 The Evolution of Human-Computer Interaction", "type": "article-journal", "issued": {"date-parts": [["2012"]]}, "author": [{"family": "Grudin", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Jonathan"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=7dc85ae6-9127-4956-afc8-74c9adff0fb7"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RND2EcUoHni6f"></span>Ihmisen
ja tietokoneen välinen vuorovaikutus (HCI) on osa suurempaa
kokonaisuutta \[Interaction design -beoynd human-computer interaction\],
jonka juuret juontavat tehdastyön tehokkuuden parantamisen tutkimiseen
1900 -luvun alussa (Grudin, 2012)⁠. Ihmisen ja tietokoneen välisen
vuorovaikutuksen tutkimisen tarve alkoi kasvaa tietokoneiden siirtyessä
80-luvulla yhä enemmän suuren, kouluttamattoman yleisön käytettäväksi
(Grudin, 2012)⁠. Teknologisen kehityksen myötä 1990-luvulla tultiin
pisteeseen, jossa tuli realistiseksi ajatukseksi kehittää sovelluksia
kaikille ihmisille \[beoynd hci\]. Teknologinen kehitys on jatkunut
edelleen tietokoneiden siirryttyä yhä enemmän myös kodinkoneisiin ja
mukanamme kantamiin laitteisiin. Nykyisin vuorovaikutus tietokoneiden
kanssa on niin arkista, ettemme välttämättä edes ymmärrä käyttävämme
tietokoneita. Vuorovaikutuksen lisäätyminen ja arkipäiväistyminen on
tehnyt hyvästä suunnittelusta ja suunnittelumenetelmien käytöstä yhä
tärkeämpää. (Meneekö vähän ohi fokuksen?)

Ihmiskeskeinen suunnittelu
--------------------------

Ihmiskeskeinen suunnittelu (HCD = human-centered design) on vallitseva
lähestymistapa HCI -kehitykseen<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kuusinen, 2015)", "formattedCitation": "(Kuusinen, 2015)", "previouslyFormattedCitation": "(Kuusinen, 2015)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "issue": "November", "title": "Integrating UX Work in Agile Enterprise Software Development", "type": "book", "ISBN": "9789521536052", "issued": {"date-parts": [["2015"]]}, "author": [{"family": "Kuusinen", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kati"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=aa007c90-e73d-44f5-b983-f713f44ad332"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDOqrIn1Zdyv"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen(Kuusinen, 2015)⁠ . Ihmiskeskeisen suunnittelun lisäksi
käytetään myös sisällöltään lähes vastaavaa termiä käyttäjäkeskeinen
suunnittelu (UCD = user-centered design). Termejä käytetään tässä työssä
samassa merkityksessä, samoin kuin useissa työssä käytetyissä
lähteissä<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kujala, Roto, V\u00e4\u00e4n\u00e4nen-Vainio-Mattila, & Sinnel\u00e4, 2011)", "formattedCitation": "(Kujala, Roto, V\u00e4\u00e4n\u00e4nen-Vainio-Mattila, & Sinnel\u00e4, 2011)", "previouslyFormattedCitation": "(Kujala, Roto, V\u00e4\u00e4n\u00e4nen-Vainio-Mattila, & Sinnel\u00e4, 2011)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"ISSN": "9781450312806", "page": "17:1-17:8", "title": "Identifying hedonic factors in long-term user experience", "id": "ITEM-1", "abstract": "User experience (UX) arises from the user's interaction with a product and its pragmatic and hedonic (pleasure) qualities. Until recently, UX evaluation has focused mainly on examining short-term experiences. However, as the user-product relationship evolves over time, the hedonic aspects of UX eventually seem to gain more weight over the pragmatic aspects. To this end, we have developed a UX Curve method for evaluating long-term user experience, particularly the hedonic quality. In this paper, we present a study in which the UX Curve was used to retrospectively evaluate the UX of Facebook and mobile phones. The results show that compared to a questionnaire, the UX Curve method is more effective for identifying the hedonic aspects of UX. This method can be used by practitioners and researchers who want to understand evolving UX and to design better products. This straightforward method is especially suited for industrial contexts where resources are limited. &copy; 2011 ACM.", "issued": {"date-parts": [["2011"]]}, "type": "paper-conference", "ISBN": "9781450312806", "DOI": "10.1145/2347504.2347523", "author": [{"family": "Kujala", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Sari"}, {"family": "Roto", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Virpi"}, {"family": "V\u00e4\u00e4n\u00e4nen-Vainio-Mattila", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kaisa"}, {"family": "Sinnel\u00e4", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Arto"}], "container-title": "Proceedings of the 2011 Conference on Designing Pleasurable Products and Interfaces (DPPI '11)"}, "uris": ["http://www.mendeley.com/documents/?uuid=54ed3255-363a-45bc-8845-199d836c27c8"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RND6lk4flF7PI"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kuusinen, 2015)", "formattedCitation": "(Kuusinen, 2015)", "previouslyFormattedCitation": "(Kuusinen, 2015)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "issue": "November", "title": "Integrating UX Work in Agile Enterprise Software Development", "type": "book", "ISBN": "9789521536052", "issued": {"date-parts": [["2015"]]}, "author": [{"family": "Kuusinen", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kati"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=aa007c90-e73d-44f5-b983-f713f44ad332"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDOqrIn1Zdyv"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen(Kuusinen, 2015)⁠ . Ihmiskeskeisen suunnittelun lisäksi
käytetään myös sisällöltään lähes vastaavaa termiä käyttäjäkeskeinen
suunnittelu (UCD = user-centered design). Termejä käytetään tässä työssä
samassa merkityksessä, samoin kuin useissa työssä käytetyissä
lähteissä(Kujala, Roto, Väänänen-Vainio-Mattila, & Sinnelä, 2011)⁠<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Lepp\u00e4nen, 2016)", "formattedCitation": "(Lepp\u00e4nen, 2016)", "previouslyFormattedCitation": "(Lepp\u00e4nen, 2016)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "type": "article-journal", "issued": {"date-parts": [["2016"]]}, "author": [{"family": "Lepp\u00e4nen", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Tiia"}], "title": "Tiia lepp\u00e4nen hyvi\u00e4 k\u00e4yt\u00e4nt\u00f6j\u00e4 k\u00e4ytt\u00e4j\u00e4keskeisen suunnittelun integroimiseksi ketteriin ohjelmistokehitysprojekteihin"}, "uris": ["http://www.mendeley.com/documents/?uuid=9d500cb7-f3f7-409a-929c-dccf7add17fe"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDfAxifPvVu1"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kuusinen, 2015)", "formattedCitation": "(Kuusinen, 2015)", "previouslyFormattedCitation": "(Kuusinen, 2015)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "issue": "November", "title": "Integrating UX Work in Agile Enterprise Software Development", "type": "book", "ISBN": "9789521536052", "issued": {"date-parts": [["2015"]]}, "author": [{"family": "Kuusinen", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kati"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=aa007c90-e73d-44f5-b983-f713f44ad332"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDOqrIn1Zdyv"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen(Kuusinen, 2015)⁠ . Ihmiskeskeisen suunnittelun lisäksi
käytetään myös sisällöltään lähes vastaavaa termiä käyttäjäkeskeinen
suunnittelu (UCD = user-centered design). Termejä käytetään tässä työssä
samassa merkityksessä, samoin kuin useissa työssä käytetyissä
lähteissä<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kujala, Roto, V\u00e4\u00e4n\u00e4nen-Vainio-Mattila, & Sinnel\u00e4, 2011)", "formattedCitation": "(Kujala, Roto, V\u00e4\u00e4n\u00e4nen-Vainio-Mattila, & Sinnel\u00e4, 2011)", "previouslyFormattedCitation": "(Kujala, Roto, V\u00e4\u00e4n\u00e4nen-Vainio-Mattila, & Sinnel\u00e4, 2011)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"ISSN": "9781450312806", "page": "17:1-17:8", "title": "Identifying hedonic factors in long-term user experience", "id": "ITEM-1", "abstract": "User experience (UX) arises from the user's interaction with a product and its pragmatic and hedonic (pleasure) qualities. Until recently, UX evaluation has focused mainly on examining short-term experiences. However, as the user-product relationship evolves over time, the hedonic aspects of UX eventually seem to gain more weight over the pragmatic aspects. To this end, we have developed a UX Curve method for evaluating long-term user experience, particularly the hedonic quality. In this paper, we present a study in which the UX Curve was used to retrospectively evaluate the UX of Facebook and mobile phones. The results show that compared to a questionnaire, the UX Curve method is more effective for identifying the hedonic aspects of UX. This method can be used by practitioners and researchers who want to understand evolving UX and to design better products. This straightforward method is especially suited for industrial contexts where resources are limited. &copy; 2011 ACM.", "issued": {"date-parts": [["2011"]]}, "type": "paper-conference", "ISBN": "9781450312806", "DOI": "10.1145/2347504.2347523", "author": [{"family": "Kujala", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Sari"}, {"family": "Roto", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Virpi"}, {"family": "V\u00e4\u00e4n\u00e4nen-Vainio-Mattila", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kaisa"}, {"family": "Sinnel\u00e4", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Arto"}], "container-title": "Proceedings of the 2011 Conference on Designing Pleasurable Products and Interfaces (DPPI '11)"}, "uris": ["http://www.mendeley.com/documents/?uuid=54ed3255-363a-45bc-8845-199d836c27c8"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RND6lk4flF7PI"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kuusinen, 2015)", "formattedCitation": "(Kuusinen, 2015)", "previouslyFormattedCitation": "(Kuusinen, 2015)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"id": "ITEM-1", "issue": "November", "title": "Integrating UX Work in Agile Enterprise Software Development", "type": "book", "ISBN": "9789521536052", "issued": {"date-parts": [["2015"]]}, "author": [{"family": "Kuusinen", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kati"}]}, "uris": ["http://www.mendeley.com/documents/?uuid=aa007c90-e73d-44f5-b983-f713f44ad332"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDOqrIn1Zdyv"></span>Ihmiskeskeinen
suunnittelu (HCD = human-centered design) on vallitseva lähestymistapa
HCI -kehitykseen(Kuusinen, 2015)⁠ . Ihmiskeskeisen suunnittelun lisäksi
käytetään myös sisällöltään lähes vastaavaa termiä käyttäjäkeskeinen
suunnittelu (UCD = user-centered design). Termejä käytetään tässä työssä
samassa merkityksessä, samoin kuin useissa työssä käytetyissä
lähteissä(Kujala, Roto, Väänänen-Vainio-Mattila, & Sinnelä,
2011)⁠(Leppänen, 2016)⁠ Ihmiskeskeinen suunnittelu on määritelty ISO
9241 -standardissa vuodelta 2010, jossa on ohjeita ihmiskeskeisten
suunnittelumenetelmien käyttöön tietokonepohjaisia vuorovaikutteisia
järjestelmiä varten koko systeemin elinajalle. Standardi määrittelee
ihmiskeskeisen suunnittelun *vuorovaikutteisten systeemien kehittämisen
lähestymistavaksi, jonka tavoitteena on tehdä järjestelmistä käytettäviä
ja hyödyllisiä keskittymällä käyttäjiin, heidän tarpeisiinsa ja
vaatimuksiinsa. Suunnittelussa otetaan huomioon inhimilliset tekijät,
ergonomia, tietämys käytettävyydestä ja käytettävyystekniikat. (ISO
9241-210:2010)*

Standardi määrittelee kuusi yleistä ihmiskeskeisen suunnittelun
periaatetta, jotka eivät liity mihinkään erityiseen kehityssyklin
vaiheeseen, 1) suunnittelu pohjautuu käyttäjien ja tehtävien vaatimukset
hyvään ymmärtämiseen 2) käyttäjät osallistuvat kehitykseen suunnittelun
ja kehitystyön aikana, 3) käyttäjäkeskeinen evaluaatio ohjaa ja hioo
suunnitteluratkaisuja ( the design is driven and refined by user-centred
evaluation), 4) suunnitteluratkaisuja iteroidaan 5) suunnittelussa
huomioidaan koko käyttäjäkokemus ja 6) suunnittelussa käytetään
poikkitieteellisesti useiden eri sovellusalueiden menetelmiä ja
näkökulmia. Standardin ytimenä on käyttäjäkeskeisten
suunnitteluaktiviteettien esittely. <span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Jokela, Iivari, Matero, & Karukka, 2003)", "formattedCitation": "(Jokela, Iivari, Matero, & Karukka, 2003)", "previouslyFormattedCitation": "(Jokela, Iivari, Matero, & Karukka, 2003)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"abstract": "ISO 9241-11 and ISO 13407 are two important standards related to usability: the former one provides the definition of usability and the latter one guidance for designing usability. We carried out an interpretative analysis of ISO 13407 from the viewpoint of the standard definition of usability from ISO 9241-11. The results show that ISO 13407 provides only partly guidance for designing usability as presumed by the definition. Guidance for describing users and environments are provided but very limited guidance is provided for the descriptions of user goals and usability measures, and generally for the process of producing the various outcomes.", "page": "53-60", "title": "The Standard of User-Centered Design and the Standard Definition of Usability : Analyzing ISO 13407 against ISO 9241-11", "id": "ITEM-1", "issued": {"date-parts": [["2003"]]}, "type": "article-journal", "ISBN": "9781450343244", "DOI": "10.1145/944519.944525", "author": [{"family": "Jokela", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Timo"}, {"family": "Iivari", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Netta"}, {"family": "Matero", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Juha"}, {"family": "Karukka", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Minna"}], "volume": "46", "container-title": "Design"}, "uris": ["http://www.mendeley.com/documents/?uuid=98a64631-18aa-41a0-bdde-935a9c9f65e5"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDcodgd6dcLu"></span>Standardi
määrittelee kuusi yleistä ihmiskeskeisen suunnittelun periaatetta, jotka
eivät liity mihinkään erityiseen kehityssyklin vaiheeseen, 1)
suunnittelu pohjautuu käyttäjien ja tehtävien vaatimukset hyvään
ymmärtämiseen 2) käyttäjät osallistuvat kehitykseen suunnittelun ja
kehitystyön aikana, 3) käyttäjäkeskeinen evaluaatio ohjaa ja hioo
suunnitteluratkaisuja ( the design is driven and refined by user-centred
evaluation), 4) suunnitteluratkaisuja iteroidaan 5) suunnittelussa
huomioidaan koko käyttäjäkokemus ja 6) suunnittelussa käytetään
poikkitieteellisesti useiden eri sovellusalueiden menetelmiä ja
näkökulmia. Standardin ytimenä on käyttäjäkeskeisten
suunnitteluaktiviteettien esittely. (Jokela, Iivari, Matero, & Karukka,
2003)⁠

Prosessi alkaa ihmiskeskeisen suunnittelun tarpeen tunnistamisesta.
Tämän jälkeen siirrytään luomaan iteroimalla ratkaisua, joka tyydyttää
sekä käyttäjän, että organisaation vaatimukset. Iteraatiosyklissä on
neljä vaihetta. Ensimmäiseksi täytyy ymmärtää ja täsmentää
käyttökonteksti. Tämä tarkoittaa käyttäjän ja käyttöympäristön
tuntemista, sekä käyttäjän tehtävien tuntemista.<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kujala et al., 2011)", "formattedCitation": "(Kujala et al., 2011)", "previouslyFormattedCitation": "(Kujala et al., 2011)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"ISSN": "9781450312806", "page": "17:1-17:8", "title": "Identifying hedonic factors in long-term user experience", "id": "ITEM-1", "abstract": "User experience (UX) arises from the user's interaction with a product and its pragmatic and hedonic (pleasure) qualities. Until recently, UX evaluation has focused mainly on examining short-term experiences. However, as the user-product relationship evolves over time, the hedonic aspects of UX eventually seem to gain more weight over the pragmatic aspects. To this end, we have developed a UX Curve method for evaluating long-term user experience, particularly the hedonic quality. In this paper, we present a study in which the UX Curve was used to retrospectively evaluate the UX of Facebook and mobile phones. The results show that compared to a questionnaire, the UX Curve method is more effective for identifying the hedonic aspects of UX. This method can be used by practitioners and researchers who want to understand evolving UX and to design better products. This straightforward method is especially suited for industrial contexts where resources are limited. &copy; 2011 ACM.", "issued": {"date-parts": [["2011"]]}, "type": "paper-conference", "ISBN": "9781450312806", "DOI": "10.1145/2347504.2347523", "author": [{"family": "Kujala", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Sari"}, {"family": "Roto", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Virpi"}, {"family": "V\u00e4\u00e4n\u00e4nen-Vainio-Mattila", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kaisa"}, {"family": "Sinnel\u00e4", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Arto"}], "container-title": "Proceedings of the 2011 Conference on Designing Pleasurable Products and Interfaces (DPPI '11)"}, "uris": ["http://www.mendeley.com/documents/?uuid=54ed3255-363a-45bc-8845-199d836c27c8"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RND4Zfb63iTmW"></span>Prosessi
alkaa ihmiskeskeisen suunnittelun tarpeen tunnistamisesta. Tämän jälkeen
siirrytään luomaan iteroimalla ratkaisua, joka tyydyttää sekä käyttäjän,
että organisaation vaatimukset. Iteraatiosyklissä on neljä vaihetta.
Ensimmäiseksi täytyy ymmärtää ja täsmentää käyttökonteksti. Tämä
tarkoittaa käyttäjän ja käyttöympäristön tuntemista, sekä käyttäjän
tehtävien tuntemista.(Kujala et al., 2011)⁠ Oleellista tietoa
käyttäjistä voi olla esimerkiksi käyttäjien taidot, koulutus ja kokemus.
Sovelluksesta riippuen myös käyttäjän fyysisillä ominaisuuksilla,
tavoilla, mieltymyksillä ja muilla kyvyillä voi olla merkitystä. Jos on
tarpeellista käyttäjien ominaisuudet voidaan määritellä
käyttäjätyypeittäin. Esimerkiksi sovelluksen ylläpitäjällä voi olla
erilaiset taidot kuin sovelluksen loppukäyttäjällä. Käyttäjien
tehtävistä pitäisi tietää myös tehtävän kesto ja se kuinka usein
tehtävää suoritetaan. Lisäksi kuvauksesta tulisi käydä ilmi käyttäjän
lopulliset tavoitteet, miksi käyttäjä käyttää järjestelmää. Tehtäviä ei
tulisi kuvailla pelkästään sovelluksen toiminnallisuuksien tai
ominaisuuksien kautta. Käyttöympäristöön kuuluu käytettyjen laitteiden
ja ohjelmistojen lisäksi myös fyysinen ja sosiaalinen ympäristö, jossa
tuotetta tullaan käyttämään. Käyttöympäristön kannalta oleellisia voivat
olla myös tuotteen käyttöön liittyvät lait tai kulttuuriset tekijät.
\[ISO-standardi\]

Seuraavaksi määritellään käyttäjän ja organisaation vaatimukset.
Vaatimuksissa tulisi määritellä käyttäjät ja muut suunnitteluun
oleellisesti liittyvät henkilöt, esittää selkeästi ihmiskeskeiset
suunnittelutavoitteet ja priorisoida vaatimukset, Vaatimuksia tehtäessä
tulee ottaa huomioon useita erityyppisiä asioita käyttäjien suorittamien
tehtävien lisäksi, kuten lainsäädännöstä tulevat vaatimukset,
liiketoiminnan asettamat vaatimukset, ylläpidettävyys ja käyttäjien
koulutus. Tuotteen käytettävyydelle määritellään vaatimusten pohjalta
onnistumiskriteerit. Kriteerit määritellään käyttäjän tehtävittäin.
Esimerkkinä voisi olla kriteeri, että kuinka nopeasti tyypillinen
käyttäjä pystyy tallentamaan lisäämänsä tiedot. Kriteerien tulee olla
sellaisia, että niiden toteutumista voidaan mitata. Kerätyt vaatimukset
ja niiden onnistumiskriteerit varmistetaan käyttäjiltä. Myös riittävästä
dokumentaatiosta tulee huolehtia.<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kujala et al., 2011)", "formattedCitation": "(Kujala et al., 2011)", "previouslyFormattedCitation": "(Kujala et al., 2011)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"ISSN": "9781450312806", "page": "17:1-17:8", "title": "Identifying hedonic factors in long-term user experience", "id": "ITEM-1", "abstract": "User experience (UX) arises from the user's interaction with a product and its pragmatic and hedonic (pleasure) qualities. Until recently, UX evaluation has focused mainly on examining short-term experiences. However, as the user-product relationship evolves over time, the hedonic aspects of UX eventually seem to gain more weight over the pragmatic aspects. To this end, we have developed a UX Curve method for evaluating long-term user experience, particularly the hedonic quality. In this paper, we present a study in which the UX Curve was used to retrospectively evaluate the UX of Facebook and mobile phones. The results show that compared to a questionnaire, the UX Curve method is more effective for identifying the hedonic aspects of UX. This method can be used by practitioners and researchers who want to understand evolving UX and to design better products. This straightforward method is especially suited for industrial contexts where resources are limited. &copy; 2011 ACM.", "issued": {"date-parts": [["2011"]]}, "type": "paper-conference", "ISBN": "9781450312806", "DOI": "10.1145/2347504.2347523", "author": [{"family": "Kujala", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Sari"}, {"family": "Roto", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Virpi"}, {"family": "V\u00e4\u00e4n\u00e4nen-Vainio-Mattila", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kaisa"}, {"family": "Sinnel\u00e4", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Arto"}], "container-title": "Proceedings of the 2011 Conference on Designing Pleasurable Products and Interfaces (DPPI '11)"}, "uris": ["http://www.mendeley.com/documents/?uuid=54ed3255-363a-45bc-8845-199d836c27c8"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDySOP07hIcu"></span>Seuraavaksi
määritellään käyttäjän ja organisaation vaatimukset. Vaatimuksissa
tulisi määritellä käyttäjät ja muut suunnitteluun oleellisesti liittyvät
henkilöt, esittää selkeästi ihmiskeskeiset suunnittelutavoitteet ja
priorisoida vaatimukset, Vaatimuksia tehtäessä tulee ottaa huomioon
useita erityyppisiä asioita käyttäjien suorittamien tehtävien lisäksi,
kuten lainsäädännöstä tulevat vaatimukset, liiketoiminnan asettamat
vaatimukset, ylläpidettävyys ja käyttäjien koulutus. Tuotteen
käytettävyydelle määritellään vaatimusten pohjalta onnistumiskriteerit.
Kriteerit määritellään käyttäjän tehtävittäin. Esimerkkinä voisi olla
kriteeri, että kuinka nopeasti tyypillinen käyttäjä pystyy tallentamaan
lisäämänsä tiedot. Kriteerien tulee olla sellaisia, että niiden
toteutumista voidaan mitata. Kerätyt vaatimukset ja niiden
onnistumiskriteerit varmistetaan käyttäjiltä. Myös riittävästä
dokumentaatiosta tulee huolehtia.(Kujala et al., 2011)⁠ Standardi\]

Seuraavassa vaiheessa tuotetaan suunnitteluratkaisut kerätyn tiedon
pohjalta. Viimeisessä iteraation vaiheessa suunnitteluratkaisut
evaluoidaan luotuja vaatimuksia vasten. Jos suunnitteluratkaisu ei täytä
vielä vaatimuksia, aloitetaan seuraava iteraatiosykli. Iterointia
jatketaan, kunnes vaatimukset on saavutettu. \[\]

Ihmiskeskeisen suunnittelun filosofia on yksinkertainen: käyttäjät
tietävät parhaiten omat tarpeensa, tavoitteensa ja mieltymyksensä
\[Designing for interaction\] Suunnittelijan tehtäväksi jää selvittää ne
ja suunnitella käyttäjien tarpeet täyttäviä järjestelmiä. Endsleyn
(2016) mukaan tämä ei kuitenkaan tarkoita, että käyttäjiltä
kysyttäisiin, että mitä he tarvitsevat ja sen antamista käyttäjille.
Ensinnäkin käyttäjät tietävät usein vain osittain, mitä he haluavat
verrattuna nykytilanteeseen. Käyttäjillä on yleensä myös hyvin
rajoittunut käsitys siitä, kuinka nämä tarpeet voidaan tehokkaasti
toteuttaa käyttöliittymässä. Lisäksi Endsleyn mukaan useimmilla
systeemeillä on useita eri käyttäjiä, joilla on kaikilla omat
käsityksensä siitä, mitä he haluaisivat toteutettavan järjestelmään.
Tuloksena on suunnitteluratkaisuja, jotka ovat tyypillisesti satunnaisia
ja epäsäännönmukaisia käyttöliittymässä. Lisäksi Endsley huomauttaa,
että useita suunnitteluvirheitä ei huomata. <span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Endsley, 2016)", "formattedCitation": "(Endsley, 2016)", "previouslyFormattedCitation": "(Endsley, 2016)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"publisher": "CRC Press", "ISSN": "1759-4774", "id": "ITEM-1", "type": "book", "ISBN": "9781420063585", "issued": {"date-parts": [["2016", "7", "10"]]}, "container-title": "Design", "author": [{"family": "Endsley", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Mica R"}], "abstract": "Enhancing situational awareness (SA) is a major design goal for projects in many fields, including aviation, ground transportation, air traffic control, nuclear power, medicine, space and systems maintenance, but little information exists in an integral format to support this. Designing for Situation Awareness is directed at human factors researchers and practitioners who are engaged in designing systems to support Situation Awareness (SA) in a wide variety of areas and is liberally illustrated with actual design examples. It requires that designers understand how people acquire and interpret information in such worlds and appreciate the factors that undermine this process.", "edition": "2nd", "title": "Designing for Situation Awareness: An Approach to User-Centered Design, Second Edition", "number-of-pages": "30-34", "PMID": "25421280", "DOI": "10.1201/9780203485088"}, "uris": ["http://www.mendeley.com/documents/?uuid=7e0a26ec-cd5c-43ca-99a5-ce39fed25427"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RND0exyRJATZO"></span>Ihmiskeskeisen
suunnittelun filosofia on yksinkertainen: käyttäjät tietävät parhaiten
omat tarpeensa, tavoitteensa ja mieltymyksensä \[Designing for
interaction\] Suunnittelijan tehtäväksi jää selvittää ne ja suunnitella
käyttäjien tarpeet täyttäviä järjestelmiä. Endsleyn (2016) mukaan tämä
ei kuitenkaan tarkoita, että käyttäjiltä kysyttäisiin, että mitä he
tarvitsevat ja sen antamista käyttäjille. Ensinnäkin käyttäjät tietävät
usein vain osittain, mitä he haluavat verrattuna nykytilanteeseen.
Käyttäjillä on yleensä myös hyvin rajoittunut käsitys siitä, kuinka nämä
tarpeet voidaan tehokkaasti toteuttaa käyttöliittymässä. Lisäksi
Endsleyn mukaan useimmilla systeemeillä on useita eri käyttäjiä, joilla
on kaikilla omat käsityksensä siitä, mitä he haluaisivat toteutettavan
järjestelmään. Tuloksena on suunnitteluratkaisuja, jotka ovat
tyypillisesti satunnaisia ja epäsäännönmukaisia käyttöliittymässä.
Lisäksi Endsley huomauttaa, että useita suunnitteluvirheitä ei huomata.
(Endsley, 2016)⁠

Käytettävyys ja käyttäjäkokemus
-------------------------------

Jotta voitaisiin ymmärtää, mitä käyttäjäkeskeisellä suunnittelulla
haetaan, on hyvä ymmärtää peruskäsitteet käytettävyys ja
käyttäjäkokemus. Käytettävyys on yksi ohjelmiston laadullinen ominaisuus
samoin kuin toimivuus, tehokkuus tai ylläpidettävyys<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kujala et al., 2011)", "formattedCitation": "(Kujala et al., 2011)", "previouslyFormattedCitation": "(Kujala et al., 2011)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"ISSN": "9781450312806", "page": "17:1-17:8", "title": "Identifying hedonic factors in long-term user experience", "id": "ITEM-1", "abstract": "User experience (UX) arises from the user's interaction with a product and its pragmatic and hedonic (pleasure) qualities. Until recently, UX evaluation has focused mainly on examining short-term experiences. However, as the user-product relationship evolves over time, the hedonic aspects of UX eventually seem to gain more weight over the pragmatic aspects. To this end, we have developed a UX Curve method for evaluating long-term user experience, particularly the hedonic quality. In this paper, we present a study in which the UX Curve was used to retrospectively evaluate the UX of Facebook and mobile phones. The results show that compared to a questionnaire, the UX Curve method is more effective for identifying the hedonic aspects of UX. This method can be used by practitioners and researchers who want to understand evolving UX and to design better products. This straightforward method is especially suited for industrial contexts where resources are limited. &copy; 2011 ACM.", "issued": {"date-parts": [["2011"]]}, "type": "paper-conference", "ISBN": "9781450312806", "DOI": "10.1145/2347504.2347523", "author": [{"family": "Kujala", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Sari"}, {"family": "Roto", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Virpi"}, {"family": "V\u00e4\u00e4n\u00e4nen-Vainio-Mattila", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kaisa"}, {"family": "Sinnel\u00e4", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Arto"}], "container-title": "Proceedings of the 2011 Conference on Designing Pleasurable Products and Interfaces (DPPI '11)"}, "uris": ["http://www.mendeley.com/documents/?uuid=54ed3255-363a-45bc-8845-199d836c27c8"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDl4ZB5MfCNN"></span>Jotta
voitaisiin ymmärtää, mitä käyttäjäkeskeisellä suunnittelulla haetaan, on
hyvä ymmärtää peruskäsitteet käytettävyys ja käyttäjäkokemus.
Käytettävyys on yksi ohjelmiston laadullinen ominaisuus samoin kuin
toimivuus, tehokkuus tai ylläpidettävyys(Kujala et al., 2011)⁠ .
Määriteltäessä ohjelmiston laatuvaatimuksia, myös
käytettävyysvaatimukset tulisi määritellä.

 Käytettävyys määritellään ISO-9241-standardin mukaan sinä
“vaikuttavuutena, tehokkuutena ja tyytyväisyytenä, joilla palvelulle
määritellyt käyttäjät saavuttavat määritellyt tavoitteet tietyssä
ympäristössä”. Vaikuttavuudella tarkoitetaan sitä tarkkuutta ja
täydellisyyttä, millä käyttäjät saavuttavat määritellyt tavoitteet.
Tehokkuudella tarkoitetaan sitä kuinka paljon resursseja tavoitteiden
saavuttamiseen joudutaan käyttämään. Tyytyväisyydellä tarkoitetaan
käyttäjän tyytyväisyyttä laitteen tai järjestelmän käyttöön,
vuorovaikutuksen sujuvuuteen ja saavutettuihin tuloksiin. (ISO-standardi
9241-11, 1998)

Toinen suosittu käytettävyyden määritelmä on alan pioneerin Jacob
Nielsenin () määritelmä, joka jakaa käytettävyyden viiteen eri
komponenttiin:

1\) opittavuus, eli kuinka helppoa käyttäjien on suorittaa tavallisia
toimenpiteitä ensimmäisellä käyttökerralla,

2\) tehokkuus, eli kuinka nopeasti käyttäjät, jotka ovat oppineet
käyttämään järjestelmää, pystyvät suoriutumaan tehtävistään,

3\) muistettavuus, eli kuinka nopeasti käyttäjät pystyvät käyttämään
järjestelmää jälleen tehokkaasti tauon jälkeen, 

4\) kuinka paljon virheitä käyttäjät tekevät, kuinka vakavia nämä virheet
ovat ja kuinka helppo niistä on toipua,

5\) kuinka miellyttävää käyttö on.

Nielsenin määritelmässä käytettävyys-käsitteessä on ISO-standardiin
verrattuna lisätty aikaulottuvuus. Nielsenin määritelmässä käytettävyys
on suure, joka voi muuttua ajan kuluessa, kun käyttäjä oppii käyttämään
järjestelmää tai pitää taukoa järjestelmän käytöstä.

ISO-9241-210 mukaan käyttäjäkokemus sisältää henkilön käsitykset ja
reaktiot, jotka ovat seurausta tuotteen, järjestelmän tai palvelun
käytöstä tai odotetusta käytöstä \[ISO-9241-210\]. Käyttäjäkokemus
koostuu käyttäjän tunteista, uskomuksista, mieltymyksistä, fyysisistä ja
psyykkisistä vasteista, käyttäytymisestä ja aikaansaannoksista, jotka
syntyvät ennen käyttöä, käytön aikana ja käytön jälkeen. Käyttäjäkokemus
sisältää sekä kokemuksen käytännölliset tekijät, että nautinnolliset
tekijät.

Käytännölliset ominaisuudet liittyvät käyttäjän tarpeeseen suorittaa
tietyt tehtävät. Sitä vastoin nautinnollisilla ominaisuuksilla, kuten
esteettisyydellä, innovatisuudella ja omaleimaisuudella, ei ole
varsinaisesti tekemistä tehtävän suorittamisen kanssa. Pitkässä käytössä
nautinnolliset tekijät vaikuttavat olevan tärkeämpiä käyttäjäkokemuksen
kannalta kuin käytännölliset tekijät.<span
id="ADDIN CSL_CITATION {"properties": {"noteIndex": 0}, "mendeley": {"plainTextFormattedCitation": "(Kujala et al., 2011)", "formattedCitation": "(Kujala et al., 2011)"}, "citationItems": [{"id": "ITEM-1", "itemData": {"ISSN": "9781450312806", "page": "17:1-17:8", "title": "Identifying hedonic factors in long-term user experience", "id": "ITEM-1", "abstract": "User experience (UX) arises from the user's interaction with a product and its pragmatic and hedonic (pleasure) qualities. Until recently, UX evaluation has focused mainly on examining short-term experiences. However, as the user-product relationship evolves over time, the hedonic aspects of UX eventually seem to gain more weight over the pragmatic aspects. To this end, we have developed a UX Curve method for evaluating long-term user experience, particularly the hedonic quality. In this paper, we present a study in which the UX Curve was used to retrospectively evaluate the UX of Facebook and mobile phones. The results show that compared to a questionnaire, the UX Curve method is more effective for identifying the hedonic aspects of UX. This method can be used by practitioners and researchers who want to understand evolving UX and to design better products. This straightforward method is especially suited for industrial contexts where resources are limited. &copy; 2011 ACM.", "issued": {"date-parts": [["2011"]]}, "type": "paper-conference", "ISBN": "9781450312806", "DOI": "10.1145/2347504.2347523", "author": [{"family": "Kujala", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Sari"}, {"family": "Roto", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Virpi"}, {"family": "V\u00e4\u00e4n\u00e4nen-Vainio-Mattila", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Kaisa"}, {"family": "Sinnel\u00e4", "parse-names": false, "suffix": "", "non-dropping-particle": "", "dropping-particle": "", "given": "Arto"}], "container-title": "Proceedings of the 2011 Conference on Designing Pleasurable Products and Interfaces (DPPI '11)"}, "uris": ["http://www.mendeley.com/documents/?uuid=54ed3255-363a-45bc-8845-199d836c27c8"]}], "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"} RNDdmtJX3Weq0"></span>Käytännölliset
ominaisuudet liittyvät käyttäjän tarpeeseen suorittaa tietyt tehtävät.
Sitä vastoin nautinnollisilla ominaisuuksilla, kuten esteettisyydellä,
innovatisuudella ja omaleimaisuudella, ei ole varsinaisesti tekemistä
tehtävän suorittamisen kanssa. Pitkässä käytössä nautinnolliset tekijät
vaikuttavat olevan tärkeämpiä käyttäjäkokemuksen kannalta kuin
käytännölliset tekijät.(Kujala et al., 2011)

 Samoin kuin käytettävyyden ISO-standardin mukainen määritelmä, myöskään
tämä määritelmä ei tuo esiin sitä, että käyttäjäkokemus kestää koko
tuotteen käyttämisen ajan ja voi muuttua käytön aikana esimerkiksi
alkuinnostuksesta tuskastumiseen tai päinvastoin.

Usein kehittäjän, joka näkee konepellin alla toimivat syy ja seuraus
-suhteet, voi olla vaikea ymmärtää käyttäjän näkemystä asiasta.


