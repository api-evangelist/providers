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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Causa Prima Agentic Access
  operation_count: 8
  slug: causa-prima-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://scribo.causaprima.ai
  baseurl_source: declared
  description: The Invoices API from Causa Prima — 3 operation(s) for invoices.
  name: Causa Prima Invoices API
  slug: causa-prima-invoices-api
- baseURL: https://scribo.causaprima.ai
  baseurl_source: declared
  description: The Jurisdictions API from Causa Prima — 1 operation(s) for jurisdictions.
  name: Causa Prima Jurisdictions API
  slug: causa-prima-jurisdictions-api
- baseURL: https://scribo.causaprima.ai
  baseurl_source: declared
  description: The Scribo API from Causa Prima — 4 operation(s) for scribo.
  name: Causa Prima Scribo API
  slug: causa-prima-scribo-api
artifact_total: 11
collections:
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
  href: https://artifacts.apis.io/causa-prima/capabilities/causa-prima-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/causa-prima-capability-edges.yml
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
  href: https://artifacts.apis.io/causa-prima/openapi/_original/causa-prima-scribo-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/causa-prima-scribo-openapi.json
- group: agent
  href: https://artifacts.apis.io/causa-prima/llms/causa-prima-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/causa-prima-llms.txt
- group: agent
  href: https://artifacts.apis.io/causa-prima/mcp/causa-prima-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/causa-prima-mcp.yml
- group: agent
  href: https://artifacts.apis.io/causa-prima/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/causa-prima/packages/causa-prima-packages.yml
  title: ''
  type: Packages
  url: packages/causa-prima-packages.yml
- group: build
  href: https://artifacts.apis.io/causa-prima/cli/causa-prima-cli.yml
  title: ''
  type: CLI
  url: cli/causa-prima-cli.yml
- group: design
  href: https://artifacts.apis.io/causa-prima/errors/causa-prima-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/causa-prima-problem-types.yml
- group: design
  href: https://artifacts.apis.io/causa-prima/conventions/causa-prima-conventions.yml
  title: ''
  type: Conventions
  url: conventions/causa-prima-conventions.yml
- group: design
  href: https://artifacts.apis.io/causa-prima/conventions/causa-prima-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/causa-prima-conventions.yml
- group: design
  href: https://artifacts.apis.io/causa-prima/data-model/causa-prima-data-model.yml
  title: ''
  type: DataModel
  url: data-model/causa-prima-data-model.yml
- group: design
  href: https://artifacts.apis.io/causa-prima/conformance/causa-prima-conformance.yml
  title: ''
  type: Conformance
  url: conformance/causa-prima-conformance.yml
- group: design
  href: https://artifacts.apis.io/causa-prima/lifecycle/causa-prima-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/causa-prima-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/causa-prima/overlays/causa-prima-scribo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/causa-prima-scribo-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/causa-prima/security/causa-prima-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causa-prima-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/causa-prima/agentic-access/causa-prima-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/causa-prima-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/causa-prima/authentication/causa-prima-authentication.yml
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
  slug: scribo
modified: '2026-07-18'
name: Causa Prima
nav: Providers
network: true
overview: 'Causa Prima publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Invoices API, Jurisdictions API, and Scribo API. Tagged areas include Company, Artificial Intelligence, Fintech, E-Invoicing, and Invoicing.


  Causa Prima''s developer surface includes documentation, API reference, getting-started guide, CLI, authentication, and 21 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 64.3
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 40.6
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
    score: 25.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/causa-prima/causa-prima-2026-07-25T204814.png
security:
- kind: authentication
  name: Causa Prima Authentication
  slug: causa-prima-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Causa Prima Domain Security
  slug: causa-prima-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: scribo
  slug: causa-prima-scribo
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
