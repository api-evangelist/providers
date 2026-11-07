---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Immersa provides a data gateway platform for AI agents and developers, offering governed data access and secure AI workflows.
  name: Immersa API
  slug: immersa-api-2
- baseURL: https://mcp.marcopolo.dev
  baseurl_source: declared
  description: 'Immersa API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Immersa API
  slug: immersa-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/immersa/plans/immersa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/immersa-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/immersa/rules/immersa-rules.yml
  title: ''
  type: Spectral
  url: rules/immersa-rules.yml
- group: design
  href: https://artifacts.apis.io/immersa/json-ld/immersa-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/immersa-context.jsonld
- group: design
  href: https://artifacts.apis.io/immersa/vocabulary/immersa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/immersa-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/immersa/data-model/immersa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/immersa-data-model.yml
- group: auth
  href: https://artifacts.apis.io/immersa/authentication/immersa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/immersa-authentication.yml
- group: design
  href: https://artifacts.apis.io/immersa/conformance/immersa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/immersa-conformance.yml
- group: agent
  href: https://artifacts.apis.io/immersa/llms/immersa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/immersa-llms.txt
- group: agent
  href: https://artifacts.apis.io/immersa/well-known/immersa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/immersa-well-known.yml
- group: other
  href: https://artifacts.apis.io/immersa/hosts/immersa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/immersa-hosts.yml
- group: other
  href: https://artifacts.apis.io/immersa/vendors/immersa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/immersa-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.marcopolo.dev/trust
- group: auth
  title: ''
  type: Security
  url: https://www.marcopolo.dev/for/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.marcopolo.dev/for/developers
- group: auth
  href: https://artifacts.apis.io/immersa/security/immersa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/immersa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marcopolo.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.marcopolo.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.marcopolo.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.marcopolo.dev/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.marcopolo.dev/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marcopolo.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marcopolo.dev/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marcopolo.dev/privacy-policy
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are public HTML but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.marcopolo.dev/for/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Immersa, operating under the brand MarcoPolo, provides a data gateway platform for AI agents and developers. It enables governed data access, live querying of distributed systems, adaptive context, and secure AI workflows across industries such as manufacturing, finance, and consulting. The platform offers tools like Agent SDK, Agent Console, and One MCP to build, provision, and monitor AI-driven applications, emphasizing security, compliance, and operational reliability.
image: https://marcopolo.dev/opengraph-image.png?opengraph-image.3yy145u8-gdwo.png?dpl=dpl_2Xz2zCw6FJwuh3VKVGJaWcfoQjAg
json_schemas:
- name: GetApiV1ConnectionSetupSessionsSetupsessionidResponse
  property_count: 9
  slug: immersa-get-api-v1-connection-setup-sessions-setupsessionid-response
- name: PostApiV1ConnectionSetupSessionsRequest
  property_count: 5
  slug: immersa-post-api-v1-connection-setup-sessions-request
- name: PostApiV1ConnectionSetupSessionsResponse
  property_count: 10
  slug: immersa-post-api-v1-connection-setup-sessions-response
jsonld:
- class_count: 3
  name: Immersa Context
  property_count: 12
  slug: immersa-context
layout: provider
modified: '2026-10-17'
name: Immersa
nav: Providers
network: true
overview: 'Immersa is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, DataGateway, Platform, and Security.


  The Immersa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Immersa''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 17 more developer resources.'
plans:
- name: Immersa Plans Pricing
  plan_count: 2
  slug: immersa-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Immersa API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: immersa-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 8.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 46.1
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 39.3
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 40.5
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
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/immersa/immersa-2026-11-03T133708.png
security:
- kind: authentication
  name: Immersa Authentication
  slug: immersa-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Immersa Domain Security
  slug: immersa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: immersa
tags:
- Company
- Artificial Intelligence
- DataGateway
- Platform
- Security
website: https://www.marcopolo.dev/
---
