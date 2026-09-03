---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 10.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: OpenID Connect / OAuth 2.0 identity endpoints served from the Vecna Robotics partner portal host (vecnarobotics.my.site.com), a Salesforce Experience Cloud community. The discovery document at /.well-
  name: Vecna Robotics Partner Portal Identity (OpenID Connect)
  slug: partner-portal-identity
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vecna-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vecnarobotics.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vecna-robotics_stock/
- group: company
  title: ''
  type: About
  url: https://www.vecnarobotics.com/company/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.vecnarobotics.com/resource-hub/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vecnarobotics.com/resource-hub/feed/
- group: company
  title: ''
  type: Press
  url: https://www.vecnarobotics.com/news-and-press/
- group: company
  title: ''
  type: PressRSS
  url: https://www.vecnarobotics.com/news-and-press/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.vecnarobotics.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vecnarobotics.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vecnarobotics
- group: company
  title: ''
  type: Careers
  url: https://www.vecnarobotics.com/company/careers/
- group: company
  title: ''
  type: Partners
  url: https://www.vecnarobotics.com/partners/
- group: start
  title: ''
  type: Login
  url: https://vecnarobotics.my.site.com/partner/s/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vecna-robotics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vecna-robotics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vecna-robotics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vecna-robotics-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vecna-robotics-conformance.yml
created: '2026-08-02'
description: Vecna Robotics is a Waltham, Massachusetts material-handling automation company, spun out of Vecna Technologies in 2018, that builds autonomous mobile robots (AMRs) — autonomous forklifts, pallet trucks, tuggers, conveyor and lifter platforms — together with Pivotal, its end-to-end orchestration software suite for warehouse and manufacturing operations. Pivotal spans Orchestration (real-time task allocation and routing), Autonomous Navigation (3D lidar/vision sensor fusion), Insights (analytics and KPI dashboards), Integrations (WMS / MES / ERP, barcode scanning, on-robot and remote tablet UIs, call buttons, smart I/O) and the Pivotal Command Center, a 24/7 human-in-the-loop teleoperation and remote monitoring service. Vecna sells the fleet as Robots-as-a-Service (RaaS) alongside the CaseFlow case-picking solution, and markets "flexible API integrations" into existing WMS/WES environments — but publishes no public developer portal, API reference, or machine-readable API contract
  as of this profiling pass. The only anonymous machine-readable surface found is the OpenID Connect discovery document served by its Salesforce Experience Cloud partner portal.
image: https://www.vecnarobotics.com/wp-content/uploads/2024/02/Vecna_OpenGraph_Fleet@2x.png
layout: provider
modified: '2026-08-02'
name: Vecna Robotics
nav: Providers
network: true
overview: 'Vecna Robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Warehouse Automation, Autonomous Mobile Robots, and Material Handling.


  Vecna Robotics'' developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 11
scopes:
- name: Vecna Robotics Scopes
  scope_count: 36
  slug: vecna-robotics-scopes
  summary_line: 36 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.3
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vecna-robotics/refs/heads/main/screenshots/vecna-robotics-2026-09-02T165537.png
security:
- kind: authentication
  name: Vecna Robotics Authentication
  slug: vecna-robotics-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Vecna Robotics Domain Security
  slug: vecna-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vecna-robotics
tags:
- Company
- Robotics
- Warehouse Automation
- Autonomous Mobile Robots
- Material Handling
- Logistics
- Supply Chain
- Manufacturing
- Industrial Automation
- Robotics as a Service
website: https://www.vecnarobotics.com/
---
