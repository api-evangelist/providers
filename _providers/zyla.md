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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Zyla API Hub provides a centralized marketplace for discovering, testing, and integrating thousands of APIs across categories including finance, weather, geolocation, communication, and more, all acce
  name: Zyla API Hub
  slug: zyla-api-hub
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zyla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zylalabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zyla.com/docs/zyla-developer-doc/zyla_enterprise_solution/api_overview
- group: other
  title: ''
  type: API Marketplace
  url: https://zylalabs.com/api-marketplace
- group: company
  title: ''
  type: Blog
  url: https://zylalabs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://zylalabs-doc.freshdesk.com/support/solutions/articles/151000011508-what-is-zyla-api-hub-
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zyla-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zyla-labs
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/zylalabs/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Zyla-Labs/zyla-mcp-plugin
created: '2025-01-08'
description: Zyla API Hub is an API marketplace that provides unified access to over 10,000 APIs through a single account, API key, and SDK, simplifying API discovery, integration, and management for developers.
finops:
- name: Zyla Finops
  service_category: API
  slug: zyla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zyla.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Zyla
nav: Providers
network: true
overview: 'Zyla publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Hub, Discovery, Marketplace, Platform, and Search.


  Zyla''s developer surface includes documentation, engineering blog, support, and 7 more developer resources.'
plans:
- name: Zyla Plans Pricing
  plan_count: 3
  slug: zyla-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Zyla Rate Limits
  slug: zyla-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zyla/refs/heads/main/screenshots/zyla-2026-06-20T202016.png
security:
- kind: domain-security
  name: Zyla Domain Security
  slug: zyla-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zyla
tags:
- API Hub
- Discovery
- Marketplace
- Platform
- Search
website: https://zylalabs.com/
---
