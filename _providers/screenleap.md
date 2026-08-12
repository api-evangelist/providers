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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Create, retrieve, list and stop screen share sessions.
  name: Screenleap Screen Shares API
  slug: screenleap-screen-shares-api
artifact_total: 4
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/screenleap-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.screenleap.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.screenleap.com/api/native/doc
- group: docs
  title: ''
  type: APIReference
  url: https://www.screenleap.com/api/doc/http-calls
- group: start
  title: ''
  type: GettingStarted
  url: https://www.screenleap.com/api/native/quick-start
- group: operate
  title: ''
  type: FAQ
  url: https://www.screenleap.com/api/v1/faq
- group: company
  title: ''
  type: Blog
  url: https://blog.screenleap.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Screenleap
- group: operate
  title: ''
  type: Support
  url: https://www.screenleap.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.screenleap.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.screenleap.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.screenleap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.screenleap.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/screenleap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/screenleap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/screenleap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/screenleap-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/screenleap-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/screenleap-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/screenleap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/screenleap-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/screenleap-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/screenleap-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Screenleap is a screen sharing and online meeting service that lets anyone share their screen instantly from a browser with no software install required for viewers. Beyond the consumer product, Screenleap offers a REST-style developer API (api.screenleap.com/v2) that lets businesses embed live interaction — screen sharing, video conferencing, audio conferencing, chat and cloud recording — directly into their own websites and online services. The API creates and manages screen share sessions, returns a viewer URL and the screenShareData used by the screenleap.js JavaScript library to start sharing, and reports session usage and participant detail. Authentication uses an account id and auth token passed as request headers over SSL. Screenleap is backed by Andreessen Horowitz (a16z).
image: https://www.screenleap.com/img/logo.png
layout: provider
mcp_servers:
- description: ''
  name: screenleap-mcp.yml
  slug: screenleap-mcpyml
modified: '2026-07-21'
name: Screenleap
nav: Providers
network: true
overview: 'Screenleap publishes 1 API on the [APIs.io](https://apis.io/) network: Screen Shares API. Tagged areas include Company, Screen Sharing, Video Conferencing, Screen Recording, and Collaboration.


  Screenleap''s developer surface includes documentation, API reference, getting-started guide, FAQ, engineering blog, support, pricing, and 17 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 44.0
  delta: -1.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.7
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Screenleap Authentication
  slug: screenleap-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Screenleap Domain Security
  slug: screenleap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: screenleap
tags:
- Company
- Screen Sharing
- Video Conferencing
- Screen Recording
- Collaboration
- Real-Time Communication
- WebRTC
- Embeddable
- Developer API
website: https://www.screenleap.com/api
---
