---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: East West Bancorp's API surface is delivered by its banking subsidiary, East West Bank, through the Bridge Open Banking developer program for Global Transaction Services clients. Documented capabiliti
  name: East West Bank Bridge Open Banking API
  slug: east-west-bancorp-api
artifact_total: 7
asyncapis:
- description: ''
  name: East West Bancorp Webhooks
  slug: east-west-bancorp-webhooks
common:
- group: start
  title: ''
  type: Signup
  url: https://apiportal.eastwestbank.com/signup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/security/east-west-bancorp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/east-west-bancorp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/east-west-bank
- group: company
  title: ''
  type: Website
  url: https://www.eastwestbank.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.eastwestbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apiportal.eastwestbank.com/how-it-works
- group: docs
  title: ''
  type: APIReference
  url: https://apiportal.eastwestbank.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://apiportal.eastwestbank.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://apiportal.eastwestbank.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://apiportal.eastwestbank.com/faqs
- group: start
  title: ''
  type: SignUp
  url: https://apiportal.eastwestbank.com/signup
- group: start
  title: ''
  type: Login
  url: https://apiportal.eastwestbank.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiportal.eastwestbank.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiportal.eastwestbank.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.eastwestbank.com/ReachFurther
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EastWestBank
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://apiportal.eastwestbank.com/release-notes
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/changelog/east-west-bancorp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/east-west-bancorp-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/authentication/east-west-bancorp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/east-west-bancorp-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/conventions/east-west-bancorp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/east-west-bancorp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/conventions/east-west-bancorp-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/east-west-bancorp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/conformance/east-west-bancorp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/east-west-bancorp-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/sandbox/east-west-bancorp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/east-west-bancorp-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/lifecycle/east-west-bancorp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/east-west-bancorp-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/asyncapi/east-west-bancorp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/east-west-bancorp-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/llms/east-west-bancorp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/east-west-bancorp-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/packages/east-west-bancorp-packages.yml
  title: ''
  type: Packages
  url: packages/east-west-bancorp-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/plans/east-west-bancorp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/east-west-bancorp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/rate-limits/east-west-bancorp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/east-west-bancorp-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/finops/east-west-bancorp-finops.yml
  title: ''
  type: FinOps
  url: finops/east-west-bancorp-finops.yml
created: '2026-04-19'
description: 'East West Bancorp, Inc. (NASDAQ: EWBC) is the Pasadena, California bank holding company for East West Bank, a California state-chartered commercial bank and Member FDIC institution (NMLSR ID 469761) that specializes in cross-border U.S.-Greater China commercial banking and Global Transaction Services. The holding company publishes no API of its own; the group''s entire developer surface is East West Bank''s first-party "Bridge Open Banking" program at apiportal.eastwestbank.com, which documents APIs to open and manage master and sub accounts (with ACH transaction permissions and Excess, Deficit or TwoWay sweeps), retrieve balances, transactions and statements, transfer funds, and receive incoming and outgoing wire push notifications. Authorization is OAuth 2.0 client_credentials against an Okta token endpoint with a Bearer token, account-opening and funds-transfer requests are made idempotent by a client-generated GUID requestId, and a client certificate is required for sandbox
  and production connectivity. Portal sign-up is free and self-serve, but the API list, product library and every callable environment sit behind sign-in and Global Transaction Services sales onboarding, so no OpenAPI, Swagger or AsyncAPI document is publicly downloadable.'
finops:
- name: East West Bancorp Finops
  service_category: Banking
  slug: east-west-bancorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/east-west-bancorp.png
layout: provider
modified: '2026-09-14'
name: East West Bancorp
nav: Providers
network: true
overview: 'East West Bancorp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Commercial Banking, Treasury Management, and Open Banking.


  The East West Bancorp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  East West Bancorp''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, release notes, and 23 more developer resources.'
plans:
- name: East West Bancorp Plans Pricing
  plan_count: 0
  slug: east-west-bancorp-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: East West Bancorp Rate Limits
  slug: east-west-bancorp-rate-limits
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 46.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/east-west-bancorp/refs/heads/main/screenshots/east-west-bancorp-2026-06-20T180412.png
security:
- kind: authentication
  name: East West Bancorp Authentication
  slug: east-west-bancorp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: East West Bancorp Domain Security
  slug: east-west-bancorp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: east-west-bancorp
tags:
- Banking
- Financial Services
- Commercial Banking
- Treasury Management
- Open Banking
- Payments
- Cross-Border
- United States
website: https://www.eastwestbank.com
---
