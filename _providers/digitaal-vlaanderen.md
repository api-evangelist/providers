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
api_count: 1
apis:
- description: Public digital government services API (no machine-readable spec discovered)
  name: Digitaal Vlaanderen API
  slug: digitaal-vlaanderen-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://yeswehack.com/programs/digital-flanders-vulnerability-disclosure-program
- group: auth
  href: https://artifacts.apis.io/digitaal-vlaanderen/well-known/digitaal-vlaanderen-yeswehack-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/digitaal-vlaanderen-yeswehack-security.txt
- group: auth
  href: https://artifacts.apis.io/digitaal-vlaanderen/well-known/digitaal-vlaanderen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/digitaal-vlaanderen-security.txt
- group: agent
  href: https://artifacts.apis.io/digitaal-vlaanderen/well-known/digitaal-vlaanderen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digitaal-vlaanderen-well-known.yml
- group: other
  href: https://artifacts.apis.io/digitaal-vlaanderen/hosts/digitaal-vlaanderen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitaal-vlaanderen-hosts.yml
- group: other
  href: https://artifacts.apis.io/digitaal-vlaanderen/vendors/digitaal-vlaanderen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitaal-vlaanderen-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://doc.vlaanderen.be/
- group: auth
  href: https://artifacts.apis.io/digitaal-vlaanderen/security/digitaal-vlaanderen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/digitaal-vlaanderen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/digitaal-vlaanderen/security/digitaal-vlaanderen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitaal-vlaanderen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vlaanderen.be/digitaal-vlaanderen
coverage:
  checked: '2026-10-26'
  detail: Main site renders via JavaScript and no OpenAPI/Swagger spec was found despite probing common endpoints.
  evidence:
  - status: 200
    url: https://www.vlaanderen.be/digitaal-vlaanderen
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Digitaal Vlaanderen is a digital government initiative of the Flemish region of Belgium, aiming to provide digital transformation services and platforms for public administrations and local governments. Its mission is to create a collaborative, modern public sector that works for everyone, offering expertise, tools, and support for digital projects across the region.
image: https://www.vlaanderen.be/sites/default/files/styles/large/public/2021-03/digitaal_vlaanderen_logo.png
layout: provider
modified: '2026-10-26'
name: Digitaal Vlaanderen
nav: Providers
network: true
overview: 'Digitaal Vlaanderen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Digital Transformation, Belgium, and Public Sector.


  Digitaal Vlaanderen''s developer surface includes documentation and 9 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/digitaal-vlaanderen/digitaal-vlaanderen-2026-11-03T130708.png
security:
- kind: domain-security
  name: Digitaal Vlaanderen Domain Security
  slug: digitaal-vlaanderen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Digitaal Vlaanderen Vulnerability Disclosure
  slug: digitaal-vlaanderen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: digitaal-vlaanderen
tags:
- Company
- Government
- Digital Transformation
- Belgium
- Public Sector
website: https://www.vlaanderen.be/digitaal-vlaanderen
---
