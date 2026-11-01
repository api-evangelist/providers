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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Practice management software for law firms. Streamline operations, billing, and client relationships to boost productivity and profitability.
  name: SurePoint API
  slug: surepoint-api-2
- description: 'SurePoint Pro API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: SurePoint Pro API
  slug: surepoint-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/surepoint/rules/surepoint-rules.yml
  title: ''
  type: Spectral
  url: rules/surepoint-rules.yml
- group: design
  href: https://artifacts.apis.io/surepoint/json-ld/surepoint-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/surepoint-context.jsonld
- group: design
  href: https://artifacts.apis.io/surepoint/vocabulary/surepoint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/surepoint-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/surepoint/data-model/surepoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/surepoint-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://surepoint.com/resources/research/trust-accounting-quick-reference-guide/
- group: design
  href: https://artifacts.apis.io/surepoint/conformance/surepoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/surepoint-conformance.yml
- group: agent
  href: https://artifacts.apis.io/surepoint/llms/surepoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/surepoint-llms.txt
- group: auth
  href: https://artifacts.apis.io/surepoint/well-known/surepoint-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/surepoint-status-security.txt
- group: agent
  href: https://artifacts.apis.io/surepoint/well-known/surepoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/surepoint-well-known.yml
- group: other
  href: https://artifacts.apis.io/surepoint/hosts/surepoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surepoint-hosts.yml
- group: other
  href: https://artifacts.apis.io/surepoint/vendors/surepoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surepoint-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://surepoint.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.surepoint.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.surepoint.com/
- group: auth
  title: ''
  type: Security
  url: https://surepoint.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://surepoint.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://surepoint.com/login/
- group: other
  title: ''
  type: Leadership
  url: https://surepoint.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://surepoint.com/blog/
- group: auth
  href: https://artifacts.apis.io/surepoint/security/surepoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/surepoint-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/surepoint/security/surepoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surepoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://surepoint.com/
coverage:
  checked: '2026-10-29'
  detail: MCP endpoint requires authentication (403/401), preventing access to contract.
  evidence:
  - status: 403
    url: https://status.surepoint.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-28'
description: 'SurePoint Pro is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling. The company operates the website https://surepoint.com/, which currently presents a Cloudflare-protected landing page with privacy and cookie consent notices but does not expose public API documentation or developer resources. No API endpoints, documentation portals, or developer portals were discovered after probing the main domain and common subpaths. This profile records the limited publicly available information about SurePoint Pro.'
image: https://surepoint.com/wp-content/uploads/2025/08/Ellipse-54-1.png
json_schemas:
- name: GetLmsApiAddressesResponse
  property_count: 41
  slug: surepoint-get-lms-api-addresses-response
- name: PatchLmsApiAddressesAbc00000Abc00000Id0Response
  property_count: 5
  slug: surepoint-patch-lms-api-addresses-abc00000-abc00000-id0-response
- name: PatchLmsApiAddressesAbc00000Abc00000Id0StatusResponse
  property_count: 5
  slug: surepoint-patch-lms-api-addresses-abc00000-abc00000-id0-status-response
- name: PostAddressesRequest
  property_count: 38
  slug: surepoint-post-addresses-request
- name: PostLmsApiAddressesRequest
  property_count: 38
  slug: surepoint-post-lms-api-addresses-request
- name: PostLmsApiAddressesResponse
  property_count: 5
  slug: surepoint-post-lms-api-addresses-response
jsonld:
- class_count: 9
  name: Surepoint Context
  property_count: 43
  slug: surepoint-context
layout: provider
modified: '2026-10-28'
name: SurePoint Pro
nav: Providers
network: true
overview: 'SurePoint Pro is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Software, Platform, and Services.


  The SurePoint Pro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SurePoint Pro''s developer surface includes support, engineering blog, and 20 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: SurePoint Pro API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: surepoint-rules
scopes:
- name: Surepoint Scopes
  scope_count: 0
  slug: surepoint-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Surepoint Authentication
  slug: surepoint-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Surepoint Domain Security
  slug: surepoint-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Surepoint Trust Center
  slug: surepoint-trust-center
  summary_line: SOC 2
slug: surepoint
tags:
- Company
- Technology
- Software
- Platform
- Services
website: https://surepoint.com/
---
