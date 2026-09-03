---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: Referral coupon API published as a public Postman collection. Checks and burns coupons for a referrer or a newly referred prospect, authenticated by a SHA-256 hash of the coupon code concatenated with
  name: Splio Referral API
  slug: splio-referral-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Blacklist API from Splio — 4 operation(s) for blacklist.
  name: Splio Blacklist API
  slug: splio-blacklist-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Contact API from Splio — 13 operation(s) for contact.
  name: Splio Contact API
  slug: splio-contact-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Coupon API from Splio — 1 operation(s) for coupon.
  name: Splio Coupon API
  slug: splio-coupon-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Export API from Splio — 1 operation(s) for export.
  name: Splio Export API
  slug: splio-export-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Fields API from Splio — 9 operation(s) for fields.
  name: Splio Fields API
  slug: splio-fields-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Filter API from Splio — 1 operation(s) for filter.
  name: Splio Filter API
  slug: splio-filter-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The General API from Splio — 2 operation(s) for general.
  name: Splio General API
  slug: splio-general-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Group API from Splio — 5 operation(s) for group.
  name: Splio Group API
  slug: splio-group-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Loyalty API from Splio — 1 operation(s) for loyalty.
  name: Splio Loyalty API
  slug: splio-loyalty-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Members API from Splio — 6 operation(s) for members.
  name: Splio Members API
  slug: splio-members-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The One Shot API from Splio — 3 operation(s) for one shot.
  name: Splio One Shot API
  slug: splio-one-shot-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Points API from Splio — 2 operation(s) for points.
  name: Splio Points API
  slug: splio-points-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Programs API from Splio — 4 operation(s) for programs.
  name: Splio Programs API
  slug: splio-programs-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Reward API from Splio — 11 operation(s) for reward.
  name: Splio Reward API
  slug: splio-reward-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Reward stock and codes API from Splio — 1 operation(s) for reward stock and codes.
  name: Splio Reward stock and codes API
  slug: splio-reward-stock-and-codes-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Sales data API from Splio — 14 operation(s) for sales data.
  name: Splio Sales data API
  slug: splio-sales-data-api
- baseURL: https://api.splio.com
  baseurl_source: declared
  description: The Universe API from Splio — 2 operation(s) for universe.
  name: Splio Universe API
  slug: splio-universe-api
artifact_total: 22
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/splio-customer-platform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splio-messaging-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splio-campaign-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splio-campaign-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splio-content-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splio-interactions-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://splio.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev-scp.splio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev-scp.splio.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev-scp.splio.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev-scp.splio.com/docs/how-splio-customer-platform-works
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.splio.com/kb/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.splio.com/kb/en
- group: company
  title: ''
  type: Blog
  url: https://splio.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Splio
- group: operate
  title: ''
  type: Roadmap
  url: https://helpcenter.splio.com/kb/en/splio-roadmap-446541
- group: start
  title: ''
  type: SignUp
  url: https://splio.com/en/book-a-demo/
- group: start
  title: ''
  type: Login
  url: https://www.sp-ring.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://splio.com/en/legal-notices/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://splio.com/en/personal-data-protection-policy/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/10206569/TzRX9kyT
- group: operate
  title: ''
  type: StatusPage
  url: https://status.splio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://helpcenter.splio.com/kb/en/splio-product-updates-405810
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splio-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/splio-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/splio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/splio-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/splio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/splio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/splio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/splio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/splio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/splio-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/splio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/splio-packages.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/splio-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/splio-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/splio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/splio-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/splio-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-29'
description: Splio is a Paris-headquartered customer marketing platform for retail, e-commerce, restaurant and travel brands, combining a Customer Data Platform, omnichannel marketing automation (email, SMS, WhatsApp, push), loyalty and rewards programs, mobile wallet cards and Tinyclues-derived predictive AI targeting into one "Splio Customer Platform". Brands integrate it through a JWT-authenticated REST API on api.splio.com covering contacts, custom fields, blacklists, orders, abandoned carts, products, stores, targeting groups and filters, loyalty members, points, tiers, programs and reward grant/burn, plus separate Messaging, Campaign, Content and Interactions APIs, a Datahub SFTP/CSV import path, and packaged connectors for Shopify, Magento, PrestaShop, Meta/Google/TikTok/Snapchat Ads, Criteo, Zendesk, OneSignal and Make.
image: https://splio.com/wp-content/uploads/2022/05/3250_Splio_Logo_RGB-2.png
layout: provider
modified: '2026-08-29'
name: Splio
nav: Providers
network: true
overview: 'Splio publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Referral API, Blacklist API, Contact API, and 15 more. Tagged areas include Marketing Automation, Customer Data Platform, Loyalty, CRM, and Email Marketing.


  Splio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 36 more developer resources.'
plans:
- name: Splio Plans Pricing
  plan_count: 0
  slug: splio-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Splio Rate Limits
  slug: splio-rate-limits
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 53.4
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 51.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 51.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splio/refs/heads/main/screenshots/splio-2026-09-02T160514.png
security:
- kind: authentication
  name: Splio Authentication
  slug: splio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Splio Domain Security
  slug: splio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: splio
tags:
- Marketing Automation
- Customer Data Platform
- Loyalty
- CRM
- Email Marketing
- SMS
- Mobile Wallet
- Retail
- E-Commerce
- Predictive AI
- Customer Engagement
- France
website: https://splio.com/en/
---
