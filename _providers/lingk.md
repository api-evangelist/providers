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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://www.lingkapis.com/v1
  baseurl_source: declared
  description: 'Lingk API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Lingk API
  slug: lingk-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/lingk/rules/lingk-rules.yml
  title: ''
  type: Spectral
  url: rules/lingk-rules.yml
- group: design
  href: https://artifacts.apis.io/lingk/json-ld/lingk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lingk-context.jsonld
- group: design
  href: https://artifacts.apis.io/lingk/vocabulary/lingk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lingk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lingk/data-model/lingk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lingk-data-model.yml
- group: design
  href: https://artifacts.apis.io/lingk/conformance/lingk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lingk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lingk/llms/lingk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lingk-llms.txt
- group: agent
  href: https://artifacts.apis.io/lingk/well-known/lingk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lingk-well-known.yml
- group: other
  href: https://artifacts.apis.io/lingk/hosts/lingk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lingk-hosts.yml
- group: other
  href: https://artifacts.apis.io/lingk/vendors/lingk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lingk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lingk.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lingk.io/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lingk.io/
- group: auth
  href: https://artifacts.apis.io/lingk/security/lingk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lingk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lingk.io/
coverage:
  checked: '2026-10-20'
  detail: Provider's docs are public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://developers.lingk.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Lingk provides an expert-led, AI-accelerated data integration, migration, and automation platform. Combining an enterprise iPaaS with expert services, Lingk modernizes business processes through seamless data flow and modernized workflows across systems.
image: http://static1.squarespace.com/static/630cf9e1f6232e304ef0bc28/t/67003a0ad95b9f7fea51ba7e/1666915972884/Screen_Shot_2022-09-30_at_7.42.56_AM_224x164.png?format=1500w
json_schemas:
- name: PostSelfEventsRequest
  property_count: 3
  slug: lingk-post-self-events-request
- name: PostSelfWebhooksSubscriptionsRequest
  property_count: 5
  slug: lingk-post-self-webhooks-subscriptions-request
jsonld:
- class_count: 2
  name: Lingk Context
  property_count: 8
  slug: lingk-context
layout: provider
modified: '2026-10-20'
name: Lingk
nav: Providers
network: true
overview: 'Lingk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, iPaaS, Automation, and Artificial Intelligence.


  The Lingk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lingk''s developer surface includes documentation and 13 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Lingk API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: lingk-rules
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
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
  name: Lingk Domain Security
  slug: lingk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lingk
tags:
- Company
- Data Integration
- iPaaS
- Automation
- Artificial Intelligence
website: https://lingk.io/
---
