---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 73
  human_in_the_loop: 4
  name: Tenzro Xyz Agentic Access
  operation_count: 159
  slug: tenzro-xyz-agentic-access
  summary_line: 159 operations · 73 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: Browse the curated catalogue; manage credits, billing, keys, plans and rentals; place and pay orders; run Datasets, Fieldwork, Voices and Forecasts. Chat, embeddings, images, speech and the model list
  name: Tenzro Labs Platform API
  slug: tenzro-labs-platform-api
- description: Call Tenzro Labs models with a Platform API key. Each model kind has its own endpoint; the Platform routes each call to a machine on the Tenzro Network that serves the model. Chat and embeddings are O
  name: Tenzro Labs Model API
  slug: tenzro-labs-model-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Account API from tenzro-xyz — 1 operation(s) for account.
  name: tenzro-xyz Account API
  slug: tenzro-xyz-account-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The API keys API from tenzro-xyz — 2 operation(s) for api keys.
  name: tenzro-xyz API keys API
  slug: tenzro-xyz-api-keys-api
- baseURL: https://api.tenzro.xyz/v1
  baseurl_source: declared
  description: The Audio API from tenzro-xyz — 1 operation(s) for audio.
  name: tenzro-xyz Audio API
  slug: tenzro-xyz-audio-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Billing API from tenzro-xyz — 14 operation(s) for billing.
  name: tenzro-xyz Billing API
  slug: tenzro-xyz-billing-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Catalogue API from tenzro-xyz — 10 operation(s) for catalogue.
  name: tenzro-xyz Catalogue API
  slug: tenzro-xyz-catalogue-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Credits API from tenzro-xyz — 4 operation(s) for credits.
  name: tenzro-xyz Credits API
  slug: tenzro-xyz-credits-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Datasets API from tenzro-xyz — 9 operation(s) for datasets.
  name: tenzro-xyz Datasets API
  slug: tenzro-xyz-datasets-api
- baseURL: https://api.tenzro.xyz/v1
  baseurl_source: declared
  description: The Embeddings API from tenzro-xyz — 1 operation(s) for embeddings.
  name: tenzro-xyz Embeddings API
  slug: tenzro-xyz-embeddings-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Fieldwork API from tenzro-xyz — 23 operation(s) for fieldwork.
  name: tenzro-xyz Fieldwork API
  slug: tenzro-xyz-fieldwork-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Fieldwork ingest API from tenzro-xyz — 8 operation(s) for fieldwork ingest.
  name: tenzro-xyz Fieldwork ingest API
  slug: tenzro-xyz-fieldwork-ingest-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Forecasts API from tenzro-xyz — 1 operation(s) for forecasts.
  name: tenzro-xyz Forecasts API
  slug: tenzro-xyz-forecasts-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Identity & agents API from tenzro-xyz — 6 operation(s) for identity & agents.
  name: tenzro-xyz Identity & agents API
  slug: tenzro-xyz-identity-agents-api
- baseURL: https://api.tenzro.xyz/v1
  baseurl_source: declared
  description: The Images API from tenzro-xyz — 1 operation(s) for images.
  name: tenzro-xyz Images API
  slug: tenzro-xyz-images-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Keys API from tenzro-xyz — 1 operation(s) for keys.
  name: tenzro-xyz Keys API
  slug: tenzro-xyz-keys-api
- baseURL: https://api.tenzro.xyz/v1
  baseurl_source: declared
  description: The Models API from tenzro-xyz — 1 operation(s) for models.
  name: tenzro-xyz Models API
  slug: tenzro-xyz-models-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Orders API from tenzro-xyz — 3 operation(s) for orders.
  name: tenzro-xyz Orders API
  slug: tenzro-xyz-orders-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Plans & rentals API from tenzro-xyz — 4 operation(s) for plans & rentals.
  name: tenzro-xyz Plans & rentals API
  slug: tenzro-xyz-plans-rentals-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Time API from tenzro-xyz — 6 operation(s) for time.
  name: tenzro-xyz Time API
  slug: tenzro-xyz-time-api
