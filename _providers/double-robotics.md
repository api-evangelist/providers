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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Local developer API for the Double 3 telepresence robot. Commands and events are exchanged as JSON packets over a standard Unix domain socket with the core D3 system service (Ubuntu 18.04, aarch64). A
  name: Double 3 SDK
  slug: double-3-sdk
- description: REST API for Double fleet management data — robots, users, call logs, and visitor passes. API keys and reference documentation are issued through the Fleet Management account portal.
  name: Fleet REST API
  slug: fleet-rest-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/doublerobotics/d3-sdk/issues
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.doublerobotics.com/developer.html
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/doublerobotics/d3-sdk/blob/master/docs/API.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doublerobotics
- group: start
  title: ''
  type: Login
  url: https://drive.doublerobotics.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doublerobotics.com/privacy.html
- group: build
  title: ''
  type: Packages
  url: packages/double-robotics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/double-robotics-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/double-robotics-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/double-robotics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/double-robotics-llms.txt
created: '2026-07-17'
description: 'Double Robotics builds telepresence robots for hybrid work and education, best known for the self-driving Double 3 videoconferencing robot and the earlier iPad-based Double 2. Its developer program spans three surfaces: the Double 3 SDK (a local command-and-event API exposed over a Unix domain socket on the robot, covering base movement, navigation, PTZ cameras, depth sensors, WebRTC calling, and standby/sidebar apps), iOS SDKs for the Double 2 (Basic Control and Camera Kit), and a Fleet REST API for programmatic access to fleet-management data such as robots, users, call logs, and visitor passes. Added to the API Evangelist network from VC-portfolio discovery and enriched against the company''s public developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/double-robotics.png
layout: provider
modified: '2026-07-18'
name: Double Robotics
nav: Providers
network: true
overview: 'Double Robotics publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telepresence, Robotics, Videoconferencing, and Hybrid Work.


  Double Robotics'' developer surface includes documentation, authentication, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/double-robotics/refs/heads/main/screenshots/double-robotics-2026-07-25T212319.png
security:
- kind: authentication
  name: Double Robotics Authentication
  slug: double-robotics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Double Robotics Domain Security
  slug: double-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: double-robotics
tags:
- Company
- Telepresence
- Robotics
- Videoconferencing
- Hybrid Work
- SDK
- Fleet Management
- Hardware
website: https://www.doublerobotics.com/developer.html
---
