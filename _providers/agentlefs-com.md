---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://mcp.agentlefs.com
  baseurl_source: declared
  description: 'agentleFS API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: agentleFS API
  slug: agentlefs-com-api
artifact_total: 11
common:
- group: other
  href: https://artifacts.apis.io/agentlefs-com/vendors/agentlefs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentlefs-com-vendors.yml
- group: design
  href: https://artifacts.apis.io/agentlefs-com/rules/agentlefs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentlefs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentlefs-com/json-ld/agentlefs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentlefs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentlefs-com/vocabulary/agentlefs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentlefs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentlefs-com/data-model/agentlefs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentlefs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentlefs-com/conventions/agentlefs-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentlefs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentlefs-com/conventions/agentlefs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentlefs-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentlefs-com/security/agentlefs-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentlefs-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentlefs-com/conformance/agentlefs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentlefs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentlefs-com/llms/agentlefs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentlefs-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentlefs-com/well-known/agentlefs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentlefs-com-security.txt
- group: auth
  href: https://artifacts.apis.io/agentlefs-com/well-known/agentlefs-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentlefs-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/agentlefs-com/well-known/agentlefs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentlefs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentlefs-com/hosts/agentlefs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentlefs-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/agentlefs-com/packages/agentlefs-com-packages.yml
  title: ''
  type: Packages
  url: packages/agentlefs-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentlefs.com/terms
- group: operate
  title: ''
  type: Support
  url: https://agentlefs.com/support
- group: start
  title: ''
  type: SignUp
  url: https://agentlefs.com/sign-up?return_to=%2F
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@agentlefs/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentlefs.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://agentlefs.com/docs/reference
- group: auth
  href: https://artifacts.apis.io/agentlefs-com/security/agentlefs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentlefs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentlefs-com/security/agentlefs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentlefs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentlefs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentlefs.com/docs
- group: company
  title: ''
  type: Blog
  url: https://agentlefs.com/blog
coverage:
  checked: '2026-11-01'
  detail: Docs pages are rendered via JavaScript and no machine‑readable OpenAPI spec is publicly accessible.
  evidence:
  - status: 200
    url: https://agentlefs.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: agentleFS provides a collaborative AI workspace where teams can share context, make decisions, and coordinate work across multiple AI models and tools. It offers a permissioned environment for agents to interact, share data, and streamline workflows, enabling seamless integration of AI capabilities into everyday team processes. The platform emphasizes security, flexibility, and ease of use for both technical and non‑technical users.
image: https://agentlefs.com/assets/og-card-DCEn8B2u.png
json_schemas:
- name: GetV1DocumentsLocationResponse
  property_count: 2
  slug: agentlefs-com-get-v1-documents-location-response
- name: PostMcpRequest
  property_count: 5
  slug: agentlefs-com-post-mcp-request
- name: PostV1DocumentsRequest
  property_count: 2
  slug: agentlefs-com-post-v1-documents-request
- name: PostV1GrantsRequest
  property_count: 1
  slug: agentlefs-com-post-v1-grants-request
- name: PostV1MovesRequest
  property_count: 3
  slug: agentlefs-com-post-v1-moves-request
- name: PostV1RenamesRequest
  property_count: 2
  slug: agentlefs-com-post-v1-renames-request
jsonld:
- class_count: 12
  name: Agentlefs Com Context
  property_count: 14
  slug: agentlefs-com-context
layout: provider
modified: '2026-11-01'
name: agentleFS
nav: Providers
network: true
overview: 'agentleFS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Artificial Intelligence, Workspace, Team, and Permissioned.


  The agentleFS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agentleFS''s developer surface includes support, signup flow, API reference, documentation, engineering blog, and 21 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: agentleFS API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agentlefs-com-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 32.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentlefs Com Domain Security
  slug: agentlefs-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentlefs Com Vulnerability Disclosure
  slug: agentlefs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentlefs-com
tags:
- Collaboration
- Artificial Intelligence
- Workspace
- Team
- Permissioned
- Company
website: https://agentlefs.com/
---
