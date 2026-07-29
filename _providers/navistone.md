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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 20
  name: Navistone Agentic Access
  operation_count: 36
  slug: navistone-agentic-access
  summary_line: 36 operations · 20 acting · 20 human-in-the-loop
api_count: 8
apis:
- description: API information and endpoints
  name: NaviStone API Info API
  slug: navistone-api-info-api
- description: Campaign management
  name: NaviStone Campaigns API
  slug: navistone-campaigns-api
- description: Client management
  name: NaviStone Clients API
  slug: navistone-clients-api
- description: Domain management
  name: NaviStone Domains API
  slug: navistone-domains-api
- description: Geographic targeting
  name: NaviStone Geo Targeting API
  slug: navistone-geo-targeting-api
- description: Health checks
  name: NaviStone Health API
  slug: navistone-health-api
- description: Output tracking
  name: NaviStone Output API
  slug: navistone-output-api
- description: Audience segments
  name: NaviStone Segments API
  slug: navistone-segments-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Onboard a client, create a direct-mail campaign, add ZIP geo-targeting, and read output.
  name: NaviStone campaign launch
  slug: navistone-campaign-launch
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/navistone-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.navistone.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.navistone.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.navistone.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.navistone.com
- group: company
  title: ''
  type: Blog
  url: https://www.navistone.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.navistone.com/get-started
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.navistone.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/navistone-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navistone-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/navistone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/navistone-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/navistone-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/navistone-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/navistone-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/navistone-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/navistone-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/navistone-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/navistone-campaign-launch.yml
created: '2026-07-17'
description: NaviStone is a direct-mail marketing technology company that turns first-party and "unknown" website audiences into addressable postcard campaigns for consumer brands. Its platform helps businesses prospect (lookalike audiences), retain (mailing customers who opt out of digital channels), and retarget (postcards that amplify campaign performance), claiming up to a 70% increase in return on marketing spend. NaviStone's platform API (implemented on the Zazmic platform and published at docs.navistone.com) manages clients, website domains, audience segments, campaigns tied to Modern Postcard creative IDs, ZIP-code and state geo-targeting, and output tracking, all secured with an X-API-Key header. NaviStone is backed by Bullpen Capital and works with brands including Sleep Number, Vitamix, and Hey Dude across retail, travel, beauty, apparel, and home services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navistone.png
layout: provider
mcp_servers:
- description: ''
  name: navistone-mcp.yml
  slug: navistone-mcpyml
modified: '2026-07-20'
name: NaviStone
nav: Providers
network: true
overview: 'NaviStone publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Info API, Campaigns API, Clients API, and 5 more. Tagged areas include Company, Marketing, Direct Mail, Advertising, and Customer Acquisition.


  NaviStone''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 33.4
  delta: -3.8
  facets:
    commercial_clarity: 23.7
    contract_quality: 43.9
    developer_ergonomics: 40.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Navistone Authentication
  slug: navistone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Navistone Domain Security
  slug: navistone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: navistone
tags:
- Company
- Marketing
- Direct Mail
- Advertising
- Customer Acquisition
- Audience Targeting
- MarTech
- AdTech
- Postcards
- Retargeting
website: https://www.navistone.com
---
