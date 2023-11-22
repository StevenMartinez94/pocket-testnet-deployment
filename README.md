# pocket-testnet-deployment
Repo for pocket-core support infrastructure deployments

## Run Testnet validators/seeds/fullnodes
1- Edit each `chains.json` file as required by your own infra.
2- Set up env variables for `traefik` config, `prometheus` config and services from `docker-compose.yaml`.
3- Run:

```
envsubst < traefik/services/services.yaml.template > traefik/services/services.yaml
envsubst < monitoring/prometheus/prometheus.yaml.template > monitoring/prometheus/prometheus.yaml
envsubst < docker-compose.yaml.template > docker-compose.yaml
```

4- Run `docker-compose up -d {service}`.
5- There you go.


## Run Testnet Faucet
1- Edit the `.env.example` file and rename it as .`env`.
2- Go to Testnet Faucet folder and run `docker-compose up -d`.

## Run Testnet State Backup Bot
1- Edit the `.env.example` file and rename it as .`env`.
2- Go to Testnet Backup Bot folder and run `docker-compose up -d`.

