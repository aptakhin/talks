
```bash
./shell/server.sh
./shell/pdf.sh
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

# CPU
python load/parsing-document-on-cpu-intensive-application.py


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
