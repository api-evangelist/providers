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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Friendbuy Agentic Access
  operation_count: 31
  slug: friendbuy-agentic-access
  summary_line: 31 operations · 12 acting
api_count: 1
apis:
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Pull campaign, share, click, conversion, and reward analytics.
  name: Friendbuy Analytics API
  slug: friendbuy-analytics-api
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Exchange account key and secret for a Bearer token.
  name: Friendbuy Authorization API
  slug: friendbuy-authorization-api
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Create and retrieve customer records and manage customer data requests.
  name: Friendbuy Customers API
  slug: friendbuy-customers-api
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Track purchase, sign-up, and custom conversion events.
  name: Friendbuy Events API
  slug: friendbuy-events-api
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Block users from campaigns.
  name: Friendbuy Management API
  slug: friendbuy-management-api
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Generate personal referral links and check referral status.
  name: Friendbuy Referrals API
  slug: friendbuy-referrals-api
- baseURL: https://mapi.fbot.me/v1
  baseurl_source: declared
  description: Manage loyalty ledger balances, adjustments, redemptions, and coupons.
  name: Friendbuy Rewards & Loyalty API
  slug: friendbuy-rewards-loyalty-api
artifact_total: 23
asyncapis:
- description: ''
  name: Friendbuy Webhooks
  slug: friendbuy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Friendbuy Merchant Analytics API
  slug: open-friendbuy-analytics-api
- collection_type: open
  name: Friendbuy Merchant Analytics Authorization API
  slug: open-friendbuy-authorization-api
- collection_type: open
  name: Friendbuy Merchant Analytics Customers API
  slug: open-friendbuy-customers-api
- collection_type: open
  name: Friendbuy Merchant Analytics Events API
  slug: open-friendbuy-events-api
- collection_type: open
  name: Friendbuy Merchant Analytics Management API
  slug: open-friendbuy-management-api
- collection_type: open
  name: Friendbuy Merchant Analytics Referrals API
  slug: open-friendbuy-referrals-api
- collection_type: open
  name: Friendbuy Merchant Analytics Rewards & Loyalty API
  slug: open-friendbuy-rewards-loyalty-api
- collection_type: open
  name: Friendbuy Merchant API
  slug: open-friendbuy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/friendbuy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friendbuy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/friendbuy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/friendbuy
- group: company
  title: ''
  type: Website
  url: https://friendbuy.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.friendbuy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/friendbuy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/friendbuy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/friendbuy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://friendbuy.com/blog
- group: build
  title: ''
  type: Packages
  url: packages/friendbuy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/friendbuy-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/friendbuy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/friendbuy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/friendbuy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://friendbuy.statuspage.io
- group: design
  title: ''
  type: Conformance
  url: conformance/friendbuy-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/friendbuy-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/friendbuy-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/friendbuy-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/friendbuy-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.friendbuy.com/product-updates
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.friendbuy.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.friendbuy.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.friendbuy.com#integration-setup
- group: operate
  title: ''
  type: Support
  url: https://support.friendbuy.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/friendbuy
- group: start
  title: ''
  type: Login
  url: https://retailer.fbot.me
- group: commercial
  title: ''
  type: TermsOfService
  url: https://friendbuy.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://friendbuy.com/privacy
created: '2026-07-10'
description: Friendbuy is a referral and loyalty marketing platform for ecommerce and direct-to-consumer brands. Merchants launch referral, loyalty, and reward campaigns through on-site widgets and a no-code dashboard, and integrate server-to-server through the Friendbuy Merchant API (base https://mapi.fbot.me/v1). The Merchant API lets merchants sync customer records, generate personal referral links, track purchase / sign-up / custom conversion events, pull campaign and reward analytics, and manage loyalty ledger balances, adjustments, redemptions, and coupons. Authentication is a key/secret exchange at POST /authorization that returns a short-lived Bearer JWT. Access to the API and to production credentials is gated behind a paid, contact-sales plan.
finops:
- name: Friendbuy Finops
  service_category: Marketing and Advertising
  slug: friendbuy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friendbuy.png
layout: provider
modified: '2026-08-13'
name: Friendbuy
nav: Providers
network: true
overview: 'Friendbuy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authorization API, Customers API, and 4 more. Tagged areas include Referral Marketing, Loyalty, Rewards, E-Commerce, and Marketing.


  The Friendbuy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Friendbuy''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, support, and 24 more developer resources.'
plans:
- name: Friendbuy Plans Pricing
  plan_count: 3
  slug: friendbuy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Friendbuy Rate Limits
  slug: friendbuy-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 4.5
    contract_quality: 21.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/friendbuy/refs/heads/main/screenshots/friendbuy-2026-07-25T215215.png
security:
- kind: authentication
  name: Friendbuy Authentication
  slug: friendbuy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Friendbuy Domain Security
  slug: friendbuy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: friendbuy
tags:
- Referral Marketing
- Loyalty
- Rewards
- E-Commerce
- Marketing
- Advocacy
website: https://friendbuy.com
---
