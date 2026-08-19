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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Podio Agentic Access
  operation_count: 6
  slug: podio-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 6
apis:
- description: REST API providing complete programmatic access to Podio apps, items, workspaces, organizations, users, tasks, files, comments, and webhooks. Authentication uses OAuth2 with several supported flows (s
  name: Podio REST API
  slug: rest-api
- description: Podio application definitions.
  name: Podio Applications API
  slug: podio-applications-api
- description: Webhooks.
  name: Podio Hooks API
  slug: podio-hooks-api
- description: Items (records) inside Podio applications.
  name: Podio Items API
  slug: podio-items-api
- description: OAuth 2.0 authorization endpoints.
  name: Podio OAuth API
  slug: podio-oauth-api
- description: Work tasks.
  name: Podio Tasks API
  slug: podio-tasks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Podio Applications API
  slug: open-podio-applications-api
- collection_type: open
  name: Podio Applications Hooks API
  slug: open-podio-hooks-api
- collection_type: open
  name: Podio Applications Items API
  slug: open-podio-items-api
- collection_type: open
  name: Podio Applications OAuth API
  slug: open-podio-oauth-api
- collection_type: open
  name: Podio Applications Tasks API
  slug: open-podio-tasks-api
- collection_type: open
  name: Podio API
  slug: open-podio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podio-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/podio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/podio-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/citrix-work-collaboration-solutions
- group: company
  title: ''
  type: Website
  url: https://www.podio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.podio.com
- group: operate
  title: ''
  type: Help Center
  url: https://help.podio.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.podio.com/site/en/premium
- group: start
  title: ''
  type: Signup
  url: https://podio.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.podio.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/podio
- group: docs
  title: ''
  type: Progress Podio Docs
  url: https://docs.sharefile.com/en-us/podio.html
created: '2026-05-11'
description: Podio is a flexible work management and collaboration platform (originally acquired by Citrix in 2012, and now part of Progress Software following the October 2024 acquisition of ShareFile and Podio) that lets teams build custom apps, workspaces, and workflows for project management, CRM, and internal operations. The Podio API offers a complete programmable interface to all Podio functionality including apps, items, tasks, workspaces, users, files, and webhooks, with official client libraries available for PHP, .NET, Ruby, Java, Python, Android, and Objective-C.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podio.png
layout: provider
modified: '2026-05-11'
name: Podio
nav: Providers
network: true
overview: 'Podio publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Hooks API, Items API, and 2 more. Tagged areas include Work Management, Collaboration, Project Management, CRM, and Workflow.


  Podio''s developer surface includes authentication, documentation, pricing, signup flow, and 10 more developer resources.'
random_paper: 92
scopes:
- name: Podio Scopes
  scope_count: 5
  slug: podio-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 33.1
  delta: -0.7
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podio/refs/heads/main/screenshots/podio-2026-06-20T191835.png
security:
- kind: authentication
  name: Podio Authentication
  slug: podio-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Podio Domain Security
  slug: podio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Podio Vulnerability Disclosure
  slug: podio-vulnerability-disclosure
  summary_line: disclosure policy published
slug: podio
tags:
- Work Management
- Collaboration
- Project Management
- CRM
- Workflow
- Custom Apps
website: https://www.podio.com
---
