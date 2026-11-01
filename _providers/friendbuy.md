---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-10-31'
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
artifact_total: 26
asyncapis:
- description: ''
  name: Friendbuy Webhooks
  slug: friendbuy-webhooks
collections:
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.friendbuy.com/book-a-meeting
- group: other
  href: https://artifacts.apis.io/friendbuy/capabilities/friendbuy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/friendbuy-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/friendbuy/agentic-access/friendbuy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/friendbuy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/friendbuy/security/friendbuy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/friendbuy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/friendbuy/authentication/friendbuy-authentication.yml
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
  href: https://artifacts.apis.io/friendbuy/plans/friendbuy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/friendbuy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/friendbuy/rate-limits/friendbuy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/friendbuy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/friendbuy/finops/friendbuy-finops.yml
  title: ''
  type: FinOps
  url: finops/friendbuy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://friendbuy.com/blog
- group: build
  href: https://artifacts.apis.io/friendbuy/packages/friendbuy-packages.yml
  title: ''
  type: Packages
  url: packages/friendbuy-packages.yml
- group: build
  href: https://artifacts.apis.io/friendbuy/packages/friendbuy-packages.yml
  title: ''
  type: SDKs
  url: packages/friendbuy-packages.yml
- group: design
  href: https://artifacts.apis.io/friendbuy/conventions/friendbuy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/friendbuy-conventions.yml
- group: design
  href: https://artifacts.apis.io/friendbuy/errors/friendbuy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/friendbuy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/friendbuy/lifecycle/friendbuy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/friendbuy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://friendbuy.statuspage.io
- group: design
  href: https://artifacts.apis.io/friendbuy/conformance/friendbuy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/friendbuy-conformance.yml
- group: design
  href: https://artifacts.apis.io/friendbuy/asyncapi/friendbuy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/friendbuy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/friendbuy/data-model/friendbuy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/friendbuy-data-model.yml
- group: design
  href: https://artifacts.apis.io/friendbuy/components/friendbuy-components.yml
  title: ''
  type: Components
  url: components/friendbuy-components.yml
- group: agent
  href: https://artifacts.apis.io/friendbuy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/friendbuy/llms/friendbuy-llms.txt
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
- has_sources: true
  method: derived
  name: Friendbuy Finops
  primary_unit: ''
  service_category: ''
  slug: friendbuy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friendbuy.png
layout: provider
modified: '2026-08-13'
name: Friendbuy
nav: Providers
network: true
overview: 'Friendbuy publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Authorization API, Customers API, and 4 more. Tagged areas include Referral Marketing, Loyalty, Rewards, E-Commerce, and Marketing.


  The Friendbuy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Friendbuy''s developer surface includes pricing, authentication, documentation, engineering blog, changelog, API reference, getting-started guide, and 26 more developer resources.'
plans:
- name: Friendbuy Plans Pricing
  plan_count: 3
  slug: friendbuy-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Friendbuy Rate Limits
  slug: friendbuy-rate-limits
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 8.1
    developer_ergonomics: 67.3
    discoverability: 66.1
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/friendbuy/friendbuy-2026-07-25T215215.png
security:
- kind: authentication
  name: Friendbuy Authentication
  slug: friendbuy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Friendbuy Domain Security
  slug: friendbuy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Receive and verify Friendbuy webhooks and callbacks
  slug: friendbuy-consume-webhooks
- name: Read, adjust and redeem a Friendbuy loyalty ledger
  slug: friendbuy-loyalty-ledger-and-redeem
- name: Service a CCPA/GDPR data request against Friendbuy
  slug: friendbuy-privacy-data-requests
- name: Mint a Friendbuy referral link and track the conversion it produces
  slug: friendbuy-referral-link-and-track-conversion
slug: friendbuy
tags:
- Referral Marketing
- Loyalty
- Rewards
- E-Commerce
- Marketing
- Advocacy
- Loyalty & Incentives
website: https://friendbuy.com
---
