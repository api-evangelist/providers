---
aid: caddy
name: Caddy
description: Caddy is a modern, extensible, open-source web server and reverse proxy written in Go that provides automatic HTTPS via Let's Encrypt, a dynamic JSON-based admin API, a human-friendly Caddyfile configuration format, and a modular architecture with a rich ecosystem of plugins for authentication, observability, and custom behavior.
type: Index
x-type: opensource
position: Consumer
access: Open Source
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automatic HTTPS
  - Go
  - Load Balancer
  - Reverse Proxy
  - TLS
  - Web Server
url: https://raw.githubusercontent.com/api-evangelist/caddy/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: caddy:caddy-web-server
    name: Caddy Web Server
    description: Caddy is an open-source HTTP/2 and HTTP/3 web server and reverse proxy that obtains TLS certificates automatically via Let's Encrypt and ZeroSSL. Configured via a native JSON config, a human-friendly Caddyfile, or dynamically via the admin API. Built on a modular architecture that supports custom modules for virtually any HTTP behavior.
    humanURL: https://caddyserver.com/
    tags:
      - Automatic HTTPS
      - Go
      - Reverse Proxy
      - TLS
      - Web Server
    properties:
      - type: Documentation
        url: https://caddyserver.com/docs/
      - type: Getting Started
        url: https://caddyserver.com/docs/getting-started
      - type: GitHub Repository
        url: https://github.com/caddyserver/caddy
      - type: Download
        url: https://caddyserver.com/download
    x-features:
      - Automatic HTTPS via Let's Encrypt and ZeroSSL
      - HTTP/1.1, HTTP/2, HTTP/3 (QUIC) support
      - Dynamic JSON configuration
      - Human-friendly Caddyfile format
      - Reverse proxy with load balancing
      - Static file serving with automatic compression
      - Modular architecture with plugins
      - On-demand TLS certificates
      - Wildcard and DNS-01 challenge support
    x-use-cases:
      - Production web and API hosting
      - Zero-config HTTPS reverse proxy
      - Multi-tenant platforms with on-demand TLS
      - Static website hosting with SSL
      - Edge routing for microservices
  - aid: caddy:caddy-admin-api
    name: Caddy Admin API
    description: Caddy exposes a RESTful administration API on localhost:2019 by default for dynamically loading and modifying server configuration at runtime without restarts. Endpoints support loading full JSON configs, traversing and mutating specific config paths, adapting Caddyfile to JSON, and querying PKI and reverse proxy state.
    humanURL: https://caddyserver.com/docs/api
    baseURL: http://localhost:2019
    tags:
      - Admin API
      - Configuration
      - REST
    properties:
      - type: Documentation
        url: https://caddyserver.com/docs/api
      - type: JSON Config Structure
        url: https://caddyserver.com/docs/json/
      - type: Modules Reference
        url: https://caddyserver.com/docs/modules/
      - type: API Tutorial
        url: https://caddyserver.com/docs/api-tutorial
    x-features:
      - POST /load for full config replacement
      - GET/POST/PUT/PATCH/DELETE /config/[path] for granular updates
      - POST /adapt to convert Caddyfile to JSON without loading
      - POST /stop for graceful shutdown
      - GET /pki/ca/{id} for internal CA inspection
      - GET /reverse_proxy/upstreams for upstream status
      - ETag and If-Match concurrency control
    x-use-cases:
      - Dynamic configuration in orchestrated environments
      - Multi-tenant SaaS with per-tenant routes
      - Zero-downtime config changes
      - Integration with service discovery
      - Observability of upstream health
common:
  - type: Website
    url: https://caddyserver.com/
  - type: Documentation
    url: https://caddyserver.com/docs/
  - type: GitHub Organization
    url: https://github.com/caddyserver
  - type: Community Forum
    url: https://caddy.community/
  - type: Download
    url: https://caddyserver.com/download
  - type: Sponsors
    url: https://github.com/sponsors/mholt
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
