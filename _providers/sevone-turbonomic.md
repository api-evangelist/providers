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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sevone-turbonomic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sevone-turbonomic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sevone.com
- group: company
  title: ''
  type: Website
  url: https://www.turbonomic.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/sevone-npm
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/tarm
- group: operate
  title: ''
  type: Support
  url: https://community.ibm.com/community/user/aiops/communities/community-home?CommunityKey=turbonomic
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sevone-turbonomic-llms.txt
created: '2026-07-17'
description: 'SevOne and Turbonomic are enterprise IT operations products now part of IBM''s AIOps portfolio. IBM SevOne Network Performance Management (NPM) delivers real-time, multi-vendor network monitoring, flow analytics, and capacity planning across hybrid and enterprise networks. IBM Turbonomic is an application resource management (ARM) platform that continuously analyzes application demand and automates resourcing, scaling, and placement decisions across on-premises, cloud, and Kubernetes environments to assure performance while reducing cost. Both products expose REST APIs, but those APIs are hosted on the customer''s own appliance / deployment rather than on a public developer portal, so there is no public base URL or published OpenAPI to catalog: the Turbonomic REST API is served from the appliance (for example the /vmturbo/rest path with its bundled Swagger UI), and SevOne exposes the SevOne NMS API and SevOne Data Insight API from the deployed instance. Product and API reference
  documentation is published by IBM.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sevone-turbonomic.png
layout: provider
modified: '2026-07-21'
name: SevOne (Turbonomic)
nav: Providers
network: true
overview: 'SevOne (Turbonomic) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Infrastructure, Network Monitoring, Observability, and AIOps.


  SevOne (Turbonomic)''s developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 96
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Sevone Turbonomic Domain Security
  slug: sevone-turbonomic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sevone Turbonomic Vulnerability Disclosure
  slug: sevone-turbonomic-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sevone-turbonomic
tags:
- Company
- Ai Infrastructure
- Network Monitoring
- Observability
- AIOps
- Application Resource Management
- Cloud Cost Optimization
- Kubernetes
- IBM
website: https://www.sevone.com
---
