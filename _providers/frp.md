---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Frp Agentic Access
  operation_count: 28
  slug: frp-agentic-access
  summary_line: 28 operations · 9 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Connected client inventory
  name: frp Clients API
  slug: frp-clients-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Read and replace the in-memory frpc configuration
  name: frp Configuration API
  slug: frp-configuration-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Liveness probe
  name: frp Health API
  slug: frp-health-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Reload and stop the running frpc process
  name: frp Lifecycle API
  slug: frp-lifecycle-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Prometheus metrics endpoint
  name: frp Metrics API
  slug: frp-metrics-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Active proxy inventory and traffic stats
  name: frp Proxies API
  slug: frp-proxies-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Server runtime information
  name: frp Server API
  slug: frp-server-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Runtime status of proxies and visitors
  name: frp Status API
  slug: frp-status-api
- baseURL: http://localhost:7500
  baseurl_source: declared
  description: Persistent configuration store for proxies and visitors
  name: frp Store API
  slug: frp-store-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: frp Client Admin API
  slug: open-frp-client-admin-api
- collection_type: open
  name: frp Client Admin Clients API
  slug: open-frp-clients-api
- collection_type: open
  name: frp Client Admin Clients Configuration API
  slug: open-frp-configuration-api
- collection_type: open
  name: frp Client Admin Clients Health API
  slug: open-frp-health-api
- collection_type: open
  name: frp Client Admin Clients Lifecycle API
  slug: open-frp-lifecycle-api
- collection_type: open
  name: frp Client Admin Clients Metrics API
  slug: open-frp-metrics-api
- collection_type: open
  name: frp Client Admin Clients Proxies API
  slug: open-frp-proxies-api
- collection_type: open
  name: frp Server Admin API
  slug: open-frp-server-admin-api
- collection_type: open
  name: frp Client Admin Clients Server API
  slug: open-frp-server-api
- collection_type: open
  name: frp Client Admin Clients Status API
  slug: open-frp-status-api
- collection_type: open
  name: frp Client Admin Clients Store API
  slug: open-frp-store-api
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
overview: 'frp publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Configuration API, Health API, and 6 more. Tagged areas include NAT Traversal, Reverse Proxy, Tunneling, and Open-Source.


  frp''s developer surface includes authentication, documentation, getting-started guide, release notes, and 6 more developer resources.'
plans:
- name: Frp Plans Pricing
  plan_count: 3
  slug: frp-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Frp Rate Limits
  slug: frp-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.4
    developer_ergonomics: 33.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
website: https://gofrp.org/
---
