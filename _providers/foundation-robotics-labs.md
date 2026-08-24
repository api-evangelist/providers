---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foundation-robotics-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foundation.bot/
- group: other
  title: ''
  type: Product
  url: https://foundation.bot/phantom
- group: other
  title: ''
  type: Platform
  url: https://foundation.bot/cortex
- group: other
  title: ''
  type: Company
  url: https://foundation.bot/master-plan
- group: other
  title: ''
  type: Culture
  url: https://foundation.bot/culture
- group: company
  title: ''
  type: Careers
  url: https://foundation.bot/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foundationbot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foundation-bot
- group: company
  title: ''
  type: Twitter
  url: https://x.com/foundation_robo
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@foundation_bot
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/foundation-robotics-labs_stock/
coverage:
  checked: '2026-08-16'
  detail: Foundation's entire public presence is a five-page Framer marketing site whose own sitemap.xml lists only /, /cortex, /careers, /master-plan and /culture — /docs, /developers, /api and /llms.txt all 404, api.foundation.bot and docs.foundation.bot are NXDOMAIN, and the first-party GitHub org github.com/foundationbot (verified by @foundation.bot commit-author emails) contains only internal test benches and forks of open-source robotics tooling with no OpenAPI, AsyncAPI, GraphQL SDL or .proto.
  evidence:
  - status: 200
    url: https://foundation.bot/sitemap.xml
  - status: 404
    url: https://foundation.bot/openapi.json
  - status: 404
    url: https://foundation.bot/docs
  - status: 404
    url: https://foundation.bot/llms.txt
  - status: 404
    url: https://foundation.bot/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/repos/foundationbot/general_test_bench/git/trees/main?recursive=1
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: Foundation Robotics Labs — trading publicly as Foundation and incorporated as Foundation Future Industries, Inc. — is a San Francisco humanoid robotics company founded in April 2024 by Sankaet Pathak, Arjun Sethi and Mike LeBlanc. It builds Phantom, a general-purpose humanoid robot aimed at industrial automation, logistics, inspection, disaster response and defense, and Cortex, the company's self-described physics foundation model built on Deep Variational Bayes Filters that pairs physics-informed prediction with vision-language reasoning to drive the robot. The company's published master plan runs from building humanoids through fleet coherence and on to building cities, and it states explicitly that it designs for military environments, unlike U.S. competitors committed to non-weaponization. Foundation has raised a reported $111M and is traded on the secondary market via Forge Global. As of this profile Foundation publishes NO public developer surface — no developer portal,
  documentation, API reference, OpenAPI/AsyncAPI definition, SDK, package, MCP server or agent card. Its entire public web presence is a five-page Framer marketing site (home, Phantom, Cortex, master plan, culture, careers) with no /docs, /developers, /api, /pricing, /terms or /privacy paths and no llms.txt. Its GitHub organization (github.com/foundationbot, verified first-party by @foundation.bot commit-author domains) holds internal test benches and forks of open-source robotics tooling — Drake, jetson-containers, Kalibr, PlotJuggler, Fast-DDS, an EtherCAT master, actuator dyno benches and NXP S32K MCU demos — and contains no API specification of any kind.
image: https://framerusercontent.com/images/vOWp77Vwkl0Uc9IhOzerydxulQ8.png
layout: provider
modified: '2026-08-16'
name: Foundation Robotics Labs
nav: Providers
network: true
overview: 'Foundation Robotics Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Humanoid Robots, Embodied AI, Foundation Models, and Defense.


  Foundation Robotics Labs'' developer surface includes YouTube channel and 11 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Foundation Robotics Labs Domain Security
  slug: foundation-robotics-labs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: foundation-robotics-labs
tags:
- Robotics
- Humanoid Robots
- Embodied AI
- Foundation Models
- Defense
- Industrial Automation
- Logistics
- Hardware
- Phantom
- Cortex
- Autonomous Systems
- San Francisco
website: https://foundation.bot/
---
