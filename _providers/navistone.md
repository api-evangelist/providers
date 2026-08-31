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
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 20
  name: Navistone Agentic Access
  operation_count: 36
  slug: navistone-agentic-access
  summary_line: 36 operations · 20 acting · 20 human-in-the-loop
api_count: 1
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
- description: Onboard a client, create a direct-mail campaign, add ZIP geo-targeting, and read output.
  name: NaviStone campaign launch
  slug: navistone-campaign-launch
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zazmic Platform API Info API
  slug: open-navistone-api-info-api
- collection_type: open
  name: Zazmic Platform API Info Campaigns API
  slug: open-navistone-campaigns-api
- collection_type: open
  name: Zazmic Platform API Info Clients API
  slug: open-navistone-clients-api
- collection_type: open
  name: Zazmic Platform API Info Domains API
  slug: open-navistone-domains-api
- collection_type: open
  name: Zazmic Platform API Info Geo Targeting API
  slug: open-navistone-geo-targeting-api
- collection_type: open
  name: Zazmic Platform API Info Health API
  slug: open-navistone-health-api
- collection_type: open
  name: Zazmic Platform API Info Output API
  slug: open-navistone-output-api
- collection_type: open
  name: Zazmic Platform API Info Segments API
  slug: open-navistone-segments-api
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/navistone-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/navistone-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/navistone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/navistone-rate-limits.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.navistone.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/navistone
created: '2026-07-17'
description: NaviStone is a direct-mail marketing technology company that turns first-party and "unknown" website audiences into addressable postcard campaigns for consumer brands. Its platform helps businesses prospect (lookalike audiences), retain (mailing customers who opt out of digital channels), and retarget (postcards that amplify campaign performance), claiming up to a 70% increase in return on marketing spend. NaviStone's platform API (implemented on the Zazmic platform and published at docs.navistone.com) manages clients, website domains, audience segments, campaigns tied to Modern Postcard creative IDs, ZIP-code and state geo-targeting, and output tracking, all secured with an X-API-Key header. NaviStone is backed by Bullpen Capital and works with brands including Sleep Number, Vitamix, and Hey Dude across retail, travel, beauty, apparel, and home services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navistone.png
layout: provider
mcp_servers:
- description: ''
  name: NaviStone MCP Server
  slug: navistone-mcp-server
modified: '2026-08-13'
name: NaviStone
nav: Providers
network: true
overview: 'NaviStone publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Info API, Campaigns API, Clients API, and 5 more. Tagged areas include Company, Marketing, Direct Mail, Advertising, and Customer Acquisition.


  NaviStone''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Navistone Plans Pricing
  plan_count: 0
  slug: navistone-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Navistone Rate Limits
  slug: navistone-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 46.1
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/navistone/refs/heads/main/screenshots/navistone-2026-08-07T184732.png
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
