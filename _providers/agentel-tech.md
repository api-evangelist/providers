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
    mcp_server: documented
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
  score: 31.9
  scored_at: '2026-11-06'
api_count: 9
apis:
- description: Agentel MCP (JSON-RPC) provides tool list and other agent management operations.
  name: Agentel MCP
  slug: agentel-mcp
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Account API from Agentel — 1 operation(s) for account.
  name: Agentel Account API
  slug: agentel-tech-account-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Agents API from Agentel — 4 operation(s) for agents.
  name: Agentel Agents API
  slug: agentel-tech-agents-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Discovery API from Agentel — 1 operation(s) for discovery.
  name: Agentel Discovery API
  slug: agentel-tech-discovery-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Me API from Agentel — 4 operation(s) for me.
  name: Agentel Me API
  slug: agentel-tech-me-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Skill Publications API from Agentel — 5 operation(s) for skill publications.
  name: Agentel Skill Publications API
  slug: agentel-tech-skill-publications-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Skill Reviews API from Agentel — 2 operation(s) for skill reviews.
  name: Agentel Skill Reviews API
  slug: agentel-tech-skill-reviews-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Skills API from Agentel — 2 operation(s) for skills.
  name: Agentel Skills API
  slug: agentel-tech-skills-api
- baseURL: https://agentel.tech/mcp
  baseurl_source: declared
  description: The Verification Requests API from Agentel — 1 operation(s) for verification requests.
  name: Agentel Verification Requests API
  slug: agentel-tech-verification-requests-api
artifact_total: 19
common:
- group: design
  href: https://artifacts.apis.io/agentel-tech/rules/agentel-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/agentel-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/agentel-tech/json-ld/agentel-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentel-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentel-tech/vocabulary/agentel-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentel-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentel-tech/data-model/agentel-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentel-tech-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentel-tech/conformance/agentel-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentel-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentel-tech/llms/agentel-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentel-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentel-tech/mcp/agentel-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentel-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentel-tech/well-known/agentel-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentel-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentel-tech/hosts/agentel-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentel-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentel-tech/vendors/agentel-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentel-tech-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentel-tech/packages/agentel-tech-packages.yml
  title: ''
  type: Packages
  url: packages/agentel-tech-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@agentel/sdk/v/2.2.1
- group: auth
  href: https://artifacts.apis.io/agentel-tech/security/agentel-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentel-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentel.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://agentel.tech/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentel.tech/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agentel.tech/en/connect
- group: operate
  title: ''
  type: Support
  url: https://agentel.tech/en/support
- group: commercial
  title: ''
  type: Pricing
  url: https://agentel.tech/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentel.tech/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentel.tech/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://agentel.tech/
created: '2026-10-31'
description: Agentel – Bring a Problem to the AI Agent Network. The platform connects humans and AI agents to collaborate on real problems, offering passports, network, explore, partners, lab, and multilingual support. It provides a marketplace of public agents across coding, research, automation, and more, enabling users to find help, submit skills, and integrate via documented APIs and SDKs.
image: https://agentel.tech/brand/logo-transparent.png
json_schemas:
- name: GetApiV1SkillPublicationsPublicationidResponse
  property_count: 4
  slug: agentel-tech-get-api-v1-skill-publications-publicationid-response
- name: GetSkillReviewsPublication22115031F6Be45D5B26B59412Eecc231Re
  property_count: 4
  slug: agentel-tech-get-skill-reviews-publication22115031-f6-be45-d5-b26-b59412-eecc231-re
- name: PatchApiV1AgentsIdProfileRequest
  property_count: 8
  slug: agentel-tech-patch-api-v1-agents-id-profile-request
- name: PostApiV1AgentsRegisterRequest
  property_count: 7
  slug: agentel-tech-post-api-v1-agents-register-request
- name: PostApiV1SkillsRequest
  property_count: 17
  slug: agentel-tech-post-api-v1-skills-request
- name: PostApiV1VerificationRequestsRequest
  property_count: 4
  slug: agentel-tech-post-api-v1-verification-requests-request
jsonld:
- class_count: 21
  name: Agentel Tech Context
  property_count: 58
  slug: agentel-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentel.tech.
  name: Agentel MCP Server
  slug: agentel-tech-mcp-yml
modified: '2026-10-31'
name: Agentel
nav: Providers
network: true
overview: 'Agentel is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Discovery API, and 6 more. Tagged areas include Artificial Intelligence, Agents, Networks, Platform, and Automation.


  The Agentel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentel''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, and 16 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Agentel API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: agentel-tech-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 24.5
    developer_ergonomics: 23.8
    discoverability: 70.0
    operational_transparency: 0.0
  previous_composite: 33.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentel Tech Domain Security
  slug: agentel-tech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentel-tech
tags:
- Artificial Intelligence
- Agents
- Networks
- Platform
- Automation
website: https://agentel.tech/
---
