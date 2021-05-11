%rebase('base.tpl', naslov='Igra vislic')
<h1>{{igra.pravilni_del_gesla()}}</h1>

Nepravilne črke: {{igra.nepravilni_ugibi()}} <br/>
Stopnja obešenosti: {{igra.stevilo_napak()}}

% if igra.zmaga():
<h1>Čestitke, uganila si geslo {{igra.geslo}}!</h1>

% elif igra.poraz():
<h1>Geslo je bilo {{igra.geslo}}, več sreče prihodnjič.</h>

% else:
<form method="post" action="">
<input name="crka" /> <input type="submit" value="Ugibaj"/>
</form>

% end
