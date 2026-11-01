---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://xmlfeed.theeasyapi.com
  baseurl_source: declared
  description: 'The Easy API API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: The Easy API API
  slug: theeasyapi-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/theeasyapi/plans/theeasyapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/theeasyapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/theeasyapi/rules/theeasyapi-rules.yml
  title: ''
  type: Spectral
  url: rules/theeasyapi-rules.yml
- group: design
  href: https://artifacts.apis.io/theeasyapi/vocabulary/theeasyapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/theeasyapi-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/theeasyapi/authentication/theeasyapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theeasyapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/theeasyapi/conformance/theeasyapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theeasyapi-conformance.yml
- group: other
  href: https://artifacts.apis.io/theeasyapi/hosts/theeasyapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theeasyapi-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://theeasyapi.com/login
- group: auth
  href: https://artifacts.apis.io/theeasyapi/security/theeasyapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theeasyapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theeasyapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://theeasyapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://theeasyapi.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://theeasyapi.com/pricing
- group: company
  title: ''
  type: About
  url: https://theeasyapi.com/about
- group: operate
  title: ''
  type: Contact
  url: https://theeasyapi.com/contact
coverage:
  checked: '2026-10-21'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://theeasyapi.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: The Easy API provides a unified interface to a variety of data services, including worldwide country information, Google PageRank, Safe Browsing URLs, U.S. zip code data, and zip code radius searches. Since 2010, the company has offered developers a single API that consolidates multiple data sources, delivering fast responses in under a second, reliable support, and flexible pricing plans. Their platform aims to save developers time and energy by handling the integration and translation of multiple APIs into one cohesive service, backed by a history of trusted performance and customer support.
layout: provider
modified: '2026-10-21'
name: The Easy API
nav: Providers
network: true
overview: 'The Easy API is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Integration, Developer Tools, and Services.


  The The Easy API catalog on APIs.io includes 1 Spectral governance ruleset.


  The Easy API''s developer surface includes authentication, documentation, getting-started guide, pricing, and 10 more developer resources.'
plans:
- name: Theeasyapi Plans Pricing
  plan_count: 3
  slug: theeasyapi-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: The Easy API API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: theeasyapi-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 47.8
    catalog_earned_first_party: 12.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 33.3
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Theeasyapi Authentication
  slug: theeasyapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Theeasyapi Domain Security
  slug: theeasyapi-domain-security
  summary_line: TLSv1.3
slug: theeasyapi
tags:
- Data
- Integration
- Developer Tools
- Services
website: https://theeasyapi.com/
---
