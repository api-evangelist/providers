---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Plex by Rockwell Automation provides a Smart Manufacturing Platform ERP API with REST/JSON endpoints for customer orders, shipping, production, quality, and just-in-sequence parts delivery. Enables in
  name: Rockwell Automation Plex ERP API
  slug: plex-erp-api
- description: FactoryTalk DataMosaix is an Industrial DataOps solution that provides REST API access for industrial data management, contextualization, and analytics. Supports machine-to-machine (M2M) communication
  name: Rockwell Automation FactoryTalk DataMosaix API
  slug: factorytalk-datamosaix-api
- description: FactoryTalk Remote Access (FTRA) Web API provides RESTful HTTP interface for remote access management, enabling developers to integrate industrial device remote access capabilities into third-party ap
  name: Rockwell Automation FactoryTalk Remote Access Web API
  slug: factorytalk-remote-access-api
- description: The Studio 5000 Logix Designer Software Development Kit (LDSDK) provides programmatic access to Logix controller programming for CI/CD pipeline automation, version control integration, and export of L
  name: Rockwell Automation Logix Designer SDK
  slug: logix-designer-api
- description: Emulate3D Core API provides programmatic access to 3D simulation and digital twin capabilities for factory automation. Enables integration with Nvidia Omniverse and custom automation workflows via scr
  name: Rockwell Automation Emulate3D API
  slug: emulate3d-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockwell-automation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rockwell-automation
- group: company
  title: ''
  type: Website
  url: https://www.rockwellautomation.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.rockwellautomation.com/en-us/support/documentation.html
- group: start
  title: ''
  type: Portal
  url: https://developers.plex.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RockwellAutomation
- group: operate
  title: ''
  type: Support
  url: https://www.rockwellautomation.com/en-us/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rockwellautomation.com/en-us/company/about-us/legal-notices/privacy-and-cookies-policy.html
- group: company
  title: ''
  type: Blog
  url: https://www.rockwellautomation.com/en-us/company/news/blogs/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rockwell-automation-plex-order-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/rockwell-automation-plex-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rockwell-automation-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rockwell-automation-vocabulary.yml
created: '2026-03-21'
description: Rockwell Automation is a global provider of industrial automation and digital transformation solutions, helping manufacturers boost productivity, sustainability, and agility. The company offers a portfolio of hardware, software, and services including programmable logic controllers (PLCs), industrial networking, motor control, safety systems, and the FactoryTalk software suite for MES, SCADA, historian, remote access, and industrial data management.
finops:
- name: Rockwell Automation Finops
  service_category: API
  slug: rockwell-automation-finops
graphqls:
- description: Rockwell Automation provides industrial automation and information technology. Their FactoryTalk API covers PLC data, production metrics, quality management, OEE analytics, asset management, batch rec
  name: Rockwell Automation GraphQL API
  slug: rockwell-automation-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rockwell-automation.png
json_schemas:
- name: Rockwell Automation Plex Customer Order
  property_count: 11
  slug: rockwell-automation-plex-order
json_structures:
- name: Rockwell Automation Plex Structure
  property_count: 0
  slug: rockwell-automation-plex-structure
jsonld:
- class_count: 7
  name: Rockwell Automation Context
  property_count: 15
  slug: rockwell-automation-context
layout: provider
modified: '2026-05-02'
name: Rockwell Automation
nav: Providers
network: true
overview: 'Rockwell Automation publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial Automation, Manufacturing, PLC, SCADA, and IIoT.


  The Rockwell Automation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rockwell Automation''s developer surface includes documentation, developer portal, support, engineering blog, and 9 more developer resources.'
plans:
- name: Rockwell Automation Plans Pricing
  plan_count: 3
  slug: rockwell-automation-plans-pricing
press:
- date: '2026-05-25'
  title: ROCKWELL AUTOMATION TO ADVANCE INDUSTRIAL ...
  url: https://www.prnewswire.com/news-releases/rockwell-automation-to-advance-industrial-intelligence-through-edge-based-generative-ai-with-nvidia-nemotron-302614991.html
- date: '2026-05-25'
  title: Rockwell Automation Showcases AI Orchestrated Factory ...
  url: https://www.rockwellautomation.com/en-dk/company/news/press-releases/ai-orchestrated-factory-design-at-hannover-messe.html
- date: '2026-05-25'
  title: Press Releases | Rockwell Automation | US
  url: https://www.rockwellautomation.com/en-us/company/news/press-releases.html
- date: '2026-05-25'
  title: Industrial AI | Rockwell Automation | US
  url: https://www.rockwellautomation.com/en-us/future-trends-industrial-operations/industrial-ai.html
- date: '2026-05-25'
  title: Press Releases & News
  url: https://www.rockwellautomation.com/en-us/company/investor-relations/news.html
random_paper: 33
rate_limits:
- limit_count: 5
  name: Rockwell Automation Rate Limits
  slug: rockwell-automation-rate-limits
rules:
- name: Rockwell Automation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rockwell-automation-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.4
  delta: 4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.8
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 45.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockwell-automation/refs/heads/main/screenshots/rockwell-automation-2026-06-20T193157.png
security:
- kind: domain-security
  name: Rockwell Automation Domain Security
  slug: rockwell-automation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rockwell-automation
tags:
- Industrial Automation
- Manufacturing
- PLC
- SCADA
- IIoT
- Fortune 500
website: https://www.rockwellautomation.com
---
