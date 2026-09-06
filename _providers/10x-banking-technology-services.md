---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The REST API surface of the 10x SuperCore platform, covering parties, subscriptions, arrangements, transaction/deposit/loan/credit-card products, repayment schedules, interest overrides, cards, statem
  name: 10x Banking Platform API
  slug: 10x-banking-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.10xbanking.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.10xbanking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.10xbanking.com/
- group: company
  title: ''
  type: Blog
  url: https://www.10xbanking.com/insights
- group: company
  title: ''
  type: BlogFeed
  url: https://www.10xbanking.com/engineering
- group: company
  title: ''
  type: Newsroom
  url: https://www.10xbanking.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.10xbanking.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.10xbanking.com/book-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.10xbanking.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.10xbanking.com/platform-evaluation-agreement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10x-banking
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/openbanking10x/10x-banking-public-workspace/overview
- group: auth
  title: ''
  type: Security
  url: https://www.10xbanking.com/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/10x-banking-technology-services-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/10x-banking-technology-services-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/10x-banking-technology-services-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/10x-banking-technology-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/10x-banking-technology-services-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/10x-banking-technology-services-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/10x-banking-technology-services-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/10x-banking-technology-services-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/10x-banking-technology-services-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/10x-banking-technology-services-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/10x-banking-technology-services-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/10x-banking-technology-services-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/10x-banking-technology-services-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/10x-banking-technology-services-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/10x-banking-technology-services-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Every path on docs.10xbanking.com — including /, /reference and /changelog — returns HTTP 302 to https://dash.readme.com/to/docs-10xbanking, the ReadMe login for 10x's private documentation project, and the sandbox API host 10x names in its own public Postman environment answers HTTP 401 (code 401.002.001) on every path including /openapi.json and every /.well-known/ location.
  evidence:
  - status: 302
    url: https://docs.10xbanking.com/
  - status: 302
    url: https://docs.10xbanking.com/reference
  - status: 401
    url: https://api.sandbox.10xbanking.com/openapi.json
  - status: 401
    url: https://api.sandbox.10xbanking.com/.well-known/oauth-authorization-server
  - status: 404
    url: https://postman.10xbanking.com/
  - status: 200
    url: https://www.10xbanking.com/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-05'
description: '10x Banking Technology Services is a London-headquartered cloud-native core banking platform vendor, founded by former Barclays CEO Antony Jenkins, whose SuperCore and "meta core" platform runs retail, business, corporate and embedded-finance banking for institutions including Chase UK, Westpac, Old Mutual, The Co-operative Bank and West Brom Building Society. The platform is sold as an API-first managed core: banks configure products rather than rebuild them, extend the core through the ProductKit SDK, APIs, templates, console and CLI tooling in Java, JavaScript, Python, Go, Ruby or .NET, and consume real-time event streams. The API contract itself is not public — the developer documentation at docs.10xbanking.com redirects every path to a ReadMe login, and the sandbox API host returns a blanket 401 — so this profile records the public surface only.'
image: https://www.10xbanking.com/hubfs/10x-fav-1.svg
layout: provider
modified: '2026-09-05'
name: 10x Banking Technology Services
nav: Providers
network: true
overview: '10x Banking Technology Services publishes 1 API on the [APIs.io](https://apis.io/) network: 10x Banking Platform API. Tagged areas include Financial-Services, Banking, Core Banking, Cloud Native, and Banking as a Service.


  10x Banking Technology Services'' developer surface includes documentation, engineering blog, support, signup flow, authentication, changelog, sandbox, and 21 more developer resources.'
plans:
- name: 10X Banking Technology Services Plans Pricing
  plan_count: 0
  slug: 10x-banking-technology-services-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: 10X Banking Technology Services Rate Limits
  slug: 10x-banking-technology-services-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 10X Banking Technology Services Authentication
  slug: 10x-banking-technology-services-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 10X Banking Technology Services Domain Security
  slug: 10x-banking-technology-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 10X Banking Technology Services Vulnerability Disclosure
  slug: 10x-banking-technology-services-vulnerability-disclosure
  summary_line: Hackerone
slug: 10x-banking-technology-services
tags:
- Financial-Services
- Banking
- Core Banking
- Cloud Native
- Banking as a Service
- Embedded Finance
- Payments
- Lending
- Deposits
- Cards
- Event Driven
- United Kingdom
- SaaS
- Fintech
website: https://www.10xbanking.com/
---
