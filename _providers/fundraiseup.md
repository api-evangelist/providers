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
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fundraiseup Agentic Access
  operation_count: 14
  slug: fundraiseup-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: One-time and recurring donations, including offline and ACH donations.
  name: Fundraise Up Donations API
  slug: fundraiseup-donations-api
- description: Secure access-link generation for the self-service Donor Portal.
  name: Fundraise Up Donor Portal API
  slug: fundraiseup-donor-portal-api
- description: Audit-log events across donations, recurring plans, tributes, and supporters.
  name: Fundraise Up Events API
  slug: fundraiseup-events-api
- description: Recurring donation plans modeling a supporter's ongoing giving.
  name: Fundraise Up Recurring Plans API
  slug: fundraiseup-recurring-plans-api
- description: Donor records (Fundraise Up calls donors "supporters").
  name: Fundraise Up Supporters API
  slug: fundraiseup-supporters-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fundraise Up REST Donations API
  slug: open-fundraiseup-donations-api
- collection_type: open
  name: Fundraise Up REST Donations Donor Portal API
  slug: open-fundraiseup-donor-portal-api
- collection_type: open
  name: Fundraise Up REST Donations Events API
  slug: open-fundraiseup-events-api
- collection_type: open
  name: Fundraise Up REST Donations Recurring Plans API
  slug: open-fundraiseup-recurring-plans-api
- collection_type: open
  name: Fundraise Up REST Donations Supporters API
  slug: open-fundraiseup-supporters-api
- collection_type: open
  name: Fundraise Up REST API
  slug: open-fundraiseup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fundraiseup-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundraiseup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fundraiseup-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fundraiseup
- group: company
  title: ''
  type: Website
  url: https://fundraiseup.com
- group: docs
  title: ''
  type: Documentation
  url: https://fundraiseup.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/fundraiseup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fundraiseup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fundraiseup-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fundraiseup.com/blog/
- group: other
  title: ''
  type: AICatalog
  url: ai-catalog/fundraiseup-ai-catalog.yml
created: '2026-07-05'
description: Fundraise Up is an online donation and fundraising platform for nonprofits that optimizes the digital giving experience to increase conversion and recurring revenue. Its REST API gives programmatic access to fundraising data - donations, recurring plans, supporters (donors), and an events audit log - so organizations can process offline and non-digital donations through their Fundraise Up account, combine them with online giving, and sync everything to CRMs, BI tools, and data warehouses. The API is resource-oriented, uses JSON-encoded request bodies, and authenticates with an API key over HTTP Bearer. Base URL is https://api.fundraiseup.com/v1.
finops:
- name: Fundraiseup Finops
  service_category: Fundraising and Payments
  slug: fundraiseup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fundraiseup.png
layout: provider
modified: '2026-07-05'
name: Fundraise Up
nav: Providers
network: true
overview: 'Fundraise Up publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Donations API, Donor Portal API, Events API, and 2 more. Tagged areas include Fundraising, Donations, Non-Profit, Payments, and Recurring Giving.


  Fundraise Up''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Fundraiseup Plans Pricing
  plan_count: 2
  slug: fundraiseup-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Fundraiseup Rate Limits
  slug: fundraiseup-rate-limits
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fundraiseup/refs/heads/main/screenshots/fundraiseup-2026-07-25T215319.png
security:
- kind: authentication
  name: Fundraiseup Authentication
  slug: fundraiseup-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fundraiseup Domain Security
  slug: fundraiseup-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fundraiseup
tags:
- Fundraising
- Donations
- Non-Profit
- Payments
- Recurring Giving
- Donor Management
website: https://fundraiseup.com
---
