---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'Token-based REST API for managing first-party data, building and editing audience segments, activating audiences, and retrieving behavior and audience analytics on the Lotame Spherical platform. JSON '
  name: Lotame Admin Services API
  slug: lotame-admin-services-api
- description: 'Real-time server-side API that returns the assigned Panorama ID for an IP address and user-agent (web) or Mobile Advertiser ID / MAID (mobile app). JSON POST to sid.crwdcntrl.net/sid, identified by a '
  name: Panorama ID Server-Side API
  slug: panorama-id-server-side-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.lotame.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.lotame.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.lotame.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://my.lotame.com/category/administrative-api
- group: operate
  title: ''
  type: Support
  url: https://www.cognitoforms.com/LotameSolutionsInc/SupportTicketForm
- group: start
  title: ''
  type: SignUp
  url: https://my.lotame.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.lotame.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lotame.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lotame.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lotame.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/lotame-solutions-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lotame-solutions-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lotame-solutions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lotame-solutions-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lotame-solutions-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lotame-solutions-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lotame-solutions-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lotame-solutions-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lotame-solutions-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lotame-solutions-packages.yml
- group: design
  title: ''
  type: Components
  url: components/lotame-solutions-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lotame-solutions-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lotame-solutions-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lotame-solutions-rate-limits.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lotame.com/legal/eu-privacy-consent-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lotame
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Lotame/api-examples
created: '2026-07-17'
description: Lotame Solutions is a data collaboration and identity company for digital marketing and advertising. Its Spherical platform lets marketers, agencies, and publishers connect, enrich, and activate first- and third-party audience data, while Panorama ID delivers a privacy-first, cookieless identity for addressability across web, mobile app, and CTV. Lotame exposes a token-based Admin Services REST API (api.lotame.com/2/) for managing first-party data, building audiences, and pulling behavior and audience statistics, plus a server-side Panorama ID resolution API on sid.crwdcntrl.net for web and mobile (MAID) identity lookups. Lotame operates across 24 countries and was acquired by Publicis Groupe.
image: https://cdn-ilbibgp.nitrocdn.com/eakWUVxgVLoymIJUurpQZcwTweYHDeju/assets/images/optimized/rev-6d2d189/www.lotame.com/wp-content/uploads/2025/05/lotame-website-favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: Lotame Solutions MCP Server (candidate)
  slug: lotame-solutions-mcp-server-candidate
modified: '2026-08-13'
name: Lotame Solutions
nav: Providers
network: true
overview: 'Lotame Solutions publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Management Platform, Identity, Advertising, and Marketing.


  Lotame Solutions'' developer surface includes documentation, API reference, support, signup flow, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Lotame Solutions Plans Pricing
  plan_count: 0
  slug: lotame-solutions-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Lotame Solutions Rate Limits
  slug: lotame-solutions-rate-limits
score:
  band: thin
  composite: 26.7
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lotame-solutions/refs/heads/main/screenshots/lotame-solutions-2026-07-25T225550.png
security:
- kind: authentication
  name: Lotame Solutions Authentication
  slug: lotame-solutions-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lotame Solutions Domain Security
  slug: lotame-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lotame-solutions
tags:
- Company
- Data Management Platform
- Identity
- Advertising
- Marketing
- Audience Data
- Data Collaboration
- AdTech
website: https://www.lotame.com/
---
