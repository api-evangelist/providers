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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft To Do Agentic Access
  operation_count: 18
  slug: microsoft-to-do-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 4
apis:
- description: The ChecklistItems API from Microsoft to Do — 2 operation(s) for checklistitems.
  name: Microsoft to Do ChecklistItems API
  slug: microsoft-to-do-checklistitems-api
- description: The LinkedResources API from Microsoft to Do — 1 operation(s) for linkedresources.
  name: Microsoft to Do LinkedResources API
  slug: microsoft-to-do-linkedresources-api
- description: The TaskLists API from Microsoft to Do — 2 operation(s) for tasklists.
  name: Microsoft to Do TaskLists API
  slug: microsoft-to-do-tasklists-api
- description: The Tasks API from Microsoft to Do — 3 operation(s) for tasks.
  name: Microsoft to Do Tasks API
  slug: microsoft-to-do-tasks-api
artifact_total: 12
collections:
- collection_type: open
  name: Microsoft To Do API (Microsoft Graph)
  slug: open-microsoft-to-do
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-to-do-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-to-do-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-to-do-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-to-do-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://to-do.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/microsoft-to-do-list-app
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/todo-concept-overview
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-01'
description: Microsoft To Do is a task management application that helps users organize and manage their day. It provides API access through Microsoft Graph for managing task lists and tasks across Microsoft 365.
finops:
- name: Microsoft To Do Finops
  service_category: API
  slug: microsoft-to-do-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-to-do.png
layout: provider
modified: '2026-05-19'
name: Microsoft to Do
nav: Providers
network: true
overview: 'Microsoft to Do publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ChecklistItems API, LinkedResources API, TaskLists API, and 1 more. Tagged areas include Microsoft, Microsoft 365, Productivity, and Tasks.


  Microsoft to Do''s developer surface includes authentication, developer portal, documentation, support, and 9 more developer resources.'
plans:
- name: Microsoft To Do Plans Pricing
  plan_count: 3
  slug: microsoft-to-do-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Microsoft To Do Rate Limits
  slug: microsoft-to-do-rate-limits
score:
  band: developing
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.3
    developer_ergonomics: 39.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-to-do/refs/heads/main/screenshots/microsoft-to-do-2026-06-20T185539.png
security:
- kind: authentication
  name: Microsoft To Do Authentication
  slug: microsoft-to-do-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft To Do Domain Security
  slug: microsoft-to-do-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft To Do Vulnerability Disclosure
  slug: microsoft-to-do-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-to-do
tags:
- Microsoft
- Microsoft 365
- Productivity
- Tasks
website: https://www.microsoft.com/en-us/microsoft-365/microsoft-to-do-list-app
---
