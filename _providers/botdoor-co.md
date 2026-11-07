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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://botdoor.co
  baseurl_source: declared
  description: 'Botdoor API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Botdoor API
  slug: botdoor-co-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/botdoor-co/plans/botdoor-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botdoor-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botdoor-co/rules/botdoor-co-rules.yml
  title: ''
  type: Spectral
  url: rules/botdoor-co-rules.yml
- group: design
  href: https://artifacts.apis.io/botdoor-co/json-ld/botdoor-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botdoor-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/botdoor-co/vocabulary/botdoor-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botdoor-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botdoor-co/data-model/botdoor-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botdoor-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/botdoor-co/conventions/botdoor-co-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/botdoor-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/botdoor-co/conventions/botdoor-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botdoor-co-conventions.yml
- group: auth
  href: https://artifacts.apis.io/botdoor-co/authentication/botdoor-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botdoor-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/botdoor-co/conformance/botdoor-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botdoor-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botdoor-co/llms/botdoor-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botdoor-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/botdoor-co/well-known/botdoor-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botdoor-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/botdoor-co/hosts/botdoor-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botdoor-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/botdoor-co/vendors/botdoor-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botdoor-co-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://botdoor.co/login
- group: auth
  href: https://artifacts.apis.io/botdoor-co/security/botdoor-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botdoor-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botdoor.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.botdoor.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://botdoor.co/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://botdoor.co/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botdoor.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botdoor.co/privacy
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 308
    url: https://botdoor.co/api/v1/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Botdoor is a social‑media automation platform that lets AI bots draft, schedule, and post content across Instagram, TikTok, X, LinkedIn, and six other networks. Users connect their accounts once, approve each post, and can manage multiple accounts with granular approval controls. The service offers free and paid plans, detailed pricing, and an MCP endpoint for tool integration.
image: https://botdoor.co/og.png
json_schemas:
- name: GetApiV1ConnectInstagramResponse
  property_count: 4
  slug: botdoor-co-get-api-v1-connect-instagram-response
- name: PostApiV1ClaimLinkResponse
  property_count: 3
  slug: botdoor-co-post-api-v1-claim-link-response
- name: PostApiV1MediaRequest
  property_count: 3
  slug: botdoor-co-post-api-v1-media-request
- name: PostApiV1MediaResponse
  property_count: 1
  slug: botdoor-co-post-api-v1-media-response
- name: PostMediaRequest
  property_count: 4
  slug: botdoor-co-post-media-request
- name: PostMediaResponse
  property_count: 9
  slug: botdoor-co-post-media-response
jsonld:
- class_count: 8
  name: Botdoor Co Context
  property_count: 23
  slug: botdoor-co-context
layout: provider
modified: '2026-11-02'
name: Botdoor
nav: Providers
network: true
overview: 'Botdoor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Automation, AI Bots, Scheduling, and Marketing.


  The Botdoor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Botdoor''s developer surface includes authentication, documentation, getting-started guide, pricing, and 17 more developer resources.'
plans:
- name: Botdoor Co Plans Pricing
  plan_count: 3
  slug: botdoor-co-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Botdoor API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: botdoor-co-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 0.0
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Botdoor Co Authentication
  slug: botdoor-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Botdoor Co Domain Security
  slug: botdoor-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botdoor-co
tags:
- Social Media
- Automation
- AI Bots
- Scheduling
- Marketing
website: https://botdoor.co/
---
