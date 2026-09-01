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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Coviu Agentic Access
  operation_count: 21
  slug: coviu-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 1
apis:
- description: In-call Plugin (Apps) API for building custom experiences inside the Coviu video room — adding UI elements, connecting to third-party systems, and enriching the clinical encounter. Documented as a cli
  name: Coviu Plugin API
  slug: coviu-plugin-api
- description: The Auth API from Coviu — 1 operation(s) for auth.
  name: Coviu Auth API
  slug: coviu-auth-api
- description: The Collections API from Coviu — 5 operation(s) for collections.
  name: Coviu Collections API
  slug: coviu-collections-api
- description: The Participants API from Coviu — 2 operation(s) for participants.
  name: Coviu Participants API
  slug: coviu-participants-api
- description: The Sessions API from Coviu — 3 operation(s) for sessions.
  name: Coviu Sessions API
  slug: coviu-sessions-api
- description: The Waiting Area API from Coviu — 3 operation(s) for waiting area.
  name: Coviu Waiting Area API
  slug: coviu-waiting-area-api
- description: The Webhook Requests API from Coviu — 1 operation(s) for webhook requests.
  name: Coviu Webhook Requests API
  slug: coviu-webhook-requests-api
artifact_total: 15
asyncapis:
- description: ''
  name: Coviu Webhooks
  slug: coviu-webhooks
collections:
- collection_type: open
  name: Coviu REST API
  slug: open-coviu-rest-api
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
  name: Coviu MCP Server
  slug: coviu-mcp-server
modified: '2026-07-24'
name: Coviu
nav: Providers
network: true
overview: 'Coviu publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Collections API, Participants API, and 3 more. Tagged areas include Healthcare, Telehealth, Australia, Virtual Care, and Video.


  The Coviu catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coviu''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 26 more developer resources.'
random_paper: 4
scopes:
- name: Coviu Scopes
  scope_count: 0
  slug: coviu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 41.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 50.4
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
    jurisdictions:
    - jurisdiction: US
      standard: ferpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
