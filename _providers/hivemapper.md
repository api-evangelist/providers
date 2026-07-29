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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Devices, calibration, and query history.
  name: Hivemapper Account API
  slug: hivemapper-account-api
- description: AI-detected driving event videos with synchronized sensor data.
  name: Hivemapper AI Events API
  slug: hivemapper-ai-events-api
- description: On-demand incentivized mapping requests.
  name: Hivemapper Bursts API
  slug: hivemapper-bursts-api
- description: Street-level dashcam imagery queries.
  name: Hivemapper Imagery API
  slug: hivemapper-imagery-api
- description: ML-detected road objects and features.
  name: Hivemapper Map Features API
  slug: hivemapper-map-features-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hivemapper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hivemapper.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://beemaps.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beemaps.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beemaps.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beemaps.com/platform/road-intelligence-api
- group: commercial
  title: ''
  type: Pricing
  url: https://beemaps.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://beemaps.com/login
- group: company
  title: ''
  type: Blog
  url: https://beemaps.com/blog
- group: operate
  title: ''
  type: Support
  url: https://beemaps.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hivemapper.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hivemapper.com/privacy/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hivemapper
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hivemapper-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/hivemapper-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hivemapper-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hivemapper-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hivemapper-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hivemapper-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hivemapper-well-known.yml
- group: other
  title: ''
  type: X
  url: https://x.com/TryBeeMaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bee-maps
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/FRWMKyy5v2
created: '2026-07-17'
description: Hivemapper (Bee Maps) is a decentralized mapping network that turns a planetary-scale fleet of purpose-built "Bee" dashcams into fresh, structured, queryable street-level data. Contributors passively collect imagery while driving and earn HONEY tokens on Solana; the data is processed through on-device and cloud ML pipelines and delivered to developers as REST APIs. The Bee Maps Developer API offers a Street-Level Imagery API, a Map Features API (ML-detected signs, hydrants, lane lines and more), an AI Event Videos API (harsh braking, swerving, violations with synchronized sensor data), and Burst on-demand mapping, plus Edge AI for deploying custom ML workloads to cameras. Enterprise customers include HERE Technologies, Lyft, Mapbox, and Volkswagen. Billing is consumption-based (API credits plus per-view metering).
image: https://hivemapper.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: hivemapper-mcp.yml
  slug: hivemapper-mcpyml
modified: '2026-07-19'
name: Hivemapper
nav: Providers
network: true
overview: 'Hivemapper publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, AI Events API, Bursts API, and 2 more. Tagged areas include Company, Logistics, Mapping, Geospatial, and Imagery.


  Hivemapper''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 17 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 50.0
  delta: 0.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.9
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 49.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hivemapper/refs/heads/main/screenshots/hivemapper-2026-07-25T221306.png
security:
- kind: authentication
  name: Hivemapper Authentication
  slug: hivemapper-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Hivemapper Domain Security
  slug: hivemapper-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: hivemapper
tags:
- Company
- Logistics
- Mapping
- Geospatial
- Imagery
- Location
- Street View
- Mobility
- Machine Learning
- Web3
website: https://hivemapper.com
---
