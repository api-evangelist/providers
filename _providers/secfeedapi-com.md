---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SEC EDGAR filings, insider trades, 13F holdings, 8-K events, XBRL financials and proxy data as JSON.
  name: SecFeed API
  slug: secfeed-api
- baseURL: https://secfeedapi.com
  baseurl_source: declared
  description: 'Every SEC EDGAR filing since 1993 as clean JSON: search and full-text search, a real-time stream and webhooks, XBRL financial statements, Forms 3/4/5, 13F, 13D/13G, 8-K items, proxy pay and governance'
  name: SecFeed API API
  slug: secfeed-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/secfeedapi-com/rules/secfeedapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/secfeedapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/secfeedapi-com/json-ld/secfeedapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/secfeedapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/secfeedapi-com/vocabulary/secfeedapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/secfeedapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/secfeedapi-com/conformance/secfeedapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/secfeedapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/secfeedapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/secfeedapi-com/data-model/secfeedapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/secfeedapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/secfeedapi-com/errors/secfeedapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/secfeedapi-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/secfeedapi-com/llms/secfeedapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secfeedapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/secfeedapi-com/hosts/secfeedapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secfeedapi-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secfeedapi.com/terms/
- group: start
  title: ''
  type: Login
  url: https://secfeedapi.com/login/
- group: auth
  href: https://artifacts.apis.io/secfeedapi-com/security/secfeedapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secfeedapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secfeedapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://secfeedapi.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://secfeedapi.com/blog/
created: '2026-10-31'
description: SecFeed provides a comprehensive SEC EDGAR data API delivering filings, insider trades, 13F holdings, and XBRL financials as clean JSON. The service offers REST endpoints, real‑time streaming, and MCP access, covering all SEC filing types since 1993 for developers, analysts, and financial applications.
image: https://secfeedapi.com/assets/logo-500.png
jsonld:
- class_count: 1
  name: Secfeedapi Com Context
  property_count: 1
  slug: secfeedapi-com-context
layout: provider
modified: '2026-10-31'
name: secfeedapi-com
nav: Providers
network: true
overview: 'secfeedapi-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including SecFeed API API, and 1 more. Tagged areas include Company, SEC, EDGAR, Data, and API.


  The secfeedapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  secfeedapi-com''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: secfeedapi-com API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: secfeedapi-com-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.7
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 79.1
    contract_quality: 30.7
    developer_ergonomics: 18.3
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Secfeedapi Com Domain Security
  slug: secfeedapi-com-domain-security
  summary_line: TLSv1.3
slug: secfeedapi-com
tags:
- Company
- SEC
- EDGAR
- Data
- API
- Finance
website: https://secfeedapi.com/
---
