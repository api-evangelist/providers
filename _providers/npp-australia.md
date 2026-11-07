---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: The NPP API Framework defines the mandatory technical approach and data attributes for APIs built on the New Payments Platform, aligned to the ISO 20022 messaging standard. NPP Australia does not itse
  name: NPP API Framework
  slug: npp-api-framework
- description: PayTo is NPP's real-time, digital mandated-debit overlay service. It lets businesses initiate real-time payments from a customer's bank account under a pre-authorised agreement, giving consumers visib
  name: PayTo
  slug: payto
- description: 'PayID is NPP''s addressing service, allowing payments to be directed using a simple identifier such as a mobile number, email address, ABN or organisation ID instead of a BSB and account number. It is '
  name: PayID
  slug: payid
- description: 'NPP Australia (AP+) API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: NPP Australia (AP+) API
  slug: npp-australia-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/npp-australia/plans/npp-australia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/npp-australia-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/npp-australia/rules/npp-australia-rules.yml
  title: ''
  type: Spectral
  url: rules/npp-australia-rules.yml
- group: design
  href: https://artifacts.apis.io/npp-australia/vocabulary/npp-australia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/npp-australia-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/npp-australia/conventions/npp-australia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/npp-australia-conventions.yml
- group: start
  href: https://artifacts.apis.io/npp-australia/sandbox/npp-australia-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/npp-australia-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/npp-australia/lifecycle/npp-australia-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/npp-australia-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/npp-australia/errors/npp-australia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/npp-australia-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/npp-australia/llms/npp-australia-auspayplus-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/npp-australia-auspayplus-site-llms.txt
- group: other
  href: https://artifacts.apis.io/npp-australia/hosts/npp-australia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/npp-australia-hosts.yml
- group: other
  href: https://artifacts.apis.io/npp-australia/vendors/npp-australia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/npp-australia-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.auspayplus.com.au/feed
- group: auth
  href: https://artifacts.apis.io/npp-australia/security/npp-australia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/npp-australia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/npp-australia/security/npp-australia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/npp-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auspayplus.com.au/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.auspayplus.com.au/2026-ap-roadmap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developers.auspayplus.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auspayplus.com.au/solutions/npp-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.developers.auspayplus.com.au/apis/
- group: start
  title: ''
  type: Sandbox
  url: https://nppa-developer.swift.com/user/register
- group: start
  title: ''
  type: SignUp
  url: https://www.developers.auspayplus.com.au/auth/login?screen_hint=signup
- group: start
  title: ''
  type: Login
  url: https://www.developers.auspayplus.com.au/auth/login?returnTo=/
- group: company
  title: ''
  type: Blog
  url: https://www.auspayplus.com.au/news-updates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auspayplus.com.au/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auspayplus.com.au/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.developers.auspayplus.com.au/go-live/
- group: operate
  title: ''
  type: Support
  url: https://www.developers.auspayplus.com.au/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auspayplus
- group: agent
  href: https://artifacts.apis.io/npp-australia/well-known/npp-australia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/npp-australia-well-known.yml
- group: auth
  href: https://artifacts.apis.io/npp-australia/well-known/npp-australia-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/npp-australia-security.txt
- group: auth
  href: https://artifacts.apis.io/npp-australia/authentication/npp-australia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/npp-australia-authentication.yml
- group: design
  href: https://artifacts.apis.io/npp-australia/conformance/npp-australia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/npp-australia-conformance.yml
- group: design
  href: https://artifacts.apis.io/npp-australia/lifecycle/npp-australia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/npp-australia-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.auspayplus.com.au/security.txt
- group: agent
  href: https://artifacts.apis.io/npp-australia/llms/npp-australia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/npp-australia-llms.txt
created: '2026-07-24'
description: 'NPP Australia is the operator of the New Payments Platform (NPP), Australia''s national real-time, data-rich, account-to-account payments infrastructure that settles 24 hours a day, 365 days a year across more than 100 connected banks, credit unions, fintechs and government agencies. Since 2021 NPP Australia has been a wholly owned subsidiary of Australian Payments Plus (AP+), the entity formed by amalgamating NPP Australia, BPAY Group and eftpos. On top of the core clearing-and-settlement rail, NPP operates two overlay services: PayID, an addressing service that maps a mobile number, email, ABN or organisation ID to a bank account, and PayTo, a real-time mandated-debit capability that gives consumers visibility and control over recurring and one-off account debits. Its home market is Australia, and it sits alongside the Consumer Data Right as the country''s payments spine. Its API posture is that of a scheme and rail operator rather than a self-serve PSP: NPP Australia itself
  does not sell a public API, but it publishes the ISO 20022-aligned NPP API Framework that defines the mandatory technical approach and data attributes NPP Participants implement, and AP+ runs a (registration-gated) developer portal plus a SWIFT-hosted API sandbox. The consumable APIs are offered by NPP Participants, not by NPP Australia.'
image: https://www.auspayplus.com.au/wp-content/uploads/2025/09/home-logo-npp.png
layout: provider
modified: '2026-10-21'
name: NPP Australia (AP+)
nav: Providers
network: true
overview: 'NPP Australia (AP+) is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and ISO 20022.


  The NPP Australia (AP+) catalog on APIs.io includes 1 Spectral governance ruleset.


  NPP Australia (AP+)''s developer surface includes sandbox, documentation, API reference, signup flow, engineering blog, getting-started guide, support, and 27 more developer resources.'
plans:
- name: Npp Australia Plans Pricing
  plan_count: 8
  slug: npp-australia-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Npp Australia Rate Limits
  slug: npp-australia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: NPP Australia (AP+) API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: npp-australia-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 59.5
    discoverability: 69.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 41.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 22.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/npp-australia/npp-australia-2026-08-07T185651.png
security:
- kind: authentication
  name: Npp Australia Authentication
  slug: npp-australia-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Npp Australia Domain Security
  slug: npp-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Npp Australia Vulnerability Disclosure
  slug: npp-australia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: npp-australia
tags:
- Payments
- Australia
- Real-Time Payments
- Account-to-Account
- ISO 20022
- Payment Scheme
- Payment Rails
- PayTo
- PayID
- Open Banking
website: https://www.auspayplus.com.au/
---
