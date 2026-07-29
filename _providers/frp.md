---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Frp Agentic Access
  operation_count: 28
  slug: frp-agentic-access
  summary_line: 28 operations · 9 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Connected client inventory
  name: frp Clients API
  slug: frp-clients-api
- description: Read and replace the in-memory frpc configuration
  name: frp Configuration API
  slug: frp-configuration-api
- description: Liveness probe
  name: frp Health API
  slug: frp-health-api
- description: Reload and stop the running frpc process
  name: frp Lifecycle API
  slug: frp-lifecycle-api
- description: Prometheus metrics endpoint
  name: frp Metrics API
  slug: frp-metrics-api
- description: Active proxy inventory and traffic stats
  name: frp Proxies API
  slug: frp-proxies-api
- description: Server runtime information
  name: frp Server API
  slug: frp-server-api
- description: Runtime status of proxies and visitors
  name: frp Status API
  slug: frp-status-api
- description: Persistent configuration store for proxies and visitors
  name: frp Store API
  slug: frp-store-api
artifact_total: 17
collections:
- collection_type: open
  name: frp Client Admin API
  slug: open-frp-client-admin-api
- collection_type: open
  name: frp Server Admin API
  slug: open-frp-server-admin-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/frp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gofrp.org/
- group: docs
  title: ''
  type: Documentation
  url: https://gofrp.org/en/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://gofrp.org/en/docs/setup/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/fatedier/frp
- group: operate
  title: ''
  type: Issues
  url: https://github.com/fatedier/frp/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/fatedier/frp/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/fatedier/frp/blob/master/LICENSE
created: '2026-03-27'
description: frp is an open-source fast reverse proxy that exposes services running behind a NAT or firewall to the public internet. Both the server (frps) and the client (frpc) include built-in HTTP admin APIs that operators can use to inspect runtime status, manage proxies and visitors, hot-reload configuration, and scrape Prometheus metrics.
finops:
- name: Frp Finops
  service_category: API
  slug: frp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frp.png
layout: provider
modified: '2026-05-19'
name: frp
nav: Providers
network: true
overview: 'frp publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Configuration API, Health API, and 6 more. Tagged areas include NAT Traversal, Reverse Proxy, Tunneling, and Open Source.


  frp''s developer surface includes authentication, documentation, getting-started guide, release notes, and 6 more developer resources.'
plans:
- name: Frp Plans Pricing
  plan_count: 3
  slug: frp-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Frp Rate Limits
  slug: frp-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.2
    developer_ergonomics: 30.4
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frp/refs/heads/main/screenshots/frp-2026-06-20T181558.png
security:
- kind: authentication
  name: Frp Authentication
  slug: frp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Frp Domain Security
  slug: frp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: frp
tags:
- NAT Traversal
- Reverse Proxy
- Tunneling
- Open Source
website: https://gofrp.org/
---
