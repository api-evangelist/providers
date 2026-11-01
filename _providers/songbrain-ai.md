---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Songbrain Ai Agentic Access
  operation_count: 15
  slug: songbrain-ai-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 1
apis:
- description: Music analysis API for AI video generation
  name: Songbrain API
  slug: songbrain-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/songbrain-ai/plans/songbrain-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/songbrain-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/songbrain-ai/rules/songbrain-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/songbrain-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/songbrain-ai/json-ld/songbrain-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/songbrain-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/songbrain-ai/vocabulary/songbrain-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/songbrain-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/songbrain-ai/data-model/songbrain-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/songbrain-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/songbrain-ai/conventions/songbrain-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/songbrain-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/songbrain-ai/conventions/songbrain-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/songbrain-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.songbrain.ai/security
- group: design
  href: https://artifacts.apis.io/songbrain-ai/errors/songbrain-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/songbrain-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/songbrain-ai/conformance/songbrain-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/songbrain-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/songbrain-ai/llms/songbrain-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/songbrain-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/songbrain-ai/mcp/songbrain-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/songbrain-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/songbrain-ai/mcp/songbrain-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/songbrain-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/songbrain-ai/hosts/songbrain-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/songbrain-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/songbrain-ai/vendors/songbrain-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/songbrain-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.songbrain.ai/status
- group: auth
  title: ''
  type: Security
  url: https://www.songbrain.ai/security
- group: start
  title: ''
  type: Login
  url: https://app.songbrain.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.songbrain.ai/docs/api/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.songbrain.ai\
- group: auth
  href: https://artifacts.apis.io/songbrain-ai/security/songbrain-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/songbrain-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/songbrain-ai/security/songbrain-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/songbrain-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/songbrain-ai/security/songbrain-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/songbrain-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://songbrain.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.songbrain.ai/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://api.songbrain.ai/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.songbrain.ai/api-access
- group: commercial
  title: ''
  type: Pricing
  url: https://www.songbrain.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.songbrain.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.songbrain.ai/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.songbrain.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.songbrain.ai/privacy
created: '2026-10-30'
description: Songbrain AI provides an AI-powered music video generation platform that analyzes songs to identify their strongest moments, beats, and mood, then creates beat‑synced video shot plans for creators. Users can generate up to five free song analyses per month, with paid options for higher volume and additional video direction features. The service offers a public API for developers to integrate music analysis into their own video tools, complete with example endpoints, documentation, and a Postman collection. Songbrain AI aims to simplify the creation of engaging music videos by leveraging AI to decode song DNA and automate visual storytelling.
image: https://www.songbrain.ai/og-image.png
jsonld:
- class_count: 3
  name: Songbrain Ai Context
  property_count: 7
  slug: songbrain-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.songbrain.ai requiring an API key.
  name: songbrain-ai MCP Server
  slug: songbrain-ai-mcp-yml
modified: '2026-10-30'
name: songbrain-ai
nav: Providers
network: true
overview: 'songbrain-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Music, Video, and API.


  The songbrain-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  songbrain-ai''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 25 more developer resources.'
plans:
- name: Songbrain Ai Plans Pricing
  plan_count: 3
  slug: songbrain-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Songbrain Ai Rate Limits
  slug: songbrain-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: songbrain-ai API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: songbrain-ai-rules
scopes:
- name: Songbrain Ai Scopes
  scope_count: 0
  slug: songbrain-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 12.7
    developer_ergonomics: 45.2
    discoverability: 65.0
    operational_transparency: 63.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Songbrain Ai Authentication
  slug: songbrain-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Songbrain Ai Domain Security
  slug: songbrain-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Songbrain Ai Vulnerability Disclosure
  slug: songbrain-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Songbrain Ai Trust Center
  slug: songbrain-ai-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: analyze-song
  slug: songbrain-ai-analyze-song
- name: get-example-shot-plan
  slug: songbrain-ai-get-example-shot-plan
slug: songbrain-ai
tags:
- Company
- AI
- Music
- Video
- API
website: https://songbrain.ai/
---
