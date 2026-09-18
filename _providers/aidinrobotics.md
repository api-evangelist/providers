---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: An anonymous remote Model Context Protocol endpoint served on AIDIN ROBOTICS' own host and advertised in the company's own /llms.txt under an "AI 에이전트 액세스" section. An unauthenticated JSON-RPC initial
  name: AIDIN ROBOTICS Site MCP
  slug: site-mcp
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/security/aidinrobotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidinrobotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aidinrobotics.co.kr/en
- group: company
  title: ''
  type: About
  url: https://www.aidinrobotics.co.kr/en/about
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/aidinrobotics/aidin-hand2-sdk#documentation
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/aidinrobotics/aidin-hand2-sdk/blob/main/docs/en/08_cpp_api_reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/aidinrobotics/aidin-hand2-sdk/blob/main/docs/en/06_sdk_build_and_install.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aidinrobotics
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aidinrobotics/aidin-hand2-sdk
- group: operate
  title: ''
  type: Support
  url: https://help.aidinrobotics.co.kr/
- group: operate
  title: ''
  type: FAQ
  url: https://www.aidinrobotics.co.kr/en/faq
- group: company
  title: ''
  type: Blog
  url: https://www.aidinrobotics.co.kr/en/knowledgeblog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aidinrobotics.co.kr/blog-feed.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aidinrobotics.co.kr/en/news
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.aidinrobotics.co.kr/
- group: operate
  title: ''
  type: Contact
  url: https://www.aidinrobotics.co.kr/en/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aidinrobotics.co.kr/en/privacypolicy
- group: auth
  title: ''
  type: Compliance
  url: https://www.aidinrobotics.co.kr/en/certification
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/llms/aidinrobotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidinrobotics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/mcp/aidinrobotics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aidinrobotics-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/packages/aidinrobotics-packages.yml
  title: ''
  type: Packages
  url: packages/aidinrobotics-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/packages/aidinrobotics-packages.yml
  title: ''
  type: SDKs
  url: packages/aidinrobotics-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/changelog/aidinrobotics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aidinrobotics-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/errors/aidinrobotics-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/aidinrobotics-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/lifecycle/aidinrobotics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aidinrobotics-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/conventions/aidinrobotics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aidinrobotics-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/conformance/aidinrobotics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidinrobotics-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/authentication/aidinrobotics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aidinrobotics-authentication.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/plans/aidinrobotics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidinrobotics-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aidinrobotics/refs/heads/main/rate-limits/aidinrobotics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aidinrobotics-rate-limits.yml
created: '2026-09-14'
description: 'AIDIN ROBOTICS Inc. (에이딘로보틱스) is a South Korean robot-sensor company founded in 2019 out of the Robotics Innovatory lab in the Department of Mechanical Engineering at Sungkyunkwan University, and headquartered in Anyang, Gyeonggi-do. It builds the force-sensing layer that sits between a robot and the physical world: six-axis force/torque sensors (AFT200 series), miniature and three-axis F/T sensors, ultra-thin joint torque sensors (ATS/ATSB series), proximity and tactile safety sensors, the Susgrip smart gripper, the AIDIN Hand Gen2 robot hand, the ARC robot motion controller, and the AIDIN9 quadruped platform. Sensors ship in EtherCAT, EtherNet/IP, CAN and RS-485 variants and carry ISO 9001, CE, KC, FCC and RoHS marks. AIDIN ROBOTICS runs no web API product and publishes no OpenAPI, GraphQL, AsyncAPI, gRPC or SOAP contract. Its real developer surface is device-side and first-party: the Apache-2.0 AIDIN Hand Gen2 SDK on GitHub — a C++ library speaking CAN-FD over Linux SocketCAN
  with a CiA 402 drive state machine, a documented error catalog, a Keep a Changelog history and semantic versioning — plus an older ROS package for reading the AFT force/torque sensor over RS-485. Alongside that, the company''s Wix-hosted marketing site serves a company-authored llms.txt and an anonymous remote Model Context Protocol endpoint, which is the only network-callable API surface it publishes.'
image: https://static.wixstatic.com/media/d71e42_e1d5db6bf45d40c484b0c0ff01481556%7Emv2.png/v1/fit/w_2500,h_1330,al_c/d71e42_e1d5db6bf45d40c484b0c0ff01481556%7Emv2.png
layout: provider
mcp_servers:
- description: AIDIN ROBOTICS serves a live, unauthenticated remote MCP endpoint at https://www.aidinrobotics.co.kr/_api/mcp, advertised in the company's own /llms.txt under an "AI 에이전트 액세스" (AI agent access) sectio
  name: AIDIN ROBOTICS Site MCP manifest
  slug: aidin-robotics-site-mcp-manifest
modified: '2026-09-14'
name: AIDIN ROBOTICS
nav: Providers
network: true
overview: 'AIDIN ROBOTICS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Sensors, Hardware, Industrial Automation, and Manufacturing.


  AIDIN ROBOTICS''s developer surface includes documentation, API reference, getting-started guide, support, FAQ, engineering blog, changelog, and 22 more developer resources.'
plans:
- name: Aidinrobotics Plans Pricing
  plan_count: 0
  slug: aidinrobotics-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Aidinrobotics Rate Limits
  slug: aidinrobotics-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 27.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aidinrobotics Authentication
  slug: aidinrobotics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aidinrobotics Domain Security
  slug: aidinrobotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aidinrobotics
tags:
- Robotics
- Sensors
- Hardware
- Industrial Automation
- Manufacturing
- Force and Torque Sensing
- Cobots
- Humanoid Robotics
- ROS
- SDK
- Company
website: https://www.aidinrobotics.co.kr/en
---
