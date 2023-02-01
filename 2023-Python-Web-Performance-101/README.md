
```bash
python3 -m http.server 4004
```

```bash
# Bootstrapping
DO_SSH_KEY_ID=...
doctl compute droplet create PyConFr2023 --image ubuntu-22-04-x64 --size s-2vcpu-4gb --region ams3 --ssh-keys $DO_SSH_KEY_ID --wait
doctl compute droplet get PyConFr2023
IP=...

ssh root@165.232.80.79

# CPU
python load/parsing-document-on-cpu-intensive-application.py


# Finishing
doctl compute droplet delete PyConFr2023 -f
```


```bash
# Make pdf
cd pdf
npx playwright test
```

```
poetry install
poetry shell
```
