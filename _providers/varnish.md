---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://varnish-cache.org/'', ''status'': 302, ''note'': ''declared website redirects to https://www.varnish.org/ — a different registrable domain (varnish-cache.org -> varnish.org), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Varnish Cache CLI management interface provides programmatic control over a running Varnish instance. It is accessible via varnishadm or TCP socket and supports configuration management (VCL load/
  name: Varnish Cache CLI API
  slug: varnish-cache
- description: Varnish ships with a suite of log-analysis tools that read from the Varnish Shared Log (VSL). Tools include varnishlog (raw log streaming), varnishncsa (NCSA/Apache log format), varnishstat (live coun
  name: Varnish Logging Tools
  slug: varnish-logging
- description: VMODs are extensions written for Varnish Cache that extend VCL capabilities. Bundled modules include blob (binary data handling), cookie (HTTP cookie parsing), directors (load balancing strategies), h
  name: Varnish Modules (VMODs)
  slug: varnish-vmods
artifact_total: 32
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/varnishcache/varnish-cache/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/varnishcache/varnish-cache/blob/master/CONTRIBUTING
- group: auth
  title: ''
  type: DomainSecurity
  url: security/varnish-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/varnish-software
- group: company
  title: ''
  type: Website
  url: https://varnish-cache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://varnish-cache.org/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/varnishcache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/varnishcache/varnish-cache
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://varnish-cache.org/docs/trunk/whatsNew/
- group: company
  title: ''
  type: Blog
  url: https://info.varnish-software.com/blog
- group: operate
  title: ''
  type: Forums
  url: https://discourse.varnish-cache.org/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/varnish
created: '2026-03-27'
description: Varnish Cache is a high-performance HTTP accelerator and reverse proxy designed for content-heavy dynamic websites and APIs. It sits in front of web servers and caches HTTP responses to serve repeated requests without hitting the backend, dramatically reducing load and latency. Varnish is configured via VCL (Varnish Configuration Language), a domain-specific language for request/response policy, and managed through a CLI interface (varnishadm) and a set of command-line tools for logging, statistics, and monitoring.
features:
- description: Caches HTTP responses to reduce backend load and improve response times for repeated requests.
  name: HTTP Caching
- description: Domain-specific language for defining request/response handling policies with full programmability.
  name: VCL Configuration Language
- description: TCP-based management interface for runtime configuration, VCL deployment, and cache control.
  name: CLI Management Interface
- description: Configurable health checks for backends with automatic failover to healthy backends.
  name: Backend Health Probes
- description: Flexible cache invalidation via ban expressions matching any request/response attribute.
  name: Cache Invalidation (Bans)
- description: CLI commands support -j flag for structured JSON output, enabling programmatic management.
  name: JSON Output
- description: Loadable modules (VMODs) extend VCL with cookie parsing, load balancing, digest, auth, and more.
  name: VMOD Extension System
- description: Native HTTP/2 support via the h2 VMOD for modern protocol acceleration.
  name: HTTP/2 Support
- description: High-speed shared memory logging with rich request/response attributes for analysis tools.
  name: Shared Memory Log (VSL)
- description: Worker thread pool for high-throughput concurrent request handling with configurable threading.
  name: Multi-threaded Architecture
finops:
- name: Varnish Finops
  service_category: API
  slug: varnish-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/varnish.png
integrations:
- description: Common deployment pairing with Nginx as backend web server behind Varnish.
  name: Nginx
- description: Classic deployment with Apache as origin server behind Varnish Cache.
  name: Apache HTTP Server
- description: Deployable as a sidecar or DaemonSet in Kubernetes clusters for service-level caching.
  name: Kubernetes
- description: Varnish statistics exportable via varnish_exporter for Prometheus scraping.
  name: Prometheus
- description: Community dashboards available for Varnish Cache statistics via Prometheus/Grafana.
  name: Grafana
- description: Deep integration with Drupal Cache Tags for efficient purging of cached pages.
  name: Drupal
- description: VCL configurations and plugins available for WordPress caching integration.
  name: WordPress
- description: Fastly CDN is built on Varnish Cache; Fastly VCL is a fork of Varnish VCL.
  name: Fastly
layout: provider
modified: '2026-05-03'
name: Varnish Cache
nav: Providers
network: true
overview: 'Varnish Cache publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Caching, Caching Proxy, Content Delivery, HTTP Accelerator, and Open-Source.


  Varnish Cache''s developer surface includes documentation, release notes, engineering blog, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Varnish Plans Pricing
  plan_count: 3
  slug: varnish-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Varnish Rate Limits
  slug: varnish-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/varnish/refs/heads/main/screenshots/varnish-2026-06-20T200817.png
security:
- kind: domain-security
  name: Varnish Domain Security
  slug: varnish-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: varnish
tags:
- Caching
- Caching Proxy
- Content Delivery
- HTTP Accelerator
- Open-Source
- Proxy
- Reverse Proxy
use_cases:
- description: Cache REST API responses at the edge to reduce database and application server load.
  name: API Gateway Caching
- description: Act as origin shield between CDN edge nodes and web/application servers.
  name: CDN Origin Shield
- description: Cache and serve static assets (images, JS, CSS) with long TTLs.
  name: Static Asset Acceleration
- description: Use VCL to route traffic fractions to different backends for controlled experiments.
  name: A/B Testing
- description: Absorb traffic spikes and rate-limit abusive clients via VCL policies.
  name: DDoS Mitigation
- description: Offload token validation and session checks to VCL logic at the cache layer.
  name: Authentication Offloading
- description: Route requests to different backend pools based on URL patterns, headers, or cookies.
  name: Request Routing
website: https://varnish-cache.org/
---
