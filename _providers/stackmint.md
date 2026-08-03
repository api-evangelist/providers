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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Stackmint Agentic Access
  operation_count: 11
  slug: stackmint-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 3
apis:
- description: 'REST API for managing Stackmint workflows. Provides endpoints for listing and retrieving clients (orgs), enumerating and running Branches (composable workflows) and Buds (atomic execution units), and '
  name: Stackmint Platform API
  slug: platform-api
- description: The Admin API from Stackmint — 2 operation(s) for admin.
  name: Stackmint Admin API
  slug: stackmint-admin-api
- description: The Clients API from Stackmint — 9 operation(s) for clients.
  name: Stackmint Clients API
  slug: stackmint-clients-api
artifact_total: 9
collections:
- collection_type: open
  name: Stackmint Platform API
  slug: open-stackmint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stackmint-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stackmint-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackmint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackmint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stackmint-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://stackmint.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://stackmint.ai/en/developers
- group: docs
  title: ''
  type: APIReference
  url: https://stackmint.ai/en/api-reference
- group: other
  title: ''
  type: Semantic Standard
  url: https://stackmint.ai/en/semantic-standard
- group: company
  title: ''
  type: Blog
  url: https://stackmint.ai/en/blog
- group: start
  title: ''
  type: Signup
  url: https://stackmint.ai/en/signup
- group: other
  title: ''
  type: Models
  url: https://stackmint.ai/en/models
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackmint-ai
- group: operate
  title: ''
  type: Support
  url: mailto:api@stackmint.ai
created: '2026-05-15'
description: Stackmint is a governed execution platform for enterprise AI workflows. Rather than deploying raw agents, the platform packages AI capabilities with built-in controls — budget circuit breakers, human approval gates, compliance routing, and ROI measurement — so organizations can move AI projects from research into production with auditable execution paths. The platform exposes a Semantic Execution Layer (SEL) of ontology, semantics, branches, agents, and runtime/audit, and offers a REST API for managing clients, branches (workflows), buds (atomic units), and MCP-compatible tool surfaces for LLM integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackmint.png
layout: provider
modified: '2026-05-15'
name: Stackmint
nav: Providers
network: true
overview: 'Stackmint publishes 2 APIs on the [APIs.io](https://apis.io/) network: Admin API and Clients API. Tagged areas include AI Governance, AI Agents, Workflow Automation, Enterprise AI, and MCP.


  Stackmint''s developer surface includes authentication, documentation, API reference, engineering blog, signup flow, support, and 8 more developer resources.'
random_paper: 24
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 54.3
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackmint/refs/heads/main/screenshots/stackmint-2026-06-20T194447.png
security:
- kind: authentication
  name: Stackmint Authentication
  slug: stackmint-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Stackmint Domain Security
  slug: stackmint-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Stackmint Vulnerability Disclosure
  slug: stackmint-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Stackmint Trust Center
  slug: stackmint-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: stackmint
tags:
- AI Governance
- AI Agents
- Workflow Automation
- Enterprise AI
- MCP
- Semantic Layer
- Audit
- Compliance
website: https://stackmint.ai/
---
