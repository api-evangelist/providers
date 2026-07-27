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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Synthego Agentic Access
  operation_count: 3
  slug: synthego-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: The Order API from Synthego — 3 operation(s) for order.
  name: Synthego Order API
  slug: synthego-order-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synthego-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.synthego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.synthego.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.synthego.com/
- group: company
  title: ''
  type: Blog
  url: https://www.synthego.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.synthego.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synthego
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synthego.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthego.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.synthego.com/legal/iso-certification/
- group: auth
  title: ''
  type: Authentication
  url: authentication/synthego-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthego-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synthego-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synthego-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synthego-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synthego-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synthego-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/synthego-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/synthego-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthego-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/synthego-place-order.md
created: '2026-07-17'
description: Synthego is a genome-engineering company that manufactures synthetic guide RNA (sgRNA, crRNA, trRNA), CRISPR kits, and engineered cells for research and cell/gene-therapy development. Its public Synthego Order API is a third-party integration API that lets partners retrieve current product pricing, generate a priced order preview from a list of guide-RNA sequences, and track an order through to checkout on Synthego's eCommerce site. Authentication is by an API key passed in the SYNTHEGOAPIKEY header. Synthego was surfaced as a portfolio company of SoftBank Vision Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synthego.png
layout: provider
mcp_servers:
- description: ''
  name: synthego-mcp.yml
  slug: synthego-mcpyml
modified: '2026-07-21'
name: Synthego
nav: Providers
network: true
overview: 'Synthego publishes 1 API on the [APIs.io](https://apis.io/) network: Order API. Tagged areas include Company, Health Tech, Genomics, CRISPR, and Biotechnology.


  Synthego''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 65
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 37.7
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 39.3
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Synthego Authentication
  slug: synthego-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Synthego Domain Security
  slug: synthego-domain-security
  summary_line: TLSv1.2 · DMARC
slug: synthego
tags:
- Company
- Health Tech
- Genomics
- CRISPR
- Biotechnology
- Life Sciences
- Synthetic Biology
- Ordering
website: https://www.synthego.com/
---
