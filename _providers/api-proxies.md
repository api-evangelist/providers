---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 30
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering reverse-proxy and edge-proxy software used in front of APIs, including HTTP reverse proxies, edge proxies, load balancers, caching proxies, and service mesh sidecars. API proxies sit between API consumers and upstream services to provide TLS termination, routing, rate limiting, observability, traffic shaping, caching, authentication enforcement, and resilience features such as retries and circuit breaking. This collection includes general-purpose reverse proxies like NGINX, HAProxy, Caddy, Apache HTTP Server, Traefik, and Varnish, edge and service mesh proxies like Envoy, Linkerd2-proxy, Istio, Consul Connect, and AWS App Mesh, and proxy-oriented gateways like KrakenD, Tyk, Ambassador, Emissary, and Apache APISIX that overlap with the API gateway category but operate primarily as L7 proxies.
examples:
- key_count: 12
  name: Api Proxies Proxy Route Example
  slug: api-proxies-proxy-route-example
- key_count: 9
  name: Api Proxies Upstream Cluster Example
  slug: api-proxies-upstream-cluster-example
features:
- description: API proxies terminate HTTP/HTTPS connections from clients and forward requests to upstream API services, hiding internal topology and providing a single front door.
  name: Layer 7 Reverse Proxying
- description: Proxies like NGINX, HAProxy, Envoy, and Linkerd2-proxy terminate TLS at the edge and can enforce mutual TLS between services in a mesh.
  name: TLS Termination and mTLS
- description: Edge proxies route requests by host, path, header, or method, and support traffic splitting, canary releases, and blue-green deployments.
  name: Routing and Traffic Splitting
- description: Reverse proxies enforce rate limits, quotas, and concurrency limits at the edge to protect upstream APIs from abuse and overload.
  name: Rate Limiting and Throttling
- description: Caching proxies like Varnish, NGINX, Squid, and Cloudflare cache API responses to reduce upstream load and improve client latency.
  name: Caching and HTTP Acceleration
- description: Proxies emit structured access logs, metrics, and traces (OpenTelemetry, Prometheus, statsd) for every request crossing the edge or mesh.
  name: Observability and Access Logging
- description: Sidecar proxies like Envoy, Linkerd2-proxy, and Consul Connect run alongside each service to provide identity, encryption, retries, and traffic policy without changing application code.
  name: Service Mesh Sidecar Pattern
- description: Edge proxies and CDNs like Cloudflare, Akamai, and Azure Application Gateway provide WAF rules, bot mitigation, and DDoS protection in front of APIs.
  name: WAF and Edge Security
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: CNCF L7 proxy used as the data plane for Istio, Consul Connect, Envoy Gateway, Ambassador, and Emissary, with an xDS configuration API.
  name: Envoy
- description: Widely deployed open-source web server and reverse proxy with HTTP/2, HTTP/3, load balancing, caching, and Lua-based extension via OpenResty.
  name: NGINX
- description: High-performance TCP and HTTP reverse proxy and load balancer with a runtime Data Plane API for dynamic configuration.
  name: HAProxy
- description: Cloud-native reverse proxy and ingress controller with automatic service discovery for Kubernetes, Docker, and Consul.
  name: Traefik
- description: HTTP/2 reverse proxy with automatic HTTPS via ACME, a JSON config API, and a plugin architecture.
  name: Caddy
- description: Service mesh that uses Envoy sidecars to provide mTLS, traffic management, and policy for Kubernetes APIs.
  name: Istio
- description: Lightweight CNCF service mesh built around a purpose-built Rust micro-proxy (linkerd2-proxy) for east-west API traffic.
  name: Linkerd
- description: Global edge proxy and CDN providing TLS termination, WAF, bot management, and caching in front of APIs and websites.
  name: Cloudflare
json_schemas:
- name: ProxyRoute
  property_count: 12
  slug: api-proxies-proxy-route
- name: UpstreamCluster
  property_count: 9
  slug: api-proxies-upstream-cluster
json_structures:
- name: Api Proxies Proxy Route Structure
  property_count: 12
  slug: api-proxies-proxy-route-structure
- name: Api Proxies Upstream Cluster Structure
  property_count: 9
  slug: api-proxies-upstream-cluster-structure
jsonld:
- class_count: 6
  name: Api Proxies Context
  property_count: 21
  slug: api-proxies-context
layout: provider
modified: '2026-05-19'
name: API Proxies
nav: Providers
network: true
overview: 'API Proxies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Reverse Proxy, Edge Proxy, API Proxy, Service Mesh Sidecar, and Load Balancer.


  The API Proxies catalog on APIs.io includes 1 JSON-LD context.


  API Proxies'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: api-proxies
tags:
- Reverse Proxy
- Edge Proxy
- API Proxy
- Service Mesh Sidecar
- Load Balancer
- HTTP Proxy
- Ingress
use_cases:
- description: Front internal APIs with NGINX, HAProxy, or Envoy to handle TLS, HTTP/2, HTTP/3, compression, and request normalization before requests reach application servers.
  name: API Edge Termination
- description: Use Envoy Gateway, Emissary, Ambassador, or Traefik as Kubernetes ingress controllers to expose APIs running across multiple clusters and namespaces.
  name: Multi-Cluster Ingress
- description: Deploy Istio, Linkerd, or Consul Connect to manage service-to-service API calls with mTLS, retries, and traffic policy inside a Kubernetes cluster.
  name: Service Mesh East-West Traffic
- description: Front public APIs with Cloudflare, Fastly, or Akamai to terminate connections at the edge, cache safe responses, and absorb DDoS traffic.
  name: Global API Acceleration
- description: Use proxy-based traffic splitting in Envoy, Istio, or Linkerd to shift a percentage of API traffic to a new version and roll back on error budget breach.
  name: Canary and Progressive Delivery
- description: Place HAProxy, NGINX, or Apache HTTP Server in front of legacy SOAP or HTTP services to add TLS, modern auth, rate limiting, and observability without rewriting the backend.
  name: Legacy API Modernization
- description: Use a reverse proxy to gradually route traffic from a legacy monolith API to new microservice APIs based on path or header rules.
  name: API Migration and Strangler Pattern
website: https://apievangelist.com
---
