---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/bensaid-avocats-fr/llms/bensaid-avocats-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bensaid-avocats-fr-llms.txt
- group: other
  href: https://artifacts.apis.io/bensaid-avocats-fr/hosts/bensaid-avocats-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bensaid-avocats-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/bensaid-avocats-fr/vendors/bensaid-avocats-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bensaid-avocats-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bensaid-avocats-fr/security/bensaid-avocats-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bensaid-avocats-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bensaid-avocats.fr/
- group: company
  title: ''
  type: Blog
  url: https://www.bensaid-avocats.fr/actualites-du-cabinet/
- group: operate
  title: ''
  type: Support
  url: https://www.bensaid-avocats.fr/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bensaid-avocats.fr/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bensaid-avocats.fr/mentions-legales/
coverage:
  checked: '2026-11-02'
  detail: Bensaid Avocats is a law firm with no public API.
  evidence:
  - status: 404
    url: https://bensaid-avocats.fr/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: 'Cabinet d''avocats fiscalistes : fiscalité immobilière, internationale, non-résidents, fiducie, art, contentieux fiscal. Bensaid Avocats advises an international clientele on structuring, transfer and tax management of wealth, with offices in Paris, Geneva, Marseille, Cannes and Lisbon. The firm offers services in real estate, art, finance, and litigation, serving France, Switzerland and Portugal.'
image: https://www.bensaid-avocats.fr/wp-content/uploads/2019/03/Artboard-1hdpi.png
layout: provider
modified: '2026-11-02'
name: Bensaid Avocats
nav: Providers
network: true
overview: 'Bensaid Avocats is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Law, Tax, Wealth, International, and Real Estate.


  Bensaid Avocats'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 9
scopes:
- name: Bensaid Avocats Fr Scopes
  scope_count: 0
  slug: bensaid-avocats-fr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bensaid Avocats Fr Authentication
  slug: bensaid-avocats-fr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bensaid Avocats Fr Domain Security
  slug: bensaid-avocats-fr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bensaid-avocats-fr
tags:
- Law
- Tax
- Wealth
- International
- Real Estate
- Art
website: https://bensaid-avocats.fr/
---
