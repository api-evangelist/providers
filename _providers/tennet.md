---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: Public API (v1) providing electricity market data.
  name: TenneT Public API
  slug: tennet-public-api
- baseURL: https://api.tennet.eu
  baseurl_source: declared
  description: 'TenneT API as documented publicly: 71 operations. Contract generated from the documentation by API Evangelist (2026-09-23); not the provider''s own document.'
  name: TenneT API
  slug: tennet-api
artifact_total: 7
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/rules/tennet-rules.yml
  title: ''
  type: Spectral
  url: rules/tennet-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/json-ld/tennet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tennet-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/vocabulary/tennet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tennet-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/data-model/tennet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tennet-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/security/tennet-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tennet-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/conformance/tennet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tennet-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/well-known/tennet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tennet-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/well-known/tennet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tennet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/hosts/tennet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tennet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/vendors/tennet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tennet-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tennet.eu/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/security/tennet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tennet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tennet/refs/heads/main/security/tennet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tennet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tennet.eu/
coverage:
  checked: 2026-09-23
  detail: API spec is embedded in HTML page and not directly machine‑readable.
  evidence:
  - status: 200
    url: https://developer.tennet.eu/specs/v1/public-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: TenneT is a leading European transmission system operator (TSO) responsible for high‑voltage electricity grids in the Netherlands and Germany. It ensures reliable, secure power supply, drives the energy transition, and provides market platforms for electricity trading. The company focuses on sustainability, grid expansion, and digital innovation to support a low‑carbon future.
json_schemas:
- name: GetPublicationsV1V1IdResponse
  property_count: 2
  slug: tennet-get-publications-v1-v1-id-response
jsonld:
- class_count: 1
  name: Tennet Context
  property_count: 2
  slug: tennet-context
layout: provider
modified: '2026-09-23'
name: TenneT
nav: Providers
network: true
overview: 'TenneT publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Transmission, Grid Operator, Europe, and Sustainability.


  The TenneT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TenneT''s developer surface includes documentation and 13 more developer resources.'
random_paper: 16
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: TenneT API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: tennet-rules
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 14.5
    developer_ergonomics: 9.5
    discoverability: 55.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tennet Domain Security
  slug: tennet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tennet Vulnerability Disclosure
  slug: tennet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tennet
tags:
- Energy
- Transmission
- Grid Operator
- Europe
- Sustainability
- Company
website: https://www.tennet.eu/
---
