# update-firebrick-lns-graph

Updates a Firebrick graph from the LNS address from a RouterOS router's pppoe-client

## Usage

- install deps with pipenv
- create config.yaml
- run (probably on cron!)

## config example

```yaml
router:
  host: 192.168.1.1
  username: some-username-here
  password: some-password-here
  pppoe-interface: pppoe1

firebrick:
  uri: https://your-firebrick-here
  username: some-username-here
  password: some-password-here
  graph: pppoe-lns
```