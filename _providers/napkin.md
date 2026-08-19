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
  name: Napkin Agentic Access
  operation_count: 3
  slug: napkin-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Create, poll, and download programmatic visual generations.
  name: Napkin Visuals API
  slug: napkin-visuals-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Napkin Visuals API
  slug: open-napkin-visuals-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/napkin-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/napkin-agentic-access.yml
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
  url: https://api.napkin.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.napkin.ai/docs/changelog
- group: operate
  title: ''
  type: Support
  url: https://help.napkin.ai/en/
- group: company
  title: ''
  type: Blog
  url: https://www.napkin.ai/blog/
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
- group: auth
  title: ''
  type: Authentication
  url: authentication/napkin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/napkin-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/napkin-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://api.napkin.ai/docs/changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/napkin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/napkin-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/napkin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/napkin-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/napkin-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/napkin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.napkin.ai
- group: auth
  title: ''
  type: DomainSecurity
  url: security/napkin-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/napkin-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/napkin-generate-visual.md
- group: design
  title: ''
  type: DataModel
  url: data-model/napkin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/napkin-conformance.yml
created: '2026-07-17'
description: 'Napkin AI turns typed or pasted text into editable visuals — diagrams, charts, icons, and infographics — and into full presentation decks, with no prompting or design skill required. Two products share one text-to-visual engine: Napkin Visuals (standalone diagrams and graphics) and Napkin Slides (beta AI presentation agent). Napkin also ships a developer API (currently a developer preview) for generating visuals programmatically: submit text, poll the asynchronous request, and download the results as SVG, PNG, or PPT. The API authenticates with account bearer tokens or an OAuth 2.0 authorization-code flow. Napkin is an AI company backed by CRV.'
image: https://www.napkin.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: napkin-mcp.yml
  slug: napkin-mcpyml
modified: '2026-07-20'
name: Napkin
nav: Providers
network: true
overview: 'Napkin publishes 1 API on the [APIs.io](https://apis.io/) network: Visuals API. Tagged areas include Company, Ai, Visualization, Diagrams, and Infographics.


  Napkin''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 45
scopes:
- name: Napkin Scopes
  scope_count: 2
  slug: napkin-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.6
  delta: -3.3
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 23.7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/napkin/refs/heads/main/screenshots/napkin-2026-08-07T184622.png
security:
- kind: authentication
  name: Napkin Authentication
  slug: napkin-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Napkin Domain Security
  slug: napkin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Napkin Vulnerability Disclosure
  slug: napkin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: napkin
tags:
- Company
- Ai
- Visualization
- Diagrams
- Infographics
- Presentations
- Content Generation
- Developer API
- Design
website: https://www.napkin.ai/
---
