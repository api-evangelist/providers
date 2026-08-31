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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Create, retrieve, list and stop screen sharing sessions.
  name: Screenleap Inc Screen Shares API
  slug: screenleap-inc-screen-shares-api
artifact_total: 7
asyncapis:
- description: ''
  name: Screenleap Inc Webhooks
  slug: screenleap-inc-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Screenleap Screen Sharing Screen Shares API
  slug: open-screenleap-inc-screen-shares-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/screenleap-inc-screen-sharing-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/screenleap-inc-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.screenleap.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.screenleap.com/api/doc
- group: docs
  title: ''
  type: APIReference
  url: https://www.screenleap.com/api/native/doc/http-calls
- group: start
  title: ''
  type: GettingStarted
  url: https://www.screenleap.com/api/native/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://www.screenleap.com/api/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.screenleap.com/signup/developer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.screenleap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.screenleap.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.screenleap.com/support
- group: company
  title: ''
  type: Blog
  url: https://blog.screenleap.com/tag/screenleap-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Screenleap
- group: auth
  title: ''
  type: Authentication
  url: authentication/screenleap-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/screenleap-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/screenleap-inc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/screenleap-inc-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.screenleap.com/api/native/update
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/screenleap-inc-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/screenleap-inc-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/screenleap-inc-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/screenleap-inc-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/screenleap-inc-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/screenleap-inc-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/screenleap-inc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/screenleap-inc-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Screenleap is a Y Combinator-backed company whose API lets developers add live screen sharing, video conferencing, audio conferencing and chat to their own websites and online products. Integrations create a session server-to-server over a REST/JSON HTTP interface (base https://api.screenleap.com/v2), load a hosted screenleap.js library on the presenter's page, and render the share to viewers through a returned viewer URL or embedded iframe. Authentication uses an account id plus an auth token; billing is per participant-minute (Basic $0.003/min, White-Label $0.010/min) with no Screenleap subscription required.
image: https://www.screenleap.com/img/screenleap-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Screenleap Inc MCP Server
  slug: screenleap-inc-mcp-server
modified: '2026-07-21'
name: Screenleap Inc
nav: Providers
network: true
overview: 'Screenleap Inc publishes 1 API on the [APIs.io](https://apis.io/) network: Screen Shares API. Tagged areas include Company, Screen Sharing, Video Conferencing, Collaboration, and Real-Time Communication.


  The Screenleap Inc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Screenleap Inc''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 20 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 22.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 38.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Screenleap Inc Authentication
  slug: screenleap-inc-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Screenleap Inc Domain Security
  slug: screenleap-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: screenleap-inc
tags:
- Company
- Screen Sharing
- Video Conferencing
- Collaboration
- Real-Time Communication
- WebRTC
- Embedded
- Developer Tools
website: https://www.screenleap.com/developer
---
