---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Freshservice Agentic Access
  operation_count: 40
  slug: freshservice-agentic-access
  summary_line: 40 operations · 24 acting
api_count: 9
apis:
- description: REST API providing JSON-over-HTTP access to tickets, conversations, problems, changes, releases, assets, software, agents, requesters, groups, the service catalog, and approvals. Uses HTTP Basic authe
  name: Freshservice API v2
  slug: itsm-api
- description: The Agents API from Freshservice — 2 operation(s) for agents.
  name: Freshservice Agents API
  slug: freshservice-agents-api
- description: The Assets API from Freshservice — 2 operation(s) for assets.
  name: Freshservice Assets API
  slug: freshservice-assets-api
- description: The Changes API from Freshservice — 2 operation(s) for changes.
  name: Freshservice Changes API
  slug: freshservice-changes-api
- description: The Groups API from Freshservice — 2 operation(s) for groups.
  name: Freshservice Groups API
  slug: freshservice-groups-api
- description: The Problems API from Freshservice — 2 operation(s) for problems.
  name: Freshservice Problems API
  slug: freshservice-problems-api
- description: The Releases API from Freshservice — 2 operation(s) for releases.
  name: Freshservice Releases API
  slug: freshservice-releases-api
- description: The Requesters API from Freshservice — 2 operation(s) for requesters.
  name: Freshservice Requesters API
  slug: freshservice-requesters-api
- description: The Tickets API from Freshservice — 2 operation(s) for tickets.
  name: Freshservice Tickets API
  slug: freshservice-tickets-api
artifact_total: 15
collections:
- collection_type: open
  name: Freshservice API v2
  slug: open-freshservice
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshservice-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freshservice-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/freshservice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshservice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshservice-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshservice
- group: company
  title: ''
  type: Website
  url: https://www.freshworks.com/freshservice/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.freshservice.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.freshservice.com/
- group: start
  title: ''
  type: Signup
  url: https://www.freshworks.com/freshservice/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freshworks.com/freshservice/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.freshservice.com/
created: '2026-05-11'
description: Freshservice is Freshworks' cloud-based IT service management (ITSM) and enterprise service management platform, covering ticketing, problem, change and release management, asset and configuration management, and a self-service portal. The Freshservice REST API provides JSON-over-HTTP access to tickets, problems, changes, assets, agents, requesters, and the service catalog for ITSM automation and integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshservice.png
layout: provider
modified: '2026-05-11'
name: Freshservice
nav: Providers
network: true
overview: 'Freshservice publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Assets API, Changes API, and 5 more. Tagged areas include ITSM, IT Service Management, Help Desk, Ticketing, and Asset Management.


  Freshservice''s developer surface includes authentication, documentation, signup flow, pricing, support, and 8 more developer resources.'
random_paper: 74
score:
  band: thin
  composite: 30.4
  delta: -2.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 48.3
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshservice/refs/heads/main/screenshots/freshservice-2026-06-20T181545.png
security:
- kind: authentication
  name: Freshservice Authentication
  slug: freshservice-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freshservice Domain Security
  slug: freshservice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Freshservice Vulnerability Disclosure
  slug: freshservice-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Freshservice Trust Center
  slug: freshservice-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: freshservice
tags:
- ITSM
- IT Service Management
- Help Desk
- Ticketing
- Asset Management
- Change Management
- Freshworks
website: https://www.freshworks.com/freshservice/
---
