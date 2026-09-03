---
access_model:
  confidence: medium
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agent_card: flavored
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
  score: 21.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Forter Agentic Access
  operation_count: 8
  slug: forter-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.forter.secure.com
  baseurl_source: declared
  description: Signup and login (account takeover) decisions.
  name: Forter Accounts API
  slug: forter-accounts-api
- baseURL: https://api.forter.secure.com
  baseurl_source: declared
  description: Data-subject profile access for privacy and compliance.
  name: Forter Data Privacy API
  slug: forter-data-privacy-api
- baseURL: https://api.forter.secure.com
  baseurl_source: declared
  description: Chargeback disputes and customer compensation requests.
  name: Forter Disputes API
  slug: forter-disputes-api
- baseURL: https://api.forter.secure.com
  baseurl_source: declared
  description: Order and checkout fraud/abuse decisions and order status.
  name: Forter Orders API
  slug: forter-orders-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Forter Accounts API
  slug: open-forter-accounts-api
- collection_type: open
  name: Forter Accounts Data Privacy API
  slug: open-forter-data-privacy-api
- collection_type: open
  name: Forter Accounts Disputes API
  slug: open-forter-disputes-api
- collection_type: open
  name: Forter Accounts Orders API
  slug: open-forter-orders-api
- collection_type: open
  name: Forter API
  slug: open-forter
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/forter-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forter
- group: company
  title: ''
  type: Website
  url: https://www.forter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forter.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/forter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forter-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.forter.com/blog/
created: '2026-07-12'
description: Forter is a fraud prevention and digital identity platform for online commerce. Its Decision API returns real-time trust-or-not decisions for orders, payments, account signups, and logins, drawing on a global identity graph and machine learning trained across a large network of merchants. Beyond fraud management, Forter covers chargeback recovery, abuse prevention, payment optimization, 3DS orchestration, and identity protection. Access is enterprise / contact-sales - API credentials (a per-account site ID and API key) are provisioned by Forter during onboarding, and requests are sent to a dedicated per-tenant host.
finops:
- name: Forter Finops
  service_category: Fraud Prevention and Identity
  slug: forter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-12'
name: Forter
nav: Providers
network: true
overview: 'Forter publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Data Privacy API, Disputes API, and 1 more. Tagged areas include Fraud Detection, Fraud Prevention, Identity, Trust, and Payments.


  Forter''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Forter Plans Pricing
  plan_count: 1
  slug: forter-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Forter Rate Limits
  slug: forter-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.4
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forter/refs/heads/main/screenshots/forter-2026-07-25T215001.png
security:
- kind: authentication
  name: Forter Authentication
  slug: forter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forter Domain Security
  slug: forter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: forter
tags:
- Fraud Detection
- Fraud Prevention
- Identity
- Trust
- Payments
- Chargebacks
- Account Protection
- E-Commerce
- Risk
- Machine-Learning
website: https://www.forter.com/
---
