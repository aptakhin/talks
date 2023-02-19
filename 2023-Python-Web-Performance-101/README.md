
```bash
./shell/server.sh

# for pdf
./shell/pdf.sh
# collect pdf files and create pdf and name it "2023-Python-Web-Performance-101" and move to root of repo
```

```bash
# Bootstrapping
doctl compute size list
doctl compute ssh-key list
DO_SSH_KEY_ID=...
doctl compute droplet create PyConFr2023 --image ubuntu-22-04-x64 --size m-2vcpu-16gb --region ams3 --ssh-keys $DO_SSH_KEY_ID --wait
doctl compute droplet get PyConFr2023
PERFORMANCE23IP=...

ssh root@PERFORMANCE23IP

python load/parsing-document-in-cpu-intensive-application.py
python load/parsing-document-in-ram-intensive-application.py


# Finishing
doctl compute droplet delete PyConFr2023 -f
```


```bash
# Make pdf
(cd pdf && npx playwright test)
```

```
poetry install
poetry shell
```
