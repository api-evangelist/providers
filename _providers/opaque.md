---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-11'
api_count: 11
apis:
- description: Asset Configurations
  name: OPAQUE Asset Configs API
  slug: opaque-asset-configs-api
- description: Authentication
  name: OPAQUE Auth API
  slug: opaque-auth-api
- description: Data & Datum
  name: OPAQUE Datasets API
  slug: opaque-datasets-api
- description: Jobs
  name: OPAQUE Jobs API
  slug: opaque-jobs-api
- description: The organizations API from OPAQUE — 4 operation(s) for organizations.
  name: OPAQUE Organizations API
  slug: opaque-organizations-api
- description: The pinned-queries API from OPAQUE — 3 operation(s) for pinned-queries.
  name: OPAQUE Pinned Queries API
  slug: opaque-pinned-queries-api
- description: The predefined-query-templates API from OPAQUE — 3 operation(s) for predefined-query-templates.
  name: OPAQUE Predefined Query Templates API
  slug: opaque-predefined-query-templates-api
- description: Users
  name: OPAQUE Users API
  slug: opaque-users-api
- description: The versioning API from OPAQUE — 1 operation(s) for versioning.
  name: OPAQUE Versioning API
  slug: opaque-versioning-api
- description: The workflows API from OPAQUE — 9 operation(s) for workflows.
  name: OPAQUE Workflows API
  slug: opaque-workflows-api
- description: Workspaces
  name: OPAQUE Workspaces API
  slug: opaque-workspaces-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opaque-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opaque-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opaque.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.opaque.co/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opaque.co/en/latest/public_guide/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opaque.co/en/latest/api_reference/rest_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opaque.co/en/latest/public_guide/users/get_started/
- group: operate
  title: ''
  type: Support
  url: https://docs.opaque.co/en/latest/support/
- group: company
  title: ''
  type: Blog
  url: https://www.opaque.co/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opaque-systems
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opaque.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opaque.co/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.opaque.co/en/latest/release_notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opaque-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opaque-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opaque-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opaque-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opaque-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opaque-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opaque.co/resources/articles/the-opaque-platform-is-now-soc-2-certified
- group: design
  title: ''
  type: DataModel
  url: data-model/opaque-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/opaque-platform-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opaque-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/opaque-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opaque-sandbox.yml
created: '2026-08-04'
description: 'OPAQUE Systems, Inc. is a confidential-AI platform company that lets enterprises run AI and analytics on their most sensitive data without exposing it. The OPAQUE Confidential AI Platform executes agentic workflows, retrieval-augmented generation, and analytics jobs inside hardware trusted execution environments (TEEs), with attested TLS between components, signed attestation reports, and tamper-evident audit logs so every run can be independently verified. It is deployed in a hybrid architecture: an OPAQUE-hosted control plane manages users, workspaces, job metadata, notifications, audit logging, and key management, while the data plane, client/API pod, and encrypted storage all run inside the customer''s own cloud environment. The platform exposes a documented REST API (workspaces, datasets, jobs, workflows, asset configs, users, organizations) described by an OpenAPI 3.0.3 specification, plus a Python SDK for invoking deployed workflows. It is used in insurance, financial
  services, and high-tech for confidential RAG, secure multi-party analytics, and governed agent execution.'
image: https://cdn.prod.website-files.com/66d977be14c1ef2f8e88c93c/68cb38f2400045b985a92458_Opaque%20Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: opaque-mcp.yml
  slug: opaque-mcpyml
modified: '2026-08-04'
name: OPAQUE
nav: Providers
network: true
overview: 'OPAQUE publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Asset Configs API, Auth API, Datasets API, and 8 more. Tagged areas include confidential-computing, confidential-ai, ai-governance, data-privacy, and trusted-execution-environment.


  OPAQUE''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 19 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 44.8
  delta: -0.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.4
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 45.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opaque/refs/heads/main/screenshots/opaque-2026-08-07T190445.png
security:
- kind: authentication
  name: Opaque Authentication
  slug: opaque-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Opaque Domain Security
  slug: opaque-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opaque
tags:
- confidential-computing
- confidential-ai
- ai-governance
- data-privacy
- trusted-execution-environment
- attestation
- agentic-workflows
- retrieval-augmented-generation
- enterprise-ai
- secure-analytics
- data-clean-room
- model-context-protocol
website: https://www.opaque.co/
---
