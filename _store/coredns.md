---
aid: coredns
url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/apis.yml
apis:
- aid: coredns:coredns-dns-api
  name: CoreDNS DNS Interface
  description: CoreDNS implements the standard DNS protocol (RFC 1035) serving both UDP and TCP queries. In Kubernetes, it resolves service names to cluster IPs, headless services to pod IPs, and supports SRV records for port discovery. The Kubernetes plugin watches the API server for service and endpoint changes to keep DNS records current.
  humanURL: https://coredns.io/manual/toc/
  properties:
  - type: Documentation
    url: https://coredns.io/manual/toc/
  tags:
  - DNS
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
  description: The CoreDNS health plugin exposes an HTTP health check endpoint at /health on port 8080 by default. It reports the overall health of the CoreDNS process and is used by Kubernetes liveness and readiness probes to determine if the DNS server is operational.
  humanURL: https://coredns.io/plugins/health/
  properties:
  - type: Documentation
    url: https://coredns.io/plugins/health/
  - type: OpenAPI
    url: openapi/coredns-health-openapi.yml
  tags:
  - Health Check
  - Kubernetes
  - Observability
- aid: coredns:coredns-metrics-api
  name: CoreDNS Metrics API
  description: The CoreDNS prometheus plugin exposes a Prometheus-compatible metrics endpoint at /metrics on port 9153. It provides DNS request counters, response size histograms, latency distributions, and build information metrics for monitoring CoreDNS performance and behavior.
  humanURL: https://coredns.io/plugins/metrics/
  properties:
  - type: Documentation
    url: https://coredns.io/plugins/metrics/
  - type: OpenAPI
    url: openapi/coredns-metrics-openapi.yml
  tags:
  - Metrics
  - Monitoring
  - Observability
  - Prometheus
name: CoreDNS
tags:
- Cloud Native
- DNS
- Graduated
- Kubernetes
- Networking
- Service Discovery
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CoreDNS is a CNCF graduated DNS server written in Go that serves as the default DNS service for Kubernetes clusters. It is flexible and extensible through a plugin architecture, supporting DNS-based service discovery, forwarding, caching, and integration with etcd, Kubernetes, and other backends. CoreDNS can serve as an authoritative DNS server or a recursive resolver.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

