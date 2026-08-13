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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Hpe Agentic Access
  operation_count: 20
  slug: hpe-agentic-access
  summary_line: 20 operations · 14 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Unified REST API gateway for HPE GreenLake edge-to-cloud services including Compute Ops Management, Data Services Cloud Console, identity, workspaces, and API client credentials. Conforms to OpenAPI 3
  name: HPE GreenLake API
  slug: greenlake-api
- description: The Authorization API from Hewlett Packard Enterprise — 7 operation(s) for authorization.
  name: Hewlett Packard Enterprise Authorization API
  slug: hpe-authorization-api
- description: The Identity API from Hewlett Packard Enterprise — 2 operation(s) for identity.
  name: Hewlett Packard Enterprise Identity API
  slug: hpe-identity-api
- description: The Workspaces API from Hewlett Packard Enterprise — 3 operation(s) for workspaces.
  name: Hewlett Packard Enterprise Workspaces API
  slug: hpe-workspaces-api
artifact_total: 8
collections:
- collection_type: open
  name: HPE GreenLake API
  slug: open-hpe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hpe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hpe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hpe-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HewlettPackard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hewlett-packard-enterprise
- group: company
  title: ''
  type: Website
  url: https://www.hpe.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.greenlake.hpe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hpe.com
- group: start
  title: ''
  type: Signup
  url: https://common.cloud.hpe.com/sign-up
created: '2026-05-11'
description: Hewlett Packard Enterprise (HPE) is a global edge-to-cloud technology company providing servers, storage, networking, and hybrid cloud services, with HPE GreenLake serving as the unified edge-to-cloud platform delivering infrastructure as a service. The HPE GreenLake developer platform exposes OpenAPI 3.0 REST APIs covering compute, storage, networking, data services, identity, and workspace management, all authenticated via OAuth 2.0 client credentials and bearer tokens through a unified global API gateway.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hpe.png
layout: provider
modified: '2026-05-11'
name: Hewlett Packard Enterprise
nav: Providers
network: true
overview: 'Hewlett Packard Enterprise publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authorization API, Identity API, and Workspaces API. Tagged areas include Cloud, Edge to Cloud, Infrastructure as a Service, Compute, and Storage.


  Hewlett Packard Enterprise''s developer surface includes authentication, documentation, signup flow, and 6 more developer resources.'
random_paper: 77
score:
  band: thin
  composite: 30.2
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 55.2
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hpe/refs/heads/main/screenshots/hpe-2026-06-20T182854.png
security:
- kind: authentication
  name: Hpe Authentication
  slug: hpe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hpe Domain Security
  slug: hpe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hpe
tags:
- Cloud
- Edge to Cloud
- Infrastructure as a Service
- Compute
- Storage
- Networking
- Hybrid Cloud
- Enterprise IT
website: https://www.hpe.com
---
