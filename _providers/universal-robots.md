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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 0.0
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: Real-Time Data Exchange is Universal Robots' synchronous binary TCP protocol on port 30004 that lets external applications stream robot state at the controller's 500 Hz cycle (e-Series) or 125 Hz cycl
  name: Universal Robots Real-Time Data Exchange (RTDE)
  slug: rtde
- description: Plain-text TCP command interface on port 29999 used to power on/off the robot, load and play programs, query safety state, and manage installations. Dashboard Server is the easiest remote-control entr
  name: Universal Robots Dashboard Server
  slug: dashboard-server
- description: Streaming binary interface on ports 30001 (Primary, 10 Hz) and 30002 (Secondary, 10 Hz) that emits robot state and configuration messages and accepts URScript programs and commands. The Primary interf
  name: Universal Robots Primary and Secondary Client Interface
  slug: primary-secondary-client-interface
- description: URScript is Universal Robots' purpose-built scripting language for cobot motion, I/O, and process control. URScript programs can be authored in PolyScope, streamed over the Secondary Client Interface,
  name: URScript
  slug: urscript
- description: The URCap SDK is the Java-based extension framework for PolyScope 5 that powers Universal Robots' UR+ ecosystem. URCaps add program nodes, installation screens, daemons, and driver contributions (grip
  name: URCap SDK (PolyScope 5)
  slug: urcap-sdk
- description: The PolyScope X URCap SDK is the TypeScript/HTML extension framework for Universal Robots' next-generation PolyScope X teach-pendant operating system that ships on UR15/UR20/UR30 and newer cobots. Pol
  name: PolyScope X URCap SDK
  slug: polyscopex-urcap-sdk
- description: Binary state interface on port 30003 emitting robot state at the 125 Hz / 500 Hz controller cycle. Predates RTDE and is still supported for low-latency one-way state streaming; new integrations should
  name: Universal Robots Real-Time Interface
  slug: realtime-interface
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universal-robots-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.universal-robots.com/
- group: other
  title: ''
  type: DeveloperSuite
  url: https://www.universal-robots.com/products/ur-developer-suite/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.universal-robots.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversalRobots
- group: operate
  title: ''
  type: Forums
  url: https://forum.universal-robots.com/
- group: other
  title: ''
  type: Marketplace
  url: https://www.universal-robots.com/plus/
- group: learn
  title: ''
  type: Academy
  url: https://academy.universal-robots.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://partners.universal-robots.com/
- group: operate
  title: ''
  type: Support
  url: https://www.universal-robots.com/support/
- group: other
  title: ''
  type: Downloads
  url: https://www.universal-robots.com/download/
- group: other
  title: ''
  type: Products
  url: https://www.universal-robots.com/products/
- group: company
  title: ''
  type: About
  url: https://www.universal-robots.com/about-universal-robots/
- group: company
  title: ''
  type: Newsroom
  url: https://www.universal-robots.com/news-centre/
- group: company
  title: ''
  type: Careers
  url: https://www.universal-robots.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.universal-robots.com/contact/
- group: other
  title: ''
  type: Parent
  url: https://www.teradyne.com/
- group: other
  title: ''
  type: Sibling
  url: https://www.mobile-industrial-robots.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/universal-robots/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/UniversalRobots
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/universal_robot
created: '2026-05-25'
description: 'Universal Robots is a Danish collaborative-robot (cobot) manufacturer headquartered in Odense, Denmark, founded in 2005 by Esben Østergaard, Kasper Støy, and Kristian Kassow, and acquired by Teradyne in 2015 for USD 285 million. Universal Robots is the market leader in cobots, with more than 100,000 units sold worldwide and a 40–50% share of the global collaborative-robot market. The company ships two product generations — the e-Series (UR3e, UR7e, UR12e, UR16e) and the newer high-payload UR series (UR8 Long, UR15, UR18, UR20, UR30) — running the PolyScope 5 teach-pendant software stack and the next-generation PolyScope X platform. Universal Robots is unusual among industrial-robot vendors in publishing an extensive open developer surface: the C++ Universal_Robots_Client_Library, the Universal_Robots_ROS_Driver and Universal_Robots_ROS2_Driver, the RTDE Python Client Library, the Universal_Robots_Isaac_Driver for NVIDIA Isaac, the URCap SDK (PolyScope 5 Java) and PolyScopeX
  URCap SDK (TypeScript/HTML), and the URScript language. The wire-level protocols — Real-Time Data Exchange (RTDE), Dashboard Server, Primary/Secondary Client Interface, Reverse/Trajectory interfaces, XML-RPC, and the Tool Communication forwarder — are all documented and externally addressable over TCP, making UR cobots first-class citizens in third-party automation stacks, ROS/ROS 2, MoveIt, Isaac Sim, and the UR+ ecosystem (500+ certified end-effectors, vision systems, and URCap software extensions on universal-robots.com/plus). Universal Robots does not publish a public HTTP/REST API or OpenAPI specification — all programmatic access is via the documented socket protocols and SDKs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universal-robots.png
jsonld:
- class_count: 6
  name: Universal Robots Context
  property_count: 29
  slug: universal-robots-context
layout: provider
modified: '2026-07-25'
name: Universal Robots
nav: Providers
network: true
overview: 'Universal Robots publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Collaborative Robots, Cobots, Industrial Automation, and Manufacturing.


  The Universal Robots catalog on APIs.io includes 1 JSON-LD context.


  Universal Robots'' developer surface includes documentation, GitHub presence, academy / training, support, YouTube channel, and 16 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 17.0
  delta: 3.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universal-robots/refs/heads/main/screenshots/universal-robots-2026-06-20T200111.png
security:
- kind: domain-security
  name: Universal Robots Domain Security
  slug: universal-robots-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: universal-robots
tags:
- Robotics
- Collaborative Robots
- Cobots
- Industrial Automation
- Manufacturing
- PolyScope
- PolyScopeX
- URCaps
- URScript
- RTDE
- ROS
- ROS 2
- Teradyne
- Danish
- Hardware
website: https://www.universal-robots.com/
---
