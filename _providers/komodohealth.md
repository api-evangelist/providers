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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Marmot Development Kit (MDK) is Komodo Health''s first-party developer surface: the `komodo` Python SDK and CLI. It authenticates against the Komodo Platform with OAuth 2.0 — a browser-based device'
  name: Marmot Development Kit
  slug: marmot-development-kit
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://komodohealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.komodohealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.komodohealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.komodohealth.com/reference/sdk/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.komodohealth.com/guides-tutorials/guides/1-quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.komodohealth.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.komodohealth.com/perspectives/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/komodohealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.komodohealth.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.komodohealth.com/privacy-notice/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.komodohealth.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.komodohealth.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.komodohealth.com/
- group: build
  title: ''
  type: Packages
  url: packages/komodohealth-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/komodohealth-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/komodohealth-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/komodohealth-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/komodohealth-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/komodohealth-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/komodohealth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/komodohealth-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/komodohealth-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/komodohealth-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/komodohealth-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/komodohealth-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/komodohealth-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Komodo Health is a healthcare technology company that operates a patient-centric "Healthcare Map" of the U.S. healthcare system, combining real-world data, validated healthcare AI, and purpose-built Life Sciences workflows so commercial, clinical, and HEOR teams can generate verified evidence quickly. Developer access is delivered through the Marmot Development Kit (MDK) — the first-party `komodo` Python SDK and CLI published on PyPI — which authenticates with OAuth 2.0 (browser device flow for users, service-principal client credentials for machine-to-machine) and returns a DB-API 2.0 connection to the customer's Komodo-managed Snowflake warehouse. The kit also ships a local stdio MCP server for AI clients, a Secrets Service API, and an App Builder surface for scaffolding, building, and deploying Komodo Apps. Platform access is account-scoped and subscription-gated rather than self-serve.
image: https://www.komodohealth.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: komodohealth-mcp.yml
  slug: komodohealth-mcpyml
modified: '2026-07-19'
name: Komodo Health
nav: Providers
network: true
overview: 'Komodo Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Life Sciences, and Real-World Data.


  Komodo Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 20 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 37.5
  delta: -4.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 75.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komodohealth/refs/heads/main/screenshots/komodohealth-2026-07-25T224138.png
security:
- kind: authentication
  name: Komodohealth Authentication
  slug: komodohealth-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Komodohealth Domain Security
  slug: komodohealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Komodohealth Trust Center
  slug: komodohealth-trust-center
  summary_line: SOC 2 Type 2, SOC 2 Type 1, GDPR, CCPA, Secure by Design Pledge, EcoVadis
slug: komodohealth
tags:
- Company
- Healthcare
- Health Data
- Life Sciences
- Real-World Data
- Real-World Evidence
- Healthcare AI
- Analytics
- Data Platform
- Snowflake
- Python SDK
- MCP
website: https://komodohealth.com
---
