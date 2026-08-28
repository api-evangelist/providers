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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kuka-robotics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuka-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuka.com
- group: other
  title: ''
  type: Products
  url: https://www.kuka.com/en-de/products
- group: start
  title: ''
  type: IndustrialRobots
  url: https://www.kuka.com/en-de/products/robotics-systems/industrial-robots
- group: other
  title: ''
  type: MobileRobots
  url: https://www.kuka.com/en-de/products/mobility
- group: other
  title: ''
  type: Controllers
  url: https://www.kuka.com/en-de/products/robotics-systems/robot-controllers
- group: other
  title: ''
  type: Software
  url: https://www.kuka.com/en-de/products/robotics-systems/software
- group: other
  title: ''
  type: iiQKA
  url: https://www.kuka.com/iiQKA
- group: build
  title: ''
  type: CreatorDeveloperTools
  url: https://www.kuka.com/en-us/future-production/iiqka-robots-for-the-people/creator-portal/creator-developer-tools
- group: other
  title: ''
  type: KUKAXpert
  url: https://xpert.kuka.com
- group: other
  title: ''
  type: iiQoT
  url: https://www.kuka.com/en-de/products/robotics-systems/software/cloud-software/kuka-iiqot
- group: other
  title: ''
  type: MyKUKA
  url: https://my.kuka.com
- group: other
  title: ''
  type: KUKACollege
  url: https://www.kuka.com/en-de/services/training
- group: other
  title: ''
  type: Industries
  url: https://www.kuka.com/en-de/industries
- group: other
  title: ''
  type: Services
  url: https://www.kuka.com/en-de/services
- group: other
  title: ''
  type: Company
  url: https://www.kuka.com/en-de/company
- group: company
  title: ''
  type: Press
  url: https://www.kuka.com/en-de/press
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.kuka.com/en-de/investor-relations
- group: company
  title: ''
  type: Careers
  url: https://www.kuka.com/en-de/career
- group: operate
  title: ''
  type: Contact
  url: https://www.kuka.com/en-de/contact-and-support
- group: other
  title: ''
  type: Swisslog
  url: https://www.swisslog.com
- group: other
  title: ''
  type: Midea
  url: https://www.midea-group.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kroshu
- group: other
  title: ''
  type: ROSDrivers
  url: https://github.com/kroshu/kuka_drivers
- group: build
  title: ''
  type: ExternalControlSDK
  url: https://github.com/kroshu/kuka-external-control-sdk
- group: other
  title: ''
  type: RobotDescriptions
  url: https://github.com/kroshu/kuka_robot_descriptions
- group: other
  title: ''
  type: RoboticsAPI
  url: https://github.com/roboticsapi
- group: other
  title: ''
  type: OpenKuka
  url: https://github.com/openkuka
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kuka
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/KUKAGlobal
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/KUKAGlobal
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/KUKAGlobal
created: '2026-05-25'
description: KUKA AG is a German industrial automation company headquartered in Augsburg, Bavaria, founded in 1898 and majority-owned by China's Midea Group since 2016. KUKA designs and manufactures industrial robots, autonomous mobile robots (AMRs), production cells, controllers, and the software stack that drives them. Its product portfolio spans six-axis articulated robots (KR series), sensitive collaborative robots (LBR iiwa, LBR iisy), mobile platforms (KMR iiwa, KMP), and palletizing/welding/CNC cells, controlled by the KR C4 and KR C5 / KR C5 micro controller generations. The robot software stack centers on KUKA System Software (KSS/VSS) for KR C4-class hardware, the newer iiQKA.OS / iiQKA.OS2 operating system for KR C5, and the KUKA Robot Language (KRL) for motion programming, with extension surfaces including KUKA.RobotSensorInterface (RSI), KUKA.EthernetKRL, KUKA.PLC mxAutomation for external PLC control, KUKA.OPC UA, and KUKA.AppTech / iiQKA App Builder for option packages. Engineering
  and simulation are delivered through iiQWorks (iiQWorks.Sim, iiQWorks.App Builder, iiQWorks.Copilot) and KUKA.Sim, while operational software includes KUKA Xpert (documentation/cloud), KUKA iiQoT (condition monitoring), and KUKA Connect / my.KUKA customer portals. KUKA does not publish a first-party public REST/OpenAPI developer API or an official GitHub organization for its robot control stack; integration is performed through proprietary protocols (RSI, EthernetKRL, mxAutomation, OPC UA, PROFINET, EtherCAT) and SDKs distributed via the iiQKA Creator portal and KUKA Xpert. A meaningful body of open-source KUKA integration code lives in the community-maintained kroshu GitHub organization (ROS 2 drivers, external-control SDK, URDF robot descriptions) and the roboticsapi / openkuka projects. KUKA serves automotive, electronics, battery, metal, consumer goods, healthcare, aerospace, and e-commerce logistics customers, and through its Swisslog subsidiary extends into warehouse and intralogistics
  automation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kuka-robotics.png
jsonld:
- class_count: 8
  name: Kuka Robotics Context
  property_count: 20
  slug: kuka-robotics-context
layout: provider
modified: '2026-05-25'
name: KUKA
nav: Providers
network: true
overview: 'KUKA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Industrial Robots, Industrial Automation, Collaborative Robots, and Cobots.


  The KUKA catalog on APIs.io includes 1 JSON-LD context.


  KUKA''s developer surface includes GitHub presence, YouTube channel, and 31 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuka-robotics/refs/heads/main/screenshots/kuka-robotics-2026-06-20T184213.png
security:
- kind: domain-security
  name: Kuka Robotics Domain Security
  slug: kuka-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kuka Robotics Vulnerability Disclosure
  slug: kuka-robotics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kuka-robotics
tags:
- Robotics
- Industrial Robots
- Industrial Automation
- Collaborative Robots
- Cobots
- Autonomous Mobile Robots
- Robot Controllers
- Robot Operating System
- KRL
- KSS
- KR C4
- KR C5
- iiQKA
- LBR iiwa
- PROFINET
- OPC UA
- Manufacturing
- Automotive
- Intralogistics
- Welding
- Palletizing
- Hardware
- Germany
- Midea
website: https://www.kuka.com
---
