---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API behind the Ethernovia Customer Portal (portal.ethernovia.com), built on Strapi 5. Exposes the portal content model — products, product families and categories, document and software-package c
  name: Ethernovia Customer Portal API
  slug: ethernovia-customer-portal-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ethernovia.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.ethernovia.com/
- group: operate
  title: ''
  type: Support
  url: https://support.ethernovia.com/support/home
- group: start
  title: ''
  type: SignUp
  url: https://portal.ethernovia.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://portal-admin.ethernovia.com/api/connect/auth0
- group: company
  title: ''
  type: Blog
  url: https://www.ethernovia.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ethernovia.com/news/feed/
- group: company
  title: ''
  type: News
  url: https://www.ethernovia.com/news/
- group: other
  title: ''
  type: Events
  url: https://www.ethernovia.com/events/
- group: other
  title: ''
  type: Products
  url: https://www.ethernovia.com/products/
- group: operate
  title: ''
  type: Contact
  url: https://www.ethernovia.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.ethernovia.com/careers/
- group: company
  title: ''
  type: Investors
  url: https://www.ethernovia.com/investors/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ethernovia.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ethernovia.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ethernovia.com/certificates-standards/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ethernovia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ethernovia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ethernovia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ethernovia-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ethernovia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ethernovia-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ethernovia-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethernovia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ethernovia-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Ethernovia is a San Jose, California semiconductor company building deterministic Ethernet networking silicon for software-defined vehicles, robotics and physical AI. Its portfolio spans single-pair (T1) Ethernet PHYs from 1G to 10G (ENT11100, ENT11025, ENT14100, ENT14025), deterministic packet processors and switches, and the High-Speed Sensor Bridge platform that bridges GMSL 2/3 cameras and CAN FD/XL onto 10GBASE-T1 Ethernet for NVIDIA Holoscan, Orin and Thor compute. Ethernovia publishes no public product API: its software binaries, source-code drivers, header files and plug-in APIs are distributed to customers under NDA and a separate EULA through the Ethernovia Customer Portal. The one machine-readable contract reachable without credentials is the Customer Portal''s own backend API, whose Swagger UI is served publicly at portal-admin.ethernovia.com/documentation.'
image: https://www.ethernovia.com/wp-content/uploads/2026/02/ethernovia-physical-ai-networking-chips.jpg
layout: provider
modified: '2026-08-04'
name: Ethernovia
nav: Providers
network: true
overview: 'Ethernovia publishes 1 API on the [APIs.io](https://apis.io/) network: Customer Portal API. Tagged areas include Company, Semiconductors, Automotive, Ethernet, and Networking.


  Ethernovia''s developer surface includes developer portal, support, signup flow, engineering blog, product news, authentication, and 20 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 38.5
    developer_ergonomics: 27.7
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 34.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Ethernovia Authentication
  slug: ethernovia-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Ethernovia Domain Security
  slug: ethernovia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ethernovia
tags:
- Company
- Semiconductors
- Automotive
- Ethernet
- Networking
- Hardware
- Robotics
- Artificial Intelligence
- Autonomous Vehicles
- Physical AI
website: https://www.ethernovia.com/
---
