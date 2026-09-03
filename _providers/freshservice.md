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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Freshservice Agentic Access
  operation_count: 40
  slug: freshservice-agentic-access
  summary_line: 40 operations · 24 acting
api_count: 1
apis:
- description: REST API providing JSON-over-HTTP access to tickets, conversations, problems, changes, releases, assets, software, agents, requesters, groups, the service catalog, and approvals. Uses HTTP Basic authe
  name: Freshservice API v2
  slug: itsm-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Agents API from Freshservice — 2 operation(s) for agents.
  name: Freshservice Agents API
  slug: freshservice-agents-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Assets API from Freshservice — 2 operation(s) for assets.
  name: Freshservice Assets API
  slug: freshservice-assets-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Changes API from Freshservice — 2 operation(s) for changes.
  name: Freshservice Changes API
  slug: freshservice-changes-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Groups API from Freshservice — 2 operation(s) for groups.
  name: Freshservice Groups API
  slug: freshservice-groups-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Problems API from Freshservice — 2 operation(s) for problems.
  name: Freshservice Problems API
  slug: freshservice-problems-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Releases API from Freshservice — 2 operation(s) for releases.
  name: Freshservice Releases API
  slug: freshservice-releases-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Requesters API from Freshservice — 2 operation(s) for requesters.
  name: Freshservice Requesters API
  slug: freshservice-requesters-api
- baseURL: https://<domain>.freshservice.com/api/v2
  baseurl_source: declared
  description: The Tickets API from Freshservice — 2 operation(s) for tickets.
  name: Freshservice Tickets API
  slug: freshservice-tickets-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freshservice API v2 Agents API
  slug: open-freshservice-agents-api
- collection_type: open
  name: Freshservice API v2 Agents Assets API
  slug: open-freshservice-assets-api
- collection_type: open
  name: Freshservice API v2 Agents Changes API
  slug: open-freshservice-changes-api
- collection_type: open
  name: Freshservice API v2 Agents Groups API
  slug: open-freshservice-groups-api
- collection_type: open
  name: Freshservice API v2 Agents Problems API
  slug: open-freshservice-problems-api
- collection_type: open
  name: Freshservice API v2 Agents Releases API
  slug: open-freshservice-releases-api
- collection_type: open
  name: Freshservice API v2 Agents Requesters API
  slug: open-freshservice-requesters-api
- collection_type: open
  name: Freshservice API v2 Agents Tickets API
  slug: open-freshservice-tickets-api
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
overview: 'Freshservice publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Assets API, Changes API, and 5 more. Tagged areas include ITSM, Help Desk, Ticketing, Asset Management, and Change Management.


  Freshservice''s developer surface includes authentication, documentation, signup flow, pricing, support, and 8 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Help Desk
- Ticketing
- Asset Management
- Change Management
- Freshworks
website: https://www.freshworks.com/freshservice/
---
