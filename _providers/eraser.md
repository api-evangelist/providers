---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Eraser Agentic Access
  operation_count: 20
  slug: eraser-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 7
apis:
- description: Retrieve previously generated AI diagram requests
  name: Eraser AI Requests API
  slug: eraser-ai-requests-api
- description: Query audit events for compliance and monitoring
  name: Eraser Audit Logs API
  slug: eraser-audit-logs-api
- description: Manage diagram elements within files
  name: Eraser Diagram Elements API
  slug: eraser-diagram-elements-api
- description: Generate diagrams from natural language prompts or Eraser DSL using AI
  name: Eraser Diagrams (AI) API
  slug: eraser-diagrams-ai-api
- description: Create and manage Eraser files
  name: Eraser Files API
  slug: eraser-files-api
- description: Create and manage folders for organizing files
  name: Eraser Folders API
  slug: eraser-folders-api
- description: Retrieve team usage and activity metrics
  name: Eraser Usage Metrics API
  slug: eraser-usage-metrics-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eraser-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eraser-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eraser-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.eraser.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eraser.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.eraser.io/reference
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/eraserlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eraser
- group: company
  title: ''
  type: Blog
  url: https://www.eraser.io/decision-node
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eraser.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/eraserlabs
- group: commercial
  title: ''
  type: Plans
  url: plans/eraser-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eraser-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eraser-finops.yml
created: '2026-06-13'
description: Eraser is an AI-powered diagramming and technical documentation platform designed for engineering teams. It provides a REST API for generating diagrams from natural language prompts or structured DSL, managing files and workspaces, and embedding interactive technical visuals into documentation workflows. The platform supports a wide range of diagram types including flow charts, ERDs, sequence diagrams, cloud architecture diagrams, and BPMN diagrams. Eraser integrates with tools such as GitHub, VS Code, Notion, and Confluence, and provides an MCP server for AI agent-driven diagram automation.
examples:
- key_count: 4
  name: Eraser Create File Example
  slug: eraser-create-file-example
- key_count: 4
  name: Eraser Generate Diagram Example
  slug: eraser-generate-diagram-example
finops:
- name: Eraser Finops
  service_category: ''
  slug: eraser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eraser.png
json_schemas:
- name: Eraser Diagram
  property_count: 5
  slug: eraser-diagram
- name: Eraser File
  property_count: 9
  slug: eraser-file
- name: Eraser Folder
  property_count: 8
  slug: eraser-folder
jsonld:
- class_count: 10
  name: Eraser Context
  property_count: 45
  slug: eraser-context
layout: provider
modified: '2026-06-13'
name: Eraser
nav: Providers
network: true
overview: 'Eraser publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AI Requests API, Audit Logs API, Diagram Elements API, and 4 more. Tagged areas include Diagrams, Documentation, AI, Technical Documentation, and Diagramming.


  The Eraser catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Eraser''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Eraser Plans Pricing
  plan_count: 4
  slug: eraser-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 0
  name: Eraser Rate Limits
  slug: eraser-rate-limits
rules:
- name: Eraser API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: eraser-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.1
  delta: -0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eraser/refs/heads/main/screenshots/eraser-2026-06-20T180810.png
security:
- kind: authentication
  name: Eraser Authentication
  slug: eraser-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Eraser Domain Security
  slug: eraser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eraser
tags:
- Diagrams
- Documentation
- AI
- Technical Documentation
- Diagramming
- Architecture
- Developer Tools
website: https://www.eraser.io/
---
