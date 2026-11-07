---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Framethrower Agentic Access
  operation_count: 11
  slug: framethrower-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 2
apis:
- description: Remote Model Context Protocol server (streamable HTTP) at https://framethrower.ai/api/mcp with four tools (search_frames, find_by_craft, find_similar, get_frame_details), OAuth 2.1 with dynamic client
  name: FrameThrower MCP Server
  slug: framethrower-mcp-server
- baseURL: https://framethrower.ai/api/v1
  baseurl_source: declared
  description: Autocomplete and helpers
  name: FrameThrower Discovery API
  slug: framethrower-discovery-api
- baseURL: https://framethrower.ai/api/v1
  baseurl_source: declared
  description: The film catalogue
  name: FrameThrower Films API
  slug: framethrower-films-api
- baseURL: https://framethrower.ai/api/v1
  baseurl_source: declared
  description: Individual frames and their metadata
  name: FrameThrower Frames API
  slug: framethrower-frames-api
- baseURL: https://framethrower.ai/api/v1
  baseurl_source: declared
  description: Find frames by text, image or colour
  name: FrameThrower Search API
  slug: framethrower-search-api
artifact_total: 19
common:
- group: operate
  href: https://artifacts.apis.io/framethrower/rate-limits/framethrower-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/framethrower-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/framethrower/agentic-access/framethrower-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/framethrower-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/framethrower/plans/framethrower-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/framethrower-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/framethrower/rules/framethrower-rules.yml
  title: ''
  type: Spectral
  url: rules/framethrower-rules.yml
- group: design
  href: https://artifacts.apis.io/framethrower/json-ld/framethrower-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/framethrower-context.jsonld
- group: design
  href: https://artifacts.apis.io/framethrower/vocabulary/framethrower-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/framethrower-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/framethrower/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/framethrower/data-model/framethrower-data-model.yml
  title: ''
  type: DataModel
  url: data-model/framethrower-data-model.yml
- group: design
  href: https://artifacts.apis.io/framethrower/conventions/framethrower-conventions.yml
  title: ''
  type: Conventions
  url: conventions/framethrower-conventions.yml
- group: auth
  href: https://artifacts.apis.io/framethrower/scopes/framethrower-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/framethrower-scopes.yml
- group: design
  href: https://artifacts.apis.io/framethrower/lifecycle/framethrower-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/framethrower-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/framethrower/errors/framethrower-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/framethrower-problem-types.yml
- group: design
  href: https://artifacts.apis.io/framethrower/conformance/framethrower-conformance.yml
  title: ''
  type: Conformance
  url: conformance/framethrower-conformance.yml
- group: other
  href: https://artifacts.apis.io/framethrower/overlays/framethrower-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/framethrower-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/framethrower/llms/framethrower-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/framethrower-llms.txt
- group: build
  href: https://artifacts.apis.io/framethrower/mcp/framethrower-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/framethrower-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/framethrower/mcp/framethrower-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/framethrower-mcp.yml
- group: agent
  href: https://artifacts.apis.io/framethrower/well-known/framethrower-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/framethrower-well-known.yml
- group: other
  href: https://artifacts.apis.io/framethrower/hosts/framethrower-hosts.yml
  title: ''
  type: Hosts
  url: hosts/framethrower-hosts.yml
- group: other
  href: https://artifacts.apis.io/framethrower/vendors/framethrower-vendors.yml
  title: ''
  type: Vendors
  url: vendors/framethrower-vendors.yml
- group: build
  href: https://artifacts.apis.io/framethrower/packages/framethrower-packages.yml
  title: ''
  type: SDKs
  url: packages/framethrower-packages.yml
- group: build
  href: https://artifacts.apis.io/framethrower/packages/framethrower-packages.yml
  title: ''
  type: Packages
  url: packages/framethrower-packages.yml
- group: auth
  href: https://artifacts.apis.io/framethrower/authentication/framethrower-authentication.yml
  title: ''
  type: Authentication
  url: authentication/framethrower-authentication.yml
- group: auth
  href: https://artifacts.apis.io/framethrower/security/framethrower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/framethrower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://framethrower.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://framethrower.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://framethrower.ai/api/v1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/framethrower-ai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/framethrower-ai/framethrower-mcp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/framethrower-ai/framethrower-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/framethrower-ai/comfyui-framethrower
- group: commercial
  title: ''
  type: Pricing
  url: https://framethrower.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://framethrower.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://framethrower.ai/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://framethrower.ai/legal/privacy
- group: company
  title: ''
  type: AboutUs
  url: https://framethrower.ai/about
created: '2026-09-25'
description: FrameThrower is a film-still reference library for filmmakers, students and creative teams, indexed frame by frame on lighting, lens character, shot size, camera angle, colour palette, mood and era. A REST API (OpenAPI 3.1 at https://framethrower.ai/api/v1/openapi.json, 11 endpoints, bearer-token auth) and an MCP server at https://framethrower.ai/api/mcp (four tools, OAuth 2.1) expose visual-reference search and film and frame information; an npm SDK (framethrower-ai) and an MIT-licensed MCP repository (github.com/framethrower-ai/framethrower-mcp) are published. Free plan with usage-based paid upgrades. Submitter-stated by the founder, Leo Kadieff.
finops:
- has_sources: true
  method: derived
  name: Framethrower Finops
  primary_unit: subscription
  service_category: ''
  slug: framethrower-finops
  template: false
image: https://framethrower.ai/logo/og-image.png?v=3
json_schemas:
- name: Frame
  property_count: 15
  slug: framethrower-frame
jsonld:
- class_count: 2
  name: Framethrower Context
  property_count: 18
  slug: framethrower-context
layout: provider
mcp_servers:
- description: Remote MCP server at framethrower.ai over streamable HTTP requiring OAuth; 4 tools listed.
  name: FrameThrower
  slug: framethrower
modified: '2026-09-25'
name: FrameThrower
nav: Providers
network: true
overview: 'FrameThrower publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Films API, Frames API, and 2 more. Tagged areas include Film, Cinematography, Visual Reference, Image Search, and Media.


  The FrameThrower catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FrameThrower''s developer surface includes authentication, documentation, API reference, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Framethrower Plans Pricing
  plan_count: 4
  slug: framethrower-plans-pricing
- name: Framethrower Price Estimates
  plan_count: 0
  slug: framethrower-price-estimates
random_paper: 6
rate_limits:
- limit_count: 0
  name: Framethrower Rate Limits
  slug: framethrower-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: FrameThrower API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: framethrower-rules
scopes:
- name: Framethrower Scopes
  scope_count: 4
  slug: framethrower-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 71.2
    catalog_earned_first_party: 12.0
    catalog_gap: 43.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 61.8
    contract_governance: 35.6
    contract_quality: 66.8
    developer_ergonomics: 29.2
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/framethrower/framethrower-2026-10-11T104642.png
security:
- kind: authentication
  name: Framethrower Authentication
  slug: framethrower-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Framethrower Domain Security
  slug: framethrower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: framethrower-explore-a-film
  slug: framethrower-explore-a-film
- name: framethrower-find-visual-references
  slug: framethrower-find-visual-references
slug: framethrower
tags:
- Film
- Cinematography
- Visual Reference
- Image Search
- Media
- Creative Tools
- MCP
- Agent-Native
website: https://framethrower.ai/
---
