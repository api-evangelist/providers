---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Miele provides a REST API for accessing appliance data and control. Documentation is available at the developer portal.
  name: Miele API
  slug: miele-api-2
- description: 'Miele API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Miele API
  slug: miele-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/miele/well-known/miele-miele-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/miele-miele-security.txt
- group: design
  href: https://artifacts.apis.io/miele/rules/miele-rules.yml
  title: ''
  type: Spectral
  url: rules/miele-rules.yml
- group: design
  href: https://artifacts.apis.io/miele/json-ld/miele-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/miele-context.jsonld
- group: design
  href: https://artifacts.apis.io/miele/vocabulary/miele-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/miele-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/miele/data-model/miele-data-model.yml
  title: ''
  type: DataModel
  url: data-model/miele-data-model.yml
- group: operate
  href: https://artifacts.apis.io/miele/changelog/miele-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/miele-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.miele.com/en/com/cybersicherheit-5047.htm#p5262
- group: auth
  href: https://artifacts.apis.io/miele/authentication/miele-authentication.yml
  title: ''
  type: Authentication
  url: authentication/miele-authentication.yml
- group: design
  href: https://artifacts.apis.io/miele/conformance/miele-conformance.yml
  title: ''
  type: Conformance
  url: conformance/miele-conformance.yml
- group: agent
  href: https://artifacts.apis.io/miele/llms/miele-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/miele-llms.txt
- group: auth
  href: https://artifacts.apis.io/miele/well-known/miele-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/miele-www-security.txt
- group: auth
  href: https://artifacts.apis.io/miele/well-known/miele-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/miele-security.txt
- group: agent
  href: https://artifacts.apis.io/miele/well-known/miele-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/miele-well-known.yml
- group: other
  href: https://artifacts.apis.io/miele/hosts/miele-hosts.yml
  title: ''
  type: Hosts
  url: hosts/miele-hosts.yml
- group: build
  href: https://artifacts.apis.io/miele/packages/miele-packages.yml
  title: ''
  type: SDKs
  url: packages/miele-packages.yml
- group: build
  href: https://artifacts.apis.io/miele/packages/miele-packages.yml
  title: ''
  type: Packages
  url: packages/miele-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.miele.com/legal-notice
- group: docs
  title: ''
  type: APIReference
  url: https://developer.miele.com/docs/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.miele.com/docs/general-concept
- group: docs
  title: ''
  type: Documentation
  url: https://developer.miele.com/
- group: auth
  href: https://artifacts.apis.io/miele/security/miele-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/miele-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/miele/security/miele-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/miele-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://miele.com/
coverage:
  detail: Developer portal Swagger UI is rendered via JavaScript, no machine‑readable OpenAPI spec could be retrieved.
  evidence:
  - status: 200
    url: https://developer.miele.com/docs/swagger
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Miele is a German manufacturer of high-end domestic appliances and commercial equipment, known for its premium quality, innovative technology, and timeless design. The company offers a wide range of products including washing machines, dryers, dishwashers, ovens, refrigerators, coffee machines, and vacuum cleaners. Miele emphasizes durability, sustainability, and user-friendly features, serving customers worldwide through a network of subsidiaries and authorized dealers.
json_schemas:
- name: GetFeaturesResponse
  property_count: 4
  slug: miele-get-features-response
jsonld:
- class_count: 1
  name: Miele Context
  property_count: 4
  slug: miele-context
layout: provider
modified: '2026-10-28'
name: Miele
nav: Providers
network: true
overview: 'Miele is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Appliances, Home, Technology, and German.


  The Miele catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Miele''s developer surface includes changelog, authentication, API reference, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Miele API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: miele-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.2
    catalog_earned_first_party: 0.0
    catalog_gap: 68.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 16.5
    developer_ergonomics: 47.6
    discoverability: 53.6
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Miele Authentication
  slug: miele-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Miele Domain Security
  slug: miele-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Miele Vulnerability Disclosure
  slug: miele-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: miele
tags:
- Company
- Appliances
- Home
- Technology
- German
website: https://miele.com/
---
