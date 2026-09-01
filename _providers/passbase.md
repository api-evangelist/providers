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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Passbase Agentic Access
  operation_count: 6
  slug: passbase-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Access verified identities, their resources and resource files.
  name: Passbase Identity API
  slug: passbase-identity-api
- description: Read project settings and verification configuration.
  name: Passbase Project API
  slug: passbase-project-api
artifact_total: 10
asyncapis:
- description: ''
  name: Passbase Webhooks
  slug: passbase-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Passbase Verifications Identity API
  slug: open-passbase-identity-api
- collection_type: open
  name: Passbase Verifications Identity Project API
  slug: open-passbase-project-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/passbase-verification-overlay.yaml
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
  name: Passbase MCP Server
  slug: passbase-mcp-server
modified: '2026-07-20'
name: Passbase
nav: Providers
network: true
overview: 'Passbase publishes 2 APIs on the [APIs.io](https://apis.io/) network: Identity API and Project API. Tagged areas include Company, Security, Identity Verification, KYC, and Biometrics.


  The Passbase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Passbase''s developer surface includes authentication and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 61.6
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
