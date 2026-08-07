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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Brocade Agentic Access
  operation_count: 15
  slug: brocade-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 12
apis:
- description: The Brocade Fabric OS REST API provides a programmable web-service interface for managing Brocade SAN switches across a fabric. It supports YANG-based modules for configuring and monitoring switch res
  name: Brocade Fabric OS REST API
  slug: brocade-fabric-os-rest-api
- description: 'The Brocade SANnav Management Portal REST API provides a programmable web-service interface for accessing and managing the SANnav Management Portal server. REST API services include Login, Discovery, '
  name: Brocade SANnav Management Portal REST API
  slug: brocade-sannav-management-portal-rest-api
- description: The Brocade SANnav Northbound Streaming API enables real-time streaming of SAN telemetry and event data from the SANnav Management Portal to external systems. It provides northbound streaming of fault
  name: Brocade SANnav Northbound Streaming API
  slug: brocade-sannav-northbound-streaming-api
- description: The Brocade Network Advisor REST API provided a web-services interface for configuring and monitoring Brocade SAN switches, including fabric management, topology, zoning, and performance data retrieva
  name: Brocade Network Advisor REST API
  slug: brocade-network-advisor-rest-api
- description: 'The Brocade Workflow Composer was a network automation platform based on StackStorm for event-driven automation and orchestration workflows. The product was transferred to Extreme Networks as part of '
  name: Brocade Workflow Composer API
  slug: brocade-workflow-composer-api
- description: 'The Brocade VCS Fabric API provided REST interfaces for Virtual Cluster Switching fabric configuration on Brocade VDX switches. The VCS Fabric product line was transferred to Extreme Networks as part '
  name: Brocade VCS Fabric API
  slug: brocade-vcs-fabric-api
- description: The Chassis API from Brocade — 1 operation(s) for chassis.
  name: Brocade Chassis API
  slug: brocade-chassis-api
- description: The Interfaces API from Brocade — 2 operation(s) for interfaces.
  name: Brocade Interfaces API
  slug: brocade-interfaces-api
- description: The Operations API from Brocade — 4 operation(s) for operations.
  name: Brocade Operations API
  slug: brocade-operations-api
- description: The Session API from Brocade — 2 operation(s) for session.
  name: Brocade Session API
  slug: brocade-session-api
- description: The Switch API from Brocade — 1 operation(s) for switch.
  name: Brocade Switch API
  slug: brocade-switch-api
- description: The Zoning API from Brocade — 2 operation(s) for zoning.
  name: Brocade Zoning API
  slug: brocade-zoning-api
artifact_total: 19
collections:
- collection_type: open
  name: Brocade Fabric OS REST API
  slug: open-brocade
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brocade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brocade-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brocade-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brocade
- group: start
  title: ''
  type: Portal
  url: https://techdocs.broadcom.com/us/en/fibre-channel-networking.html
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.broadcom.com/us/en/fibre-channel-networking.html
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x/v26395730/v24190001.html
- group: operate
  title: ''
  type: Support
  url: https://www.broadcom.com/support/fibre-channel-networking
- group: company
  title: ''
  type: Website
  url: https://www.broadcom.com/products/fibre-channel-networking
- group: start
  title: ''
  type: Signup
  url: https://www.broadcom.com/support/fibre-channel-networking
- group: start
  title: ''
  type: Login
  url: https://www.broadcom.com/support/fibre-channel-networking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy/policy
- group: operate
  title: ''
  type: Community
  url: https://community.broadcom.com/t5/Fibre-Channel-SAN-Forums/bd-p/fibre
- group: company
  title: ''
  type: Blog
  url: https://community.broadcom.com/landingpage/brocade-community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brocade
- group: build
  title: ''
  type: SDKs
  url: https://github.com/brocade/pyfos
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.broadcom.com/support/fibre-channel-networking/eol
created: '2024-01-01'
description: Brocade, now part of Broadcom, provides Fibre Channel networking solutions for storage area networks (SANs). The Brocade portfolio includes SAN switches, directors, Fabric OS software, and the SANnav management platform, all offering REST APIs for programmable management and automation of SAN infrastructure.
finops:
- name: Brocade Finops
  service_category: API
  slug: brocade-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brocade.png
layout: provider
modified: '2026-04-21'
name: Brocade
nav: Providers
network: true
overview: 'Brocade publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chassis API, Interfaces API, Operations API, and 3 more. Tagged areas include Data Center, Directors, Fibre Channel, Network Automation, and Networking.


  Brocade''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Brocade Plans Pricing
  plan_count: 3
  slug: brocade-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Brocade Rate Limits
  slug: brocade-rate-limits
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 53.5
    developer_ergonomics: 52.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brocade/refs/heads/main/screenshots/brocade-2026-06-20T173715.png
security:
- kind: authentication
  name: Brocade Authentication
  slug: brocade-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Brocade Domain Security
  slug: brocade-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brocade
tags:
- Data Center
- Directors
- Fibre Channel
- Network Automation
- Networking
- SAN
- Storage Area Networks
- Switches
- Fortune 1000
website: https://www.broadcom.com/products/fibre-channel-networking
---
