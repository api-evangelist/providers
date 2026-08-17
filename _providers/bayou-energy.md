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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bayou Energy Agentic Access
  operation_count: 12
  slug: bayou-energy-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 4
apis:
- description: The Bills API from Bayou Energy — 4 operation(s) for bills.
  name: Bayou Energy Bills API
  slug: bayou-energy-bills-api
- description: The Customers API from Bayou Energy — 2 operation(s) for customers.
  name: Bayou Energy Customers API
  slug: bayou-energy-customers-api
- description: The Intervals API from Bayou Energy — 1 operation(s) for intervals.
  name: Bayou Energy Intervals API
  slug: bayou-energy-intervals-api
- description: The Utilities API from Bayou Energy — 2 operation(s) for utilities.
  name: Bayou Energy Utilities API
  slug: bayou-energy-utilities-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bayou Energy Bills API
  slug: open-bayou-energy-bills-api
- collection_type: open
  name: Bayou Energy Bills Customers API
  slug: open-bayou-energy-customers-api
- collection_type: open
  name: Bayou Energy Bills Intervals API
  slug: open-bayou-energy-intervals-api
- collection_type: open
  name: Bayou Energy Bills Utilities API
  slug: open-bayou-energy-utilities-api
- collection_type: open
  name: Bayou Energy API
  slug: open-bayou-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bayou-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bayou-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bayou-energy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bayouenergy
- group: company
  title: ''
  type: Website
  url: https://www.bayou.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bayou.energy/
- group: commercial
  title: ''
  type: Plans
  url: plans/bayou-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bayou-energy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bayou-energy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.bayou.energy/feed
created: '2026-06-21'
description: Bayou Energy provides a utility-bill and usage-data API that lets companies collect their customers' utility account, bill, and interval meter data from US utilities. Customers link their utility credentials through a hosted onboarding flow, and Bayou continuously fetches the full bill and interval history, exposing it through a REST API secured with HTTP Basic authentication.
finops:
- name: Bayou Energy Finops
  service_category: Analytics
  slug: bayou-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bayou-energy.png
layout: provider
modified: '2026-06-21'
name: Bayou Energy
nav: Providers
network: true
overview: 'Bayou Energy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bills API, Customers API, Intervals API, and 1 more. Tagged areas include Utility Data, Energy, Utility Bills, Interval Data, and Metering.


  Bayou Energy''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Bayou Energy Plans Pricing
  plan_count: 2
  slug: bayou-energy-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Bayou Energy Rate Limits
  slug: bayou-energy-rate-limits
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bayou-energy/refs/heads/main/screenshots/bayou-energy-2026-07-25T202450.png
security:
- kind: authentication
  name: Bayou Energy Authentication
  slug: bayou-energy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bayou Energy Domain Security
  slug: bayou-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bayou-energy
tags:
- Utility Data
- Energy
- Utility Bills
- Interval Data
- Metering
website: https://www.bayou.energy/
---
