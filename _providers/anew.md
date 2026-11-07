---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://anew.page
  baseurl_source: spec
  description: Agent2Agent (A2A) protocol JSON-RPC endpoint.
  name: anew A2a API
  slug: anew-a2a-api
- baseURL: https://anew.page
  baseurl_source: spec
  description: Model Context Protocol JSON-RPC endpoint.
  name: anew MCP API
  slug: anew-mcp-api
- baseURL: https://anew.page
  baseurl_source: spec
  description: Write self-contained HTML pages, and read them back.
  name: anew Pages API
  slug: anew-pages-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/anew/rate-limits/anew-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anew-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/anew/overlays/anew-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anew-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/anew/mcp/anew-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anew-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.anew.page/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anew.page
- group: docs
  title: ''
  type: Documentation
  url: https://anew.page/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://anew.page/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://setup.anew.page
- group: operate
  title: ''
  type: Support
  url: https://github.com/round/anew.page/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/round
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/round/anew.page/blob/main/LICENSE.md#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://github.com/round/anew.page/blob/main/LICENSE.md#privacy
- group: agent
  href: https://artifacts.apis.io/anew/llms/anew-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anew-llms.txt
- group: agent
  href: https://artifacts.apis.io/anew/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/anew/well-known/anew-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anew-well-known.yml
- group: other
  href: https://artifacts.apis.io/anew/well-known/anew-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/anew-api-catalog.json
- group: design
  href: https://artifacts.apis.io/anew/conformance/anew-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anew-conformance.yml
- group: design
  href: https://artifacts.apis.io/anew/lifecycle/anew-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anew-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/anew/lifecycle/anew-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/anew-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/anew/security/anew-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/anew-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anew/security/anew-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anew-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anew/security/anew-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anew-domain-security.yml
- group: build
  href: https://artifacts.apis.io/anew/packages/anew-packages.yml
  title: ''
  type: Packages
  url: packages/anew-packages.yml
- group: design
  href: https://artifacts.apis.io/anew/components/anew-components.yml
  title: ''
  type: Components
  url: components/anew-components.yml
- group: commercial
  href: https://artifacts.apis.io/anew/plans/anew-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anew-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/anew/mcp/anew-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anew-tool-crosswalk.yml
created: '2026-09-04'
description: A stateless "page-in-a-URL" service that encodes a self-contained HTML document into a shareable, immutable URL (HTML → URL) and reads it back (URL → HTML). No account, no hosting; free, deterministic, and unauthenticated. Exposes a REST/HTTP API, a hosted MCP server, an A2A agent, and llms.txt.
finops:
- has_sources: true
  method: derived
  name: Anew Finops
  primary_unit: ''
  service_category: ''
  slug: anew-finops
  template: true
image: https://anew.page/anew.png
layout: provider
mcp_servers:
- description: anew ships a first-party hosted remote MCP server that answers tools/list anonymously over plain HTTP. No OAuth challenge, no session handshake, no client library — a single POST returns the real tool
  name: anew MCP Server
  slug: anew-mcp-yml
modified: '2026-09-04'
name: anew
nav: Providers
network: true
overview: 'anew publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: A2a API, MCP API, and Pages API. Tagged areas include HTML, Webpage, Websites, URLs, and Encode.


  The anew catalog on APIs.io includes 1 Spectral governance ruleset.


  anew''s developer surface includes documentation, API reference, getting-started guide, support, and 22 more developer resources.'
plans:
- name: Anew Plans Pricing
  plan_count: 0
  slug: anew-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Anew Rate Limits
  slug: anew-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: anew API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 3
  slug: anew-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 8.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 52.2
    developer_ergonomics: 69.0
    discoverability: 61.7
    operational_transparency: 42.1
  previous_composite: 46.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/anew/anew-2026-10-11T094042.png
security:
- kind: authentication
  name: Anew Authentication
  slug: anew-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anew Domain Security
  slug: anew-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Anew Vulnerability Disclosure
  slug: anew-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Anew Trust Center
  slug: anew-trust-center
  summary_line: trust center published
skill_count: 1
skills:
- name: anew
  slug: anew-anew
slug: anew
tags:
- HTML
- Webpage
- Websites
- URLs
- Encode
- Share
- Web Publishing
- Developer Tools
- MCP
- A2A
- AI / Agent Tooling
- Llms.txt
- Agents.txt
- Agent Skills
- WebMCP
- OpenAPI
- stateless
- Immutable
- No Auth
- Static Sites
- url-encoding
website: https://www.anew.page/
---
