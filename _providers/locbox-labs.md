---
access_model:
  confidence: medium
  label: Partner-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://github.com/LocBoxLabs/hownd-examples
  - https://hownd.com/pricing/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A secured REST API that lets an approved Hownd partner manage Subscribers on behalf of Hownd customers (merchants and businesses). Partners are issued OAuth 2.0 client credentials and retrieve a beare
  name: Hownd Partner API
  slug: hownd-partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/locbox-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hownd.com
- group: docs
  title: ''
  type: Documentation
  url: https://hownd.com/knowledge-base/
- group: start
  title: ''
  type: GettingStarted
  url: https://hownd.com/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LocBoxLabs
- group: commercial
  title: ''
  type: Pricing
  url: https://hownd.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/locbox-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/locbox-labs-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://hownd.app/sign-in/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hownd.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hownd.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://hownd.com/data-protection-addendum/
- group: company
  title: ''
  type: Blog
  url: https://hownd.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hownd.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://hownd.com/contact/
- group: build
  title: ''
  type: Packages
  url: packages/locbox-labs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/locbox-labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/locbox-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/locbox-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/locbox-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/locbox-labs-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/locbox-labs-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/locbox-labs-llms.txt
created: '2026-07-17'
description: LocBox Labs is the engineering identity behind Hownd, Inc. (formerly FetchRev, originally LocBox), a Tempe, Arizona automated promotions and local-merchant marketing platform that helps restaurants, health and beauty businesses, family entertainment centers, attractions and retail merchants generate new and repeat customers. The platform runs automated marketing across website popups, email drip and birthday campaigns, social media, buy-now promos, gift cards, a promo discovery portal, the MyHownd consumer mobile app, and guest-WiFi capture, billed at a flat monthly fee plus a share of each transaction. Merchants work in the Hownd app at hownd.app, with the legacy FetchRev merchant application still served at app.locbox.com. Hownd operates a partner-gated REST API at partner-api.hownd.com that lets approved partners manage subscribers on behalf of Hownd merchants; it is authenticated with OAuth 2.0 client-credentials against the company's Auth0 tenant and scoped per merchant
  with an X-Tenant-Id header. No OpenAPI, public API reference, or developer portal is published for it — the only public documentation is the first-party example repository in the company's LocBoxLabs GitHub org.
image: https://s21429.pcdn.co/wp-content/uploads/2020/05/hownd-logo-blue.svg
layout: provider
modified: '2026-08-13'
name: LocBox Labs
nav: Providers
network: true
overview: 'LocBox Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Promotions, Local Marketing, and Small Business.


  LocBox Labs'' developer surface includes documentation, getting-started guide, pricing, engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Locbox Labs Plans Pricing
  plan_count: 1
  slug: locbox-labs-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Locbox Labs Rate Limits
  slug: locbox-labs-rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 31.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/locbox-labs/refs/heads/main/screenshots/locbox-labs-2026-07-25T225435.png
security:
- kind: authentication
  name: Locbox Labs Authentication
  slug: locbox-labs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Locbox Labs Domain Security
  slug: locbox-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: locbox-labs
tags:
- Company
- Marketing
- Promotions
- Local Marketing
- Small Business
- Automation
- Coupons
- Email Marketing
- Loyalty
- Guest WiFi
- Family Entertainment
- Restaurant
website: https://hownd.com
---
