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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Confrere Agentic Access
  operation_count: 3
  slug: confrere-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: The Room API from Confrere — 2 operation(s) for room.
  name: Confrere Room API
  slug: confrere-room-api
- description: The Token API from Confrere — 1 operation(s) for token.
  name: Confrere Token API
  slug: confrere-token-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Mint a single-use room URL for a participant, then end the session by invalidating the room.
  name: Confrere — start and end a video session
  slug: confrere-video-session
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://confrere.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.compodium.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.compodium.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.compodium.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://confrere.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://confrere.com/signup
- group: start
  title: ''
  type: Login
  url: https://confrere.com/login
- group: operate
  title: ''
  type: Support
  url: https://confrere.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://confrere.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://confrere.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://confrere.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.confrere.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/confrere-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/confrere-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/confrere-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/confrere-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/confrere-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/confrere-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/confrere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confrere-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confrere-video-session.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confrere-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confrere-domain-security.yml
created: '2026-07-17'
description: Confrere is a privacy-first, embeddable video-consultation platform (now a Compodium product) built in the Nordics for healthcare providers, therapists, consultants, tutors, and sales teams who need secure, encrypted video meetings that clients join from any modern browser with no download. Its server-side API mints single-use, one-minute room URLs that redirect a participant into a Confrere video room, and lets integrators invalidate a room or eject a specific user. Reliability is advertised at 99% across more than one million completed meetings. Backed by Point Nine.
image: https://confrere.com/static/images/Thumbnail.webp
layout: provider
mcp_servers:
- description: ''
  name: confrere-mcp.yml
  slug: confrere-mcpyml
modified: '2026-07-18'
name: Confrere
nav: Providers
network: true
overview: 'Confrere publishes 2 APIs on the [APIs.io](https://apis.io/) network: Room API and Token API. Tagged areas include Company, Video, Video Conferencing, Communications, and Healthcare.


  Confrere''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 38.5
  delta: -5.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 42.4
    developer_ergonomics: 45.1
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/confrere/refs/heads/main/screenshots/confrere-2026-07-25T210253.png
security:
- kind: authentication
  name: Confrere Authentication
  slug: confrere-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Confrere Domain Security
  slug: confrere-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: confrere
tags:
- Company
- Video
- Video Conferencing
- Communications
- Healthcare
- Telehealth
- Embeddable
- WebRTC
website: https://confrere.com
---
