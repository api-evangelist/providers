---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/ideal/well-known/ideal-ideal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ideal-ideal-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.ideal.nl/en/coordinated-vulnerability-disclosure
- group: auth
  href: https://artifacts.apis.io/ideal/well-known/ideal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ideal-security.txt
- group: agent
  href: https://artifacts.apis.io/ideal/well-known/ideal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ideal-well-known.yml
- group: other
  href: https://artifacts.apis.io/ideal/hosts/ideal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ideal-hosts.yml
- group: build
  href: https://artifacts.apis.io/ideal/packages/ideal-packages.yml
  title: ''
  type: SDKs
  url: packages/ideal-packages.yml
- group: build
  href: https://artifacts.apis.io/ideal/packages/ideal-packages.yml
  title: ''
  type: Packages
  url: packages/ideal-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://profile.ideal.nl/public/api/v1/auth/management
- group: auth
  href: https://artifacts.apis.io/ideal/security/ideal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ideal-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ideal/security/ideal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ideal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ideal.nl/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.ideal.nl/mcp
  - status: 403
    url: https://ideal.nl/mcp
  - status: 401
    url: https://profile.ideal.nl/api/mcp
  - status: 200
    url: https://ideal.nl/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: iDEAL is a Dutch online payment method that enables consumers to pay for e‑commerce purchases directly from their own bank accounts. It connects the shopper’s bank with the merchant’s website, providing a secure, real‑time transaction without the need for credit cards or third‑party wallets. The service is widely used across the Netherlands and integrates with many banks, offering a seamless checkout experience for both merchants and customers.
layout: provider
modified: '2026-10-26'
name: iDEAL
nav: Providers
network: true
overview: iDEAL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Banking, Europe, and E-Commerce.
random_paper: 7
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 36.6
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ideal Domain Security
  slug: ideal-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Ideal Vulnerability Disclosure
  slug: ideal-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ideal
tags:
- Payments
- Banking
- Europe
- E-Commerce
website: https://ideal.nl/
---
