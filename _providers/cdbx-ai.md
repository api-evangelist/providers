---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Runner API for executing CDBX AI tasks as documented in the developer reference.
  name: CDBX Runner API
  slug: cdbx-runner-api
- description: 'cdbx API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: cdbx API
  slug: cdbx-ai-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/cdbx-ai/plans/cdbx-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cdbx-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cdbx-ai/rules/cdbx-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/cdbx-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/cdbx-ai/json-ld/cdbx-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cdbx-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/cdbx-ai/vocabulary/cdbx-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cdbx-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cdbx-ai/data-model/cdbx-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cdbx-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/cdbx-ai/conformance/cdbx-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cdbx-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cdbx-ai/llms/cdbx-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdbx-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/cdbx-ai/well-known/cdbx-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cdbx-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cdbx-ai/hosts/cdbx-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cdbx-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cdbx-ai/vendors/cdbx-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cdbx-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdbx.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://cdbx.ai/status
- group: auth
  title: ''
  type: Security
  url: https://cdbx.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdbx.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cdbx.ai/docs/how-to-use-cdbx/plans
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChristopherHButler
- group: docs
  title: ''
  type: Documentation
  url: https://cdbx.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cdbx.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://cdbx.ai/docs/how-to-use-cdbx
- group: auth
  href: https://artifacts.apis.io/cdbx-ai/security/cdbx-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdbx-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cdbx.ai/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://cdbx.ai/docs/how-to-use-cdbx/runner-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: cdbx.ai is an AI‑native development platform that provides a workspace for building, testing, and deploying applications with AI assistance. It offers tools for planning, coding, and shipping software, featuring integrated AI agents that help generate code, suggest improvements, and automate routine tasks. The platform emphasizes a collaborative environment where developers can harness large language models to accelerate development cycles and enhance productivity.
image: https://cdbx.ai/social-preview.png
json_schemas:
- name: PostCheckRequest
  property_count: 5
  slug: cdbx-ai-post-check-request
- name: PostCheckResponse
  property_count: 5
  slug: cdbx-ai-post-check-response
- name: PostExecuteRequest
  property_count: 5
  slug: cdbx-ai-post-execute-request
- name: PostExecuteResponse
  property_count: 5
  slug: cdbx-ai-post-execute-response
- name: PostRunAsyncRequest
  property_count: 5
  slug: cdbx-ai-post-run-async-request
- name: PostSessionsIdRunRequest
  property_count: 4
  slug: cdbx-ai-post-sessions-id-run-request
jsonld:
- class_count: 24
  name: Cdbx Ai Context
  property_count: 18
  slug: cdbx-ai-context
layout: provider
modified: '2026-11-04'
name: cdbx
nav: Providers
network: true
overview: 'cdbx is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Development, Workspace, and Collaboration.


  The cdbx catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cdbx''s developer surface includes pricing, documentation, getting-started guide, and 18 more developer resources.'
plans:
- name: Cdbx Ai Plans Pricing
  plan_count: 3
  slug: cdbx-ai-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: cdbx API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: cdbx-ai-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cdbx Ai Domain Security
  slug: cdbx-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cdbx-ai
tags:
- Artificial Intelligence
- Platform
- Development
- Workspace
- Collaboration
- Company
website: https://cdbx.ai/
---
