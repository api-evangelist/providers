---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Mavenir Agentic Access
  operation_count: 8
  slug: mavenir-agentic-access
  summary_line: 8 operations · 7 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The TM Forum Open APIs implemented in Mavenir's cloud-native Digital Enablement (MDE) BSS, converged charging and digital marketplace platform. Mavenir holds TM Forum Open API Conformance certificatio
  name: Mavenir Digital Enablement (MDE) TM Forum Open APIs
  slug: mavenir-digital-enablement-tm-forum-open-apis
- baseURL_template: '{apiRoot}/vvoip/{apiVersion}/{userId}'
  baseurl_source: spec_template
  description: APIs related to 1-1 voice/video call session
  name: Mavenir One To One Call API
  slug: mavenir-onetoonecall-api
- baseURL_template: '{apiRoot}/racm/{apiVersion}/{userId}'
  baseurl_source: spec_template
  description: The Push Token API from Mavenir — 1 operation(s) for push token.
  name: Mavenir Push Token API
  slug: mavenir-push-token-api
- baseURL_template: '{apiRoot}/racm/{apiVersion}/{userId}'
  baseurl_source: spec_template
  description: The RACM API from Mavenir — 2 operation(s) for racm.
  name: Mavenir RACM API
  slug: mavenir-racm-api
arazzos:
- description: Originate a one-to-one voice/video session on a Mavenir BYON call handling deployment, read it back, drive it to Connected, then terminate it. Every operationId is verified against openapi/mavenir-byo
  name: Place and manage a 1-1 VVoIP call (Mavenir BYON)
  slug: mavenir-byon-place-and-manage-call
artifact_total: 11
asyncapis:
- description: ''
  name: Mavenir Byon Events
  slug: mavenir-byon-events
collections:
- collection_type: open
  name: Bring Your Own Number (BYON) call handling API (VVOIP Service)
  slug: open-mavenir-byon-call-handling
- collection_type: open
  name: Bring Your Own Number (BYON) Registration and Connectivity Management (RACM) Service APIs
  slug: open-mavenir-byon-racm
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mavenir-byon-call-handling-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mavenir-byon-racm-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mavenir-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mavenir-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mavenir-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mavenir-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mavenir-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mavenir-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mavenir-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mavenir-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mavenir-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mavenir-byon-events.yml
- group: build
  title: ''
  type: Packages
  url: packages/mavenir-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mavenir-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mavenir-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mavenir-byon-place-and-manage-call.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mavenir-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.mavenir.com/
- group: company
  title: ''
  type: About
  url: https://www.mavenir.com/about/
- group: other
  title: ''
  type: Portfolio
  url: https://www.mavenir.com/portfolio/mavapps/
- group: company
  title: ''
  type: Newsroom
  url: https://www.mavenir.com/newsroom/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.mavenir.com/press-releases/
- group: operate
  title: ''
  type: Contact
  url: https://www.mavenir.com/contact-us/
- group: start
  title: ''
  type: SupportPortal
  url: https://support.mavenir.com/
- group: operate
  title: ''
  type: Support
  url: https://support.mavenir.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mavenir.com/newsroom/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mavenir.com/newsroom/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mavenir
- group: commercial
  title: ''
  type: Privacy
  url: https://www.mavenir.com/data-privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mavenir.com/terms-use/
- group: auth
  title: ''
  type: Compliance
  url: https://www.mavenir.com/regulatory-compliance/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mavenir
- group: other
  title: ''
  type: Standards
  url: https://github.com/camaraproject/WebRTC
- group: other
  title: ''
  type: Standards
  url: https://github.com/camaraproject/Governance/blob/main/PARTICIPANTS.MD
created: '2026-07-25'
description: 'Mavenir is a US-headquartered (Richardson, Texas) cloud-native telecom network software vendor that builds the software operators run rather than a network or a developer platform of its own. Its portfolio spans Open RAN and vRAN (MAVair), converged packet core and cloud-native IMS (MAVcore), messaging, fraud and security applications, the Mavenir Digital Enablement (MDE) BSS and converged charging stack (MAVapps), private networks, MEC and an Intelligent IoT Platform (MAVedge). In the telecom value chain Mavenir sits upstream of the carrier — it supplies the Combo NEF/SCEF network-exposure function and the BSS that a mobile operator uses to expose and monetize CAMARA and GSMA Open Gateway network APIs, but it does not expose those APIs to developers itself. Its API posture is accordingly partner-gated and sales-led: there is no developer portal at any developer/docs/api subdomain, no self-serve signup, no sandbox, and no downloadable specification on mavenir.com; the only
  login-bearing surface, support.mavenir.com, is an ADFS-protected customer support wall. What Mavenir does publish is standards work — it is an active CAMARA participant with eleven named individuals in CAMARA governance, is listed in the CAMARA landscape as a Network Capability Solution Provider, co-maintains the camaraproject/WebRTC sandbox API repository (two of the four CODEOWNERS are Mavenir engineers), contributed its own Bring Your Own Number (BYON) OpenAPI definitions to the CAMARA API Backlog, and holds TM Forum Open API Platinum conformance with 20+ certified Open APIs on the MDE BSS platform. Developers reach Mavenir-powered capability only through a carrier or through a channel partner such as Spry Fox Networks, never directly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Mavenir
nav: Providers
network: true
overview: 'Mavenir publishes 3 APIs on the [APIs.io](https://apis.io/) network: One To One Call API, Push Token API, and RACM API. Tagged areas include Telecommunications, United States, Network Vendor, Network APIs, and CAMARA.


  The Mavenir catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mavenir''s developer surface includes authentication, support, engineering blog, privacy policy, and 31 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 57.9
    developer_ergonomics: 32.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mavenir/refs/heads/main/screenshots/mavenir-2026-08-07T172126.png
security:
- kind: authentication
  name: Mavenir Authentication
  slug: mavenir-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mavenir Domain Security
  slug: mavenir-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mavenir
tags:
- Telecommunications
- United States
- Network Vendor
- Network APIs
- CAMARA
- Open Gateway
- BSS
- OSS
- TM Forum
- Open RAN
- 5G
- IMS
- Messaging
- Network Exposure Function
- Standards
website: https://www.mavenir.com/
---
