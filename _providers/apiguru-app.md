---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apiguru App Agentic Access
  operation_count: 11
  slug: apiguru-app-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://dash.apiguru.app/api/v1
  baseurl_source: declared
  description: The Amazon Data API from apiguru-app — 11 operation(s) for amazon data.
  name: apiguru-app Amazon Data API
  slug: apiguru-app-amazon-data-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/apiguru-app/agentic-access/apiguru-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apiguru-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/apiguru-app/rules/apiguru-app-rules.yml
  title: ''
  type: Spectral
  url: rules/apiguru-app-rules.yml
- group: design
  href: https://artifacts.apis.io/apiguru-app/json-ld/apiguru-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apiguru-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/apiguru-app/vocabulary/apiguru-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apiguru-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apiguru-app/data-model/apiguru-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiguru-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/apiguru-app/errors/apiguru-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiguru-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apiguru-app/conformance/apiguru-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiguru-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apiguru-app/llms/apiguru-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiguru-app-llms.txt
- group: other
  href: https://artifacts.apis.io/apiguru-app/a2a/apiguru-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apiguru-app-a2a.yml
- group: auth
  href: https://artifacts.apis.io/apiguru-app/well-known/apiguru-app-agent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apiguru-app-agent-security.txt
- group: agent
  href: https://artifacts.apis.io/apiguru-app/well-known/apiguru-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiguru-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/apiguru-app/hosts/apiguru-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiguru-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiguru-app/vendors/apiguru-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiguru-app-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://dash.apiguru.app/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dash.apiguru.app/privacy
- group: auth
  href: https://artifacts.apis.io/apiguru-app/authentication/apiguru-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiguru-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/apiguru-app/security/apiguru-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiguru-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiguru.app/
created: '2026-10-30'
description: Apiguru.app provides a real‑time Amazon data API that delivers product details, pricing, reviews, seller analytics and inventory information across all Amazon marketplaces. It offers a free tier with 100 requests per month and paid plans for higher volume, targeting developers, arbitrage traders, brand owners and data‑driven businesses. The service emphasizes speed, reliability and easy integration via clean JSON responses and a no‑code dashboard.
jsonld:
- class_count: 1
  name: Apiguru App Context
  property_count: 11
  slug: apiguru-app-context
layout: provider
modified: '2026-10-30'
name: apiguru-app
nav: Providers
network: true
overview: 'apiguru-app publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Amazon Data API. Tagged areas include Company, API, Data, Amazon, and Real-time.


  The apiguru-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apiguru-app''s developer surface includes signup flow, authentication, and 16 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: apiguru-app API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: apiguru-app-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.7
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 79.1
    contract_quality: 54.4
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apiguru App Authentication
  slug: apiguru-app-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Apiguru App Domain Security
  slug: apiguru-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apiguru-app
tags:
- Company
- API
- Data
- Amazon
- Real-time
- Integration
website: https://apiguru.app/
---
