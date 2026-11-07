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
  band: agent-ready
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
    error_semantics: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Independent property intelligence API providing Dubai property price, rent and return data.
  name: Dubai Wealth Index API
  slug: dubai-wealth-index-api
- baseURL: https://dubaiwealthindex.com
  baseurl_source: declared
  description: Registered Dubai prices, rents, gross yields and short-term rates, apartments by building and area, villas by community, published as data. Medians of Dubai Land Department sale transactions and Ejari
  name: Dubai Wealth Index HTTP API API
  slug: dubai-wealth-index-http-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/dubaiwealthindex-com/rules/dubaiwealthindex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dubaiwealthindex-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dubaiwealthindex-com/json-ld/dubaiwealthindex-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dubaiwealthindex-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dubaiwealthindex-com/vocabulary/dubaiwealthindex-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dubaiwealthindex-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dubaiwealthindex-com/conformance/dubaiwealthindex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dubaiwealthindex-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/dubaiwealthindex-com/data-model/dubaiwealthindex-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dubaiwealthindex-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dubaiwealthindex-com/errors/dubaiwealthindex-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dubaiwealthindex-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dubaiwealthindex-com/llms/dubaiwealthindex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dubaiwealthindex-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dubaiwealthindex-com/well-known/dubaiwealthindex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dubaiwealthindex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dubaiwealthindex-com/hosts/dubaiwealthindex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dubaiwealthindex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dubaiwealthindex-com/vendors/dubaiwealthindex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dubaiwealthindex-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dubaiwealthindex-com/security/dubaiwealthindex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dubaiwealthindex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dubaiwealthindex.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dubaiwealthindex.com/openapi.json
  - status: 401
    url: https://dubaiwealthindex.com/api/mcp
  - status: 403
    url: https://dubaiwealthindex.com/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: Dubai Wealth Index provides independent property intelligence for Dubai, aggregating recorded sale prices, registered rents, and comparable returns from Dubai Land Department and Ejari records. It offers forward Airbnb asking rates, building data, and market analytics to help investors, developers, and renters understand property performance across the emirate.
jsonld:
- class_count: 4
  name: Dubaiwealthindex Com Context
  property_count: 67
  slug: dubaiwealthindex-com-context
layout: provider
modified: '2026-11-06'
name: Dubai Wealth Index
nav: Providers
network: true
overview: 'Dubai Wealth Index publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including HTTP API API, and 1 more. Tagged areas include Real Estate, Data Analytics, Dubai, Property Market, and Investment.


  The Dubai Wealth Index catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Dubai Wealth Index API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: dubaiwealthindex-com-rules
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 34.7
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dubaiwealthindex Com Domain Security
  slug: dubaiwealthindex-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dubaiwealthindex-com
tags:
- Real Estate
- Data Analytics
- Dubai
- Property Market
- Investment
website: https://dubaiwealthindex.com/
---
