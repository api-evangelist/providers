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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Uncovr Agentic Access
  operation_count: 1
  slug: uncovr-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Inference (V3, Backwards Compatible) API from Uncovr — 1 operation(s) for inference (v3, backwards compatible).
  name: Uncovr Inference (V3, Backwards Compatible) API
  slug: uncovr-inference-v3-backwards-compatible-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uncovr Inference (V3, Backwards Compatible) Inference (V3, Backwards Compatible) Inference (V3, Backwards Compatible) API
  slug: open-uncovr-inference-v3-backwards-compatible-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/uncovr-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uncovr-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uncovr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uncovr.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uncovr-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uncovr-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uncovr-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uncovr.ai/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uncovr.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.uncovr.ai/contact
- group: company
  title: ''
  type: Careers
  url: https://www.uncovr.ai/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uncovr-uncover/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uncovr-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uncovr-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uncovr-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uncovr-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uncovr-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Uncovr is a surgical AI company building a foundation model for surgery. Its platform captures video from any operating-room source (laparoscopic, robotic, or other devices), analyzes procedures in real time, and automatically generates operative reports, CPT billing codes, and structured clinical intelligence, with a zero-PHI on-device anonymization architecture and EHR integration. Uncovr publishes no developer portal or SDKs, but serves a live OpenAPI 3.1 inference API (with Swagger UI) at api.uncovr.ai, and publishes an llms.txt on its website.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uncovr.png
layout: provider
mcp_servers:
- description: No official Uncovr MCP server was found (none in docs, npm, or the MCP registry surface we checked). Candidate tool list derived from the served OpenAPI 3.1 operations at https://api.uncovr.ai/openapi
  name: Uncovr MCP Server
  slug: uncovr-mcp-server
modified: '2026-07-21'
name: Uncovr
nav: Providers
network: true
overview: 'Uncovr publishes 1 API on the [APIs.io](https://apis.io/) network: Inference (V3, Backwards Compatible) API. Tagged areas include Company, Healthcare, Surgery, Artificial Intelligence, and Computer-Vision.


  Uncovr''s developer surface includes authentication, support, and 16 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 31.5
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 48.3
    developer_ergonomics: 18.5
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Uncovr Authentication
  slug: uncovr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uncovr Domain Security
  slug: uncovr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: uncovr
tags:
- Company
- Healthcare
- Surgery
- Artificial Intelligence
- Computer-Vision
- Medical Documentation
- Medical Billing
- Clinical Intelligence
website: https://www.uncovr.ai/
---
