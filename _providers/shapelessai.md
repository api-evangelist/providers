---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-10-17'
api_count: 18
apis:
- description: The Ads API from ShapelessAI — 1 operation(s) for ads.
  name: ShapelessAI Ads API
  slug: shapelessai-ads-api
- description: The Brain API from ShapelessAI — 2 operation(s) for brain.
  name: ShapelessAI Brain API
  slug: shapelessai-brain-api
- description: The Capabilities API from ShapelessAI — 1 operation(s) for capabilities.
  name: ShapelessAI Capabilities API
  slug: shapelessai-capabilities-api
- description: The Connections API from ShapelessAI — 4 operation(s) for connections.
  name: ShapelessAI Connections API
  slug: shapelessai-connections-api
- description: The Groups API from ShapelessAI — 1 operation(s) for groups.
  name: ShapelessAI Groups API
  slug: shapelessai-groups-api
- description: The Jobs API from ShapelessAI — 1 operation(s) for jobs.
  name: ShapelessAI Jobs API
  slug: shapelessai-jobs-api
- description: The Manager API from ShapelessAI — 2 operation(s) for manager.
  name: ShapelessAI Manager API
  slug: shapelessai-manager-api
- description: The Me API from ShapelessAI — 1 operation(s) for me.
  name: ShapelessAI Me API
  slug: shapelessai-me-api
- description: The Metrics API from ShapelessAI — 2 operation(s) for metrics.
  name: ShapelessAI Metrics API
  slug: shapelessai-metrics-api
- description: The Posts API from ShapelessAI — 4 operation(s) for posts.
  name: ShapelessAI Posts API
  slug: shapelessai-posts-api
- description: The Profile API from ShapelessAI — 1 operation(s) for profile.
  name: ShapelessAI Profile API
  slug: shapelessai-profile-api
- description: The ShapelessAI API API from ShapelessAI — 1 operation(s) for shapelessai api.
  name: ShapelessAI ShapelessAI API
  slug: shapelessai-shapelessai-api-api
- description: The Strategies API from ShapelessAI — 1 operation(s) for strategies.
  name: ShapelessAI Strategies API
  slug: shapelessai-strategies-api
- description: The Studio API from ShapelessAI — 2 operation(s) for studio.
  name: ShapelessAI Studio API
  slug: shapelessai-studio-api
- description: The Tools API from ShapelessAI — 1 operation(s) for tools.
  name: ShapelessAI Tools API
  slug: shapelessai-tools-api
- description: The Videos API from ShapelessAI — 1 operation(s) for videos.
  name: ShapelessAI Videos API
  slug: shapelessai-videos-api
- description: The Wiki API from ShapelessAI — 1 operation(s) for wiki.
  name: ShapelessAI Wiki API
  slug: shapelessai-wiki-api
- description: The Workspace API from ShapelessAI — 2 operation(s) for workspace.
  name: ShapelessAI Workspace API
  slug: shapelessai-workspace-api
artifact_total: 30
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/rate-limits/shapelessai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shapelessai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/plans/shapelessai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shapelessai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/rules/shapelessai-rules.yml
  title: ''
  type: Spectral
  url: rules/shapelessai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/json-ld/shapelessai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shapelessai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/vocabulary/shapelessai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shapelessai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/data-model/shapelessai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shapelessai-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/cli/shapelessai-cli.yml
  title: ''
  type: CLI
  url: cli/shapelessai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/conventions/shapelessai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shapelessai-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/authentication/shapelessai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shapelessai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/errors/shapelessai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shapelessai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/conformance/shapelessai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shapelessai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/llms/shapelessai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shapelessai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/well-known/shapelessai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shapelessai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/hosts/shapelessai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shapelessai-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/packages/shapelessai-packages.yml
  title: ''
  type: SDKs
  url: packages/shapelessai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/packages/shapelessai-packages.yml
  title: ''
  type: Packages
  url: packages/shapelessai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shapelessai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shapelessai.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://shapelessai.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FirstClassTree
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shapelessai/refs/heads/main/security/shapelessai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shapelessai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shapelessai.com
- group: docs
  title: ''
  type: Documentation
  url: https://shapelessai.com/docs/api
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://shapelessai.com/mcp
  - status: 200
    url: https://shapelessai.com
  reason: partner-login
  state: gated
created: '2026-10-12'
description: ShapelessAI provides an agentic social media automation platform that creates, designs, and publishes posts, carousels, and short videos across major social networks. Users input a brief description of their product; the AI researches current market trends, generates content, and schedules it, delivering compounded traffic growth. The service offers a free tier with limited daily posts and paid plans starting at $35/month for higher caps and credits. It supports API, CLI, and MCP integrations, enabling developers to drive the agents programmatically.
image: https://shapelessai.com/opengraph-image?d1f04df5468e4746
json_schemas:
- name: GetApiPostsIdResponse
  property_count: 4
  slug: shapelessai-get-api-posts-id-response
- name: PostApiApiidRequest
  property_count: 3
  slug: shapelessai-post-api-apiid-request
- name: PostApiPostsIdIdRequest
  property_count: 3
  slug: shapelessai-post-api-posts-id-id-request
- name: PostApiV1JobsRequest
  property_count: 6
  slug: shapelessai-post-api-v1-jobs-request
- name: PostApiV1JobsResponse
  property_count: 3
  slug: shapelessai-post-api-v1-jobs-response
- name: PutApiMeEmailRequest
  property_count: 1
  slug: shapelessai-put-api-me-email-request
jsonld:
- class_count: 8
  name: Shapelessai Context
  property_count: 21
  slug: shapelessai-context
layout: provider
modified: '2026-10-12'
name: ShapelessAI
nav: Providers
network: true
overview: 'ShapelessAI is listed with 18 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Brain API, Capabilities API, and 15 more. Tagged areas include Company, Artificial Intelligence, Social Media, Automation, and Software-as-a-Service.


  The ShapelessAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ShapelessAI''s developer surface includes CLI, authentication, pricing, documentation, and 20 more developer resources.'
plans:
- name: Shapelessai Plans Pricing
  plan_count: 4
  slug: shapelessai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 19
  name: Shapelessai Rate Limits
  slug: shapelessai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ShapelessAI API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: shapelessai-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 84.0
    catalog_earned_first_party: 24.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 24.1
    developer_ergonomics: 42.1
    discoverability: 69.6
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 19
      marker_coverage: 100.0
      total: 19
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Shapelessai Authentication
  slug: shapelessai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Shapelessai Domain Security
  slug: shapelessai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shapelessai
tags:
- Company
- Artificial Intelligence
- Social Media
- Automation
- Software-as-a-Service
website: https://shapelessai.com
---
