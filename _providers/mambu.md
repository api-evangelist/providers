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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Mambu's REST API v2 for core banking — clients, loan accounts, deposit accounts, transactions, and related resources. Tenant-scoped host, HTTPS Basic or apikey auth, Idempotency-Key supported for writ
  name: Mambu API v2
  slug: mambu-api-v2
artifact_total: 5
asyncapis:
- description: ''
  name: Mambu Events
  slug: mambu-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.mambu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mambu.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mambu.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mambu.com/api/
- group: operate
  title: ''
  type: Support
  url: https://support.mambu.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mambu.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mambu.com/en/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mambu.com/release-notes/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mambu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mambu-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mambu-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mambu-events.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mambu-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mambu.com/api/
- group: design
  title: ''
  type: Conformance
  url: conformance/mambu-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mambu-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mambu-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mambu-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/mambu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mambu-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mambu-gmbh
created: '2026-07-17'
description: Mambu is a SaaS cloud banking platform — a composable, API-first core banking engine that financial institutions use to build and run lending, deposit, payment, and Islamic banking products. Banks, neobanks, fintechs, lenders, and non-financial brands (telcos, retailers) use Mambu to modernize legacy cores and launch products faster, operating across 65+ countries and serving 230M+ end users. Mambu exposes a REST API v2 (with separate Payments, Streaming, and Audit Trail APIs), customizable webhooks, and a resumable event-streaming surface, secured with HTTPS Basic auth or apikey headers and supporting Idempotency-Key for safe writes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mambu.png
layout: provider
mcp_servers:
- description: ''
  name: mambu-mcp.yml
  slug: mambu-mcpyml
modified: '2026-07-20'
name: Mambu
nav: Providers
network: true
overview: 'Mambu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Core Banking, and Lending.


  The Mambu catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mambu''s developer surface includes documentation, API reference, support, changelog, authentication, and 16 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 40.5
  delta: 4.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 36.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mambu/refs/heads/main/screenshots/mambu-2026-07-25T230014.png
security:
- kind: authentication
  name: Mambu Authentication
  slug: mambu-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Mambu Domain Security
  slug: mambu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mambu
tags:
- Company
- Fintech
- Banking
- Core Banking
- Lending
- Deposits
- Payments
- SaaS
- Embedded Finance
- Banking as a Service
website: https://www.mambu.com/
---
