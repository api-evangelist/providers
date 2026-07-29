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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cachet Agentic Access
  operation_count: 4
  slug: cachet-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: Endpoint where to send the connect request
  name: Cachet Connect API
  slug: cachet-connect-api
- description: Event actions which are sent by the platform to Cachet involving gig-workers tasks done on the platform
  name: Cachet Gig-Events API
  slug: cachet-gig-events-api
- description: User actions to send user-related data from platform to Cachet
  name: Cachet User API
  slug: cachet-user-api
- description: Used to notify Cachet about vehicle events
  name: Cachet Vehicle events API
  slug: cachet-vehicle-events-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Register a gig-worker on the Cachet Platform (Verify) API, then report a completed task event for that worker. Requires x-api-key and x-api-username headers issued by the Cachet IT team.
  name: Cachet gig-worker onboarding and task reporting
  slug: cachet-gig-onboarding
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://cachet.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cachet.me/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cachet.me/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cachet.me/
- group: operate
  title: ''
  type: Support
  url: https://help.cachet.me/en/
- group: company
  title: ''
  type: Blog
  url: https://cachet.me/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://cachet.me/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cachet.me/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cachet.me/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cachet.me/en/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cachet-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cachet-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cachet-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/cachet-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cachet-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cachet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cachet-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cachet-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cachet-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cachet-gig-onboarding.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cachet-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cachet-agentic-access.yml
created: '2026-07-17'
description: 'Cachet OÜ is an Estonian InsurTech that provides adaptive, usage-based insurance for digital platforms and their users across new mobility, gig work, and car-sharing. Digital platforms integrate Cachet through three inbound event APIs: the Parking API (car-sharing fleets stream vehicle events so Cachet manages parking), the Verify / Platform API (gig-work platforms register workers and push task events to drive worker protection), and the Partners API (embed a prefilled Cachet onboarding link into a partner app). All three are OpenAPI 3.1 and authenticated with issued x-api-key and x-api-username headers. Cachet is backed by Techstars; notable platform clients include Bolt, Bird, Ryde, and TaskRabbit.'
image: https://cachet.me/assets/img/social_share.jpg
layout: provider
mcp_servers:
- description: ''
  name: cachet-mcp.yml
  slug: cachet-mcpyml
modified: '2026-07-18'
name: Cachet
nav: Providers
network: true
overview: 'Cachet publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connect API, Gig-Events API, User API, and 1 more. Tagged areas include Company, Insurance, InsurTech, Mobility, and Gig Economy.


  Cachet''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 63
score:
  band: developing
  composite: 43.3
  delta: -5.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.9
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cachet/refs/heads/main/screenshots/cachet-2026-07-25T204205.png
security:
- kind: authentication
  name: Cachet Authentication
  slug: cachet-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cachet Domain Security
  slug: cachet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cachet
tags:
- Company
- Insurance
- InsurTech
- Mobility
- Gig Economy
- Car Sharing
- Embedded Insurance
- Events
website: https://cachet.me/
---
