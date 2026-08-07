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
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API exposed by the OPAQUE client / API pod for the Confidential AI Platform. Covers workspaces, datasets and data upload from AWS S3 / Azure Blob / Azure Files / Google Cloud Storage, analytics a
  name: OPAQUE Platform REST API
  slug: opaque-platform-rest-api
artifact_total: 3
common:
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
modified: '2026-08-04'
name: OPAQUE
nav: Providers
network: true
overview: 'OPAQUE publishes 1 API on the [APIs.io](https://apis.io/) network: Platform REST API. Tagged areas include confidential-computing, confidential-ai, ai-governance, data-privacy, and trusted-execution-environment.


  OPAQUE''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 18 more developer resources.'
random_paper: 86
score:
  band: developing
  composite: 45.4
  delta: -0.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.3
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 46.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
