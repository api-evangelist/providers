---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buckaroo Agentic Access
  operation_count: 1
  slug: buckaroo-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Payment platform API providing accounts, transactions, and related operations.
  name: Buckaroo API
  slug: buckaroo-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/buckaroo/well-known/buckaroo-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buckaroo-www-security.txt
- group: agent
  href: https://artifacts.apis.io/buckaroo/agentic-access/buckaroo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buckaroo-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/buckaroo/rate-limits/buckaroo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/buckaroo-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/buckaroo/rules/buckaroo-rules.yml
  title: ''
  type: Spectral
  url: rules/buckaroo-rules.yml
- group: design
  href: https://artifacts.apis.io/buckaroo/vocabulary/buckaroo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buckaroo-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://www.buckaroo.nl/media/fwdj2uvv/responsible-disclosure-policy-eng.pdf
- group: auth
  href: https://artifacts.apis.io/buckaroo/authentication/buckaroo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buckaroo-authentication.yml
- group: design
  href: https://artifacts.apis.io/buckaroo/conformance/buckaroo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buckaroo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buckaroo/llms/buckaroo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buckaroo-llms.txt
- group: auth
  href: https://artifacts.apis.io/buckaroo/well-known/buckaroo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buckaroo-security.txt
- group: auth
  href: https://artifacts.apis.io/buckaroo/well-known/buckaroo-buckaroo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buckaroo-buckaroo-security.txt
- group: agent
  href: https://artifacts.apis.io/buckaroo/well-known/buckaroo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buckaroo-well-known.yml
- group: other
  href: https://artifacts.apis.io/buckaroo/hosts/buckaroo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buckaroo-hosts.yml
- group: other
  href: https://artifacts.apis.io/buckaroo/vendors/buckaroo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buckaroo-vendors.yml
- group: build
  href: https://artifacts.apis.io/buckaroo/packages/buckaroo-packages.yml
  title: ''
  type: SDKs
  url: packages/buckaroo-packages.yml
- group: build
  href: https://artifacts.apis.io/buckaroo/packages/buckaroo-packages.yml
  title: ''
  type: Packages
  url: packages/buckaroo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buckaroo.eu/terms-and-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://www.buckaroo.eu/about/press
- group: start
  title: ''
  type: Login
  url: https://www.buckaroo.eu/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buckaroo-it
- group: auth
  href: https://artifacts.apis.io/buckaroo/security/buckaroo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buckaroo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buckaroo/security/buckaroo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buckaroo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buckaroo.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signup.buckaroo.nl/onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buckaroo.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.buckaroo.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.buckaroo.eu/online-payments
- group: operate
  title: ''
  type: Support
  url: https://www.buckaroo.eu/support
- group: company
  title: ''
  type: Blog
  url: https://www.buckaroo.eu/news-inspiration
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buckaroo.eu/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.buckaroo.io/swagger/v1/swagger.json
  - status: 401
    url: https://docs.buckaroo.io/mcp
  - status: 200
    url: https://buckaroo.eu/
  reason: partner-login
  state: gated
created: '2026-10-27'
description: Buckaroo provides a comprehensive payment platform offering online, in‑store and omnichannel payment solutions. It supports a wide range of payment methods including iDEAL, credit cards and PayPal, and offers plugins for major e‑commerce platforms. The company also delivers subscription management, credit management, and financing services, targeting merchants seeking integrated payment and financial tools.
image: https://www.buckaroo.eu/media/b3zlizfw/thumbnail.jpg
layout: provider
modified: '2026-10-27'
name: Buckaroo
nav: Providers
network: true
overview: 'Buckaroo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Online Payments, In‑store Payments, Omnichannel, and Credit Management.


  The Buckaroo catalog on APIs.io includes 1 Spectral governance ruleset.


  Buckaroo''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Buckaroo Plans Pricing
  plan_count: 0
  slug: buckaroo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Buckaroo Rate Limits
  slug: buckaroo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Buckaroo API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: buckaroo-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 67.9
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buckaroo Authentication
  slug: buckaroo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Buckaroo Domain Security
  slug: buckaroo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Buckaroo Vulnerability Disclosure
  slug: buckaroo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: buckaroo
tags:
- Payments
- Online Payments
- In‑store Payments
- Omnichannel
- Credit Management
- Subscription Management
- Business Lending
- Payment Terminals
website: https://buckaroo.eu/
---
