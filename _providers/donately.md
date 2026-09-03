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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Donately Agentic Access
  operation_count: 22
  slug: donately-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.donately.com/v2
  baseurl_source: declared
  description: The organizations a token has access to.
  name: Donately Accounts API
  slug: donately-accounts-api
- baseURL: https://api.donately.com/v2
  baseurl_source: declared
  description: Fundraising pages with goals and settings.
  name: Donately Campaigns API
  slug: donately-campaigns-api
- baseURL: https://api.donately.com/v2
  baseurl_source: declared
  description: One-time and recurring gifts.
  name: Donately Donations API
  slug: donately-donations-api
- baseURL: https://api.donately.com/v2
  baseurl_source: declared
  description: Peer-to-peer fundraising pages under a campaign.
  name: Donately Fundraisers API
  slug: donately-fundraisers-api
- baseURL: https://api.donately.com/v2
  baseurl_source: declared
  description: Donors and contacts.
  name: Donately People API
  slug: donately-people-api
- baseURL: https://api.donately.com/v2
  baseurl_source: declared
  description: Recurring donation schedules.
  name: Donately Subscriptions API
  slug: donately-subscriptions-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Donately Accounts API
  slug: open-donately-accounts-api
- collection_type: open
  name: Donately Accounts Campaigns API
  slug: open-donately-campaigns-api
- collection_type: open
  name: Donately Accounts Donations API
  slug: open-donately-donations-api
- collection_type: open
  name: Donately Accounts Fundraisers API
  slug: open-donately-fundraisers-api
- collection_type: open
  name: Donately Accounts People API
  slug: open-donately-people-api
- collection_type: open
  name: Donately Accounts Subscriptions API
  slug: open-donately-subscriptions-api
- collection_type: open
  name: Donately API
  slug: open-donately
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/donately-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donately-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/donately-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/donately
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/donately
- group: company
  title: ''
  type: Website
  url: https://www.donately.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.donately.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/donately-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/donately-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/donately-finops.yml
created: '2026-07-05'
description: Donately is an online donation and fundraising platform for nonprofits, churches, and businesses, offering embeddable donation forms, campaign and peer-to-peer fundraising pages, recurring giving, and donor management. Its REST API (base https://api.donately.com/v2, version 2019-03-15) exposes accounts, campaigns, donations, recurring subscriptions, people (donors), fundraisers, forms, and webhooks, authenticated with an API token via HTTP Basic Auth. Donately charges a platform fee (4%, 2%, or 0% prepaid) on top of Stripe/PayPal payment processing.
finops:
- name: Donately Finops
  service_category: Fundraising and Payments
  slug: donately-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donately.png
layout: provider
modified: '2026-07-05'
name: Donately
nav: Providers
network: true
overview: 'Donately publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Campaigns API, Donations API, and 3 more. Tagged areas include Fundraising, Donations, Non-Profit, Payments, and Donor Management.


  Donately''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Donately Plans Pricing
  plan_count: 3
  slug: donately-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Donately Rate Limits
  slug: donately-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 58.4
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.4
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
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donately/refs/heads/main/screenshots/donately-2026-07-25T212248.png
security:
- kind: authentication
  name: Donately Authentication
  slug: donately-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Donately Domain Security
  slug: donately-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donately
tags:
- Fundraising
- Donations
- Non-Profit
- Payments
- Donor Management
- Recurring Giving
website: https://www.donately.com
---
