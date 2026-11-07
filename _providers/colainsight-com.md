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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Colainsight API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Colainsight API
  slug: colainsight-com-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/colainsight-com/rules/colainsight-com-rules.yml
  title: ''
  type: Spectral
  url: rules/colainsight-com-rules.yml
- group: design
  href: https://artifacts.apis.io/colainsight-com/vocabulary/colainsight-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/colainsight-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/colainsight-com/conformance/colainsight-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/colainsight-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/colainsight-com/llms/colainsight-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/colainsight-com-llms.txt
- group: other
  href: https://artifacts.apis.io/colainsight-com/hosts/colainsight-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colainsight-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/colainsight-com/vendors/colainsight-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/colainsight-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.colainsight.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.colainsight.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.colainsight.com/guides/how-cola-is-calculated
- group: company
  title: ''
  type: Blog
  url: https://www.colainsight.com/blog
- group: auth
  href: https://artifacts.apis.io/colainsight-com/security/colainsight-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colainsight-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://colainsight.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.colainsight.com/guides/how-cola-is-calculated
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: COLA Insight provides a Social Security COLA calculator that separates forecasts, partial inflation data, and official decisions, exposing index values, linking claims to their origins, and explaining limitations. The site is designed for quick answers while offering audit‑ready data records, methods, limitations, and sources. It operates without charge, may display advertising, and is not affiliated with any government agency.
layout: provider
modified: '2026-11-04'
name: Colainsight
nav: Providers
network: true
overview: 'Colainsight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Security, COLA, Calculator, Data API, and Medicare.


  The Colainsight catalog on APIs.io includes 1 Spectral governance ruleset.


  Colainsight''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Colainsight API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: colainsight-com-rules
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 11.9
    discoverability: 53.6
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Colainsight Com Domain Security
  slug: colainsight-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: colainsight-com
tags:
- Social Security
- COLA
- Calculator
- Data API
- Medicare
- Educational tools
website: https://colainsight.com/
---
