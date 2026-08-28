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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Custom and automatic events logged during sessions
  name: UXCam Events API
  slug: uxcam-events-api
- description: Recorded usage sessions (qualitative list + quantitative analytics)
  name: UXCam Sessions API
  slug: uxcam-sessions-api
- description: App users tracked by the UXCam SDK
  name: UXCam Users API
  slug: uxcam-users-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UXCam Data Access Events API
  slug: open-uxcam-events-api
- collection_type: open
  name: UXCam Data Access Events Sessions API
  slug: open-uxcam-sessions-api
- collection_type: open
  name: UXCam Data Access Events Users API
  slug: open-uxcam-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/uxcam-data-access-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://uxcam.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uxcam.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uxcam.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uxcam.com/docs/data-access-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uxcam.com/docs/what-is-uxcam
- group: operate
  title: ''
  type: Support
  url: https://help.uxcam.com
- group: company
  title: ''
  type: Blog
  url: https://uxcam.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uxcam
- group: commercial
  title: ''
  type: Pricing
  url: https://uxcam.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.uxcam.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.uxcam.com/en/articles/10222767-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uxcam.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uxcam.com
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/9127779/2s935it5r2
- group: build
  title: ''
  type: PostmanCollection
  url: postman/uxcam-data-access-v2-postman.json
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uxcam-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uxcam-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uxcam-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/uxcam-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uxcam-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uxcam-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/uxcam-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/uxcam-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uxcam-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uxcam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uxcam-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uxcam-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uxcam-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uxcam-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uxcam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://uxcam.com/bug-bounty
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: UXCam is a mobile-first product analytics and session replay platform that helps product, UX, and engineering teams understand how people actually use their apps. SDKs for Android, iOS, React Native, Flutter, Cordova, Xamarin/MAUI, NativeScript, and the web capture session recordings, heatmaps, gestures, crashes, and custom events with built-in PII occlusion, while the Data Access API exposes session, user, and event analytics programmatically and an official MCP server guides agent-driven SDK integration.
image: https://github.com/uxcam.png
layout: provider
mcp_servers:
- description: ''
  name: UXCam MCP Server
  slug: uxcam-mcp-server
modified: '2026-07-21'
name: UXCam
nav: Providers
network: true
overview: 'UXCam publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, Sessions API, and Users API. Tagged areas include Company, Product Analytics, Session Replay, Mobile Analytics, and Heatmaps.


  UXCam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 40.0
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 14.3
    developer_ergonomics: 51.8
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 40.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uxcam/refs/heads/main/screenshots/uxcam-2026-08-17T082703.png
security:
- kind: authentication
  name: Uxcam Authentication
  slug: uxcam-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Uxcam Domain Security
  slug: uxcam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uxcam Vulnerability Disclosure
  slug: uxcam-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: uxcam
tags:
- Company
- Product Analytics
- Session Replay
- Mobile Analytics
- Heatmaps
- User Experience
- Crash Reporting
website: https://uxcam.com
---
