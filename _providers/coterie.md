---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Coterie Agentic Access
  operation_count: 13
  slug: coterie-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 6
apis:
- description: Commercial applications describing the insured business.
  name: Coterie Insurance Applications API
  slug: coterie-applications-api
- description: Policy documents and proposals.
  name: Coterie Insurance Documents API
  slug: coterie-documents-api
- description: Industry / NAICS classification lookup.
  name: Coterie Insurance Industry API
  slug: coterie-industry-api
- description: Binding and issuing policies from bindable quotes.
  name: Coterie Insurance Policies API
  slug: coterie-policies-api
- description: Rated, bindable quotes and underwriting questions.
  name: Coterie Insurance Quotes API
  slug: coterie-quotes-api
- description: Webhook subscription management.
  name: Coterie Insurance Webhooks API
  slug: coterie-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Coterie Commercial Insurance API
  slug: open-coterie
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coterie-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coterie-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coterie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coterie-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoterieInsure
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coterieinsurance
- group: company
  title: ''
  type: Website
  url: https://coterieinsurance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coterieinsurance.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/coterie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coterie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coterie-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coterieinsurance.com/feed
created: '2026-06-25'
description: Coterie Insurance is a technology-first commercial insurance provider for small businesses, offering Business Owners Policy (BOP), General Liability (GL), Professional Liability (PL), and Workers' Compensation (WC). Its REST API lets appointed agents and digital partners build applications, generate bindable quotes, bind and issue policies, look up industry/NAICS classifications, retrieve policy documents, and subscribe to webhooks for an embedded small-business insurance experience.
finops:
- name: Coterie Finops
  service_category: Insurance
  slug: coterie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coterie.png
layout: provider
modified: '2026-06-25'
name: Coterie Insurance
nav: Providers
network: true
overview: 'Coterie Insurance publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Documents API, Industry API, and 3 more. Tagged areas include Insurance, Commercial Insurance, Small Business, Embedded Insurance, and Insurtech.


  Coterie Insurance''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Coterie Plans Pricing
  plan_count: 2
  slug: coterie-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 2
  name: Coterie Rate Limits
  slug: coterie-rate-limits
scopes:
- name: Coterie Scopes
  scope_count: 0
  slug: coterie-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 43.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coterie/refs/heads/main/screenshots/coterie-2026-07-25T210459.png
security:
- kind: authentication
  name: Coterie Authentication
  slug: coterie-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Coterie Domain Security
  slug: coterie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coterie
tags:
- Insurance
- Commercial Insurance
- Small Business
- Embedded Insurance
- Insurtech
website: https://coterieinsurance.com/
---
