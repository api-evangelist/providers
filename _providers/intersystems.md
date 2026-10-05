---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: InterSystems Developer Hub provides documentation and resources for developers.
  name: InterSystems Developer Hub
  slug: intersystems-developer-hub
- description: The Group API from InterSystems — 1 operation(s) for group.
  name: InterSystems Group API
  slug: intersystems-group-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/rules/intersystems-rules.yml
  title: ''
  type: Spectral
  url: rules/intersystems-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/json-ld/intersystems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intersystems-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/vocabulary/intersystems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intersystems-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/data-model/intersystems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intersystems-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/conformance/intersystems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intersystems-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/llms/intersystems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intersystems-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/hosts/intersystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intersystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/vendors/intersystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intersystems-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.intersystems.com/intersystems-iris-getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.intersystems.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intersystems/refs/heads/main/security/intersystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intersystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.intersystems.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on InterSystems hosts.
  evidence:
  - status: 404
    url: https://developer.intersystems.com/openapi.json
  - status: 404
    url: https://developer.intersystems.com/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: 'InterSystems is a company surfaced via the API Evangelist harvest backlog (source: gartner-mq) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetGroupResponse
  property_count: 8
  slug: intersystems-get-group-response
jsonld:
- class_count: 1
  name: Intersystems Context
  property_count: 0
  slug: intersystems-context
layout: provider
modified: '2026-10-03'
name: InterSystems
nav: Providers
network: true
overview: 'InterSystems publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Group API, and 1 more. Tagged areas include Company.


  The InterSystems catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  InterSystems'' developer surface includes getting-started guide, documentation, and 10 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: InterSystems API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: intersystems-rules
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 21.4
    discoverability: 42.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Intersystems Domain Security
  slug: intersystems-domain-security
  summary_line: TLSv1.3 · DMARC
slug: intersystems
tags:
- Company
website: https://www.intersystems.com
---
