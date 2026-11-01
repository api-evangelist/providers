---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Joinbunch Com Agentic Access
  operation_count: 2
  slug: joinbunch-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://ai.bunch.capital
  baseurl_source: declared
  description: The files API from Bunch — 2 operation(s) for files.
  name: Bunch Files API
  slug: joinbunch-com-files-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/joinbunch-com/agentic-access/joinbunch-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/joinbunch-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/joinbunch-com/plans/joinbunch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/joinbunch-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/joinbunch-com/rules/joinbunch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/joinbunch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/joinbunch-com/json-ld/joinbunch-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/joinbunch-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/joinbunch-com/vocabulary/joinbunch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/joinbunch-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/joinbunch-com/data-model/joinbunch-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/joinbunch-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/joinbunch-com/errors/joinbunch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/joinbunch-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/joinbunch-com/conformance/joinbunch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/joinbunch-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/joinbunch-com/hosts/joinbunch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinbunch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinbunch-com/vendors/joinbunch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinbunch-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bunch.capital/legal/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bunch.capital/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bunch.capital/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.bunch.capital/library-category/guides
- group: company
  title: ''
  type: Blog
  url: https://www.bunch.capital/blog
- group: auth
  href: https://artifacts.apis.io/joinbunch-com/security/joinbunch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinbunch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bunch.capital
created: '2026-10-25'
description: Bunch is a Berlin‑based financial technology company building AI‑native infrastructure for private markets. It offers an all‑in‑one platform that combines secure data infrastructure, AI‑powered workflows, and expert fund services for venture capital and private equity funds, enabling seamless transactions, fund administration, SPV setup, and investor management.
image: https://cdn.prod.website-files.com/66768f27014cdc6878a27095/68f1ef65b00c7d1da8e88167_bunch.capital.webp
json_schemas:
- name: Body_extract_data_model_v1_files_extract__post
  property_count: 2
  slug: joinbunch-com-body-extract-data-model-v1-files-extract-post
- name: Body_map_columns_v1_files_map_columns__post
  property_count: 1
  slug: joinbunch-com-body-map-columns-v1-files-map-columns-post
- name: ExtractResponse
  property_count: 3
  slug: joinbunch-com-extract-response
- name: MappingResponse
  property_count: 2
  slug: joinbunch-com-mapping-response
jsonld:
- class_count: 10
  name: Joinbunch Com Context
  property_count: 14
  slug: joinbunch-com-context
layout: provider
modified: '2026-10-25'
name: Bunch
nav: Providers
network: true
overview: 'Bunch publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Files API. Tagged areas include Company, FinTech, PrivateMarkets, AI, and FundManagement.


  The Bunch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bunch''s developer surface includes pricing, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Joinbunch Com Plans Pricing
  plan_count: 4
  slug: joinbunch-com-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Bunch API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: joinbunch-com-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Joinbunch Com Domain Security
  slug: joinbunch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: joinbunch-com
tags:
- Company
- FinTech
- PrivateMarkets
- AI
- FundManagement
website: https://www.bunch.capital
---
