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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: RESTful API exposed by the Geneos Gateway for retrieving monitoring data and managing dataviews, samplers, entities, and snooze states programmatically. Authenticated and typically deployed inside ent
  name: Geneos Gateway REST API
  slug: gateway-rest
- description: XML-RPC interface for programmatic control of Geneos Gateway including executing commands, managing configuration, publishing data into Gateways from external samplers, and retrieving monitoring data.
  name: Geneos XML-RPC API
  slug: xml-rpc
- description: API for integrating with the Geneos Web Dashboard, enabling custom dashboards, data visualization, and user interface extensions on top of Geneos monitoring data.
  name: Geneos Web Dashboard API
  slug: web-dashboard
- description: Java and Python APIs delivered through the Geneos Toolkit for building custom integrations, samplers, plugins, and automation scripts that publish data into and pull data out of Geneos.
  name: Geneos Toolkit API
  slug: toolkit
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geneos-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geneos-therapeutics
- group: company
  title: ''
  type: Website
  url: https://www.itrsgroup.com/
- group: other
  title: ''
  type: ProductPage
  url: https://www.itrsgroup.com/products/geneos
- group: docs
  title: ''
  type: Documentation
  url: https://docs.itrsgroup.com/docs/geneos/
- group: operate
  title: ''
  type: Support
  url: https://www.itrsgroup.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.itrsgroup.com/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.itrsgroup.com/
- group: learn
  title: ''
  type: Training
  url: https://www.itrsgroup.com/training
- group: operate
  title: ''
  type: Contact
  url: https://www.itrsgroup.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itrsgroup.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.itrsgroup.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ITRS-Group
created: '2024-01-15'
description: Geneos is ITRS Group's real-time monitoring platform that provides comprehensive observability for trading systems, applications, and infrastructure. Widely deployed across investment banks, hedge funds, and exchanges, Geneos collects high-frequency telemetry from custom samplers and toolkits, aggregates it through Gateways, and exposes that data through REST, XML-RPC, streaming, and SDK interfaces for programmatic access, automation, and dashboarding.
finops:
- name: Geneos Finops
  service_category: API
  slug: geneos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geneos.png
layout: provider
modified: '2026-04-28'
name: Geneos
nav: Providers
network: true
overview: 'Geneos publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include APM, Capital Markets, Infrastructure, ITRS, and Monitoring.


  Geneos'' developer surface includes documentation, support, training material, and 10 more developer resources.'
plans:
- name: Geneos Plans Pricing
  plan_count: 3
  slug: geneos-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Geneos Rate Limits
  slug: geneos-rate-limits
score:
  band: emerging
  composite: 26.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geneos/refs/heads/main/screenshots/geneos-2026-06-20T181719.png
security:
- kind: domain-security
  name: Geneos Domain Security
  slug: geneos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: geneos
tags:
- APM
- Capital Markets
- Infrastructure
- ITRS
- Monitoring
- Observability
- Real-Time
- Trading Systems
website: https://www.itrsgroup.com/
---
