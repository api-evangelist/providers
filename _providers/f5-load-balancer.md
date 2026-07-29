---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 19
  human_in_the_loop: 0
  name: F5 Load Balancer Agentic Access
  operation_count: 53
  slug: f5-load-balancer-agentic-access
  summary_line: 53 operations · 19 acting
api_count: 17
apis:
- description: Retrieve the original device configuration before Declarative Onboarding modifications were applied.
  name: F5 Load Balancer Config API
  slug: f5-load-balancer-config-api
- description: Manage internal and external data groups used for address, string, and integer lookups in traffic processing decisions.
  name: F5 Load Balancer Data Groups API
  slug: f5-load-balancer-data-groups-api
- description: Submit, retrieve, and manage AS3 declarations that describe the desired application services configuration state on the BIG-IP system.
  name: F5 Load Balancer Declarations API
  slug: f5-load-balancer-declarations-api
- description: Retrieve version and capability information about the installed AS3 extension.
  name: F5 Load Balancer Info API
  slug: f5-load-balancer-info-api
- description: Inspect the current state of BIG-IP configuration classes known to Declarative Onboarding.
  name: F5 Load Balancer Inspect API
  slug: f5-load-balancer-inspect-api
- description: Manage iRules for custom traffic management logic using the F5 Tcl-based scripting language.
  name: F5 Load Balancer iRules API
  slug: f5-load-balancer-irules-api
- description: Configure health monitors that verify the availability and performance of nodes, pool members, and services.
  name: F5 Load Balancer Monitors API
  slug: f5-load-balancer-monitors-api
- description: Manage backend server nodes identified by IP address or FQDN that serve as the foundation for pool member definitions.
  name: F5 Load Balancer Nodes API
  slug: f5-load-balancer-nodes-api
- description: Manage local traffic policies that provide rule-based traffic steering and content manipulation capabilities.
  name: F5 Load Balancer Policies API
  slug: f5-load-balancer-policies-api
- description: Manage individual server members within load balancing pools including their state, ratio, priority group, and connection limits.
  name: F5 Load Balancer Pool Members API
  slug: f5-load-balancer-pool-members-api
- description: Manage pools of backend servers for load distribution and health monitoring.
  name: F5 Load Balancer Pools API
  slug: f5-load-balancer-pools-api
- description: Manage traffic profiles that define how the BIG-IP processes different types of network traffic including HTTP, TCP, SSL, and persistence.
  name: F5 Load Balancer Profiles API
  slug: f5-load-balancer-profiles-api
- description: Manage SNAT (Secure Network Address Translation) pools that define translation addresses for outbound connections.
  name: F5 Load Balancer SNAT Pools API
  slug: f5-load-balancer-snat-pools-api
- description: Manage SSL certificates and keys used for TLS/SSL termination and re-encryption on virtual servers.
  name: F5 Load Balancer SSL Certificates API
  slug: f5-load-balancer-ssl-certificates-api
- description: Access system-level information and configuration including device status, software versions, and global settings.
  name: F5 Load Balancer System API
  slug: f5-load-balancer-system-api
- description: Monitor the status of asynchronous declaration processing tasks.
  name: F5 Load Balancer Tasks API
  slug: f5-load-balancer-tasks-api
- description: Manage virtual servers that direct client traffic to appropriate server pools based on configured rules and profiles.
  name: F5 Load Balancer Virtual Servers API
  slug: f5-load-balancer-virtual-servers-api
artifact_total: 27
collections:
- collection_type: open
  name: F5 Load Balancer F5 BIG-IP Application Services 3 Extension (AS3) API
  slug: open-f5-load-balancer-as3
- collection_type: open
  name: F5 Load Balancer F5 BIG-IP Declarative Onboarding (DO) API
  slug: open-f5-load-balancer-declarative-onboarding
- collection_type: open
  name: F5 Load Balancer F5 BIG-IP iControl REST API
  slug: open-f5-load-balancer-icontrol-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/f5-load-balancer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/f5-load-balancer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/f5-load-balancer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/f5-load-balancer-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://clouddocs.f5.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clouddocs.f5.com/api/
- group: operate
  title: ''
  type: Support
  url: https://www.f5.com/services/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.f5.com/company/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.f5.com/company/policies/privacy-notice
- group: company
  title: ''
  type: Blog
  url: https://www.f5.com/company/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/F5Networks
- group: company
  title: ''
  type: Website
  url: https://www.f5.com
created: '2024-01-01'
description: APIs for managing F5 BIG-IP Load Balancer configuration, monitoring, and operations. F5 BIG-IP is an application delivery controller that provides intelligent traffic management, load balancing, and application security.
finops:
- name: F5 Load Balancer Finops
  service_category: Application Delivery / Networking
  slug: f5-load-balancer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/f5-load-balancer.png
layout: provider
modified: '2026-05-19'
name: F5 Load Balancer
nav: Providers
network: true
overview: 'F5 Load Balancer publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Config API, Data Groups API, Declarations API, and 14 more. Tagged areas include Application Delivery, BIG-IP, Load Balancer, Networking, and Traffic Management.


  F5 Load Balancer''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 7 more developer resources.'
plans:
- name: F5 Load Balancer Plans Pricing
  plan_count: 4
  slug: f5-load-balancer-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 3
  name: F5 Load Balancer Rate Limits
  slug: f5-load-balancer-rate-limits
score:
  band: developing
  composite: 48.0
  delta: -2.5
  facets:
    commercial_clarity: 68.4
    contract_quality: 57.6
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/f5-load-balancer/refs/heads/main/screenshots/f5-load-balancer-2026-06-20T180957.png
security:
- kind: authentication
  name: F5 Load Balancer Authentication
  slug: f5-load-balancer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: F5 Load Balancer Domain Security
  slug: f5-load-balancer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: F5 Load Balancer Trust Center
  slug: f5-load-balancer-trust-center
  summary_line: PCI DSS, GDPR
slug: f5-load-balancer
tags:
- Application Delivery
- BIG-IP
- Load Balancer
- Networking
- Traffic Management
website: https://www.f5.com
---
