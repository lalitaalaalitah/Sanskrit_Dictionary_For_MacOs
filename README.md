# Sanskrit_Dictionary_For_MacOs

Add some css code from this site for Mac Os Mojave : https://eclecticlight.co/2018/10/04/make-mojave-custom-dictionaries-work-better/
This must go to DefaultStyle.css of the dictionary.
@media (prefers-dark-interface)
{
html {
-apple-color-filter: apple-invert-lightness();
}
a {
-apple-color-filter: none;
color: -webkit-link;
}
img {
filter: invert(100%);
}
}
