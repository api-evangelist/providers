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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Guusto Agentic Access
  operation_count: 8
  slug: guusto-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.guusto.com/api/v1
  baseurl_source: declared
  description: Retrieve available reward budget balances.
  name: Guusto Account Budget API
  slug: guusto-account-budget-api
- baseURL: https://api.guusto.com/api/v1
  baseurl_source: declared
  description: Order digital gifts and track order status.
  name: Guusto Order Gift API
  slug: guusto-order-gift-api
- baseURL: https://api.guusto.com/api/v1
  baseurl_source: declared
  description: Recognition activity and manager-insight reports.
  name: Guusto Reports API
  slug: guusto-reports-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Guusto Gifts Account Budget API
  slug: open-guusto-account-budget-api
- collection_type: open
  name: Guusto Gifts Account Budget Order Gift API
  slug: open-guusto-order-gift-api
- collection_type: open
  name: Guusto Gifts Account Budget Reports API
  slug: open-guusto-reports-api
- collection_type: open
  name: Guusto Gifts API
  slug: open-guusto
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guusto-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/guusto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guusto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guusto-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guusto
- group: company
  title: ''
  type: Website
  url: https://guusto.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.guusto.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/guusto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/guusto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/guusto-finops.yml
created: '2026-07-10'
description: Guusto is an employee recognition and rewards platform that lets teams send digital gifts, run peer-to-peer and top-down recognition programs, and redeem rewards with 60,000+ merchant locations, prepaid Mastercard, and charitable donations. Guusto exposes a REST Gifts API - available on the Premium plan - for programmatically ordering gifts, tracking order status, retrieving workspace and member reward budgets, and pulling recognition activity and manager insight reports. Requests are authenticated with a Bearer API token plus an X-Workspace-id header against production (api.guusto.com) or a demo test environment (api-demo.guusto.io).
finops:
- name: Guusto Finops
  service_category: Human Resources and Recognition
  slug: guusto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guusto.png
layout: provider
modified: '2026-07-10'
name: Guusto
nav: Providers
network: true
overview: 'Guusto publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account Budget API, Order Gift API, and Reports API. Tagged areas include Employee Recognition, Rewards, Gifting, Gift Cards, and HR.


  Guusto''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Guusto Plans Pricing
  plan_count: 4
  slug: guusto-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Guusto Rate Limits
  slug: guusto-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guusto/refs/heads/main/screenshots/guusto-2026-07-25T220443.png
security:
- kind: authentication
  name: Guusto Authentication
  slug: guusto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Guusto Domain Security
  slug: guusto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Guusto Trust Center
  slug: guusto-trust-center
  summary_line: SOC 2, PCI DSS
slug: guusto
tags:
- Employee Recognition
- Rewards
- Gifting
- Gift Cards
- HR
- Rewards and Recognition
website: https://guusto.com
---
