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
  href: https://artifacts.apis.io/c6-bank/well-known/c6-bank-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/c6-bank-clarity-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.com.br:443/
- group: operate
  title: ''
  type: Support
  url: https://support.com.br:443/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.com.br:443/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.com.br:443/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.com.br:443/
- group: agent
  href: https://artifacts.apis.io/c6-bank/well-known/c6-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/c6-bank-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://artifacts.apis.io/c6-bank/hosts/c6-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/c6-bank-hosts.yml
- group: other
  href: https://artifacts.apis.io/c6-bank/vendors/c6-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/c6-bank-vendors.yml
- group: auth
  href: https://artifacts.apis.io/c6-bank/security/c6-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/c6-bank-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/c6-bank/security/c6-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/c6-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.c6bank.com.br:443/
coverage:
  checked: '2026-10-06'
  detail: No API documentation or OpenAPI spec found at known API hosts (api.com.br) and no developer portal is listed.
  evidence:
  - status: 404
    url: https://api.com.br/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: C6 Bank is a Brazilian digital bank offering a full suite of financial products including checking accounts, credit cards, loans, investments, and international banking, all accessible via a mobile app. It emphasizes innovative features such as C6 Carbon, C6 Graphene, and AI-powered assistance, targeting both individuals and businesses with competitive rewards and low fees.
layout: provider
modified: '2026-10-06'
name: C6 Bank
nav: Providers
network: true
overview: 'C6 Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Digital Bank, and Brazil.


  C6 Bank''s developer surface includes support, documentation, and 11 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.3
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 4.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/c6-bank/c6-bank-2026-11-03T122922.png
security:
- kind: domain-security
  name: C6 Bank Domain Security
  slug: c6-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: C6 Bank Vulnerability Disclosure
  slug: c6-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: c6-bank
tags:
- Company
- Banking
- Fintech
- Digital Bank
- Brazil
website: https://www.c6bank.com.br:443/
---
