---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Podkitapp Com Agentic Access
  operation_count: 7
  slug: podkitapp-com-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- description: The Admin API from podkitapp-com — 1 operation(s) for admin.
  name: podkitapp-com Admin API
  slug: podkitapp-com-admin-api
- description: The Episodes API from podkitapp-com — 3 operation(s) for episodes.
  name: podkitapp-com Episodes API
  slug: podkitapp-com-episodes-api
- description: The Podcasts API from podkitapp-com — 1 operation(s) for podcasts.
  name: podkitapp-com Podcasts API
  slug: podkitapp-com-podcasts-api
- description: The Search API from podkitapp-com — 1 operation(s) for search.
  name: podkitapp-com Search API
  slug: podkitapp-com-search-api
- description: The Usage API from podkitapp-com — 1 operation(s) for usage.
  name: podkitapp-com Usage API
  slug: podkitapp-com-usage-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/podkitapp-com/agentic-access/podkitapp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/podkitapp-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/podkitapp-com/plans/podkitapp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/podkitapp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/podkitapp-com/rules/podkitapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/podkitapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/podkitapp-com/json-ld/podkitapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/podkitapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/podkitapp-com/vocabulary/podkitapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/podkitapp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/podkitapp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/podkitapp-com/data-model/podkitapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/podkitapp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/podkitapp-com/authentication/podkitapp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/podkitapp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/podkitapp-com/errors/podkitapp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/podkitapp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/podkitapp-com/conformance/podkitapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/podkitapp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/podkitapp-com/mcp/podkitapp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/podkitapp-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/podkitapp-com/hosts/podkitapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/podkitapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/podkitapp-com/vendors/podkitapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/podkitapp-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/podkitapp-com/security/podkitapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/podkitapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://podkitapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://podkitapp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://podkitapp.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://podkitapp.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://podkitapp.com/#pricing
- group: company
  title: ''
  type: Blog
  url: https://podkitapp.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://podkitapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://podkitapp.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/podkitapp
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://podkitapp.com/openapi.json
  - status: 401
    url: https://podkitapp.com/mcp
  - status: 401
    url: https://podkitapp.com/v1/graphql
  - status: 200
    url: https://podkitapp.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: PodKit provides a developer‑friendly podcast data API that delivers searchable podcast metadata, episodes, chapters, and transcripts in clean JSON format. The service offers affordable pricing starting at $15 per month, supports client‑side caching, and does not require attribution. It is designed for AI agents via MCP and includes features such as transcript inclusion, caching, and flexible query parameters.
image: https://podkitapp.com/og.png
json_schemas:
- name: Chapter
  property_count: 4
  slug: podkitapp-com-chapter
- name: CreateKeyResponse
  property_count: 4
  slug: podkitapp-com-create-key-response
- name: Episode
  property_count: 7
  slug: podkitapp-com-episode
- name: Podcast
  property_count: 6
  slug: podkitapp-com-podcast
- name: TranscriptSegment
  property_count: 4
  slug: podkitapp-com-transcript-segment
- name: Usage
  property_count: 6
  slug: podkitapp-com-usage
jsonld:
- class_count: 8
  name: Podkitapp Com Context
  property_count: 25
  slug: podkitapp-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at podkitapp.com.
  name: podkitapp-com MCP Server
  slug: podkitapp-com-mcp-yml
modified: '2026-10-30'
name: podkitapp-com
nav: Providers
network: true
overview: 'podkitapp-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Episodes API, Podcasts API, and 2 more. Tagged areas include Podcasts, Data, Developers, and Audio.


  The podkitapp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  podkitapp-com''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Podkitapp Com Plans Pricing
  plan_count: 1
  slug: podkitapp-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Podkitapp Com Rate Limits
  slug: podkitapp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: podkitapp-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: podkitapp-com-rules
scopes:
- name: Podkitapp Com Scopes
  scope_count: 0
  slug: podkitapp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 35.0
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/podkitapp-com/podkitapp-com-2026-11-03T141333.png
security:
- kind: authentication
  name: Podkitapp Com Authentication
  slug: podkitapp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Podkitapp Com Domain Security
  slug: podkitapp-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: search-podkitapp-com
  slug: podkitapp-com-search-skill
slug: podkitapp-com
tags:
- Podcasts
- Data
- Developers
- Audio
website: https://podkitapp.com/
---
