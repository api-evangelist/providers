---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Poof Bg Agentic Access
  operation_count: 3
  slug: poof-bg-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.poof.bg/v1
  baseurl_source: declared
  description: Account and billing information
  name: poof-bg Account API
  slug: poof-bg-account-api
- baseURL: https://api.poof.bg/v1
  baseurl_source: declared
  description: Background removal for images and video, and the jobs that video processing creates
  name: poof-bg Background Removal API
  slug: poof-bg-background-removal-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/poof-bg/agentic-access/poof-bg-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/poof-bg-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/poof-bg/plans/poof-bg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/poof-bg-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/poof-bg/rules/poof-bg-rules.yml
  title: ''
  type: Spectral
  url: rules/poof-bg-rules.yml
- group: design
  href: https://artifacts.apis.io/poof-bg/json-ld/poof-bg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/poof-bg-context.jsonld
- group: design
  href: https://artifacts.apis.io/poof-bg/vocabulary/poof-bg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/poof-bg-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/poof-bg/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/poof-bg/data-model/poof-bg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/poof-bg-data-model.yml
- group: operate
  href: https://artifacts.apis.io/poof-bg/changelog/poof-bg-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/poof-bg-changelog.yml
- group: auth
  href: https://artifacts.apis.io/poof-bg/authentication/poof-bg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/poof-bg-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.poof.bg
- group: design
  href: https://artifacts.apis.io/poof-bg/lifecycle/poof-bg-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/poof-bg-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/poof-bg/errors/poof-bg-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/poof-bg-problem-types.yml
- group: design
  href: https://artifacts.apis.io/poof-bg/conformance/poof-bg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/poof-bg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/poof-bg/llms/poof-bg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poof-bg-llms.txt
- group: other
  href: https://artifacts.apis.io/poof-bg/a2a/poof-bg-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/poof-bg-a2a.yml
- group: agent
  href: https://artifacts.apis.io/poof-bg/mcp/poof-bg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/poof-bg-mcp.yml
- group: agent
  href: https://artifacts.apis.io/poof-bg/well-known/poof-bg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/poof-bg-well-known.yml
- group: other
  href: https://artifacts.apis.io/poof-bg/hosts/poof-bg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/poof-bg-hosts.yml
- group: other
  href: https://artifacts.apis.io/poof-bg/vendors/poof-bg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/poof-bg-vendors.yml
- group: build
  href: https://artifacts.apis.io/poof-bg/packages/poof-bg-packages.yml
  title: ''
  type: SDKs
  url: packages/poof-bg-packages.yml
- group: build
  href: https://artifacts.apis.io/poof-bg/packages/poof-bg-packages.yml
  title: ''
  type: Packages
  url: packages/poof-bg-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poof.bg/terms
- group: start
  title: ''
  type: SignUp
  url: https://dash.poof.bg/auth/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poof.bg/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/poof-bg
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.poof.bg/changelog
- group: company
  title: ''
  type: Blog
  url: https://poof.bg/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.poof.bg/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.poof.bg/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.poof.bg\
- group: auth
  href: https://artifacts.apis.io/poof-bg/security/poof-bg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/poof-bg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poof.bg/
- group: docs
  title: ''
  type: APIReference
  url: https://api.poof.bg/v1/
- group: commercial
  title: ''
  type: Pricing
  url: https://poof.bg/pricing
created: '2026-10-31'
description: Poof provides a fast, GPU‑accelerated background removal API for images and videos. Developers can send a single request to remove backgrounds from photos, product images, GIFs, or video clips, receiving transparent PNG, WebP, WebM or MOV outputs. Plans start at $0.002 per image with 100 free credits monthly, and volume discounts are available. The service emphasizes low latency, high accuracy for hair, fur and complex edges, and offers bulk batch processing for large workloads.
image: https://poof.bg/favicon.ico
json_schemas:
- name: AccountInfo
  property_count: 5
  slug: poof-bg-account-info
- name: Job
  property_count: 19
  slug: poof-bg-job
jsonld:
- class_count: 3
  name: Poof Bg Context
  property_count: 29
  slug: poof-bg-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.poof.bg.
  name: poof-bg MCP Server
  slug: poof-bg-mcp-yml
modified: '2026-10-31'
name: poof-bg
nav: Providers
network: true
overview: 'poof-bg publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API and Background Removal API. Tagged areas include Company, API, BackgroundRemoval, ImageProcessing, and VideoProcessing.


  The poof-bg catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  poof-bg''s developer surface includes changelog, authentication, signup flow, engineering blog, getting-started guide, documentation, API reference, and 27 more developer resources.'
plans:
- name: Poof Bg Plans Pricing
  plan_count: 5
  slug: poof-bg-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Poof Bg Rate Limits
  slug: poof-bg-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: poof-bg API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: poof-bg-rules
scopes:
- name: Poof Bg Scopes
  scope_count: 0
  slug: poof-bg-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 85.5
    catalog_earned_first_party: 0.0
    catalog_gap: 29.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 62.4
    developer_ergonomics: 66.0
    discoverability: 65.0
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Poof Bg Authentication
  slug: poof-bg-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Poof Bg Domain Security
  slug: poof-bg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: remove-background
  slug: poof-bg-remove-background
slug: poof-bg
tags:
- Company
- API
- BackgroundRemoval
- ImageProcessing
- VideoProcessing
website: https://poof.bg/
---
