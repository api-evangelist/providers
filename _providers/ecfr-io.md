---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ecfr Io Agentic Access
  operation_count: 3
  slug: ecfr-io-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://ecfr.io
  baseurl_source: declared
  description: The Document API from ecfr-io — 1 operation(s) for document.
  name: ecfr-io Document API
  slug: ecfr-io-document-api
- baseURL: https://ecfr.io
  baseurl_source: declared
  description: The Search API from ecfr-io — 1 operation(s) for search.
  name: ecfr-io Search API
  slug: ecfr-io-search-api
- baseURL: https://ecfr.io
  baseurl_source: declared
  description: The Titles API from ecfr-io — 1 operation(s) for titles.
  name: ecfr-io Titles API
  slug: ecfr-io-titles-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/ecfr-io/agentic-access/ecfr-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ecfr-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ecfr-io/rules/ecfr-io-rules.yml
  title: ''
  type: Spectral
  url: rules/ecfr-io-rules.yml
- group: agent
  href: https://artifacts.apis.io/ecfr-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ecfr-io/errors/ecfr-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ecfr-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ecfr-io/conformance/ecfr-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecfr-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecfr-io/llms/ecfr-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecfr-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/ecfr-io/well-known/ecfr-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecfr-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecfr-io/hosts/ecfr-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecfr-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecfr-io/vendors/ecfr-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecfr-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ecfr-io/security/ecfr-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecfr-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecfr.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ecfr.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://ecfr.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://ecfr.io/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecfr.io/privacy-policy
created: '2026-10-30'
description: eCFR.io provides free, read‑only JSON API and MCP server access to the Electronic Code of Federal Regulations (eCFR). Users can search, browse, and retrieve current and historical federal regulations without authentication. The service includes an OpenAPI specification, developer guides, and example usage, supporting cross‑origin requests for applications and AI agents.
layout: provider
modified: '2026-10-30'
name: ecfr-io
nav: Providers
network: true
overview: 'ecfr-io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Document API, Search API, and Titles API. Tagged areas include Government, Law, Regulations, API, and OpenData.


  The ecfr-io catalog on APIs.io includes 1 Spectral governance ruleset.


  ecfr-io''s developer surface includes documentation, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ecfr-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ecfr-io-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 35.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecfr Io Domain Security
  slug: ecfr-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ecfr-io
tags:
- Government
- Law
- Regulations
- API
- OpenData
- Free
website: https://ecfr.io/
---
