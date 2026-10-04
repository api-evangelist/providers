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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-03'
api_count: 2
apis:
- baseURL: https://<origin
  baseurl_source: declared
  description: The Arctop API API from Arctop — 1 operation(s) for arctop api.
  name: Arctop Arctop API
  slug: arctop-arctop-api-api
- baseURL: https://<origin
  baseurl_source: declared
  description: The Dev API from Arctop — 6 operation(s) for dev.
  name: Arctop Dev API
  slug: arctop-dev-api
artifact_total: 11
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/rules/arctop-rules.yml
  title: ''
  type: Spectral
  url: rules/arctop-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/json-ld/arctop-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arctop-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/vocabulary/arctop-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arctop-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/data-model/arctop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arctop-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/conformance/arctop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arctop-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/llms/arctop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arctop-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/well-known/arctop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arctop-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/hosts/arctop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arctop-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/vendors/arctop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arctop-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arctop.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arctop.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arctop.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arctop/refs/heads/main/security/arctop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arctop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arctop.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Arctop develops brain‑computer interface technology to decode and understand brain activity. The company builds APIs that expose neural data, enabling developers to create applications that interpret human thoughts, emotions, and intentions in real time, advancing healthcare, research, and human‑computer interaction.
image: https://arctop.com/assets/brand/social-card.jpg
json_schemas:
- name: GetApiDevV1GroupMembersResponse
  property_count: 5
  slug: arctop-get-api-dev-v1-group-members-response
- name: GetApiDevV1SessionsIdIdResponse
  property_count: 4
  slug: arctop-get-api-dev-v1-sessions-id-id-response
- name: GetApiDevV1SessionsIdResponse
  property_count: 3
  slug: arctop-get-api-dev-v1-sessions-id-response
- name: PostApiDevV1SessionsCurrentMarkersRequest
  property_count: 3
  slug: arctop-post-api-dev-v1-sessions-current-markers-request
- name: PostApiDevV1SessionsCurrentMarkersResponse
  property_count: 5
  slug: arctop-post-api-dev-v1-sessions-current-markers-response
- name: PostResponse
  property_count: 2
  slug: arctop-post-response
jsonld:
- class_count: 7
  name: Arctop Context
  property_count: 18
  slug: arctop-context
layout: provider
modified: '2026-09-25'
name: Arctop
nav: Providers
network: true
overview: 'Arctop publishes 2 APIs on the [APIs.io](https://apis.io/) network: Arctop API and Dev API. Tagged areas include Brain-Computer Interface, Neural Data, API Platform, Healthcare, and Research.


  The Arctop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arctop''s developer surface includes documentation and 13 more developer resources.'
random_paper: 11
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Arctop API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: arctop-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.1
    developer_ergonomics: 9.5
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Arctop Domain Security
  slug: arctop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arctop
tags:
- Brain-Computer Interface
- Neural Data
- API Platform
- Healthcare
- Research
website: https://arctop.com
---
