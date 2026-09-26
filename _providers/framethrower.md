---
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Framethrower Agentic Access
  operation_count: 11
  slug: framethrower-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 2
apis:
- baseURL: https://framethrower.ai/api/v1
  baseurl_source: declared
  description: 'REST API over the FrameThrower film-still library: plain-language, reference-image and colour search, craft-attribute browsing, similar-frame lookup, and film and per-frame metadata (thumbnails, palet'
  name: FrameThrower API
  slug: framethrower-api
- description: Remote Model Context Protocol server (streamable HTTP) at https://framethrower.ai/api/mcp with four tools (search_frames, find_by_craft, find_similar, get_frame_details), OAuth 2.1 with dynamic client
  name: FrameThrower MCP Server
  slug: framethrower-mcp-server
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/agentic-access/framethrower-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/framethrower-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/plans/framethrower-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/framethrower-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/rules/framethrower-rules.yml
  title: ''
  type: Spectral
  url: rules/framethrower-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/json-ld/framethrower-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/framethrower-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/vocabulary/framethrower-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/framethrower-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/data-model/framethrower-data-model.yml
  title: ''
  type: DataModel
  url: data-model/framethrower-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/conventions/framethrower-conventions.yml
  title: ''
  type: Conventions
  url: conventions/framethrower-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/scopes/framethrower-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/framethrower-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/lifecycle/framethrower-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/framethrower-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/errors/framethrower-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/framethrower-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/conformance/framethrower-conformance.yml
  title: ''
  type: Conformance
  url: conformance/framethrower-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/overlays/framethrower-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/framethrower-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/llms/framethrower-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/framethrower-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/mcp/framethrower-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/framethrower-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/mcp/framethrower-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/framethrower-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/well-known/framethrower-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/framethrower-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/hosts/framethrower-hosts.yml
  title: ''
  type: Hosts
  url: hosts/framethrower-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/vendors/framethrower-vendors.yml
  title: ''
  type: Vendors
  url: vendors/framethrower-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/packages/framethrower-packages.yml
  title: ''
  type: SDKs
  url: packages/framethrower-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/packages/framethrower-packages.yml
  title: ''
  type: Packages
  url: packages/framethrower-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/authentication/framethrower-authentication.yml
  title: ''
  type: Authentication
  url: authentication/framethrower-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/framethrower/refs/heads/main/security/framethrower-domain-security.yml
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
- description: ''
  name: FrameThrower
  slug: framethrower
modified: '2026-09-25'
name: FrameThrower
nav: Providers
network: true
overview: 'FrameThrower publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Film, Cinematography, Visual Reference, Image Search, and Media.


  The FrameThrower catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FrameThrower''s developer surface includes authentication, documentation, API reference, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Framethrower Plans Pricing
  plan_count: 4
  slug: framethrower-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Framethrower Rate Limits
  slug: framethrower-rate-limits
rules:
- effective_rule_count: 58
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
  scope_count: 0
  slug: framethrower-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.2
    catalog_earned_first_party: 12.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 61.2
    developer_ergonomics: 37.5
    discoverability: 75.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Framethrower Authentication
  slug: framethrower-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Framethrower Domain Security
  slug: framethrower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
