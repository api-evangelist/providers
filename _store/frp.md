---
aid: frp
name: frp
description: frp is an open-source fast reverse proxy that exposes services running behind a NAT or firewall to the public internet. Both the server (frps) and the client (frpc) include built-in HTTP admin APIs that operators can use to inspect runtime status, manage proxies and visitors, hot-reload configuration, and scrape Prometheus metrics.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open Source
created: '2026-03-27'
modified: '2026-04-28'
tags:
  - NAT Traversal
  - Reverse Proxy
  - Tunneling
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/frp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: frp:server-admin-api
    name: frp Server Admin API
    description: The frp server admin API is the HTTP control plane exposed by frps on its dashboard web server. It returns version and traffic information for the server, lists connected clients, lists and inspects active proxies of any type, returns daily traffic counters per proxy, and lets operators clear proxies that are offline. The API is secured with HTTP Basic auth using the dashboard user and password configured in the frps webServer block.
    humanURL: https://gofrp.org/en/docs/features/common/server-dashboard/
    baseURL: http://localhost:7500
    tags:
      - NAT Traversal
      - Reverse Proxy
      - Server Admin
      - Dashboard
    properties:
      - type: Documentation
        url: https://gofrp.org/en/docs/features/common/server-dashboard/
      - type: OpenAPI
        url: openapi/frp-server-admin-api-openapi.yml
  - aid: frp:client-admin-api
    name: frp Client Admin API
    description: The frp client admin API is the HTTP control plane exposed by frpc on its local web server. It supports hot-reloading the proxy and visitor configuration, stopping the running client, returning the active config, replacing the active config, querying per-proxy and per-visitor status, and (when a configuration store is enabled) listing, creating, updating, and deleting persisted proxy and visitor definitions. The API is secured with HTTP Basic auth using the user and password configured in the frpc webServer block.
    humanURL: https://gofrp.org/en/docs/reference/client-configures/
    baseURL: http://127.0.0.1:7400
    tags:
      - NAT Traversal
      - Reverse Proxy
      - Client Admin
      - Configuration
    properties:
      - type: Documentation
        url: https://gofrp.org/en/docs/reference/client-configures/
      - type: OpenAPI
        url: openapi/frp-client-admin-api-openapi.yml
common:
  - type: Website
    url: https://gofrp.org/
  - type: Documentation
    url: https://gofrp.org/en/docs/
  - type: GettingStarted
    url: https://gofrp.org/en/docs/setup/
  - type: SourceCode
    url: https://github.com/fatedier/frp
  - type: Issues
    url: https://github.com/fatedier/frp/issues
  - type: Releases
    url: https://github.com/fatedier/frp/releases
  - type: License
    url: https://github.com/fatedier/frp/blob/master/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
