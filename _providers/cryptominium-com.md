---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides live cryptocurrency price data, analytics tools and guides. Documentation is at the Developers portal.
  name: Cryptominium API
  slug: cryptominium-api
- description: 'Cryptominium API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cryptominium API
  slug: cryptominium-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/cryptominium-com/plans/cryptominium-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptominium-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cryptominium-com/rules/cryptominium-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptominium-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptominium-com/json-ld/cryptominium-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cryptominium-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptominium-com/vocabulary/cryptominium-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptominium-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cryptominium-com/data-model/cryptominium-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cryptominium-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cryptominium-com/conformance/cryptominium-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptominium-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cryptominium-com/well-known/cryptominium-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cryptominium-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cryptominium-com/well-known/cryptominium-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cryptominium-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cryptominium-com/hosts/cryptominium-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptominium-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptominium-com/vendors/cryptominium-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptominium-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptominium.com/terms
- group: auth
  title: ''
  type: Security
  url: https://cryptominium.com/directory/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptominium.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://cryptominium.com/press
- group: start
  title: ''
  type: Login
  url: https://cryptominium.com/account/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cryptominium.com/developers
- group: auth
  href: https://artifacts.apis.io/cryptominium-com/security/cryptominium-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cryptominium-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cryptominium-com/security/cryptominium-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptominium-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptominium.com/
coverage:
  checked: '2026-11-04'
  detail: Developers portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://cryptominium.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Cryptominium measures what crypto positions could actually be sold for, not only what they are quoted at. It provides live prices for over 1,300 cryptocurrencies and calculates measured exit costs, liquidity and routing impacts, giving users realistic valuations for their holdings. The platform offers guides, company insights, and tools for builders to understand crypto market dynamics.
image: https://cryptominium.com/assets/og-default.png?v=1793432751
json_schemas:
- name: GetExitBaseAerodromeFinanceResponse
  property_count: 5
  slug: cryptominium-com-get-exit-base-aerodrome-finance-response
jsonld:
- class_count: 1
  name: Cryptominium Com Context
  property_count: 5
  slug: cryptominium-com-context
layout: provider
modified: '2026-11-04'
name: Cryptominium
nav: Providers
network: true
overview: 'Cryptominium is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Market Data, Analytics, Guides, and Tools.


  The Cryptominium catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Cryptominium Com Plans Pricing
  plan_count: 9
  slug: cryptominium-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Cryptominium API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: cryptominium-com-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptominium Com Domain Security
  slug: cryptominium-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cryptominium Com Vulnerability Disclosure
  slug: cryptominium-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cryptominium-com
tags:
- Cryptocurrency
- Market Data
- Analytics
- Guides
- Tools
- Company
website: https://cryptominium.com/
---
