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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Passbase Agentic Access
  operation_count: 6
  slug: passbase-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: Access verified identities, their resources and resource files.
  name: Passbase Identity API
  slug: passbase-identity-api
- description: Read project settings and verification configuration.
  name: Passbase Project API
  slug: passbase-project-api
artifact_total: 7
asyncapis:
- description: ''
  name: Passbase Webhooks
  slug: passbase-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.passbase.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/passbase
- group: build
  title: ''
  type: Packages
  url: packages/passbase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/passbase-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/passbase-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/passbase-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/passbase-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/passbase-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/passbase-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/passbase-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/passbase-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/passbase-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/passbase-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passbase-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/passbase-agentic-access.yml
created: '2026-07-17'
description: Passbase was a developer-first identity verification (KYC) platform founded in Berlin and San Francisco that let companies verify users in seconds through facial comparison, liveness detection, and authenticity checks on government-issued IDs from 190+ countries. It shipped mobile and web client SDKs plus a server-side Verifications API (v2) for reading verified identities, their resources and data points, and project settings, with webhooks for verification lifecycle events. Passbase was acquired by Parallel Markets in March 2023; api.passbase.com and docs.passbase.com are no longer live, and this API Evangelist profile captures the last-published API surface reconstructed from the company's official OpenAPI-generated SDKs. Backed by Cowboy Ventures and Seedcamp.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/passbase.png
layout: provider
mcp_servers:
- description: ''
  name: passbase-mcp.yml
  slug: passbase-mcpyml
modified: '2026-07-20'
name: Passbase
nav: Providers
network: true
overview: 'Passbase publishes 2 APIs on the [APIs.io](https://apis.io/) network: Identity API and Project API. Tagged areas include Company, Security, Identity Verification, KYC, and Biometrics.


  The Passbase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Passbase''s developer surface includes authentication and 15 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 72.9
    developer_ergonomics: 21.2
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passbase/refs/heads/main/screenshots/passbase-2026-08-07T191532.png
security:
- kind: authentication
  name: Passbase Authentication
  slug: passbase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Passbase Domain Security
  slug: passbase-domain-security
  summary_line: TLSv1.3 · HSTS
slug: passbase
tags:
- Company
- Security
- Identity Verification
- KYC
- Biometrics
- Authentication
- Identity
- Compliance
website: https://www.passbase.com
---
