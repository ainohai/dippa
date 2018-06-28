git pull
#turn odt-document into html doc
pandoc ./dippa.odt -o ./testi.html
sleep 10
#splice different chapters into differerent files compatiple with wordpress github sync.
python test.py
sleep 20
git add .
git commit -m "Automatically adding post data to git."
git push