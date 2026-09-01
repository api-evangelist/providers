---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://indigov.com
- group: company
  title: ''
  type: Blog
  url: https://indigov.com/town-hall
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://indigov.com/pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://indigov.com/form/customer-support
- group: auth
  title: ''
  type: Security
  url: https://indigov.com/pages/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/indigov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indigov-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indigov-us
- group: start
  title: ''
  type: Login
  url: https://app.indigov.com/auth/signin
- group: build
  title: ''
  type: Packages
  url: packages/indigov-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/indigov-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/indigov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/indigov-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/indigov-conformance.yml
coverage:
  checked: '2026-08-13'
  detail: Indigov ships a government CRM as an end-user product only — its complete sitemap has no developer, API, docs or pricing route, api./developer./docs.indigov.com do not resolve, and the customer app at app.indigov.com returns a hard 404 for /openapi.json, /graphql, /mcp and every /.well-known/ path.
  evidence:
  - status: 404
    url: https://indigov.com/developers
  - status: 404
    url: https://app.indigov.com/openapi.json
  - status: 404
    url: https://app.indigov.com/.well-known/agent-card.json
  - status: 200
    url: https://indigov.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Indigov is a constituent relationship management (CRM) platform purpose-built for government — U.S. Congressional offices, state legislatures, and municipal agencies — that unifies inbound constituent communications from email, web forms, SMS, social media, phone, and scanned mail into a single cross-organizational inbox. It layers casework tracking, constituent routing, smart tagging, and mass-email triage with rapid response, plus a customer data platform for sentiment and engagement analytics and an award-winning mobile app for field staff. Indigov serves government offices across 35 states and 2 territories and was acquired by Granicus, joining its Government Experience Cloud (GXC). It was surfaced as a portfolio company of 8vc and added to the API Evangelist network for enrichment.
image: https://dj5q4o1v0zqkl.cloudfront.net/indigov_social_share_34443d1656.jpg
layout: provider
modified: '2026-08-13'
name: Indigov
nav: Providers
network: true
overview: 'Indigov is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, GovTech, Constituent Relationship Management, and CRM.


  Indigov''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Indigov Plans Pricing
  plan_count: 0
  slug: indigov-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Indigov Rate Limits
  slug: indigov-rate-limits
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 17.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/indigov/refs/heads/main/screenshots/indigov-2026-07-25T222319.png
security:
- kind: domain-security
  name: Indigov Domain Security
  slug: indigov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Indigov Vulnerability Disclosure
  slug: indigov-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: indigov
tags:
- Company
- Government
- GovTech
- Constituent Relationship Management
- CRM
- Civic Technology
- Casework
- Constituent Communications
- Customer Data Platform
- Public Sector
website: https://indigov.com
---
