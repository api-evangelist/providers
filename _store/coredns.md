---
aid: coredns
name: CoreDNS
x-type: opensource
description: CoreDNS is a CNCF graduated DNS server written in Go that serves as the default DNS service for Kubernetes clusters. It is flexible and extensible through a plugin architecture, supporting DNS-based service discovery, forwarding, caching, and integration with etcd, Kubernetes, and other backends. CoreDNS can serve as an authoritative DNS server or a recursive resolver, with HTTP plugins exposing health, readiness, and Prometheus metrics endpoints for Kubernetes operations.
url: https://coredns.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache 2.0
  - Cloud Native
  - CNCF
  - DNS
  - Go
  - Graduated
  - Kubernetes
  - Networking
  - Open Source
  - Plugins
  - Prometheus
  - Service Discovery
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Index
access: Public
position: Provider
apis:
  - aid: coredns:coredns-dns-api
    name: CoreDNS DNS Interface
    description: CoreDNS implements the standard DNS protocol (RFC 1035) serving both UDP and TCP queries. In Kubernetes, it resolves service names to cluster IPs, headless services to pod IPs, and supports SRV records for port discovery. The Kubernetes plugin watches the API server for service and endpoint changes to keep DNS records current. Additional protocol bindings include DNS-over-TLS (DoT), DNS-over-HTTPS (DoH), DNS-over-QUIC (DoQ), and gRPC.
    humanURL: https://coredns.io/manual/toc/
    properties:
      - type: Documentation
        url: https://coredns.io/manual/toc/
    tags:
      - DNS
      - DoH
      - DoQ
      - DoT
      - Kubernetes
      - Service Discovery
  - aid: coredns:coredns-plugin-api
    name: CoreDNS Plugin API
    description: The CoreDNS plugin framework allows extending DNS server functionality through a chain of plugins defined in the Corefile configuration. External plugins can be written in Go to add custom DNS record sources, filtering, metrics, and middleware. Each plugin implements the Handler interface to process DNS requests.
    humanURL: https://coredns.io/explugins/
    properties:
      - type: Documentation
        url: https://coredns.io/explugins/
      - type: Reference
        url: https://coredns.io/manual/plugins/
    tags:
      - Extensibility
      - Plugins
  - aid: coredns:coredns-health-api
    name: CoreDNS Health API
    description: The CoreDNS health plugin exposes HTTP /health and /ready endpoints on port 8080 by default. It reports the overall health and readiness of the CoreDNS process and is used by Kubernetes liveness and readiness probes to determine if the DNS server is operational.
    humanURL: https://coredns.io/plugins/health/
    baseURL: http://localhost:8080
    properties:
      - type: Documentation
        url: https://coredns.io/plugins/health/
      - type: ReadyDocumentation
        url: https://coredns.io/plugins/ready/
      - type: OpenAPI
        url: openapi/coredns-health-openapi.yml
      - type: Rules
        url: rules/coredns-health-rules.yml
      - type: Capabilities
        url: capabilities/coredns-health-capabilities.yml
    tags:
      - Health Check
      - Kubernetes
      - Observability
      - Readiness
  - aid: coredns:coredns-metrics-api
    name: CoreDNS Metrics API
    description: The CoreDNS prometheus plugin exposes a Prometheus-compatible metrics endpoint at /metrics on port 9153. It provides DNS request counters, response size histograms, latency distributions, and build information metrics for monitoring CoreDNS performance and behavior.
    humanURL: https://coredns.io/plugins/metrics/
    baseURL: http://localhost:9153
    properties:
      - type: Documentation
        url: https://coredns.io/plugins/metrics/
      - type: OpenAPI
        url: openapi/coredns-metrics-openapi.yml
      - type: Rules
        url: rules/coredns-metrics-rules.yml
      - type: Capabilities
        url: capabilities/coredns-metrics-capabilities.yml
    tags:
      - Metrics
      - Monitoring
      - Observability
      - Prometheus
common:
  - type: JSONSchema
    url: json-schema/coredns-corefile-schema.json
  - type: JSONLD
    url: json-ld/coredns-context.jsonld
  - type: Vocabulary
    url: vocabulary/coredns-vocabulary.yml
  - type: Website
    url: https://coredns.io/
  - type: Documentation
    url: https://coredns.io/manual/toc/
  - type: GettingStarted
    url: https://coredns.io/2017/07/24/quick-start/
  - type: GitHubOrganization
    url: https://github.com/coredns
  - type: GitHubRepository
    url: https://github.com/coredns/coredns
  - type: Plugins
    url: https://coredns.io/plugins/
  - type: ExternalPlugins
    url: https://coredns.io/explugins/
  - type: Blog
    url: https://coredns.io/blog/
  - type: ChangeLog
    url: https://github.com/coredns/coredns/releases
  - type: Community
    url: https://slack.cncf.io/
  - type: License
    url: https://github.com/coredns/coredns/blob/master/LICENSE
  - type: CNCF
    url: https://www.cncf.io/projects/coredns/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
