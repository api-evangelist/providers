---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ciena Agentic Access
  operation_count: 9
  slug: ciena-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 6
apis:
- description: Ciena's Manage, Control and Plan (MCP) is a multi-layer Software Defined Networking (SDN) and Network Management System (NMS) platform. The MCP REST and RESTCONF APIs enable network-aware management o
  name: Ciena MCP (Manage, Control and Plan) API
  slug: mcp-api
- description: Ciena Emulation Cloud is an open application development environment enabling developers to create, test, and fine-tune custom applications against full API definitions without requiring physical infr
  name: Ciena Emulation Cloud API
  slug: emulation-cloud-api
- description: Network alarm and fault management
  name: Ciena Alarms API
  slug: ciena-alarms-api
- description: Performance monitoring and metrics
  name: Ciena Performance API
  slug: ciena-performance-api
- description: The Services API from Ciena — 2 operation(s) for services.
  name: Ciena Services API
  slug: ciena-services-api
- description: Network topology resources including nodes and links
  name: Ciena Topology API
  slug: ciena-topology-api
artifact_total: 18
collections:
- collection_type: open
  name: Ciena Blue Planet Open API
  slug: open-ciena-blue-planet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ciena-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ciena-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ciena-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ciena-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ciena-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ciena
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ciena
- group: company
  title: ''
  type: Website
  url: https://www.ciena.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ciena.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.blueplanet.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blueplanet.com/technology/open-apis.html
- group: company
  title: ''
  type: Blog
  url: https://www.blueplanet.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.blueplanet.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ciena.com/about/corporate-governance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ciena.com/customers/terms-and-conditions
- group: operate
  title: ''
  type: Community
  url: https://my.ciena.com/CienaPortal/s/blue-planet
- group: build
  title: ''
  type: GitHubOrg
  url: https://git.blueplanet.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ciena-blue-planet-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ciena-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ciena-network-service-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/ciena-spectral.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.ciena.com/llms.txt
created: '2025-02-21'
description: Ciena Corporation is a global networking equipment, software, and services vendor focused on optical and packet networking, SDN, and service automation. This index covers Ciena's open APIs across the Blue Planet automation platform, the Ciena MCP (Manage, Control, and Plan) NMS, and the Emulation Cloud developer environment, exposing TM Forum Open APIs, MEF Lifecycle Service Orchestration (LSO) APIs (Legato, Sonata), and ONAP-aligned policy controls for telecom carriers and managed service providers.
finops:
- name: Ciena Finops
  service_category: Network Infrastructure / SDN
  slug: ciena-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ciena.png
json_schemas:
- name: Ciena Blue Planet Network Service
  property_count: 15
  slug: ciena-network-service
jsonld:
- class_count: 3
  name: Ciena Context
  property_count: 24
  slug: ciena-context
layout: provider
modified: '2026-05-19'
name: Ciena
nav: Providers
network: true
overview: 'Ciena publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Performance API, Services API, and 1 more. Tagged areas include MEF, NETCONF, Network Automation, Network Management, and Optical.


  The Ciena catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ciena''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 17 more developer resources.'
plans:
- name: Ciena Plans Pricing
  plan_count: 2
  slug: ciena-plans-pricing
press:
- date: '2026-05-25'
  title: Newsroom | Press Releases
  url: https://www.ciena.com/about/newsroom/press-releases
- date: '2026-05-25'
  title: Press Releases
  url: https://www.blueplanet.com/about/press-releases
- date: '2026-05-25'
  title: Newsroom |Latest News from Ciena
  url: https://www.ciena.com/about/newsroom
- date: '2026-05-25'
  title: Ciena Solidifies AI Networking Leadership, Unveils New ...
  url: https://www.businesswire.com/news/home/20260310561860/en/Ciena-Solidifies-AI-Networking-Leadership-Unveils-New-Innovations-for-High-Speed-Connectivity
- date: '2026-05-25'
  title: Ciena Solidifies AI Networking Leadership, Unveils New ...
  url: https://www.ciena.com/about/newsroom/press-releases/ciena-solidifies-ai-networking-leadership-unveils-new-innovations-for-high-speed-connectivity
random_paper: 48
rate_limits:
- limit_count: 3
  name: Ciena Rate Limits
  slug: ciena-rate-limits
rules:
- name: Ciena API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ciena-jsonschema-spectral-rules
scopes:
- name: Ciena Scopes
  scope_count: 5
  slug: ciena-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 50.3
  delta: -5.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 67.2
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/screenshots/ciena-2026-06-20T174339.png
security:
- kind: authentication
  name: Ciena Authentication
  slug: ciena-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ciena Domain Security
  slug: ciena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ciena Vulnerability Disclosure
  slug: ciena-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ciena
tags:
- MEF
- NETCONF
- Network Automation
- Network Management
- Optical
- RESTCONF
- SDN
- Telecom
- TM Forum
- Fortune 1000
website: https://www.ciena.com/
---
