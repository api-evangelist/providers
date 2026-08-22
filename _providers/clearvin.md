---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Clearvin Agentic Access
  operation_count: 2
  slug: clearvin-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The Authentication API from ClearVIN — 1 operation(s) for authentication.
  name: ClearVIN Authentication API
  slug: clearvin-authentication-api
- description: The Report API from ClearVIN — 1 operation(s) for report.
  name: ClearVIN Report API
  slug: clearvin-report-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClearVIN Vendor Authentication API
  slug: open-clearvin-authentication-api
- collection_type: open
  name: ClearVIN Vendor Authentication Report API
  slug: open-clearvin-report-api
- collection_type: open
  name: ClearVIN Vendor API
  slug: open-clearvin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clearvin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearvin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clearvin-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearvin
- group: company
  title: ''
  type: Website
  url: https://www.clearvin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clearvin.com/en/api-subscribers/
- group: commercial
  title: ''
  type: Plans
  url: plans/clearvin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clearvin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clearvin-finops.yml
created: '2026-06-21'
description: ClearVIN is a vehicle-history and VIN data provider and an approved NMVTIS data provider. Its REST API decodes North American (U.S. and Canada) VINs into 100+ specification data points and returns full vehicle history reports - title, junk / salvage / total-loss records, odometer events, and market valuation - sourced directly from government and industry data, covering model years 1981 to present.
finops:
- name: Clearvin Finops
  service_category: Data and Analytics
  slug: clearvin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearvin.png
layout: provider
modified: '2026-06-21'
name: ClearVIN
nav: Providers
network: true
overview: 'ClearVIN publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Report API. Tagged areas include VIN, Vehicle History, Automotive, NMVTIS, and Vehicle Data.


  ClearVIN''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Clearvin Plans Pricing
  plan_count: 5
  slug: clearvin-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Clearvin Rate Limits
  slug: clearvin-rate-limits
score:
  band: thin
  composite: 36.9
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearvin/refs/heads/main/screenshots/clearvin-2026-07-25T205553.png
security:
- kind: authentication
  name: Clearvin Authentication
  slug: clearvin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clearvin Domain Security
  slug: clearvin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearvin
tags:
- VIN
- Vehicle History
- Automotive
- NMVTIS
- Vehicle Data
website: https://www.clearvin.com/
---
