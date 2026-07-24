---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Printnode Agentic Access
  operation_count: 31
  slug: printnode-agentic-access
  summary_line: 31 operations · 11 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: The Account API from PrintNode — 4 operation(s) for account.
  name: PrintNode Account API
  slug: printnode-account-api
- description: The API Keys API from PrintNode — 1 operation(s) for api keys.
  name: PrintNode API Keys API
  slug: printnode-api-keys-api
- description: The Clients API from PrintNode — 1 operation(s) for clients.
  name: PrintNode Clients API
  slug: printnode-clients-api
- description: The Computers API from PrintNode — 2 operation(s) for computers.
  name: PrintNode Computers API
  slug: printnode-computers-api
- description: The Printers API from PrintNode — 3 operation(s) for printers.
  name: PrintNode Printers API
  slug: printnode-printers-api
- description: The PrintJobs API from PrintNode — 4 operation(s) for printjobs.
  name: PrintNode PrintJobs API
  slug: printnode-printjobs-api
- description: The Scales API from PrintNode — 3 operation(s) for scales.
  name: PrintNode Scales API
  slug: printnode-scales-api
- description: The Utility API from PrintNode — 2 operation(s) for utility.
  name: PrintNode Utility API
  slug: printnode-utility-api
- description: The Webhooks API from PrintNode — 1 operation(s) for webhooks.
  name: PrintNode Webhooks API
  slug: printnode-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: PrintNode API
  slug: open-printnode
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/printnode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printnode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/printnode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrintNode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printnode
- group: company
  title: ''
  type: Website
  url: https://www.printnode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.printnode.com/en/docs/api/curl
- group: commercial
  title: ''
  type: Plans
  url: plans/printnode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/printnode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/printnode-finops.yml
created: '2026-06-25'
description: PrintNode is a cloud and remote printing service that lets web and server applications print to any physical printer through a lightweight client installed on a remote computer. Its REST API at https://api.printnode.com covers accounts, computers, printers, print jobs, scales, child-account/API-key management, and webhooks, using HTTP Basic authentication with an API key.
finops:
- name: Printnode Finops
  service_category: Printing and Output Management
  slug: printnode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printnode.png
layout: provider
modified: '2026-06-25'
name: PrintNode
nav: Providers
network: true
overview: 'PrintNode publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Clients API, and 6 more. Tagged areas include Printing, Cloud Printing, Remote Printing, Print Jobs, and Hardware.


  PrintNode''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Printnode Plans Pricing
  plan_count: 7
  slug: printnode-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Printnode Rate Limits
  slug: printnode-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Printnode Authentication
  slug: printnode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Printnode Domain Security
  slug: printnode-domain-security
  summary_line: TLSv1.3 · DMARC
slug: printnode
tags:
- Printing
- Cloud Printing
- Remote Printing
- Print Jobs
- Hardware
website: https://www.printnode.com/
---
