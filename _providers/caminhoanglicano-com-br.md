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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Caminho Anglicano API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Caminho Anglicano API
  slug: caminhoanglicano-com-br-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/caminhoanglicano-com-br/rules/caminhoanglicano-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/caminhoanglicano-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/caminhoanglicano-com-br/vocabulary/caminhoanglicano-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/caminhoanglicano-com-br-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/caminhoanglicano-com-br/conformance/caminhoanglicano-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caminhoanglicano-com-br-conformance.yml
- group: other
  href: https://artifacts.apis.io/caminhoanglicano-com-br/hosts/caminhoanglicano-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caminhoanglicano-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/caminhoanglicano-com-br/vendors/caminhoanglicano-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caminhoanglicano-com-br-vendors.yml
- group: auth
  href: https://artifacts.apis.io/caminhoanglicano-com-br/security/caminhoanglicano-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caminhoanglicano-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caminhoanglicano.com.br/
coverage:
  checked: '2026-11-04'
  detail: The provider's website offers no developer documentation or API reference, and no machine-readable contracts were found.
  evidence:
  - status: 200
    url: https://caminhoanglicano.com.br/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: Caminho Anglicano is a digital portal for the Brazilian Anglican community, offering resources such as a church locator, lectionary, daily office app, glossary, statistics, and a digital library. It connects over 300 churches across 26 states, providing liturgical calendars, theological profiles, and tools for worship and study. The platform aims to foster connection and access to Anglican heritage in Brazil.
image: https://caminhoanglicano.com.br/screenshot-wide.png
layout: provider
modified: '2026-11-04'
name: Caminho Anglicano
nav: Providers
network: true
overview: 'Caminho Anglicano is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anglican, Community, Brazil, Religion, and DigitalPortal.


  The Caminho Anglicano catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Caminho Anglicano API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: caminhoanglicano-com-br-rules
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caminhoanglicano Com Br Domain Security
  slug: caminhoanglicano-com-br-domain-security
  summary_line: TLSv1.3 · HSTS
slug: caminhoanglicano-com-br
tags:
- Anglican
- Community
- Brazil
- Religion
- DigitalPortal
- Churches
website: https://caminhoanglicano.com.br/
---
