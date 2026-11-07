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
  band: agent-ready
  dimensions:
    agent_card: false
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
  score: 36.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Directories.ai provides a REST API for managing directory listings, categories, and articles.
  name: Directories.ai API
  slug: directories-ai-api-2
- baseURL: https://api.directories.ai/v1
  baseurl_source: declared
  description: 'Directories.ai API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Directories.ai API
  slug: directories-ai-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/directories-ai/plans/directories-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/directories-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/directories-ai/rules/directories-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/directories-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/directories-ai/json-ld/directories-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/directories-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/directories-ai/vocabulary/directories-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/directories-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/directories-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/directories-ai/data-model/directories-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/directories-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/directories-ai/conformance/directories-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/directories-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/directories-ai/llms/directories-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/directories-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/directories-ai/well-known/directories-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/directories-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/directories-ai/hosts/directories-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/directories-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/directories-ai/packages/directories-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/directories-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/directories-ai/packages/directories-ai-packages.yml
  title: ''
  type: Packages
  url: packages/directories-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://directories.ai/trust
- group: start
  title: ''
  type: Login
  url: https://directories.ai/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://directories.ai/for/developers
- group: auth
  href: https://artifacts.apis.io/directories-ai/security/directories-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/directories-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://directories.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://directories.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://directories.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://directories.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://directories.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://directories.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@directories.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://directories.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://directories.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/directoriesai
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://directories.ai/mcp
  - status: 200
    url: https://directories.ai/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Directories.ai is an AI‑powered directory intelligence platform that enables businesses to create, manage, and expose smart business listings through a Multi‑Channel Publishing (MCP) server. It offers AI‑driven automation, SEO optimization, and integration capabilities, allowing developers to call listings, claims, and analytics via Claude, ChatGPT, Gemini, or local models. The platform emphasizes no AI credits usage and provides robust directory building tools for seamless AI‑augmented content delivery.
image: https://directories.ai/og-image.png
json_schemas:
- name: GetDirectoriesResponse
  property_count: 4
  slug: directories-ai-get-directories-response
- name: PostDirectoriesIdListingsRequest
  property_count: 4
  slug: directories-ai-post-directories-id-listings-request
- name: PostMcpRequest
  property_count: 4
  slug: directories-ai-post-mcp-request
- name: PostMcpResponse
  property_count: 1
  slug: directories-ai-post-mcp-response
jsonld:
- class_count: 4
  name: Directories Ai Context
  property_count: 12
  slug: directories-ai-context
layout: provider
modified: '2026-11-05'
name: Directories.ai
nav: Providers
network: true
overview: 'Directories.ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Directory, Platform, MCP, and Business.


  The Directories.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Directories.ai''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, and 20 more developer resources.'
plans:
- name: Directories Ai Plans Pricing
  plan_count: 3
  slug: directories-ai-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Directories.ai API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: directories-ai-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 22.3
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 5.3
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
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Directories Ai Domain Security
  slug: directories-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: directories-ai
tags:
- Artificial Intelligence
- Directory
- Platform
- MCP
- Business
website: https://directories.ai/
---
