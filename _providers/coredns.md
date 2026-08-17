---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coredns Agentic Access
  operation_count: 3
  slug: coredns-agentic-access
  summary_line: 3 operations
api_count: 5
apis:
- description: CoreDNS implements the standard DNS protocol (RFC 1035) serving both UDP and TCP queries. In Kubernetes, it resolves service names to cluster IPs, headless services to pod IPs, and supports SRV record
  name: CoreDNS DNS Interface
  slug: coredns-dns-api
- description: 'The CoreDNS plugin framework allows extending DNS server functionality through a chain of plugins defined in the Corefile configuration. External plugins can be written in Go to add custom DNS record '
  name: CoreDNS Plugin API
  slug: coredns-plugin-api
- description: Health check endpoints used by Kubernetes liveness and readiness probes to assess the operational state of the CoreDNS process.
  name: CoreDNS Health API
  slug: coredns-health-api
- description: Prometheus-compatible metrics endpoints exposing DNS query statistics, cache performance, latency histograms, and build information.
  name: CoreDNS Metrics API
  slug: coredns-metrics-api
- description: Readiness check endpoints that indicate whether CoreDNS plugins have finished initializing and are ready to serve DNS queries.
  name: CoreDNS Ready API
  slug: coredns-ready-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CoreDNS Health API
  slug: open-coredns-health-api
- collection_type: open
  name: CoreDNS Health API
  slug: open-coredns-health
- collection_type: open
  name: CoreDNS Health Metrics API
  slug: open-coredns-metrics-api
- collection_type: open
  name: CoreDNS Metrics API
  slug: open-coredns-metrics
- collection_type: open
  name: CoreDNS Health Ready API
  slug: open-coredns-ready-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/coredns/coredns/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/coredns/coredns/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/coredns/coredns/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/coredns/coredns/blob/master/.github/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coredns-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coredns-domain-security.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coredns-corefile-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/coredns-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/coredns-vocabulary.yml
- group: company
  title: ''
  type: Website
  url: https://coredns.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coredns.io/manual/toc/
- group: start
  title: ''
  type: GettingStarted
  url: https://coredns.io/2017/07/24/quick-start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coredns
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/coredns/coredns
- group: build
  title: ''
  type: Plugins
  url: https://coredns.io/plugins/
- group: build
  title: ''
  type: ExternalPlugins
  url: https://coredns.io/explugins/
- group: company
  title: ''
  type: Blog
  url: https://coredns.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/coredns/coredns/releases
- group: operate
  title: ''
  type: Community
  url: https://slack.cncf.io/
- group: commercial
  title: ''
  type: License
  url: https://github.com/coredns/coredns/blob/master/LICENSE
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/coredns/
created: '2026-03-16'
description: CoreDNS is a CNCF graduated DNS server written in Go that serves as the default DNS service for Kubernetes clusters. It is flexible and extensible through a plugin architecture, supporting DNS-based service discovery, forwarding, caching, and integration with etcd, Kubernetes, and other backends. CoreDNS can serve as an authoritative DNS server or a recursive resolver, with HTTP plugins exposing health, readiness, and Prometheus metrics endpoints for Kubernetes operations.
finops:
- name: Coredns Finops
  service_category: Open Source DNS
  slug: coredns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coredns.png
json_schemas:
- name: CoreDNS Corefile Configuration
  property_count: 1
  slug: coredns-corefile
jsonld:
- class_count: 0
  name: Coredns Context
  property_count: 8
  slug: coredns-context
layout: provider
modified: '2026-05-19'
name: CoreDNS
nav: Providers
network: true
overview: 'CoreDNS publishes 3 APIs on the [APIs.io](https://apis.io/) network: Health API, Metrics API, and Ready API. Tagged areas include Apache 2.0, Cloud Native, CNCF, DNS, and Go.


  The CoreDNS catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  CoreDNS''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Coredns Plans Pricing
  plan_count: 1
  slug: coredns-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Coredns Rate Limits
  slug: coredns-rate-limits
rules:
- name: CoreDNS API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 2
  slug: coredns-health-rules
- name: CoreDNS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: coredns-jsonschema-spectral-rules
- name: CoreDNS API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 2
  slug: coredns-metrics-rules
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 55.2
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 31.3
    operational_transparency: 39.5
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/screenshots/coredns-2026-06-20T175025.png
security:
- kind: domain-security
  name: Coredns Domain Security
  slug: coredns-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: coredns
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
website: https://coredns.io/
---