- baseURL: https://api.tenzro.xyz/v1
  baseurl_source: declared
  description: The Videos API from tenzro-xyz — 3 operation(s) for videos.
  name: tenzro-xyz Videos API
  slug: tenzro-xyz-videos-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Vision API from tenzro-xyz — 13 operation(s) for vision.
  name: tenzro-xyz Vision API
  slug: tenzro-xyz-vision-api
- baseURL: https://api.tenzro.xyz
  baseurl_source: declared
  description: The Voices API from tenzro-xyz — 23 operation(s) for voices.
  name: tenzro-xyz Voices API
  slug: tenzro-xyz-voices-api
- baseURL: https://api.tenzro.xyz/v1
  baseurl_source: declared
  description: The Chat Completions API from tenzro-xyz — 1 operation(s) for chat completions.
  name: tenzro-xyz Chat Completions API
  slug: tenzro-xyz-chat-completions-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/tenzro-xyz/agentic-access/tenzro-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tenzro-xyz-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tenzro-xyz/rate-limits/tenzro-xyz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tenzro-xyz-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tenzro-xyz/plans/tenzro-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tenzro-xyz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tenzro-xyz/rules/tenzro-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/tenzro-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/tenzro-xyz/json-ld/tenzro-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tenzro-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/tenzro-xyz/vocabulary/tenzro-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tenzro-xyz-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tenzro-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tenzro-xyz/data-model/tenzro-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tenzro-xyz-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tenzro-xyz/authentication/tenzro-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tenzro-xyz-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tenzro-xyz/scopes/tenzro-xyz-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tenzro-xyz-scopes.yml
- group: design
  href: https://artifacts.apis.io/tenzro-xyz/errors/tenzro-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tenzro-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tenzro-xyz/conformance/tenzro-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tenzro-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tenzro-xyz/mcp/tenzro-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tenzro-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tenzro-xyz/well-known/tenzro-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tenzro-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/tenzro-xyz/hosts/tenzro-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tenzro-xyz-hosts.yml
- group: auth
  href: https://artifacts.apis.io/tenzro-xyz/security/tenzro-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenzro-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tenzro.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.tenzro.xyz/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tenzro.xyz/developers
- group: operate
  title: ''
  type: Support
  url: https://tenzro.xyz/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://tenzro.xyz/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tenzro
created: '2026-10-29'
description: Tenzro Labs offers managed access to frontier open models, custom harnesses for agentic systems, and secure deployments for agents and models with NVIDIA OpenShell and confidential, attested environments, all settled on the open Tenzro Network. The Tenzro Labs Platform is an OpenAI-compatible model API and MCP server; Cortex is the assistant for people.
image: https://tenzro.xyz/opengraph-image?31c9eec790d0cec1
jsonld:
- class_count: 1
  name: Tenzro Xyz Context
  property_count: 1
  slug: tenzro-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.tenzro.xyz.
  name: tenzro-xyz MCP Server
  slug: tenzro-xyz-mcp-yml
modified: '2026-10-29'
name: tenzro-xyz
nav: Providers
network: true
overview: 'tenzro-xyz publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API keys API, Audio API, and 21 more. Tagged areas include Company, AI, Machine-Learning, MCP, and Platform.


  The tenzro-xyz catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tenzro-xyz''s developer surface includes authentication, documentation, support, pricing, and 18 more developer resources.'
plans:
- name: Tenzro Xyz Plans Pricing
  plan_count: 2
  slug: tenzro-xyz-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Tenzro Xyz Rate Limits
  slug: tenzro-xyz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: tenzro-xyz API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: tenzro-xyz-rules
scopes:
- name: Tenzro Xyz Scopes
  scope_count: 0
  slug: tenzro-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 63.8
    catalog_earned_first_party: 16.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 42.1
    discoverability: 65.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tenzro Xyz Authentication
  slug: tenzro-xyz-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Tenzro Xyz Domain Security
  slug: tenzro-xyz-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: list-models
  slug: tenzro-xyz-list-models
slug: tenzro-xyz
tags:
- Company
- AI
- Machine-Learning
- MCP
- Platform
- OpenAI-Compatible
website: https://tenzro.xyz/
---
