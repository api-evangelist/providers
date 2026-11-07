---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Clipwright offers a REST API for video generation, pricing checks, and run‑id polling as described in their developer docs.
  name: Clipwright API
  slug: clipwright-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/clipwright/plans/clipwright-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clipwright-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clipwright/rules/clipwright-rules.yml
  title: ''
  type: Spectral
  url: rules/clipwright-rules.yml
- group: design
  href: https://artifacts.apis.io/clipwright/json-ld/clipwright-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clipwright-context.jsonld
- group: design
  href: https://artifacts.apis.io/clipwright/vocabulary/clipwright-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clipwright-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clipwright/data-model/clipwright-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clipwright-data-model.yml
- group: design
  href: https://artifacts.apis.io/clipwright/conventions/clipwright-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/clipwright-conventions.yml
- group: design
  href: https://artifacts.apis.io/clipwright/conventions/clipwright-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clipwright-conventions.yml
- group: design
  href: https://artifacts.apis.io/clipwright/errors/clipwright-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clipwright-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clipwright/conformance/clipwright-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clipwright-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clipwright/llms/clipwright-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clipwright-llms.txt
- group: agent
  href: https://artifacts.apis.io/clipwright/mcp/clipwright-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clipwright-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clipwright/well-known/clipwright-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clipwright-well-known.yml
- group: other
  href: https://artifacts.apis.io/clipwright/hosts/clipwright-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clipwright-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clipwright.io/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.clipwright.io/auth/sign-up
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@clipwright/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clipwright.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clipwright.io/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clipwright.io/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://clipwright.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://clipwright.io/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://clipwright.io/docs
- group: company
  title: ''
  type: Website
  url: https://clipwright.io
- group: auth
  href: https://artifacts.apis.io/clipwright/security/clipwright-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clipwright-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clipwright.io
coverage:
  checked: '2026-10-27'
  detail: Provider docs at https://clipwright.io/docs do not expose an OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://clipwright.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Clipwright provides AI-powered UGC video generation for agents. Users can submit scripts, images, or product details and receive a finished MP4 video featuring talking actors, faceless shorts, or presenter-led stories. The platform offers a REST API, MCP server, and CLI, supporting price checks, run‑id polling, and integration into autonomous agents. Clipwright aims to simplify video creation for marketing, sales, and support use‑cases, delivering customizable, brand‑consistent content at scale.
image: https://clipwright.io/brand/og-image.png
jsonld:
- class_count: 48
  name: Clipwright Context
  property_count: 160
  slug: clipwright-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.clipwright.io requiring OAuth.
  name: Clipwright MCP Server
  slug: clipwright-mcp-yml
modified: '2026-10-27'
name: Clipwright
nav: Providers
network: true
overview: 'Clipwright publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, UGC, and Automation.


  The Clipwright catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clipwright''s developer surface includes signup flow, pricing, changelog, getting-started guide, API reference, and 20 more developer resources.'
plans:
- name: Clipwright Plans Pricing
  plan_count: 3
  slug: clipwright-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Clipwright API Rules
  rule_count: 18
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 5
  slug: clipwright-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 15.8
    developer_ergonomics: 21.4
    discoverability: 66.7
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.4
  provenance:
    conformance: derived
    mcp: first-party
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
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/clipwright/clipwright-2026-11-03T124443.png
security:
- kind: domain-security
  name: Clipwright Domain Security
  slug: clipwright-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clipwright
tags:
- Company
- Artificial Intelligence
- Video
- UGC
- Automation
website: https://clipwright.io
---
