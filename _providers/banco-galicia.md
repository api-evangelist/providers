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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/banco-galicia/llms/banco-galicia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banco-galicia-llms.txt
- group: agent
  href: https://artifacts.apis.io/banco-galicia/well-known/banco-galicia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banco-galicia-well-known.yml
- group: other
  href: https://artifacts.apis.io/banco-galicia/hosts/banco-galicia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banco-galicia-hosts.yml
- group: other
  href: https://artifacts.apis.io/banco-galicia/vendors/banco-galicia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banco-galicia-vendors.yml
- group: auth
  href: https://artifacts.apis.io/banco-galicia/security/banco-galicia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banco-galicia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.galicia.ar/
- group: operate
  title: ''
  type: HelpCenter
  url: https://ayuda.bancogalicia.com.ar/
coverage:
  checked: '2026-11-02'
  detail: The main site https://www.galicia.ar/ serves only a JavaScript shell with no machine-readable documentation.
  evidence:
  - status: 200
    url: https://www.galicia.ar/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Banco Galicia is a leading Argentine bank offering a wide range of financial products and services, including personal and business accounts, credit cards, loans, mortgages, investments, and digital banking solutions. The bank’s website provides detailed information on its offerings, promotions, and customer support channels, reflecting its commitment to modern banking experiences for individuals and enterprises across Argentina.
image: https://www.galicia.ar/etc.clientlibs/galicia/clientlibs/clientlib-react/resources/logoGalicia.png
layout: provider
modified: '2026-11-02'
name: Banco Galicia
nav: Providers
network: true
overview: Banco Galicia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Finance, Argentina, and Consumer Banking.
random_paper: 2
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banco Galicia Domain Security
  slug: banco-galicia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banco-galicia
tags:
- Company
- Banking
- Finance
- Argentina
- Consumer Banking
website: https://www.galicia.ar/
---
