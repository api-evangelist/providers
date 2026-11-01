---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 34.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Panther API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Panther API
  slug: runpanther-io-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/runpanther-io/well-known/runpanther-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/runpanther-io-status-security.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.panther.com/quick-start
- group: design
  href: https://artifacts.apis.io/runpanther-io/rules/runpanther-io-rules.yml
  title: ''
  type: Spectral
  url: rules/runpanther-io-rules.yml
- group: design
  href: https://artifacts.apis.io/runpanther-io/json-ld/runpanther-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/runpanther-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/runpanther-io/vocabulary/runpanther-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/runpanther-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/runpanther-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/runpanther-io/data-model/runpanther-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/runpanther-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/runpanther-io/conformance/runpanther-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/runpanther-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/runpanther-io/llms/runpanther-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/runpanther-io-llms.txt
- group: other
  href: https://artifacts.apis.io/runpanther-io/a2a/runpanther-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/runpanther-io-a2a.yml
- group: auth
  href: https://artifacts.apis.io/runpanther-io/well-known/runpanther-io-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/runpanther-io-support-security.txt
- group: agent
  href: https://artifacts.apis.io/runpanther-io/well-known/runpanther-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/runpanther-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/runpanther-io/hosts/runpanther-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runpanther-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/runpanther-io/vendors/runpanther-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runpanther-io-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://panther.com/company/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.panther.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://panther.com/releases
- group: auth
  href: https://artifacts.apis.io/runpanther-io/security/runpanther-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runpanther-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://panther.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.panther.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.panther.com/
- group: operate
  title: ''
  type: Support
  url: https://help.panther.com/
- group: company
  title: ''
  type: Blog
  url: https://panther.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://panther.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://panther.com/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are markdown without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://docs.panther.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Panther provides an AI‑powered Security Operations Center (SOC) platform that unifies data ingestion, detection, and automated response across cloud, endpoint, and network environments. Leveraging machine learning, Panther automates alert triage, enriches incidents with context, and orchestrates remediation actions, helping security teams reduce mean‑time‑to‑detect and mean‑time‑to‑respond. The platform integrates with major cloud providers, SIEMs, and third‑party tools, offering a unified console for monitoring, investigation, and compliance reporting.
image: https://framerusercontent.com/images/bECYyaf1j2jroija0ScFzkorrSo.jpg
json_schemas:
- name: GetApiV2AuthIntrospectResponse
  property_count: 4
  slug: runpanther-io-get-api-v2-auth-introspect-response
- name: GetQueriesIdResponse
  property_count: 9
  slug: runpanther-io-get-queries-id-response
- name: PostQueriesResponse
  property_count: 9
  slug: runpanther-io-post-queries-response
- name: PostRolesIdRequest
  property_count: 4
  slug: runpanther-io-post-roles-id-request
- name: PostRolesRequest
  property_count: 4
  slug: runpanther-io-post-roles-request
- name: PostRulesRequest
  property_count: 19
  slug: runpanther-io-post-rules-request
jsonld:
- class_count: 38
  name: Runpanther Io Context
  property_count: 55
  slug: runpanther-io-context
layout: provider
modified: '2026-10-29'
name: Panther
nav: Providers
network: true
overview: 'Panther is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, AI, SOC, Cloud, and Automation.


  The Panther catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Panther''s developer surface includes getting-started guide, changelog, documentation, API reference, support, engineering blog, and 19 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Panther API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: runpanther-io-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 42.1
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Runpanther Io Domain Security
  slug: runpanther-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: runpanther-io
tags:
- Security
- AI
- SOC
- Cloud
- Automation
website: https://panther.com/
---
