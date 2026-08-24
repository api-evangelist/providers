---
access_model:
  confidence: medium
  label: Documented, account-gated
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://console.springserve.com/api-docs
  - https://springserve.atlassian.net/wiki/spaces/SSD/pages/1573617663/API+-+Getting+Started
  trial: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 349
  human_in_the_loop: 1
  name: Rubicon Project Agentic Access
  operation_count: 668
  slug: rubicon-project-agentic-access
  summary_line: 668 operations · 349 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The v1 REST API for SpringServe, Magnite's ad-serving and CTV/streaming ad-server platform. 379 operations across 295 paths and 53 tags, covering supply tags, demand tags, supply routers, creatives (v
  name: SpringServe UI API (v1)
  slug: rubicon-project-springserve-v1-api
- description: 'The original v0 REST API for SpringServe, still fully supported and documented alongside v1 while Magnite builds v1 equivalents for every endpoint. 289 operations across 173 paths covering campaigns, '
  name: SpringServe UI API (v0)
  slug: rubicon-project-springserve-v0-api
- description: 'ClearLine is Magnite''s direct buy-side activation platform for advertisers and agencies, running on the same SpringServe codebase and serving the identical OpenAPI 3.1.2 contract from its own console '
  name: ClearLine API
  slug: rubicon-project-clearline-api
- description: 'Magnite''s Exchange API (xAPI) protobuf extensions to the IAB OpenRTB 2.x protobuf definitions, published in the open on GitHub. Defines Magnite-specific OpenRTB extension fields (extension IDs in the '
  name: Magnite Exchange API (xAPI) OpenRTB Extensions
  slug: rubicon-project-openrtb-xapi
artifact_total: 13
collections:
- collection_type: open
  name: SpringServe UI API (V0)
  slug: open-rubicon-project-springserve-v0
- collection_type: open
  name: SpringServe UI API
  slug: open-rubicon-project-springserve-v1
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rubicon-project-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.magnite.com
- group: company
  title: ''
  type: Blog
  url: https://www.magnite.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.magnite.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.magnite.com/help
- group: docs
  title: ''
  type: Documentation
  url: https://springserve.atlassian.net/wiki/spaces/SSD/pages/1584726013/SpringServe+API+SDK
- group: docs
  title: ''
  type: APIReference
  url: https://console.springserve.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://springserve.atlassian.net/wiki/spaces/SSD/pages/1573617663/API+-+Getting+Started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MagniteEngineering
- group: start
  title: ''
  type: Login
  url: https://console.springserve.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/rubicon-project-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.magnite.com/trust-center/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.magnite.com/legal/magnite-website-privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.magnite.com/legal/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rubicon-project-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rubicon-project-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/rubicon-project-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rubicon-project-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rubicon-project-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rubicon-project-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rubicon-project-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rubicon-project-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rubicon-project-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rubicon-project-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rubicon-project-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rubicon-project-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rubicon-project-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/rubicon-project-request-examples.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://springserve.atlassian.net/wiki/spaces/SSD/overview
created: '2026-07-17'
description: Rubicon Project is a Los Angeles-based advertising technology company, founded in 2007, that built and operated one of the largest real-time bidding advertising exchanges, connecting digital publishers (the sell side) with advertisers and demand-side platforms. In 2020 Rubicon Project merged with Telaria and rebranded as Magnite, now positioned as the world's largest independent sell-side (SSP) advertising company, spanning connected TV (CTV), online video, display, and audio across its DV+, SpringServe, ClearLine and Magnite Streaming platforms. This profile tracks the company as it exists today under the Magnite brand. Magnite publishes a public, machine-readable OpenAPI 3.1 contract for the SpringServe ad-serving platform (v1 and v0) at console.springserve.com/api-docs, mirrored for the ClearLine buy-side console at console.clearline.magnite.com, together with a public Confluence documentation space, published rate limits, a first-party Python SDK, mobile In-App Ads SDKs
  for iOS and Android, and OpenRTB protobuf extensions. Account creation and API credentials remain partner-gated; the contract itself is anonymously readable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rubicon-project.png
layout: provider
mcp_servers:
- description: ''
  name: Rubicon Project MCP Server
  slug: rubicon-project-mcp-server
modified: '2026-08-12'
name: Rubicon Project
nav: Providers
network: true
overview: 'Rubicon Project publishes 3 APIs on the [APIs.io](https://apis.io/) network: SpringServe UI API (v1), SpringServe UI API (v0), and ClearLine API. Tagged areas include Company, Advertising, AdTech, Programmatic Advertising, and Sell-Side Platform.


  Rubicon Project''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, legal docs, authentication, and 23 more developer resources.'
plans:
- name: Rubicon Project Plans Pricing
  plan_count: 0
  slug: rubicon-project-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Rubicon Project Rate Limits
  slug: rubicon-project-rate-limits
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 16.7
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rubicon-project/refs/heads/main/screenshots/rubicon-project-2026-08-17T081658.png
security:
- kind: authentication
  name: Rubicon Project Authentication
  slug: rubicon-project-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Rubicon Project Domain Security
  slug: rubicon-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rubicon Project Trust Center
  slug: rubicon-project-trust-center
  summary_line: SOC 2 Type I, SOC 1 Type II
slug: rubicon-project
tags:
- Company
- Advertising
- AdTech
- Programmatic Advertising
- Sell-Side Platform
- SSP
- Real-Time Bidding
- Connected TV
- Ad Serving
- Media
- OpenRTB
- Reporting
website: https://www.magnite.com
---
