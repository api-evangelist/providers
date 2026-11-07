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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CareRanks API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: CareRanks API
  slug: careranks-com-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/careranks-com/rules/careranks-com-rules.yml
  title: ''
  type: Spectral
  url: rules/careranks-com-rules.yml
- group: design
  href: https://artifacts.apis.io/careranks-com/vocabulary/careranks-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/careranks-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/careranks-com/conformance/careranks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/careranks-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/careranks-com/llms/careranks-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/careranks-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/careranks-com/well-known/careranks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/careranks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/careranks-com/hosts/careranks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careranks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/careranks-com/vendors/careranks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careranks-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.careranks.com/
- group: auth
  href: https://artifacts.apis.io/careranks-com/security/careranks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careranks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careranks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://careranks.com/about/
- group: start
  title: ''
  type: GettingStarted
  url: https://careranks.com/guides/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careranks.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careranks.com/legal/privacy
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite documentation pages.
  evidence:
  - status: 404
    url: https://careranks.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CareRanks provides independent hospital quality ratings and price transparency for nearly 7,000 hospitals across the United States. Built by InfoBakery LLC in West Hartford, Connecticut, the platform aggregates federally required price files and quality metrics, offering patients free access to compare procedures, costs, and outcomes without paid placements. The service emphasizes data accuracy, correction submissions, and a claim‑free model, ensuring that hospital listings remain unbiased and publicly sourced.
image: https://careranks.com/og-default.png
layout: provider
modified: '2026-11-03'
name: CareRanks
nav: Providers
network: true
overview: 'CareRanks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Transparency, Data, Hospitals, and Pricing.


  The CareRanks catalog on APIs.io includes 1 Spectral governance ruleset.


  CareRanks'' developer surface includes documentation, getting-started guide, and 12 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: CareRanks API Rules
  rule_count: 24
  severity_counts:
    error: 22
    hint: 0
    info: 1
    warn: 1
  slug: careranks-com-rules
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Careranks Com Domain Security
  slug: careranks-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: careranks-com
tags:
- Healthcare
- Transparency
- Data
- Hospitals
- Pricing
website: https://careranks.com/
---
