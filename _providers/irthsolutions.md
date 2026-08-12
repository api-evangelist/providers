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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'RESTful Integration API for the Irthnet / UtiliSphere platform. Secured with a per-integration API key, it lets external systems create and modify users, create and modify map layers, and manage work '
  name: Irth Integration API
  slug: irth-integration-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/irthsolutions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/irthsolutions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://irthsolutions.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.irth.com/Irthnet/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.irth.com/Irthnet/docs/api
- group: operate
  title: ''
  type: Support
  url: https://irthsupport.irthsolutions.com/support/home
- group: start
  title: ''
  type: Login
  url: https://irth.com/Irthnet/Logon.aspx
- group: company
  title: ''
  type: Blog
  url: https://irthsolutions.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://irthsolutions.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://irthsolutions.com/privacy-policy
created: '2026-07-17'
description: Irth Solutions is a SaaS platform provider for critical-infrastructure damage prevention, asset (pipeline) integrity, and stakeholder land management, trusted by energy, utility, and telecom operators across the U.S. and Canada since 1995. Its products include 811 ticket management (UtiliSphere, Exactix, and 811spotter for contractors), one-call center notification, intelligent forms and workflows, inline-inspection and corrosion/crack asset-integrity analytics, and lease, royalty, and right-of-way land management, powered by business intelligence, analytics, and geospatial data. Irth exposes a RESTful Integration API (Irthnet / UtiliSphere) secured with a per-integration API key for creating and modifying users, map layers, and work items in real time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/irthsolutions.png
layout: provider
modified: '2026-07-19'
name: Irth Solutions
nav: Providers
network: true
overview: 'Irth Solutions publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Damage Prevention, 811 Ticket Management, Utility Locating, and Pipeline Integrity.


  Irth Solutions'' developer surface includes authentication, documentation, API reference, support, engineering blog, and 5 more developer resources.'
random_paper: 55
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/irthsolutions/refs/heads/main/screenshots/irthsolutions-2026-07-25T222928.png
security:
- kind: authentication
  name: Irthsolutions Authentication
  slug: irthsolutions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Irthsolutions Domain Security
  slug: irthsolutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: irthsolutions
tags:
- Company
- Damage Prevention
- 811 Ticket Management
- Utility Locating
- Pipeline Integrity
- Land Management
- Geospatial
- SaaS
- Energy
- Utilities
- Telecom
website: https://irthsolutions.com
---
