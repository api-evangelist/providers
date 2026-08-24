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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Classy Org Agentic Access
  operation_count: 51
  slug: classy-org-agentic-access
  summary_line: 51 operations · 21 acting
api_count: 10
apis:
- description: OAuth2 client credentials token exchange.
  name: Classy Authentication API
  slug: classy-org-authentication-api
- description: Donation forms, peer-to-peer, crowdfunding, and event campaigns.
  name: Classy Campaigns API
  slug: classy-org-campaigns-api
- description: Funds or programs donors can direct gifts toward.
  name: Classy Designations API
  slug: classy-org-designations-api
- description: Individual peer-to-peer fundraising pages under a campaign.
  name: Classy Fundraising Pages API
  slug: classy-org-fundraising-pages-api
- description: Teams and subteams of fundraising pages under a campaign.
  name: Classy Fundraising Teams API
  slug: classy-org-fundraising-teams-api
- description: The account behind a fundraiser, admin, or donor.
  name: Classy Members API
  slug: classy-org-members-api
- description: Nonprofit organization records and their nested collections.
  name: Classy Organizations API
  slug: classy-org-organizations-api
- description: Sustainer / recurring donation subscriptions.
  name: Classy Recurring Donation Plans API
  slug: classy-org-recurring-donation-plans-api
- description: Donor / CRM profile per organization.
  name: Classy Supporters API
  slug: classy-org-supporters-api
- description: Donations, ticket, and merchandise order transactions.
  name: Classy Transactions API
  slug: classy-org-transactions-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication API
  slug: open-classy-org-authentication-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Campaigns API
  slug: open-classy-org-campaigns-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Designations API
  slug: open-classy-org-designations-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Fundraising Pages API
  slug: open-classy-org-fundraising-pages-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Fundraising Teams API
  slug: open-classy-org-fundraising-teams-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Members API
  slug: open-classy-org-members-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Organizations API
  slug: open-classy-org-organizations-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Recurring Donation Plans API
  slug: open-classy-org-recurring-donation-plans-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Supporters API
  slug: open-classy-org-supporters-api
- collection_type: open
  name: Classy API (GoFundMe Pro) Authentication Transactions API
  slug: open-classy-org-transactions-api
- collection_type: open
  name: Classy API (GoFundMe Pro)
  slug: open-classy-org
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/classy-org-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/classy-org-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/classy-org-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/classy-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stayclassy
- group: company
  title: ''
  type: Website
  url: https://www.classy.org
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gofundme.com/pro/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/classy-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/classy-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/classy-org-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pro.gofundme.com/feed/
created: '2026-07-03'
description: Classy is an online fundraising platform for nonprofits - donation forms, peer-to-peer campaigns, crowdfunding, and event/ticketing pages - built around Organizations, Campaigns, Fundraising Pages, Fundraising Teams, Transactions, Recurring Donation Plans, Members, Supporters, and Designations. GoFundMe acquired Classy in 2022 and announced in 2025 that the Classy product and brand are being folded into GoFundMe Pro; the Classy name is being retired through 2026 while the underlying software, the api.classy.org/2.0 REST API, and the developer docs (developers.classy.org, now redirecting to developers.gofundme.com/pro) continue to operate under the GoFundMe Pro banner.
finops:
- name: Classy Org Finops
  service_category: Nonprofit Fundraising Software
  slug: classy-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/classy-org.png
layout: provider
modified: '2026-07-03'
name: Classy
nav: Providers
network: true
overview: 'Classy publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, Designations API, and 7 more. Tagged areas include Non-Profit, Fundraising, Donations, Peer-to-Peer, and Philanthropy.


  Classy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Classy Org Plans Pricing
  plan_count: 4
  slug: classy-org-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Classy Org Rate Limits
  slug: classy-org-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/classy-org/refs/heads/main/screenshots/classy-org-2026-07-25T205526.png
security:
- kind: authentication
  name: Classy Org Authentication
  slug: classy-org-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Classy Org Domain Security
  slug: classy-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: classy-org
tags:
- Non-Profit
- Fundraising
- Donations
- Peer-to-Peer
- Philanthropy
- Payments
- GoFundMe Pro
website: https://www.classy.org
---
