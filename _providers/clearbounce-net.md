---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Email verification API providing credit balance, single and bulk verification.
  name: ClearBounce API
  slug: clearbounce-api
- description: 'ClearBounce API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ClearBounce API
  slug: clearbounce-net-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/clearbounce-net/plans/clearbounce-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearbounce-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clearbounce-net/rules/clearbounce-net-rules.yml
  title: ''
  type: Spectral
  url: rules/clearbounce-net-rules.yml
- group: design
  href: https://artifacts.apis.io/clearbounce-net/json-ld/clearbounce-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearbounce-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearbounce-net/vocabulary/clearbounce-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearbounce-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clearbounce-net/data-model/clearbounce-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearbounce-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/clearbounce-net/authentication/clearbounce-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearbounce-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/clearbounce-net/conformance/clearbounce-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearbounce-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clearbounce-net/llms/clearbounce-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearbounce-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/clearbounce-net/mcp/clearbounce-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clearbounce-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clearbounce-net/well-known/clearbounce-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearbounce-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearbounce-net/hosts/clearbounce-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearbounce-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearbounce.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearbounce.net/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clearbounce.net/pricing
- group: start
  title: ''
  type: Login
  url: https://clearbounce.net/dashboard/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clearbounce.net/audiences/developers
- group: company
  title: ''
  type: Blog
  url: https://clearbounce.net/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clearbounce.net/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clearbounce.net/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clearbounce.net/
- group: auth
  href: https://artifacts.apis.io/clearbounce-net/security/clearbounce-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearbounce-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearbounce.net/
created: '2026-11-03'
description: ClearBounce provides email verification and list cleaning services, including bulk list verification, a real‑time verification API, a form‑validation widget (ClearBounce Shield), and deliverability tools such as inbox placement testing and blocklist monitoring. The company targets marketers, developers, enterprises, agencies, and other organizations that need to maintain clean email lists and protect sender reputation. Services are offered on a pay‑as‑you‑go basis with free credits available on sign‑up.
image: https://clearbounce.net/favicon-192.png
json_schemas:
- name: GetBulkResultsJobidResponse
  property_count: 3
  slug: clearbounce-net-get-bulk-results-jobid-response
- name: GetBulkStatusJobidResponse
  property_count: 3
  slug: clearbounce-net-get-bulk-status-jobid-response
- name: PostApiKeysResponse
  property_count: 3
  slug: clearbounce-net-post-api-keys-response
- name: PostApiV1BulkUploadResponse
  property_count: 2
  slug: clearbounce-net-post-api-v1-bulk-upload-response
- name: PostBulkUploadResponse
  property_count: 3
  slug: clearbounce-net-post-bulk-upload-response
- name: PostVerifyResponse
  property_count: 3
  slug: clearbounce-net-post-verify-response
jsonld:
- class_count: 14
  name: Clearbounce Net Context
  property_count: 9
  slug: clearbounce-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at clearbounce.net.
  name: ClearBounce MCP Server
  slug: clearbounce-net-mcp-yml
modified: '2026-11-03'
name: ClearBounce
nav: Providers
network: true
overview: 'ClearBounce is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Email Verification, List Cleaning, Form Validation, Deliverability, and Marketing Tools.


  The ClearBounce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClearBounce''s developer surface includes authentication, pricing, engineering blog, API reference, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Clearbounce Net Plans Pricing
  plan_count: 3
  slug: clearbounce-net-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: ClearBounce API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: clearbounce-net-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 32.1
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clearbounce Net Authentication
  slug: clearbounce-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Clearbounce Net Domain Security
  slug: clearbounce-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearbounce-net
tags:
- Email Verification
- List Cleaning
- Form Validation
- Deliverability
- Marketing Tools
- Enterprise Solutions
website: https://clearbounce.net/
---
