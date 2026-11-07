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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Diagram La Agentic Access
  operation_count: 11
  slug: diagram-la-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- description: Remote MCP server at https://diagram.la/mcp that lets AI tools save, edit, publish and fetch diagrams (documented tools include save_diagram, edit_diagram, publish_diagram, setup_repo and get_diagram)
  name: Diagram MCP Server
  slug: diagram-mcp-server
- baseURL: https://diagram.la/api/v1
  baseurl_source: declared
  description: The Diagrams API from Diagram — 2 operation(s) for diagrams.
  name: Diagram Diagrams API
  slug: diagram-la-diagrams-api
- baseURL: https://diagram.la/api/v1
  baseurl_source: declared
  description: The Projects API from Diagram — 4 operation(s) for projects.
  name: Diagram Projects API
  slug: diagram-la-projects-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/diagram-la/agentic-access/diagram-la-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/diagram-la-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/diagram-la/rate-limits/diagram-la-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/diagram-la-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/diagram-la/plans/diagram-la-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diagram-la-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/diagram-la/rules/diagram-la-rules.yml
  title: ''
  type: Spectral
  url: rules/diagram-la-rules.yml
- group: agent
  href: https://artifacts.apis.io/diagram-la/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/diagram-la/conventions/diagram-la-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/diagram-la-conventions.yml
- group: design
  href: https://artifacts.apis.io/diagram-la/conventions/diagram-la-conventions.yml
  title: ''
  type: Conventions
  url: conventions/diagram-la-conventions.yml
- group: operate
  href: https://artifacts.apis.io/diagram-la/lifecycle/diagram-la-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/diagram-la-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/diagram-la/lifecycle/diagram-la-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/diagram-la-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/diagram-la/errors/diagram-la-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/diagram-la-error-codes.yml
- group: design
  href: https://artifacts.apis.io/diagram-la/conformance/diagram-la-conformance.yml
  title: ''
  type: Conformance
  url: conformance/diagram-la-conformance.yml
- group: other
  href: https://artifacts.apis.io/diagram-la/overlays/diagram-la-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diagram-la-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/diagram-la/llms/diagram-la-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diagram-la-llms.txt
- group: build
  href: https://artifacts.apis.io/diagram-la/mcp/diagram-la-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/diagram-la-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/diagram-la/mcp/diagram-la-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/diagram-la-mcp.yml
- group: agent
  href: https://artifacts.apis.io/diagram-la/well-known/diagram-la-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/diagram-la-well-known.yml
- group: other
  href: https://artifacts.apis.io/diagram-la/hosts/diagram-la-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diagram-la-hosts.yml
- group: build
  href: https://artifacts.apis.io/diagram-la/integrations/diagram-la-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/diagram-la-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/diagram-la/vendors/diagram-la-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diagram-la-vendors.yml
- group: auth
  href: https://artifacts.apis.io/diagram-la/authentication/diagram-la-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diagram-la-authentication.yml
- group: auth
  href: https://artifacts.apis.io/diagram-la/security/diagram-la-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diagram-la-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diagram.la/
- group: docs
  title: ''
  type: Documentation
  url: https://diagram.la/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://diagram.la/docs
- group: docs
  title: ''
  type: APIReference
  url: https://diagram.la/docs/reference
- group: operate
  title: ''
  type: Support
  url: https://diagram.la/docs/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://diagram.la/pricing
- group: start
  title: ''
  type: SignUp
  url: https://diagram.la/signin/dashboard
- group: start
  title: ''
  type: Login
  url: https://diagram.la/start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://diagram.la/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diagram.la/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://diagram.la/llms.txt
created: '2026-11-05'
description: Diagram (diagram.la) is a hosted service for making and sharing diagrams drawn by AI. Users connect an AI tool such as Claude, ChatGPT, Claude Code, Codex, Cursor or Gemini CLI, describe a diagram in plain words, and the AI publishes it to Diagram through its MCP server or API, where it lives as an HTML page at a permanent private or public link; asking for a change updates the diagram at the same URL. It also supports publishing from CI, and its guides cover flowcharts, architecture, C4, ER, sequence and Mermaid diagrams.
image: https://diagram.la/brand/diagram-logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at diagram.la over streamable HTTP requiring OAuth; 13 tools listed.
  name: Diagram MCP Server
  slug: diagram-mcp-server
modified: '2026-11-05'
name: Diagram
nav: Providers
network: true
overview: 'Diagram publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Diagrams API, Projects API, and 1 more. Tagged areas include Company, Diagramming, Visualization, Artificial Intelligence, and MCP.


  The Diagram catalog on APIs.io includes 1 Spectral governance ruleset.


  Diagram''s developer surface includes authentication, documentation, getting-started guide, API reference, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Diagram La Plans Pricing
  plan_count: 2
  slug: diagram-la-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Diagram La Rate Limits
  slug: diagram-la-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Diagram API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: diagram-la-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 42.9
    developer_ergonomics: 47.0
    discoverability: 71.7
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Diagram La Authentication
  slug: diagram-la-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Diagram La Domain Security
  slug: diagram-la-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: publish-a-diagram-from-ci
  slug: diagram-la-publish-a-diagram-from-ci
- name: review-diagram-history
  slug: diagram-la-review-diagram-history
- name: share-a-project
  slug: diagram-la-share-a-project
slug: diagram-la
tags:
- Company
- Diagramming
- Visualization
- Artificial Intelligence
- MCP
- Collaboration
- Developer Tools
website: https://diagram.la/
---
