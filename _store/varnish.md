---
aid: varnish
name: Varnish Cache
description: Varnish Cache is a high-performance HTTP accelerator and reverse proxy designed for content-heavy dynamic websites and APIs. It sits in front of web servers and caches HTTP responses to serve repeated requests without hitting the backend, dramatically reducing load and latency. Varnish is configured via VCL (Varnish Configuration Language), a domain-specific language for request/response policy, and managed through a CLI interface (varnishadm) and a set of command-line tools for logging, statistics, and monitoring.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Caching
  - Caching Proxy
  - Content Delivery
  - HTTP Accelerator
  - Open Source
  - Proxy
  - Reverse Proxy
url: https://raw.githubusercontent.com/api-evangelist/varnish/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: varnish:varnish-cache
    name: Varnish Cache CLI API
    description: The Varnish Cache CLI management interface provides programmatic control over a running Varnish instance. It is accessible via varnishadm or TCP socket and supports configuration management (VCL load/use/discard), backend health control, cache ban/invalidation, parameter tuning, and process management. Commands can return JSON output with the -j flag.
    humanURL: https://varnish-cache.org/docs/trunk/reference/varnish-cli.html
    tags:
      - Cache Management
      - Caching
      - CLI
      - Configuration
      - Reverse Proxy
    properties:
      - type: Documentation
        url: https://varnish-cache.org/docs/trunk/reference/varnish-cli.html
      - type: GettingStarted
        url: https://varnish-cache.org/docs/trunk/users-guide/run_cli.html
      - type: APIReference
        url: https://varnish-cache.org/docs/trunk/reference/varnishadm.html
  - aid: varnish:varnish-logging
    name: Varnish Logging Tools
    description: Varnish ships with a suite of log-analysis tools that read from the Varnish Shared Log (VSL). Tools include varnishlog (raw log streaming), varnishncsa (NCSA/Apache log format), varnishstat (live counters), varnishtop (real-time activity display), and varnishhist (response time histogram).
    humanURL: https://varnish-cache.org/docs/trunk/reference/
    tags:
      - Logging
      - Monitoring
      - Observability
      - Statistics
    properties:
      - type: Documentation
        url: https://varnish-cache.org/docs/trunk/reference/varnishlog.html
      - type: APIReference
        url: https://varnish-cache.org/docs/trunk/reference/varnishstat.html
  - aid: varnish:varnish-vmods
    name: Varnish Modules (VMODs)
    description: VMODs are extensions written for Varnish Cache that extend VCL capabilities. Bundled modules include blob (binary data handling), cookie (HTTP cookie parsing), directors (load balancing strategies), h2 (HTTP/2 control), proxy (PROXY protocol support), purge (cache purging), std (standard utility functions), and unix (Unix socket support). Additional community VMODs are available for headers, digest, auth, and more.
    humanURL: https://varnish-cache.org/docs/trunk/reference/vmod.html
    tags:
      - Extensions
      - Modules
      - Plugins
      - VMODs
    properties:
      - type: Documentation
        url: https://varnish-cache.org/docs/trunk/reference/vmod.html
      - type: GitHub Repository
        url: https://github.com/varnishcache/varnish-cache
common:
  - type: Website
    url: https://varnish-cache.org/
  - type: Documentation
    url: https://varnish-cache.org/docs/
  - type: GitHub Organization
    url: https://github.com/varnishcache
  - type: GitHub Repository
    url: https://github.com/varnishcache/varnish-cache
  - type: ReleaseNotes
    url: https://varnish-cache.org/docs/trunk/whatsNew/
  - type: Blog
    url: https://info.varnish-software.com/blog
  - type: Forum
    url: https://discourse.varnish-cache.org/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/varnish
  - type: Features
    data:
      - name: HTTP Caching
        description: Caches HTTP responses to reduce backend load and improve response times for repeated requests.
      - name: VCL Configuration Language
        description: Domain-specific language for defining request/response handling policies with full programmability.
      - name: CLI Management Interface
        description: TCP-based management interface for runtime configuration, VCL deployment, and cache control.
      - name: Backend Health Probes
        description: Configurable health checks for backends with automatic failover to healthy backends.
      - name: Cache Invalidation (Bans)
        description: Flexible cache invalidation via ban expressions matching any request/response attribute.
      - name: JSON Output
        description: CLI commands support -j flag for structured JSON output, enabling programmatic management.
      - name: VMOD Extension System
        description: Loadable modules (VMODs) extend VCL with cookie parsing, load balancing, digest, auth, and more.
      - name: HTTP/2 Support
        description: Native HTTP/2 support via the h2 VMOD for modern protocol acceleration.
      - name: Shared Memory Log (VSL)
        description: High-speed shared memory logging with rich request/response attributes for analysis tools.
      - name: Multi-threaded Architecture
        description: Worker thread pool for high-throughput concurrent request handling with configurable threading.
  - type: UseCases
    data:
      - name: API Gateway Caching
        description: Cache REST API responses at the edge to reduce database and application server load.
      - name: CDN Origin Shield
        description: Act as origin shield between CDN edge nodes and web/application servers.
      - name: Static Asset Acceleration
        description: Cache and serve static assets (images, JS, CSS) with long TTLs.
      - name: A/B Testing
        description: Use VCL to route traffic fractions to different backends for controlled experiments.
      - name: DDoS Mitigation
        description: Absorb traffic spikes and rate-limit abusive clients via VCL policies.
      - name: Authentication Offloading
        description: Offload token validation and session checks to VCL logic at the cache layer.
      - name: Request Routing
        description: Route requests to different backend pools based on URL patterns, headers, or cookies.
  - type: Integrations
    data:
      - name: Nginx
        description: Common deployment pairing with Nginx as backend web server behind Varnish.
      - name: Apache HTTP Server
        description: Classic deployment with Apache as origin server behind Varnish Cache.
      - name: Kubernetes
        description: Deployable as a sidecar or DaemonSet in Kubernetes clusters for service-level caching.
      - name: Prometheus
        description: Varnish statistics exportable via varnish_exporter for Prometheus scraping.
      - name: Grafana
        description: Community dashboards available for Varnish Cache statistics via Prometheus/Grafana.
      - name: Drupal
        description: Deep integration with Drupal Cache Tags for efficient purging of cached pages.
      - name: WordPress
        description: VCL configurations and plugins available for WordPress caching integration.
      - name: Fastly
        description: Fastly CDN is built on Varnish Cache; Fastly VCL is a fork of Varnish VCL.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
