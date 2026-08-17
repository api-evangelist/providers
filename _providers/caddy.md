---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Caddy Agentic Access
  operation_count: 11
  slug: caddy-agentic-access
  summary_line: 11 operations · 7 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Caddy exposes a RESTful administration API on localhost:2019 by default for dynamically loading and modifying server configuration at runtime without restarts. Endpoints support loading full JSON conf
  name: Caddy Admin API
  slug: caddy-admin-api
- description: The Adapt API from Caddy — 1 operation(s) for adapt.
  name: Caddy Adapt API
  slug: caddy-adapt-api
- description: The Configuration API from Caddy — 1 operation(s) for configuration.
  name: Caddy Configuration API
  slug: caddy-configuration-api
- description: The Lifecycle API from Caddy — 2 operation(s) for lifecycle.
  name: Caddy Lifecycle API
  slug: caddy-lifecycle-api
- description: The PKI API from Caddy — 2 operation(s) for pki.
  name: Caddy PKI API
  slug: caddy-pki-api
- description: The Reverse Proxy API from Caddy — 1 operation(s) for reverse proxy.
  name: Caddy Reverse Proxy API
  slug: caddy-reverse-proxy-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Caddy Admin Adapt API
  slug: open-caddy-adapt-api
- collection_type: open
  name: Caddy Admin Adapt Configuration API
  slug: open-caddy-configuration-api
- collection_type: open
  name: Caddy Admin Adapt Lifecycle API
  slug: open-caddy-lifecycle-api
- collection_type: open
  name: Caddy Admin Adapt PKI API
  slug: open-caddy-pki-api
- collection_type: open
  name: Caddy Admin Adapt Reverse Proxy API
  slug: open-caddy-reverse-proxy-api
- collection_type: open
  name: Caddy Admin API
  slug: open-caddy
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/caddyserver/caddy/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/caddyserver/caddy/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/caddyserver/caddy/blob/master/.github/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/caddyserver/caddy/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/caddyserver/caddy/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/caddy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caddy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caddyserver.com/
- group: docs
  title: ''
  type: Documentation
  url: https://caddyserver.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caddyserver
- group: operate
  title: ''
  type: Community Forum
  url: https://caddy.community/
- group: other
  title: ''
  type: Download
  url: https://caddyserver.com/download
- group: other
  title: ''
  type: Sponsors
  url: https://github.com/sponsors/mholt
created: '2026-03-27'
description: Caddy is a modern, extensible, open-source web server and reverse proxy written in Go that provides automatic HTTPS via Let's Encrypt, a dynamic JSON-based admin API, a human-friendly Caddyfile configuration format, and a modular architecture with a rich ecosystem of plugins for authentication, observability, and custom behavior.
finops:
- name: Caddy Finops
  service_category: API
  slug: caddy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caddy.png
layout: provider
modified: '2026-05-19'
name: Caddy
nav: Providers
network: true
overview: 'Caddy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Adapt API, Configuration API, Lifecycle API, and 2 more. Tagged areas include Automatic HTTPS, Go, Load Balancer, Reverse Proxy, and TLS.


  Caddy''s developer surface includes documentation and 12 more developer resources.'
plans:
- name: Caddy Plans Pricing
  plan_count: 3
  slug: caddy-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Caddy Rate Limits
  slug: caddy-rate-limits
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 41.6
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caddy/refs/heads/main/screenshots/caddy-2026-06-20T173835.png
security:
- kind: domain-security
  name: Caddy Domain Security
  slug: caddy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caddy
tags:
- Automatic HTTPS
- Go
- Load Balancer
- Reverse Proxy
- TLS
- Web Server
website: https://caddyserver.com/
---
