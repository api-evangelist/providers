---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: unknown
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
  score: 37.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for ANHA Registry allowing registration and verification of AI agent handles.
  name: ANHA Registry API
  slug: anha-registry-api
- baseURL: https://resolver.anha.ai
  baseurl_source: declared
  description: 'ANHA Registry API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: ANHA Registry API
  slug: anha-ai-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/anha-ai/rules/anha-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/anha-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/anha-ai/json-ld/anha-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anha-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/anha-ai/vocabulary/anha-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anha-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anha-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anha-ai/data-model/anha-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anha-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/anha-ai/conformance/anha-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anha-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anha-ai/llms/anha-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anha-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/anha-ai/a2a/anha-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/anha-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/anha-ai/well-known/anha-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anha-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/anha-ai/hosts/anha-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anha-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/anha-ai/vendors/anha-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anha-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/anha-ai/packages/anha-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/anha-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/anha-ai/packages/anha-ai-packages.yml
  title: ''
  type: Packages
  url: packages/anha-ai-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anha.ai/register/developer
- group: auth
  href: https://artifacts.apis.io/anha-ai/security/anha-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anha-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anha.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://anha.ai/tutorial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anha.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anha.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://anha.ai/register
- group: start
  title: ''
  type: SignUp
  url: https://anha.ai/register
coverage:
  checked: '2026-11-01'
  detail: Developer portal pages are public but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 404
    url: https://anha.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ANHA Registry provides a post-quantum, zero‑trust identity platform for AI agents. It enables registration of AI Addresses, verification of autonomous agents, and cryptographic consent before actions. The service offers decentralized, tamper‑evident records, human‑in‑the‑loop approvals, and integrates with existing AI stacks without code changes. Built for security teams, it protects brands from impersonation and ensures compliance with OFAC sanctions and enterprise policies.
image: https://anha.ai/opengraph-image?a2e7888167f81e9b
json_schemas:
- name: PostV1InvokeRequest
  property_count: 3
  slug: anha-ai-post-v1-invoke-request
jsonld:
- class_count: 1
  name: Anha Ai Context
  property_count: 3
  slug: anha-ai-context
layout: provider
modified: '2026-11-01'
name: ANHA Registry
nav: Providers
network: true
overview: 'ANHA Registry is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Zero Trust, and Post-Quantum.


  The ANHA Registry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ANHA Registry''s developer surface includes documentation, getting-started guide, signup flow, and 18 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ANHA Registry API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: anha-ai-rules
scopes:
- name: Anha Ai Scopes
  scope_count: 0
  slug: anha-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 29.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 31.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anha Ai Authentication
  slug: anha-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anha Ai Domain Security
  slug: anha-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: anha-ai
tags:
- Company
- Artificial Intelligence
- Security
- Zero Trust
- Post-Quantum
- Identity
website: https://anha.ai/
---
