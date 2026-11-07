---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Cardtonic Gift Card Developer API enables merchants and platforms to integrate gift card services into their websites, mobile apps, and point-of-sale systems. The API exposes a catalog of more tha
  name: Cardtonic Gift Card Developer API
  slug: gift-card-developer-api
- description: Cardtonic Virtual Dollar Cards are user-facing USD-denominated cards that let African customers pay merchants that accept Visa/Mastercard globally. The product is currently consumed through the Cardto
  name: Cardtonic Virtual Dollar Card
  slug: virtual-dollar-card
- description: Cardtonic Bill Payments cover airtime top-ups, mobile data, electricity, TV subscriptions, and betting wallets across more than 100 countries, consumed through the Cardtonic app and dashboard. Partner
  name: Cardtonic Bill Payments
  slug: bill-payments
- baseURL: https://api.cardtonic.com/v1
  baseurl_source: declared
  description: The Auth API from Cardtonic — 6 operation(s) for auth.
  name: Cardtonic Auth API
  slug: cardtonic-auth-api
- baseURL: https://api.cardtonic.com/v1
  baseurl_source: declared
  description: The User API from Cardtonic — 8 operation(s) for user.
  name: Cardtonic User API
  slug: cardtonic-user-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-cardtonic
common:
- group: other
  href: https://artifacts.apis.io/cardtonic/overlays/cardtonic-business-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cardtonic-business-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cardtonic/mcp/cardtonic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cardtonic-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cardtonic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://cardtonic.com/
- group: other
  title: ''
  type: Developer
  url: https://cardtonic.com/developer
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cardtonic.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cardtonic.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cardtonic.com
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.cardtonic.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.cardtonic.com/signin
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.cardtonic.com/signup
- group: company
  title: ''
  type: About
  url: https://thetonictech.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://cardtonic.com/read
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cardtonic.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.cardtonic.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://cardtonic.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cardtonic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardtonic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardtonic.com/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/cardtonic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thetonictech
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/cardtonic
- group: agent
  title: ''
  type: LlmsText
  url: https://cardtonic.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/cardtonic/llms/cardtonic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardtonic-llms.txt
- group: design
  href: https://artifacts.apis.io/cardtonic/conformance/cardtonic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardtonic-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cardtonic/conformance/cardtonic-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cardtonic-conformance.yml
- group: design
  href: https://artifacts.apis.io/cardtonic/lifecycle/cardtonic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cardtonic-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/cardtonic/packages/cardtonic-packages.yml
  title: ''
  type: Packages
  url: packages/cardtonic-packages.yml
- group: commercial
  href: https://artifacts.apis.io/cardtonic/plans/cardtonic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardtonic-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cardtonic/rate-limits/cardtonic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cardtonic-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/cardtonic/security/cardtonic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardtonic-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/cardtonic/finops/cardtonic-finops.yml
  title: ''
  type: FinOps
  url: finops/cardtonic-finops.yml
created: '2025-02-08'
description: Cardtonic is an Africa-focused fintech platform, operated by The Tonic Technologies, that lets users trade gift cards (sell unused cards for cash and buy over 14,000 local and international gift cards), issue virtual dollar cards, pay bills (airtime, data, electricity, TV, betting), purchase eSIMs in 140+ countries, and shop for gadgets through its Just Gadgets storefront. Cardtonic supports Naira and Cedi settlement for users in Nigeria and Ghana, carries a PCI DSS certification badge, and is registered with the Nigeria Data Protection Commission (NDPC) as a Data Controller of Major Importance under the Nigeria Data Protection Act 2023. For businesses, Cardtonic advertises a Gift Card Developer API (waitlist-only, no published contract) and separately publishes a real OpenAPI 3.0.1 contract for its Business API - business signup, login, 2FA, BVN and corporate KYC, and API-key issuance - through an Apidog-hosted documentation site at docs.cardtonic.com, against the base https://api.cardtonic.com/v1.
finops:
- has_sources: true
  method: generated
  name: Cardtonic Finops
  primary_unit: ''
  service_category: Fintech / Gift Cards
  slug: cardtonic-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardtonic.png
layout: provider
mcp_servers:
- description: A CANDIDATE tool list derived from Cardtonic's published OpenAPI operations. Cardtonic ships no MCP server of any kind. Nothing below is offered by the provider; each entry inherits its input schema f
  name: Cardtonic MCP Server
  slug: cardtonic-mcp-yml
modified: '2026-09-05'
name: Cardtonic
nav: Providers
network: true
overview: 'Cardtonic publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, User API, and 3 more. Tagged areas include Africa, Bill Payments, eSIM, Finance, and Fintech.


  The Cardtonic catalog on APIs.io includes 1 Spectral governance ruleset.


  Cardtonic''s developer surface includes documentation, API reference, signup flow, engineering blog, support, and 27 more developer resources.'
plans:
- name: Cardtonic Plans Pricing
  plan_count: 1
  slug: cardtonic-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Cardtonic Rate Limits
  slug: cardtonic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Cardtonic API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: cardtonic-rules
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.5
    catalog_earned_first_party: 16.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 39.5
    developer_ergonomics: 54.2
    discoverability: 64.3
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ghana
    - nigeria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 49.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cardtonic/cardtonic-2026-06-20T173956.png
security:
- kind: authentication
  name: Cardtonic Authentication
  slug: cardtonic-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cardtonic Domain Security
  slug: cardtonic-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: cardtonic-account-security
  slug: cardtonic-account-security
- name: cardtonic-api-credentials
  slug: cardtonic-api-credentials
- name: cardtonic-business-onboarding
  slug: cardtonic-business-onboarding
slug: cardtonic
tags:
- Africa
- Bill Payments
- eSIM
- Finance
- Fintech
- Gift Cards
- Ghana
- Nigeria
- Payments
- Virtual Dollar Cards
website: https://cardtonic.com/
---
