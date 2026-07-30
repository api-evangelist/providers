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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Load Balancer Agentic Access
  operation_count: 7
  slug: microsoft-azure-load-balancer-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Load Balancers operations
  name: Azure Load Balancer Load Balancers API
  slug: microsoft-azure-load-balancer-load-balancers-api
- description: Operations operations
  name: Azure Load Balancer Operations API
  slug: microsoft-azure-load-balancer-operations-api
artifact_total: 22
collections:
- collection_type: open
  name: Azure Load Balancer REST API
  slug: open-microsoft-azure-load-balancer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-load-balancer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-load-balancer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-load-balancer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-load-balancer-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/load-balancer/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/load-balancer/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Load Balancer is a high-performance, low-latency layer-4 load balancing service for distributing inbound and outbound network traffic across virtual machines and other Azure resources. It supports public and internal load balancers, health probes, NAT rules, and HA scenarios.
features:
- description: Distribute TCP and UDP traffic across virtual machines and resources with high performance and low latency.
  name: Layer-4 Load Balancing
- description: Support both public-facing and internal load balancing scenarios for diverse network architectures.
  name: Public and Internal Load Balancers
- description: Monitor backend instance health with configurable TCP, HTTP, and HTTPS probes for automatic failover.
  name: Health Probes
- description: Configure inbound NAT rules to forward traffic to specific backend instances on designated ports.
  name: NAT Rules
- description: Load balance all TCP and UDP flows on all ports simultaneously for network virtual appliance scenarios.
  name: High Availability Ports
- description: Distribute traffic across Azure regions for global high availability and disaster recovery.
  name: Cross-Region Load Balancing
finops:
- name: Microsoft Azure Load Balancer Finops
  service_category: API
  slug: microsoft-azure-load-balancer-finops
image: https://azure.microsoft.com/svghandler/load-balancer/
integrations:
- description: Distribute network traffic across pools of Azure virtual machines.
  name: Azure Virtual Machines
- description: Integrate with VMSS for automatic scaling and load distribution.
  name: Azure Virtual Machine Scale Sets
- description: Monitor load balancer health, performance metrics, and diagnostic logs.
  name: Azure Monitor
layout: provider
modified: '2026-05-19'
name: Azure Load Balancer
nav: Providers
network: true
overview: 'Azure Load Balancer publishes 2 APIs on the [APIs.io](https://apis.io/) network: Load Balancers API and Operations API. Tagged areas include Azure, High Availability, Layer 4, Load Balancing, and Network.


  Azure Load Balancer''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Microsoft Azure Load Balancer Plans Pricing
  plan_count: 3
  slug: microsoft-azure-load-balancer-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Microsoft Azure Load Balancer Rate Limits
  slug: microsoft-azure-load-balancer-rate-limits
scopes:
- name: Microsoft Azure Load Balancer Scopes
  scope_count: 1
  slug: microsoft-azure-load-balancer-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.4
  delta: -1.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-load-balancer/refs/heads/main/screenshots/microsoft-azure-load-balancer-2026-06-20T185420.png
security:
- kind: authentication
  name: Microsoft Azure Load Balancer Authentication
  slug: microsoft-azure-load-balancer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Load Balancer Domain Security
  slug: microsoft-azure-load-balancer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-load-balancer
tags:
- Azure
- High Availability
- Layer 4
- Load Balancing
- Network
use_cases:
- description: Distribute traffic across multiple web servers for improved reliability and uptime.
  name: Web Application High Availability
- description: Automatically balance traffic across virtual machine scale sets with auto-scaling capabilities.
  name: VM Scale Set Load Balancing
- description: Distribute traffic across multiple firewall or NVA instances using HA ports.
  name: Network Virtual Appliance Distribution
website: https://portal.azure.com/
---
