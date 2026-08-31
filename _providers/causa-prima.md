---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Causa Prima Agentic Access
  operation_count: 8
  slug: causa-prima-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- description: The Invoices API from Causa Prima — 3 operation(s) for invoices.
  name: Causa Prima Invoices API
  slug: causa-prima-invoices-api
- description: The Jurisdictions API from Causa Prima — 1 operation(s) for jurisdictions.
  name: Causa Prima Jurisdictions API
  slug: causa-prima-jurisdictions-api
- description: The Scribo API from Causa Prima — 4 operation(s) for scribo.
  name: Causa Prima Scribo API
  slug: causa-prima-scribo-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scribo Invoice Invoices API
  slug: open-causa-prima-invoices-api
- collection_type: open
  name: Scribo Invoice Invoices Jurisdictions API
  slug: open-causa-prima-jurisdictions-api
- collection_type: open
  name: Invoice Invoices Scribo API
  slug: open-causa-prima-scribo-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: company
  title: ''
  type: Website
  url: https://causaprima.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scribo.causaprima.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://scribo.causaprima.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scribo.causaprima.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://scribo.causaprima.ai/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/causa-prima-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://causaprima.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://causaprima.ai/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://scribo.causaprima.ai/compliance
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/causa-prima-scribo-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/causa-prima-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/causa-prima-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/causa-prima-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/causa-prima-cli.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/causa-prima-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/causa-prima-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/causa-prima-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/causa-prima-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/causa-prima-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/causa-prima-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/causa-prima-scribo-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/causa-prima-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/causa-prima-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/causa-prima-authentication.yml
created: '2026-07-17'
description: 'Causa Prima is an AI-native fintech building an agent-to-agent network for finance teams — automating invoicing, dispute resolution, and dynamic (early-payment) discounting between buyers and suppliers. Its first public product, Scribo, is a free, EN 16931-compliant e-invoicing engine that generates German ZUGFeRD and XRechnung, plus plain US PDF invoices, through five surfaces: a web UI, an HTTP API, a hosted MCP server, an npm CLI, and a Claude / ChatGPT / Codex Agent Skill — all backed by the same public /api/v1 API with no signup (the sender''s email is the login via a magic link). The team previously built Taulia (acquired by SAP) and Finoa; Causa Prima is backed by Creandum.'
image: https://causaprima.ai/og-image.jpg
layout: provider
mcp_servers:
- description: Hosted Scribo MCP server for free EN 16931-compliant e-invoice generation. Compatible with Claude Desktop/Claude.ai (custom connector), Cursor, Cline, ChatGPT App, and OpenAI Codex CLI. No install, no
  name: Causa Prima MCP Server
  slug: causa-prima-mcp-server
modified: '2026-07-18'
name: Causa Prima
nav: Providers
network: true
overview: 'Causa Prima publishes 3 APIs on the [APIs.io](https://apis.io/) network: Invoices API, Jurisdictions API, and Scribo API. Tagged areas include Company, Artificial Intelligence, Fintech, E-Invoicing, and Invoicing.


  Causa Prima''s developer surface includes documentation, API reference, getting-started guide, CLI, authentication, and 21 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/causa-prima/refs/heads/main/screenshots/causa-prima-2026-07-25T204814.png
security:
- kind: authentication
  name: Causa Prima Authentication
  slug: causa-prima-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Causa Prima Domain Security
  slug: causa-prima-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: causa-prima
tags:
- Company
- Artificial Intelligence
- Fintech
- E-Invoicing
- Invoicing
- Payments
- Compliance
- Germany
- EN 16931
- Agents
- MCP
website: https://causaprima.ai/
---
