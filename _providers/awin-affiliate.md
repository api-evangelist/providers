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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Awin Affiliate Agentic Access
  operation_count: 12
  slug: awin-affiliate-agentic-access
  summary_line: 12 operations
api_count: 5
apis:
- description: Accounts the authenticated user can access.
  name: Awin Accounts API
  slug: awin-affiliate-accounts-api
- description: Commission groups and rates for a programme.
  name: Awin Commission Groups API
  slug: awin-affiliate-commission-groups-api
- description: Advertiser programmes and their details.
  name: Awin Programmes API
  slug: awin-affiliate-programmes-api
- description: Aggregated performance reports.
  name: Awin Reports API
  slug: awin-affiliate-reports-api
- description: Individual publisher and advertiser transactions.
  name: Awin Transactions API
  slug: awin-affiliate-transactions-api
artifact_total: 13
collections:
- collection_type: open
  name: Awin API
  slug: open-awin-affiliate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/awin-affiliate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/awin-affiliate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/awin-affiliate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/awin-affiliate-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/awin
- group: company
  title: ''
  type: Website
  url: https://www.awin.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.awin.com/apidocs/introduction-1
- group: auth
  title: ''
  type: Authentication
  url: https://help.awin.com/apidocs/api-authentication
- group: commercial
  title: ''
  type: Plans
  url: plans/awin-affiliate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/awin-affiliate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/awin-affiliate-finops.yml
created: '2026-07-05'
description: Awin is a global affiliate marketing network connecting advertisers (brands) with publishers (content creators, cashback, voucher, and loyalty partners) across thousands of programmes worldwide. Awin exposes a documented public REST API at https://api.awin.com that lets both publishers and advertisers pull data such as individual transactions and aggregated performance reports, inspect commission groups and programme details, list the accounts a user can access, and generate tracking links and offers. All endpoints follow REST principles, return JSON, are served over HTTPS only, and authenticate with an OAuth 2.0 Bearer access token issued at the user level from the Awin UI (the Create Transactions API is the exception and uses an x-api-key). A platform-wide throttle limits requests to 20 API calls per minute per user.
finops:
- name: Awin Affiliate Finops
  service_category: Marketing and Advertising
  slug: awin-affiliate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/awin-affiliate.png
layout: provider
modified: '2026-07-05'
name: Awin
nav: Providers
network: true
overview: 'Awin publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Commission Groups API, Programmes API, and 2 more. Tagged areas include Affiliate Marketing, Advertising, Publishers, Advertisers, and Transactions.


  Awin''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Awin Affiliate Plans Pricing
  plan_count: 4
  slug: awin-affiliate-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 2
  name: Awin Affiliate Rate Limits
  slug: awin-affiliate-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/awin-affiliate/refs/heads/main/screenshots/awin-affiliate-2026-07-25T202025.png
security:
- kind: authentication
  name: Awin Affiliate Authentication
  slug: awin-affiliate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Awin Affiliate Domain Security
  slug: awin-affiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Awin Affiliate Vulnerability Disclosure
  slug: awin-affiliate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: awin-affiliate
tags:
- Affiliate Marketing
- Advertising
- Publishers
- Advertisers
- Transactions
- Reporting
- Commissions
- Performance Marketing
website: https://www.awin.com
---
