---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Routable Agentic Access
  operation_count: 37
  slug: routable-agentic-access
  summary_line: 37 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Vendor and customer companies.
  name: Routable Companies API
  slug: routable-companies-api
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Contacts associated with companies.
  name: Routable Contacts API
  slug: routable-contacts-api
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Funding accounts and the Routable Balance.
  name: Routable Funding Sources API
  slug: routable-funding-sources-api
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Bills owed to vendors.
  name: Routable Payables API
  slug: routable-payables-api
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Bank, international, and check payment methods.
  name: Routable Payment Methods API
  slug: routable-payment-methods-api
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Amounts owed to you by customers.
  name: Routable Receivables API
  slug: routable-receivables-api
- baseURL: https://api.routable.com/v1
  baseurl_source: declared
  description: Webhook events.
  name: Routable Webhooks API
  slug: routable-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Routable Companies API
  slug: open-routable-companies-api
- collection_type: open
  name: Routable Companies Contacts API
  slug: open-routable-contacts-api
- collection_type: open
  name: Routable Companies Funding Sources API
  slug: open-routable-funding-sources-api
- collection_type: open
  name: Routable Companies Payables API
  slug: open-routable-payables-api
- collection_type: open
  name: Routable Companies Payment Methods API
  slug: open-routable-payment-methods-api
- collection_type: open
  name: Routable Companies Receivables API
  slug: open-routable-receivables-api
- collection_type: open
  name: Routable Companies Webhooks API
  slug: open-routable-webhooks-api
- collection_type: open
  name: Routable API
  slug: open-routable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/routable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/routable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/routable-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/routablehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/routable
- group: company
  title: ''
  type: Website
  url: https://www.routable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.routable.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/routable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/routable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/routable-finops.yml
created: '2026-06-21'
description: Routable is a B2B payments platform automating accounts payable and accounts receivable, mass payouts, and vendor management. Its API-first REST API lets teams onboard vendors and customers, collect payment and tax information, create payables and receivables, and move money via ACH, SWIFT, and check to more than 200 countries, with webhook events for end-to-end automation.
finops:
- name: Routable Finops
  service_category: Financial Services
  slug: routable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/routable.png
layout: provider
modified: '2026-06-21'
name: Routable
nav: Providers
network: true
overview: 'Routable publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Contacts API, Funding Sources API, and 4 more. Tagged areas include Payments, Accounts Payable, Accounts Receivable, B2B Payments, and Mass Payouts.


  Routable''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Routable Plans Pricing
  plan_count: 2
  slug: routable-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Routable Rate Limits
  slug: routable-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/routable/refs/heads/main/screenshots/routable-2026-09-02T154136.png
security:
- kind: authentication
  name: Routable Authentication
  slug: routable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Routable Domain Security
  slug: routable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: routable
tags:
- Payments
- Accounts Payable
- Accounts Receivable
- B2B Payments
- Mass Payouts
- Fintech
website: https://www.routable.com/
---
