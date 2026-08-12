---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 130
  human_in_the_loop: 9
  name: Daytona Agentic Access
  operation_count: 238
  slug: daytona-agentic-access
  summary_line: 238 operations · 130 acting · 9 human-in-the-loop
api_count: 19
apis:
- description: The admin API from Daytona — 15 operation(s) for admin.
  name: Daytona admin API
  slug: daytona-admin-api
- description: The api-keys API from Daytona — 4 operation(s) for api-keys.
  name: Daytona api-keys API
  slug: daytona-api-keys-api
- description: The audit API from Daytona — 1 operation(s) for audit.
  name: Daytona audit API
  slug: daytona-audit-api
- description: The config API from Daytona — 1 operation(s) for config.
  name: Daytona config API
  slug: daytona-config-api
- description: The docker-registry API from Daytona — 3 operation(s) for docker-registry.
  name: Daytona docker-registry API
  slug: daytona-docker-registry-api
- description: The Health API from Daytona — 2 operation(s) for health.
  name: Daytona Health API
  slug: daytona-health-api
- description: The jobs API from Daytona — 4 operation(s) for jobs.
  name: Daytona jobs API
  slug: daytona-jobs-api
- description: The object-storage API from Daytona — 1 operation(s) for object-storage.
  name: Daytona object-storage API
  slug: daytona-object-storage-api
- description: The organizations API from Daytona — 30 operation(s) for organizations.
  name: Daytona organizations API
  slug: daytona-organizations-api
- description: The preview API from Daytona — 4 operation(s) for preview.
  name: Daytona preview API
  slug: daytona-preview-api
- description: The regions API from Daytona — 1 operation(s) for regions.
  name: Daytona regions API
  slug: daytona-regions-api
- description: The runners API from Daytona — 9 operation(s) for runners.
  name: Daytona runners API
  slug: daytona-runners-api
- description: The sandbox API from Daytona — 37 operation(s) for sandbox.
  name: Daytona sandbox API
  slug: daytona-sandbox-api
- description: The snapshots API from Daytona — 6 operation(s) for snapshots.
  name: Daytona snapshots API
  slug: daytona-snapshots-api
- description: The toolbox API from Daytona — 61 operation(s) for toolbox.
  name: Daytona toolbox API
  slug: daytona-toolbox-api
- description: The users API from Daytona — 5 operation(s) for users.
  name: Daytona users API
  slug: daytona-users-api
- description: The volumes API from Daytona — 3 operation(s) for volumes.
  name: Daytona volumes API
  slug: daytona-volumes-api
- description: The webhooks API from Daytona — 3 operation(s) for webhooks.
  name: Daytona webhooks API
  slug: daytona-webhooks-api
- description: The workspace API from Daytona — 12 operation(s) for workspace.
  name: Daytona workspace API
  slug: daytona-workspace-api
artifact_total: 27
collections:
- collection_type: open
  name: Daytona
  slug: open-daytona
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/daytonaio/daytona/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/daytonaio/daytona/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/daytona-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/daytona-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daytona-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/daytona-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.daytona.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.daytona.io/docs
- group: company
  title: ''
  type: Blog
  url: https://www.daytona.io/dotfiles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daytonaio
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/daytonaio/daytona
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daytona.io/pricing
- group: other
  title: ''
  type: Customers
  url: https://www.daytona.io/customers
- group: start
  title: ''
  type: Signup
  url: https://app.daytona.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daytona.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daytona.io/privacy
created: '2026-05-23'
description: Daytona provides secure, elastic sandbox infrastructure for running AI-generated code, with sub-90ms sandbox creation, multi-language runtimes, and full filesystem, process, Git, and Language Server Protocol APIs. Sandboxes are stateful, snapshot-able, and deployable across US, EU, and Asia regions, and the platform supports HIPAA, SOC 2, and GDPR. Target customers are AI agent companies, coding-agent builders, data teams, RL labs, and enterprises that need to execute untrusted or LLM-authored code in isolation. Daytona ships Python and TypeScript SDKs (with Ruby, Go, and Java available) backed by a documented REST API and OpenAPI specs. Pricing is pay-as-you-go and per-second across vCPU, memory, GPU, and storage with a $200 free credit.
finops:
- name: Daytona Finops
  service_category: API
  slug: daytona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/daytona.png
layout: provider
modified: '2026-05-23'
name: Daytona
nav: Providers
network: true
overview: 'Daytona publishes 19 APIs on the [APIs.io](https://apis.io/) network, including admin API, api-keys API, audit API, and 16 more. Tagged areas include Sandboxes, Secure Execution, AI Agents, Coding Agents, and Code Interpreter.


  Daytona''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Daytona Plans Pricing
  plan_count: 1
  slug: daytona-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 2
  name: Daytona Rate Limits
  slug: daytona-rate-limits
score:
  band: developing
  composite: 45.1
  delta: 4.2
  facets:
    commercial_clarity: 81.6
    contract_quality: 46.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daytona/refs/heads/main/screenshots/daytona-2026-06-20T175735.png
security:
- kind: authentication
  name: Daytona Authentication
  slug: daytona-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Daytona Domain Security
  slug: daytona-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Daytona Trust Center
  slug: daytona-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: daytona
tags:
- Sandboxes
- Secure Execution
- AI Agents
- Coding Agents
- Code Interpreter
- Snapshots
- Multi-Region
- HIPAA
- SOC 2
- GDPR
- Python
- TypeScript
- Open Source
- LSP
website: https://www.daytona.io
---
