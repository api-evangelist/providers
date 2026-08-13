---
access_model:
  confidence: medium
  label: Partner
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://api.flipp.com/flyerkit/v4.0/documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Public HTTPS/JSON API that gives retailers programmatic access to the structured circular ("publication") data that powers the Flipp platform - publications by merchant and store/postal code, publicat
  name: Flipp FlyerKit API
  slug: flipp-flyerkit-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.flipp.com/
- group: company
  title: ''
  type: CompanyWebsite
  url: https://corp.flipp.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.flipp.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.flipp.com/hc/en-ca
- group: operate
  title: ''
  type: Support
  url: https://help.flipp.com/hc/en-ca
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wishabi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corp.flipp.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corp.flipp.com/legal/terms_of_use/
- group: docs
  title: ''
  type: Documentation
  url: https://api.flipp.com/flyerkit/v4.0/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.flipp.com/flyerkit/v4.0/documentation
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flipp-wishabi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flipp-wishabi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flipp-wishabi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flipp-wishabi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flipp-wishabi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/flipp-wishabi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flipp-wishabi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flipp-wishabi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/flipp-wishabi-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flipp-wishabi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flipp-wishabi-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flipp-wishabi-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flipp-wishabi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flipp-wishabi-plans-pricing.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/wishabi
created: '2026-07-17'
description: Flipp (operated by Wishabi) is a Toronto-based retail media and digital merchandising company that connects retailers, brands, and consumers through shoppable digital experiences. Its consumer app aggregates weekly digital flyers, coupons, and shopping lists from more than 2,000 retailers including Walmart, Kroger, Home Depot, CVS, and Publix, helping shoppers find local deals and clip offers to loyalty cards. For businesses, Flipp runs a retail media platform - content collection, curation, and distribution of "full fidelity" shoppable merchandising experiences reaching over 100 million high-intent households - plus sponsored video and shoppable-item ad solutions built on 400B+ intent-based shopping signals. For retail partners Flipp publishes the FlyerKit API - a public, versioned HTTPS/JSON API at api.flipp.com that exposes publications, pages, highlights, categories, products, store locators and geo lookup so retailers can embed their own circular content in web, email and
  native experiences - alongside the Flipp Platform SDKs (FlyerKit for iOS/Android, StorefrontsKit/SKit for SFML rendering, and the DVM digital-visual-merchandising SDK) distributed from github.com/wishabi and a credentialed JFrog Artifactory. Access tokens are issued by a Flipp technical contact rather than through self-service signup.
image: https://corp.flipp.com/wp-content/uploads/2024/03/cropped-cropped-blue-1000-192x192.png
layout: provider
modified: '2026-08-12'
name: Flipp (Wishabi)
nav: Providers
network: true
overview: 'Flipp (Wishabi) publishes 1 API on the [APIs.io](https://apis.io/) network: Flipp FlyerKit API. Tagged areas include Company, Retail, Retail Media, Advertising, and Flyers.


  Flipp (Wishabi)''s developer surface includes engineering blog, support, documentation, API reference, authentication, changelog, and 20 more developer resources.'
plans:
- name: Flipp Wishabi Plans Pricing
  plan_count: 0
  slug: flipp-wishabi-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Flipp Wishabi Rate Limits
  slug: flipp-wishabi-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 26.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 44.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 11.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/flipp-wishabi/refs/heads/main/screenshots/flipp-wishabi-2026-07-25T214802.png
security:
- kind: authentication
  name: Flipp Wishabi Authentication
  slug: flipp-wishabi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flipp Wishabi Domain Security
  slug: flipp-wishabi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flipp-wishabi
tags:
- Company
- Retail
- Retail Media
- Advertising
- Flyers
- Coupons
- E-commerce
- Shopping
- Marketing
- Digital Circulars
- Publications
- Merchandising
- Product Data
- Store Locator
website: https://www.flipp.com/
---
