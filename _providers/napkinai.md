---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Napkinai Agentic Access
  operation_count: 3
  slug: napkinai-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Programmatic visual content generation.
  name: Napkin.AI Visuals API
  slug: napkinai-visuals-api
arazzos:
- description: Submit text to Napkin AI, poll the asynchronous request until it completes, then download each generated file (PNG/SVG/PDF/PPT).
  name: Generate a visual from text with Napkin AI
  slug: napkinai-generate-visual
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Napkin AI Visuals API
  slug: open-napkinai-visuals-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/napkinai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.napkin.ai
- group: auth
  title: ''
  type: DomainSecurity
  url: security/napkinai-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/napkinai-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/napkinai-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/napkinai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.napkin.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.napkin.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.napkin.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.napkin.ai/api/create-visual-request
- group: start
  title: ''
  type: GettingStarted
  url: https://api.napkin.ai/api/napkin-api-documentation
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/napkinai-openapi.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.napkin.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.napkin.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.napkin.ai/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.napkin.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.napkin.ai/en/
- group: company
  title: ''
  type: Blog
  url: https://www.napkin.ai/blog/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/napkinai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/napkinai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/napkinai-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/napkinai-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/napkinai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/napkinai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/napkinai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/napkinai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/napkinai-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/napkinai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/napkinai-openapi-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/napkinai-generate-visual.yml
created: '2026-07-17'
description: 'Napkin AI turns typed or pasted text into editable visuals — diagrams, charts, mind maps, icons, and infographics — and into full presentations, with no prompting or design skill required. Two products share the same text-to-visual engine: Napkin Visuals (standalone diagrams and graphics, exportable to PPT, PNG, PDF, or SVG) and Napkin Slides (beta AI presentation agent that builds a tailored, fully editable deck). A developer-preview REST API also generates visuals programmatically: submit text to POST /v1/visual, poll the request status, then download the generated PNG/SVG/PPT files. Authentication is by account API token (HTTP Bearer) or OAuth 2.0 (beta) with user and generation scopes. Napkin AI is backed by Accel.'
image: https://www.napkin.ai/assets/og-image-v5.png?v=2
layout: provider
mcp_servers:
- description: ''
  name: napkinai-mcp.yml
  slug: napkinai-mcpyml
modified: '2026-07-20'
name: Napkin.AI
nav: Providers
network: true
overview: 'Napkin.AI publishes 1 API on the [APIs.io](https://apis.io/) network: Visuals API. Tagged areas include Company, Ai, Visualization, Diagrams, and Charts.


  Napkin.AI''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 24 more developer resources.'
random_paper: 3
scopes:
- name: Napkinai Scopes
  scope_count: 2
  slug: napkinai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.7
  delta: -3.2
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/napkinai/refs/heads/main/screenshots/napkinai-2026-08-07T184624.png
security:
- kind: authentication
  name: Napkinai Authentication
  slug: napkinai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Napkinai Domain Security
  slug: napkinai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Napkinai Vulnerability Disclosure
  slug: napkinai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: napkinai
tags:
- Company
- Ai
- Visualization
- Diagrams
- Charts
- Infographics
- Presentations
- Content Generation
- Design
- Developer API
website: https://www.napkin.ai/
---
