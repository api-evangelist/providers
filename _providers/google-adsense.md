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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Adsense Agentic Access
  operation_count: 5
  slug: google-adsense-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The Accounts API from Google AdSense Management — 1 operation(s) for accounts.
  name: Google AdSense Management Accounts API
  slug: google-adsense-accounts-api
- description: The Adclients API from Google AdSense Management — 1 operation(s) for adclients.
  name: Google AdSense Management Adclients API
  slug: google-adsense-adclients-api
- description: The Adunits API from Google AdSense Management — 1 operation(s) for adunits.
  name: Google AdSense Management Adunits API
  slug: google-adsense-adunits-api
- description: The Payments API from Google AdSense Management — 1 operation(s) for payments.
  name: Google AdSense Management Payments API
  slug: google-adsense-payments-api
- description: The Reports:generate API from Google AdSense Management — 1 operation(s) for reports:generate.
  name: Google AdSense Management Reports:generate API
  slug: google-adsense-reports-generate-api
artifact_total: 15
collections:
- collection_type: open
  name: Google AdSense Management API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-adsense-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-adsense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-adsense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-adsense-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-adsense-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-adsense
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/adsense/management/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://support.google.com/adsense/answer/180195
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google AdSense Management API allows publishers to access their inventory and run earnings and performance reports. Publishers can manage ad clients, ad units, custom channels, URL channels, and access payment and policy information programmatically.
finops:
- name: Google Adsense Finops
  service_category: API
  slug: google-adsense-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-adsense.png
layout: provider
modified: '2026-05-19'
name: Google AdSense Management
nav: Providers
network: true
overview: 'Google AdSense Management publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Adclients API, Adunits API, and 2 more. Tagged areas include Ad Units, AdSense, Advertising, Monetization, and Publishers.


  The Google AdSense Management catalog on APIs.io includes 1 Spectral governance ruleset.


  Google AdSense Management''s developer surface includes authentication, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Google Adsense Plans Pricing
  plan_count: 3
  slug: google-adsense-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Google Adsense Rate Limits
  slug: google-adsense-rate-limits
rules:
- name: Google AdSense Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-adsense-jsonschema-spectral-rules
scopes:
- name: Google Adsense Scopes
  scope_count: 2
  slug: google-adsense-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-adsense/refs/heads/main/screenshots/google-adsense-2026-06-20T182008.png
security:
- kind: authentication
  name: Google Adsense Authentication
  slug: google-adsense-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Adsense Domain Security
  slug: google-adsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Adsense Vulnerability Disclosure
  slug: google-adsense-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-adsense
tags:
- Ad Units
- AdSense
- Advertising
- Monetization
- Publishers
- Reports
- Revenue
---
