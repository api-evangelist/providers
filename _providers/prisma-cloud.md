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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Prisma Cloud Agentic Access
  operation_count: 2
  slug: prisma-cloud-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Prisma Cloud by Palo Alto Networks provides comprehensive cloud native security across the full application lifecycle, including vulnerability management, compliance, runtime protection, and cloud sec
  name: Prisma Cloud
  slug: prisma-cloud
- description: Login and JWT token lifecycle for Prisma Cloud CSPM.
  name: Prisma Cloud Authentication API
  slug: prisma-cloud-authentication-api
artifact_total: 10
collections:
- collection_type: open
  name: Prisma Cloud CSPM API (Authentication)
  slug: open-prisma-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prisma-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prisma-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prisma-cloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/prisma-cloud-by-palo-alto-networks
- group: company
  title: ''
  type: Website
  url: https://www.paloaltonetworks.com/prisma/cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prismacloud.io/en
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prismacloud.io/en/enterprise-edition/content-collections/get-started/access-prisma-cloud
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaloAltoNetworks
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paloaltonetworks.com/resources/guides/prisma-cloud-pricing-and-editions
- group: company
  title: ''
  type: Blog
  url: https://www.paloaltonetworks.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://sase.status.paloaltonetworks.com/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/PaloAltoNetworks/prisma-airs-mcp
created: '2026-03-26'
description: Prisma Cloud by Palo Alto Networks is a comprehensive cloud-native security platform that provides full lifecycle protection for applications across multi-cloud and hybrid environments. It covers cloud security posture management, workload protection, identity security, and code security.
finops:
- name: Prisma Cloud Finops
  service_category: API
  slug: prisma-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prisma-cloud.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Prisma Cloud
nav: Providers
network: true
overview: 'Prisma Cloud publishes 1 API on the [APIs.io](https://apis.io/) network: Authentication API. Tagged areas include Cloud Native, Cloud Security, Compliance, Containers, and CSPM.


  Prisma Cloud''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Prisma Cloud Plans Pricing
  plan_count: 3
  slug: prisma-cloud-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Prisma Cloud Rate Limits
  slug: prisma-cloud-rate-limits
score:
  band: thin
  composite: 38.9
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 62.7
    developer_ergonomics: 41.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prisma-cloud/refs/heads/main/screenshots/prisma-cloud-2026-06-20T192110.png
security:
- kind: authentication
  name: Prisma Cloud Authentication
  slug: prisma-cloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prisma Cloud Domain Security
  slug: prisma-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prisma-cloud
tags:
- Cloud Native
- Cloud Security
- Compliance
- Containers
- CSPM
- Security
website: https://www.paloaltonetworks.com/prisma/cloud
---
