---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: V2Json Agentic Access
  operation_count: 6
  slug: v2json-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://v2json.skyv2x.com/api/v1
  baseurl_source: declared
  description: The decode API from V2JSON (SkyV2X) — 6 operation(s) for decode.
  name: V2JSON (SkyV2X) Decode API
  slug: v2json-decode-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/agentic-access/v2json-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/v2json-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/rules/v2json-rules.yml
  title: ''
  type: Spectral
  url: rules/v2json-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/json-ld/v2json-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/v2json-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/vocabulary/v2json-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/v2json-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/data-model/v2json-data-model.yml
  title: ''
  type: DataModel
  url: data-model/v2json-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/errors/v2json-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/v2json-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/conformance/v2json-conformance.yml
  title: ''
  type: Conformance
  url: conformance/v2json-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/llms/v2json-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/v2json-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/hosts/v2json-hosts.yml
  title: ''
  type: Hosts
  url: hosts/v2json-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/v2json/refs/heads/main/security/v2json-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/v2json-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://v2json.skyv2x.com/
- group: docs
  title: ''
  type: Documentation
  url: https://v2json.skyv2x.com/docs
created: '2026-10-11'
description: V2JSON (SkyV2X) provides a free online V2X message codec that converts ETSI C‑ITS UPER binary streams to structured JSON and back. It supports a wide range of message types including CAM, DENM, CPM, VAM, MAPEM, SPATEM, SREM, SSEM, IVIM and RTCMEM, offering byte‑exact round‑trip verification. The service is publicly accessible via a REST API with endpoints for decode, encode, and verify, and requires no API key. Documentation is available through a Swagger UI at /docs, and the company also offers an interactive web‑based codec interface.
image: https://v2json.skyv2x.com/v2json-asn1-to-json-decoder-v3.jpg
json_schemas:
- name: DecodeRequest
  property_count: 3
  slug: v2json-decode-request
- name: DecodeResponse
  property_count: 5
  slug: v2json-decode-response
- name: EncodeRequest
  property_count: 2
  slug: v2json-encode-request
- name: EncodeResponse
  property_count: 4
  slug: v2json-encode-response
- name: HealthResponse
  property_count: 3
  slug: v2json-health-response
- name: VerifyResponse
  property_count: 5
  slug: v2json-verify-response
jsonld:
- class_count: 11
  name: V2Json Context
  property_count: 25
  slug: v2json-context
layout: provider
modified: '2026-10-11'
name: V2JSON (SkyV2X)
nav: Providers
network: true
overview: 'V2JSON (SkyV2X) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Decode API. Tagged areas include V2X, C-ITS, ETSI, Codec, and Free.


  The V2JSON (SkyV2X) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  V2JSON (SkyV2X)''s developer surface includes documentation and 11 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: V2JSON (SkyV2X) API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: v2json-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 54.0
    developer_ergonomics: 9.5
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: V2Json Domain Security
  slug: v2json-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: v2json
tags:
- V2X
- C-ITS
- ETSI
- Codec
- Free
website: https://v2json.skyv2x.com/
---
