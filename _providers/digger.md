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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API for OpenComputer — create and manage persistent cloud sandbox VMs, run commands and files inside them, checkpoint/fork, expose preview URLs, run durable agent sessions, and register signed we
  name: OpenComputer API
  slug: opencomputer-api
artifact_total: 4
asyncapis:
- description: ''
  name: Digger Opencomputer Webhooks
  slug: digger-opencomputer-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://digger.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opencomputer.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opencomputer.dev/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opentaco.dev/onboarding/account-setup
- group: company
  title: ''
  type: Blog
  url: https://opencomputer.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://opencomputer.dev/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.opencomputer.dev/
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/diggertalk/shared_invite/zt-1tocl4w0x-E3RkpPiK7zQkehl8O78g8Q
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diggerhq
- group: auth
  title: ''
  type: Authentication
  url: authentication/digger-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/digger-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digger-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/digger-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digger-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/digger-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/digger-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digger-opencomputer-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/digger-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/digger-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.opentaco.dev/ce/features/fips-140
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digger-domain-security.yml
created: '2026-07-17'
description: 'Digger (diggerhq), backed by Initialized Capital, builds developer infrastructure across two open-source-rooted product lines. OpenTaco (formerly the Digger CE project) is an Infrastructure-as-Code orchestration and Terraform/OpenTofu state-management platform that runs plan/apply inside your existing CI pipeline, with PR automation, PR-level locks, drift detection and remediation, RBAC via Open Policy Agent, and FIPS 140 support; it is self-hostable via Docker Compose, Railway, and Kubernetes. OpenComputer is the company''s flagship agent-infrastructure product: persistent, long-running cloud VMs for AI agents — real Linux machines that hibernate when idle and wake in seconds, with checkpoints, preview URLs, per-tenant package control, a REST API, TypeScript and Python SDKs, the oc CLI, durable agent sessions, and signed, retriable webhooks for sandbox lifecycle events.'
image: https://opencomputer.dev/social-preview.png
layout: provider
modified: '2026-07-18'
name: Digger
nav: Providers
network: true
overview: 'Digger publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Cloud Sandbox, Compute, and Infrastructure as Code.


  The Digger catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Digger''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 14 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 37.8
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digger/refs/heads/main/screenshots/digger-2026-07-25T212000.png
security:
- kind: authentication
  name: Digger Authentication
  slug: digger-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Digger Domain Security
  slug: digger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digger
tags:
- Company
- AI Agents
- Cloud Sandbox
- Compute
- Infrastructure as Code
- Terraform
- OpenTofu
- Developer Tools
- Webhook
- Open-Source
- SDK
- CLI
website: https://digger.dev/
---
