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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Liveramp Agentic Access
  operation_count: 26
  slug: liveramp-agentic-access
  summary_line: 26 operations · 9 acting
api_count: 17
apis:
- description: Programmatic activation of first-party and marketplace data across destination partners and connected platforms in the LiveRamp network.
  name: LiveRamp Activation API
  slug: activation-api
- description: Privacy-first, PII-based authentication API enabling programmatic addressability without third-party cookies via RampID envelopes.
  name: LiveRamp Authenticated Traffic Solution (ATS) API
  slug: ats-api
- description: API for setting up and managing clean rooms, data sources, and collaborative analytics queries between data partners.
  name: LiveRamp Clean Room API
  slug: clean-room-api
- description: API enabling platforms to host third-party segments from the LiveRamp Data Marketplace and access detailed segment metadata.
  name: LiveRamp Data Marketplace Buyer API
  slug: datamarketplace-buyer-api
- description: Identity resolution API that resolves offline PII data into stable AbiliTec links for enterprise customer-database unification.
  name: LiveRamp AbiliTec API
  slug: abilitec-api
- description: API for matching data to the LiveRamp Identity Graph, including envelope decryption and translation between pseudonymous identifiers.
  name: LiveRamp RampID API
  slug: rampid-api
- description: Automates Python, PySpark, and BigQuery jobs running in LiveRamp's Safe Haven Analytics Environment.
  name: LiveRamp Safe Haven Job Management API
  slug: job-management-api
- description: Automates data subject requests including opt-outs, deletions, and consent updates across the LiveRamp ecosystem.
  name: LiveRamp Privacy API
  slug: privacy-api
- description: Service enabling SSPs to decrypt RampID identity envelopes into DSP-specific identifiers for programmatic activation.
  name: LiveRamp Sidecar
  slug: sidecar
- description: The Deliveries API from LiveRamp — 1 operation(s) for deliveries.
  name: LiveRamp Deliveries API
  slug: liveramp-deliveries-api
- description: The Destination Integrations API from LiveRamp — 2 operation(s) for destination integrations.
  name: LiveRamp Destination Integrations API
  slug: liveramp-destination-integrations-api
- description: The Destinations API from LiveRamp — 2 operation(s) for destinations.
  name: LiveRamp Destinations API
  slug: liveramp-destinations-api
- description: The Distribution Managers API from LiveRamp — 2 operation(s) for distribution managers.
  name: LiveRamp Distribution Managers API
  slug: liveramp-distribution-managers-api
- description: The Integration Connections API from LiveRamp — 2 operation(s) for integration connections.
  name: LiveRamp Integration Connections API
  slug: liveramp-integration-connections-api
- description: The OAuth Connections API from LiveRamp — 4 operation(s) for oauth connections.
  name: LiveRamp OAuth Connections API
  slug: liveramp-oauth-connections-api
- description: The Segment Configurations API from LiveRamp — 2 operation(s) for segment configurations.
  name: LiveRamp Segment Configurations API
  slug: liveramp-segment-configurations-api
- description: The Segments API from LiveRamp — 3 operation(s) for segments.
  name: LiveRamp Segments API
  slug: liveramp-segments-api
artifact_total: 28
collections:
- collection_type: open
  name: LiveRamp Activation API
  slug: open-liveramp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liveramp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/liveramp-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liveramp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveramp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liveramp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liveramp
- group: company
  title: ''
  type: Website
  url: https://liveramp.com
- group: start
  title: ''
  type: Portal
  url: https://developers.liveramp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liveramp.com/
- group: start
  title: ''
  type: SupportPortal
  url: https://support.liveramp.com/
- group: company
  title: ''
  type: Blog
  url: https://liveramp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LiveRamp
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/LiveRamp/logscale-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.liveramp.com/llms.txt
created: '2026-03-16'
description: LiveRamp is a data connectivity platform that enables enterprises to safely connect, control, and activate first-party customer data across the digital ecosystem. Their developer platform exposes a suite of REST APIs for identity resolution, data activation, clean-room collaboration, marketplace data access, and privacy-first authenticated traffic.
finops:
- name: Liveramp Finops
  service_category: API
  slug: liveramp-finops
graphqls:
- description: LiveRamp is a data connectivity platform for identity resolution, data onboarding, and audience activation. Their API covers data segment management, identity links, connectivity endpoints, and data c
  name: LiveRamp GraphQL API
  slug: liveramp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liveramp.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: LiveRamp
nav: Providers
network: true
overview: 'LiveRamp publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Deliveries API, Destination Integrations API, Destinations API, and 5 more. Tagged areas include Data Connectivity, Identity Resolution, Activation, Clean Room, and Privacy.


  LiveRamp''s developer surface includes authentication, developer portal, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Liveramp Plans Pricing
  plan_count: 3
  slug: liveramp-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Liveramp Rate Limits
  slug: liveramp-rate-limits
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.1
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liveramp/refs/heads/main/screenshots/liveramp-2026-06-20T184618.png
security:
- kind: authentication
  name: Liveramp Authentication
  slug: liveramp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Liveramp Domain Security
  slug: liveramp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Liveramp Vulnerability Disclosure
  slug: liveramp-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Liveramp Trust Center
  slug: liveramp-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: liveramp
tags:
- Data Connectivity
- Identity Resolution
- Activation
- Clean Room
- Privacy
- AdTech
website: https://liveramp.com
---
