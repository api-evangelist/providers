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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://chempirical.com/api
  baseurl_source: declared
  description: The Chempirical (Nitramine) API API from Chempirical — 1 operation(s) for chempirical (nitramine) api.
  name: Chempirical Chempirical (Nitramine) API
  slug: chempirical-chempirical-nitramine-api-api
- baseURL: https://chempirical.com/api
  baseurl_source: declared
  description: The Molecule Svg API from Chempirical — 1 operation(s) for molecule svg.
  name: Chempirical Molecule Svg API
  slug: chempirical-molecule-svg-api
- baseURL: https://chempirical.com/api
  baseurl_source: declared
  description: The Molecules API from Chempirical — 1 operation(s) for molecules.
  name: Chempirical Molecules API
  slug: chempirical-molecules-api
- baseURL: https://chempirical.com/api
  baseurl_source: declared
  description: The Reactions API from Chempirical — 2 operation(s) for reactions.
  name: Chempirical Reactions API
  slug: chempirical-reactions-api
artifact_total: 15
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/rate-limits/chempirical-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chempirical-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/plans/chempirical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chempirical-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/rules/chempirical-rules.yml
  title: ''
  type: Spectral
  url: rules/chempirical-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/json-ld/chempirical-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chempirical-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/vocabulary/chempirical-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chempirical-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/data-model/chempirical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chempirical-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/conventions/chempirical-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chempirical-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/conformance/chempirical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chempirical-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/hosts/chempirical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chempirical-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/security/chempirical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chempirical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chempirical.com
- group: docs
  title: ''
  type: Documentation
  url: https://chempirical.com/api/
- group: company
  title: ''
  type: Blog
  url: https://chempirical.com/blog/
- group: start
  title: ''
  type: Login
  url: https://chempirical.com/auth/login
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://chempirical.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Chempirical (operated as Nitramine per the submission) publishes free tools for chemists and a free, keyless, read-only JSON API at chempirical.com/api covering compounds (names, formula, SMILES/InChI identifiers, molar mass, density, melting and boiling points, Antoine constants, azeotropes), substructure and similarity search, structure SVGs, reactions with participants and reaction scaling. CORS is open; the docs ask for a few requests per second.
image: https://chempirical.com/og-image.png
json_schemas:
- name: GetApiApiidResponse
  property_count: 1
  slug: chempirical-get-api-apiid-response
- name: GetApiMoleculeSvg50782Response
  property_count: 1
  slug: chempirical-get-api-molecule-svg50782-response
- name: GetApiMoleculesMoleculeidResponse
  property_count: 3
  slug: chempirical-get-api-molecules-moleculeid-response
- name: GetApiReactionsHenryNitroaldolResponse
  property_count: 1
  slug: chempirical-get-api-reactions-henry-nitroaldol-response
- name: GetApiReactionsHenryNitroaldolScaleResponse
  property_count: 1
  slug: chempirical-get-api-reactions-henry-nitroaldol-scale-response
- name: PostApiMoleculesMoleculeidResponse
  property_count: 3
  slug: chempirical-post-api-molecules-moleculeid-response
jsonld:
- class_count: 7
  name: Chempirical Context
  property_count: 9
  slug: chempirical-context
layout: provider
modified: '2026-10-09'
name: Chempirical
nav: Providers
network: true
overview: 'Chempirical is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Chempirical (Nitramine) API, Molecule Svg API, Molecules API, and 1 more. Tagged areas include Company, Chemistry, Compounds, Reactions, and Science.


  The Chempirical catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chempirical''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Chempirical Plans Pricing
  plan_count: 1
  slug: chempirical-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Chempirical Rate Limits
  slug: chempirical-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Chempirical API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: chempirical-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 21.0
    developer_ergonomics: 11.9
    discoverability: 71.4
    operational_transparency: 21.1
  previous_composite: 26.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/chempirical/refs/heads/main/screenshots/chempirical-2026-10-11T102859.png
security:
- kind: domain-security
  name: Chempirical Domain Security
  slug: chempirical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chempirical
tags:
- Company
- Chemistry
- Compounds
- Reactions
- Science
- Open Data
- JSON:API
website: https://chempirical.com
---
