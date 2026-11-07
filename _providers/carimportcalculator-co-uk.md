---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Car Import Calculator API providing duty and tax calculations.
  name: Car Import Calculator API
  slug: car-import-calculator-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/carimportcalculator-co-uk/vocabulary/carimportcalculator-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carimportcalculator-co-uk-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://carimportcalculator.co.uk/terms
- group: design
  href: https://artifacts.apis.io/carimportcalculator-co-uk/conformance/carimportcalculator-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carimportcalculator-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carimportcalculator-co-uk/llms/carimportcalculator-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carimportcalculator-co-uk-llms.txt
- group: auth
  href: https://artifacts.apis.io/carimportcalculator-co-uk/well-known/carimportcalculator-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carimportcalculator-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/carimportcalculator-co-uk/well-known/carimportcalculator-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carimportcalculator-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/carimportcalculator-co-uk/hosts/carimportcalculator-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carimportcalculator-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/carimportcalculator-co-uk/vendors/carimportcalculator-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carimportcalculator-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carimportcalculator.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carimportcalculator.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/carimportcalculator-co-uk/authentication/carimportcalculator-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carimportcalculator-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/carimportcalculator-co-uk/security/carimportcalculator-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carimportcalculator-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carimportcalculator-co-uk/security/carimportcalculator-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carimportcalculator-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carimportcalculator.co.uk/
created: '2026-11-03'
description: Car Import Calculator provides a free online tool and guides to calculate UK import duty, VAT and registration costs for vehicles imported from any country. It sources rates from gov.uk, offers detailed examples, classic‑car relief information, and links to official customs and tax resources. The site also offers newsletters, data tables, and contact support for import queries.
image: https://carimportcalculator.co.uk/og.png
layout: provider
modified: '2026-11-03'
name: Car Import Calculator
nav: Providers
network: true
overview: 'Car Import Calculator is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Import, Tax, Calculator, United Kingdom, and Vehicles.


  Car Import Calculator''s developer surface includes authentication and 13 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Carimportcalculator Co Uk Authentication
  slug: carimportcalculator-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carimportcalculator Co Uk Domain Security
  slug: carimportcalculator-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carimportcalculator Co Uk Vulnerability Disclosure
  slug: carimportcalculator-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carimportcalculator-co-uk
tags:
- Import
- Tax
- Calculator
- United Kingdom
- Vehicles
website: https://carimportcalculator.co.uk/
---
