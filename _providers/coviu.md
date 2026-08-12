---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - authentication
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Coviu Agentic Access
  operation_count: 21
  slug: coviu-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 6
apis:
- description: Create, list, retrieve, update, and cancel Coviu video consultation Sessions, and pull a Session Summary with participant entry/exit timing. OAuth2-authenticated REST over https://api.coviu.com/v1.
  name: Coviu Sessions API
  slug: coviu-sessions-api
- description: List, add, retrieve, update, and cancel Participants on a Coviu Session, controlling the per-participant join links, names, avatars, and host/guest roles.
  name: Coviu Participants API
  slug: coviu-participants-api
- description: Read the Waiting Area in real time — currently waiting calls for a team, waiting calls for a specific queue, and individual call detail — for virtual reception and triage workflows.
  name: Coviu Waiting Area API
  slug: coviu-waiting-area-api
- description: Retrieve a team's Collections and their Submissions, including submission files and audio recordings captured during consultations, for downstream clinical record-keeping and reporting.
  name: Coviu Collections API
  slug: coviu-collections-api
- description: Real-time event notifications delivered as HTTP POST callbacks to a URL you configure, firing when relevant Coviu events occur (for example a patient arriving in the waiting room or a call concluding)
  name: Coviu Webhooks
  slug: coviu-webhooks
- description: In-call Plugin (Apps) API for building custom experiences inside the Coviu video room — adding UI elements, connecting to third-party systems, and enriching the clinical encounter. Documented as a cli
  name: Coviu Plugin API
  slug: coviu-plugin-api
artifact_total: 13
asyncapis:
- description: ''
  name: Coviu Webhooks
  slug: coviu-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coviu-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coviu-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coviu-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coviu-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/coviu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coviu-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coviu-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coviu-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/coviu-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coviu-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/coviu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coviu-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coviu-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coviu-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coviu-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coviu.com/en-au/compliance-and-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/coviu-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coviu-data-model.yml
- group: company
  title: ''
  type: Website
  url: https://www.coviu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coviu.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coviu.readme.io/reference/the-coviu-rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://coviu.readme.io/reference/the-coviu-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://coviu.readme.io/reference/getting-started-with-your-api-1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coviu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coviu
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coviu.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coviu.com/en-au/pricing
- group: start
  title: ''
  type: SignUp
  url: https://signup.coviu.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coviu.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.coviu.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coviu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coviu.com/en-au/privacy-policy
created: '2026-07-24'
description: Coviu is an Australian telehealth company, headquartered in Sydney and spun out of CSIRO's Data61, that provides a purpose-built video consultation platform for healthcare providers, allied health, and enterprise clinical networks. Its browser-based, WebRTC video calling supports virtual care workflows including waiting rooms, in-call clinical tools, screen and file sharing, medical device integrations, and payments. For developers, Coviu ships a secure OAuth2-protected REST API (base https://api.coviu.com) that lets applications create and manage video consultation Sessions and Participants, monitor Waiting Area queues in real time, retrieve Collections (submissions, files, and audio recordings), and receive event Webhooks, plus an in-call Plugin API and embedded iframe mode. Coviu is a telehealth video/interoperability layer rather than an EHR or FHIR data platform, so its documented public surface is REST + webhooks, not HL7 FHIR.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: coviu-mcp.yml
  slug: coviu-mcpyml
modified: '2026-07-24'
name: Coviu
nav: Providers
network: true
overview: 'Coviu publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Sessions API, Participants API, Waiting Area API, and 2 more. Tagged areas include Healthcare, Telehealth, Australia, Virtual Care, and Video.


  The Coviu catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coviu''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 26 more developer resources.'
random_paper: 86
scopes:
- name: Coviu Scopes
  scope_count: 0
  slug: coviu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.6
  delta: -1.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.9
    developer_ergonomics: 62.5
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coviu/refs/heads/main/screenshots/coviu-2026-07-25T210604.png
security:
- kind: authentication
  name: Coviu Authentication
  slug: coviu-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Coviu Domain Security
  slug: coviu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coviu Trust Center
  slug: coviu-trust-center
  summary_line: ISO 27001, HIPAA, FERPA
slug: coviu
tags:
- Healthcare
- Telehealth
- Australia
- Virtual Care
- Video
- WebRTC
- Appointments
- Remote Monitoring
- REST
website: https://www.coviu.com/
---
