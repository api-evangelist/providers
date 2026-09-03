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
    agent_skills: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coteach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coteach.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coteach.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://www.coteach.ai/chat?login=true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coteach.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coteach.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.coteach.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.coteach.ai/faqs
- group: operate
  title: ''
  type: Roadmap
  url: https://coteach.feedbear.com/roadmap
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coteach-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coteach-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coteach-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coteach-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coteach-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coteach-conformance.yml
created: '2026-07-17'
description: CoTeach is an AI-powered curriculum co-planning assistant for K-12 mathematics teachers, built by Teaching Lab and deeply integrated with the Illustrative Mathematics (IM v.360) curriculum. Through a chat interface, teachers adapt lessons, generate curriculum-aligned practice problems and worksheets, build scaffolds and differentiated supports for multilingual learners and students with IEPs, and produce IM-style math diagrams (number lines, tape diagrams, area models), exporting to PDF or Google Docs. CoTeach preserves IM's pedagogical framework, collects no student data, and meters usage by message credits. It also exposes a hosted, OAuth-protected Model Context Protocol (MCP) server (the "Coteach Claude connector") and publishes an llms.txt so AI agents can discover the product and hand off to it.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coteach.png
layout: provider
mcp_servers:
- description: ''
  name: Coteach Claude connector
  slug: coteach-claude-connector
modified: '2026-07-18'
name: CoTeach
nav: Providers
network: true
overview: 'CoTeach is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Mathematics, and K-12.


  CoTeach''s developer surface includes pricing, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 13
scopes:
- name: Coteach Scopes
  scope_count: 4
  slug: coteach-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 25.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coteach/refs/heads/main/screenshots/coteach-2026-07-25T210502.png
security:
- kind: authentication
  name: Coteach Authentication
  slug: coteach-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Coteach Domain Security
  slug: coteach-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coteach
tags:
- Company
- Education
- EdTech
- Mathematics
- K-12
- Teachers
- Curriculum
- Lesson Planning
- AI Assistant
- Illustrative Mathematics
- MCP
website: https://www.coteach.ai
---
