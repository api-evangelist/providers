---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: The Codes API from QRX — 3 operation(s) for codes.
  name: QRX Codes API
  slug: qrx-codes-api
- description: The QRX API API from QRX — 1 operation(s) for qrx api.
  name: QRX QRX API
  slug: qrx-qrx-api-api
artifact_total: 12
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/vendors/qrx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qrx-vendors.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/plans/qrx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qrx-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/rules/qrx-rules.yml
  title: ''
  type: Spectral
  url: rules/qrx-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/json-ld/qrx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qrx-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/vocabulary/qrx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qrx-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/data-model/qrx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qrx-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/conformance/qrx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qrx-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/llms/qrx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qrx-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/well-known/qrx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qrx-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/hosts/qrx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qrx-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qrx.codes/terms
- group: operate
  title: ''
  type: Support
  url: https://qrx.codes/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qrx.codes/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://qrx.codes/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://qrx.codes/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qrx/refs/heads/main/security/qrx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qrx.codes
- group: docs
  title: ''
  type: Documentation
  url: https://qrx.codes/developers
coverage:
  checked: '2026-10-11'
  detail: QRX website returns a JavaScript shell that prevents automated fetching of documentation.
  evidence:
  - status: 200
    url: https://qrx.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: QRX provides an artistic QR code generation service powered by AI, allowing users to create visually appealing, scannable QR codes from textual prompts and destination URLs. The platform offers free and paid plans, API access for developers, and tools for customizing code appearance, with features like link redirection, Wi‑Fi codes, and post‑print updates.
image: https://qrx.codes/images/qrx-share.png
json_schemas:
- name: GetV1CodesIdResponse
  property_count: 14
  slug: qrx-get-v1-codes-id-response
- name: GetV1V1IdResponse
  property_count: 3
  slug: qrx-get-v1-v1-id-response
- name: PatchV1CodesIdRequest
  property_count: 1
  slug: qrx-patch-v1-codes-id-request
- name: PatchV1CodesIdResponse
  property_count: 14
  slug: qrx-patch-v1-codes-id-response
- name: PostV1CodesIdReportRequest
  property_count: 1
  slug: qrx-post-v1-codes-id-report-request
- name: PostV1CodesIdReportResponse
  property_count: 3
  slug: qrx-post-v1-codes-id-report-response
jsonld:
- class_count: 7
  name: Qrx Context
  property_count: 20
  slug: qrx-context
layout: provider
modified: '2026-10-11'
name: QRX
nav: Providers
network: true
overview: 'QRX is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Codes API and QRX API. Tagged areas include Company, QR Codes, Artificial Intelligence, and Art.


  The QRX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  QRX''s developer surface includes support, pricing, API reference, documentation, and 14 more developer resources.'
plans:
- name: Qrx Plans Pricing
  plan_count: 2
  slug: qrx-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: QRX API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: qrx-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 24.8
    developer_ergonomics: 21.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Qrx Domain Security
  slug: qrx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qrx
tags:
- Company
- QR Codes
- Artificial Intelligence
- Art
website: https://qrx.codes
---
