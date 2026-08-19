---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Publisher-facing reporting API for the Domob mobile advertising platform. A single POST operation returns delivery and revenue statistics — ad requests, bids, impressions, clicks, CPM and media billin
  name: Domob Media Data API
  slug: domob-media-data-api
- description: Domob's mobile ad exchange, supporting RTB, PMP, PD and PDB buying. Listed on the Domob developer platform's API docking page with a docking document updated 2025-06-13, but that document is hosted on
  name: Domob ADX
  slug: domob-adx
artifact_total: 8
collections:
- collection_type: open
  name: Domob Media Data API
  slug: open-domob-media-data-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.domob.cn
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.domob.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.domob.cn/help/techdocument.htm
- group: docs
  title: ''
  type: APIReference
  url: https://developer.domob.cn/#/doc/api
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.domob.cn/help/index.htm?t=tab0
- group: operate
  title: ''
  type: Support
  url: https://www.domob.cn/aboutUs/contact
- group: company
  title: ''
  type: Blog
  url: https://www.domob.cn/blog
- group: start
  title: ''
  type: SignUp
  url: https://developer.domob.cn/#/signup
- group: start
  title: ''
  type: Login
  url: https://developer.domob.cn/#/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Domob-SDK
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/domob-inc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.domob.cn/help/rule.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domob.cn/article?id=advertiserPlatformPrivacyPolicy
- group: build
  title: ''
  type: Packages
  url: packages/domob-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/domob-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/domob-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/domob-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/domob-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/domob-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/domob-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/domob-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/domob-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/domob-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/domob-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/domob-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/domob-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/domob-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/domob-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domob-domain-security.yml
created: '2026-07-17'
description: 'Domob (多盟) is a Beijing-based mobile intelligent marketing and advertising technology company founded in September 2010, positioned as one of China''s early smartphone advertising DSP and mobile ad-network platforms. It provides data-technology and content services spanning programmatic buying (DSP), the UGdesk user-growth platform, the BidMaster preferred buying platform, and the BlueNova traffic-monetization platform, alongside agency and short-video services partnered with ByteDance, Tencent, Kuaishou, Microsoft Advertising and Xiaohongshu. For developers and app publishers, Domob distributes first-party iOS and Android ad SDKs (banner, interstitial, splash, native and offerwall formats) plus Unity3D and Cocos2d-x game-engine plugins via its Domob-SDK and domob-inc GitHub accounts; publishers obtain a Publisher ID and Placement ID from the Domob platform to monetize apps. Its public API surface is narrow: one documented and live publisher reporting operation (the Media Data
  API on developer.domob.cn), an ad exchange at adx.domob.cn whose docking document sits behind a BlueFocus Feishu login, an undocumented "Domob Open API" gateway at open.domob.cn, and a retired Reporting API whose documentation is still published even though its host no longer resolves. No machine-readable specification is published on any host. In 2025 the Domob SDK passed CAICT dual-end (iOS/Android) security certification. This profile was surfaced as a portfolio company of Qiming Venture Partners and enriched from public sources.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domob.png
layout: provider
mcp_servers:
- description: ''
  name: domob-mcp.yml
  slug: domob-mcpyml
modified: '2026-08-12'
name: domob
nav: Providers
network: true
overview: 'domob publishes 1 API on the [APIs.io](https://apis.io/) network: Media Data API. Tagged areas include Company, Advertising, Mobile, AdTech, and Marketing.


  domob''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Domob Plans Pricing
  plan_count: 0
  slug: domob-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 0
  name: Domob Rate Limits
  slug: domob-rate-limits
score:
  band: developing
  composite: 48.1
  delta: -0.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 12.1
    contract_quality: 60.8
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 12.1
    operational_transparency: 18.4
  previous_composite: 49.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domob/refs/heads/main/screenshots/domob-2026-07-25T212250.png
security:
- kind: authentication
  name: Domob Authentication
  slug: domob-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Domob Domain Security
  slug: domob-domain-security
  summary_line: TLSv1.2 · HSTS
slug: domob
tags:
- Company
- Advertising
- Mobile
- AdTech
- Marketing
- SDK
- DSP
- Monetization
- Reporting
- China
website: https://www.domob.cn
---
