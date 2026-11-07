---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Web & Social Media Content API for Developers
  name: Supadata API
  slug: supadata-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/supadata-ai/rules/supadata-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/supadata-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/supadata-ai/json-ld/supadata-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/supadata-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/supadata-ai/vocabulary/supadata-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/supadata-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/supadata-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/supadata-ai/data-model/supadata-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/supadata-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/supadata-ai/conventions/supadata-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/supadata-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/supadata-ai/authentication/supadata-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/supadata-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/supadata-ai/errors/supadata-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/supadata-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/supadata-ai/conformance/supadata-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/supadata-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/supadata-ai/llms/supadata-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/supadata-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/supadata-ai/a2a/supadata-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/supadata-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/supadata-ai/mcp/supadata-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/supadata-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/supadata-ai/well-known/supadata-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/supadata-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/supadata-ai/hosts/supadata-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/supadata-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/supadata-ai/vendors/supadata-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/supadata-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/supadata-ai/packages/supadata-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/supadata-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/supadata-ai/packages/supadata-ai-packages.yml
  title: ''
  type: Packages
  url: packages/supadata-ai-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://supadata.ai/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.supadata.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.supadata.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/supadata-ai/security/supadata-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/supadata-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://supadata.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supadata.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.supadata.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://supadata.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://supadata.ai/blog/best-youtube-transcript-api
- group: operate
  title: ''
  type: Support
  url: https://feedback.supadata.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.supadata.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supadata-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supadata.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supadata.ai/legal/privacy
created: '2026-10-31'
description: Supadata provides a Video Transcript API that extracts transcripts, metadata, and structured JSON from videos on YouTube, TikTok, Instagram, Facebook, and X (Twitter). It offers free tier Python and JavaScript SDKs, batch processing, search, and web scraping endpoints, supporting transcript translation, metadata retrieval, and content extraction for AI-driven video analysis applications.
image: https://supadata.ai/opengraph-image.png?c5c0b1e213ff92af
jsonld:
- class_count: 20
  name: Supadata Ai Context
  property_count: 56
  slug: supadata-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.supadata.ai.
  name: supadata-ai MCP Server
  slug: supadata-ai-mcp-yml
modified: '2026-10-31'
name: supadata-ai
nav: Providers
network: true
overview: 'supadata-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Transcript, YouTube, TikTok, and Instagram.


  The supadata-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  supadata-ai''s developer surface includes authentication, sandbox, changelog, API reference, documentation, pricing, engineering blog, and 24 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: supadata-ai API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 3
    warn: 2
  slug: supadata-ai-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 14.7
    developer_ergonomics: 45.7
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 39.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
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
screenshot: https://apis.io/screenshots/supadata-ai/supadata-ai-2026-11-03T144031.png
security:
- kind: authentication
  name: Supadata Ai Authentication
  slug: supadata-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Supadata Ai Domain Security
  slug: supadata-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: supadata-ai-all
  slug: supadata-ai-all
slug: supadata-ai
tags:
- Video
- Transcript
- YouTube
- TikTok
- Instagram
- Facebook
- X
- Artificial Intelligence
- Data
website: https://supadata.ai/
---
