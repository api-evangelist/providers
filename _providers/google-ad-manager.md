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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Ad Manager Agentic Access
  operation_count: 5
  slug: google-ad-manager-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 5
apis:
- description: The adUnits API from Google Ad Manager — 1 operation(s) for adunits.
  name: Google Ad Manager adUnits API
  slug: google-ad-manager-adunits-api
- description: The Companies API from Google Ad Manager — 1 operation(s) for companies.
  name: Google Ad Manager Companies API
  slug: google-ad-manager-companies-api
- description: The Networks API from Google Ad Manager — 1 operation(s) for networks.
  name: Google Ad Manager Networks API
  slug: google-ad-manager-networks-api
- description: The Orders API from Google Ad Manager — 1 operation(s) for orders.
  name: Google Ad Manager Orders API
  slug: google-ad-manager-orders-api
- description: The Reports:run API from Google Ad Manager — 1 operation(s) for reports:run.
  name: Google Ad Manager Reports:run API
  slug: google-ad-manager-reports-run-api
artifact_total: 15
collections:
- collection_type: open
  name: Google Ad Manager API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-ad-manager-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-ad-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-ad-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-ad-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-ad-manager-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-ad-manager
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/ad-manager/api/beta/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://admanager.google.com/home/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google Ad Manager API provides programmatic access to manage Ad Manager data including ad units, companies, orders, placements, line items, creatives, reports, and targeting. It enables publishers to automate their ad operations and integrate Ad Manager with other systems.
finops:
- name: Google Ad Manager Finops
  service_category: API
  slug: google-ad-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-ad-manager.png
layout: provider
modified: '2026-05-19'
name: Google Ad Manager
nav: Providers
network: true
overview: 'Google Ad Manager publishes 5 APIs on the [APIs.io](https://apis.io/) network, including adUnits API, Companies API, Networks API, and 2 more. Tagged areas include Ad Manager, Ad Operations, Ad Serving, Creatives, and Line Items.


  The Google Ad Manager catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Ad Manager''s developer surface includes authentication, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Google Ad Manager Plans Pricing
  plan_count: 3
  slug: google-ad-manager-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Google Ad Manager Rate Limits
  slug: google-ad-manager-rate-limits
rules:
- name: Google Ad Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-ad-manager-jsonschema-spectral-rules
scopes:
- name: Google Ad Manager Scopes
  scope_count: 1
  slug: google-ad-manager-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 41.8
  delta: -8.4
  facets:
    commercial_clarity: 26.3
    contract_quality: 64.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-ad-manager/refs/heads/main/screenshots/google-ad-manager-2026-06-20T182001.png
security:
- kind: authentication
  name: Google Ad Manager Authentication
  slug: google-ad-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Ad Manager Domain Security
  slug: google-ad-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Ad Manager Vulnerability Disclosure
  slug: google-ad-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-ad-manager
tags:
- Ad Manager
- Ad Operations
- Ad Serving
- Creatives
- Line Items
- Orders
- Publishers
- Targeting
---
