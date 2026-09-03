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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Fundamental Research Labs Agentic Access
  operation_count: 10
  slug: fundamental-research-labs-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.shortcut.ai
  baseurl_source: declared
  description: API key authentication and verification
  name: Fundamental Research Labs Authentication API
  slug: fundamental-research-labs-authentication-api
- baseURL: https://api.shortcut.ai
  baseurl_source: declared
  description: Spreadsheet processing and automation endpoints
  name: Fundamental Research Labs Spreadsheets API
  slug: fundamental-research-labs-spreadsheets-api
- baseURL: https://api.shortcut.ai
  baseurl_source: declared
  description: 'Export team usage metrics for reporting, finance, and internal analytics. Usage Metrics in Shortcut provides a prefilled request with your team_id; use this reference to customize date range, format, '
  name: Fundamental Research Labs Usage API
  slug: fundamental-research-labs-usage-api
artifact_total: 16
asyncapis:
- description: ''
  name: Fundamental Research Labs Webhooks
  slug: fundamental-research-labs-webhooks
collections:
- collection_type: postman
  name: Shortcut Authentication API
  slug: postman-fundamental-research-labs-authentication-api
- collection_type: postman
  name: Shortcut Authentication Spreadsheets API
  slug: postman-fundamental-research-labs-spreadsheets-api
- collection_type: postman
  name: Shortcut Authentication Usage API
  slug: postman-fundamental-research-labs-usage-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shortcut Authentication API
  slug: open-fundamental-research-labs-authentication-api
- collection_type: open
  name: Shortcut Authentication Spreadsheets API
  slug: open-fundamental-research-labs-spreadsheets-api
- collection_type: open
  name: Shortcut Authentication Usage API
  slug: open-fundamental-research-labs-usage-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fundamental-research-labs/overview
- group: company
  title: ''
  type: Website
  url: https://fundamentalresearchlabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shortcut.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://shortcut.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://shortcut.ai/docs/platform-api
- group: start
  title: ''
  type: GettingStarted
  url: https://shortcut.ai/docs/platform-api
- group: commercial
  title: ''
  type: Pricing
  url: https://shortcut.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://shortcut.ai/shortcut
- group: company
  title: ''
  type: Blog
  url: https://shortcut.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://shortcut.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shortcut.ai/privacy/policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shortcut.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fundamental-research-labs
- group: auth
  title: ''
  type: Compliance
  url: https://shortcut.ai/pricing
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/fundamental-research-labs-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/fundamental-research-labs-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/fundamental-research-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fundamental-research-labs-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fundamental-research-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fundamental-research-labs-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fundamental-research-labs-shortcut-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fundamental-research-labs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fundamental-research-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fundamental-research-labs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fundamental-research-labs-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fundamental-research-labs-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fundamental-research-labs-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fundamental-research-labs-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fundamental-research-labs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fundamental-research-labs-plans.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fundamental-research-labs-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundamental-research-labs-domain-security.yml
created: '2026-07-17'
description: Fundamental Research Labs (formerly Altera) is an applied AI research company building autonomous, collaborative AI agents, founded by researchers from MIT EECS, the Stanford NLP Group, Google X, and Citadel and backed by Andreessen Horowitz and Prosus. Its flagship product, Shortcut, is an AI analyst for Excel that turns natural-language prompts into full spreadsheet models — LBOs, DCFs, three-statement models, waterfalls — and ships a web app, desktop app, Excel and Google Sheets plugins, a ShortcutXL terminal agent (CLI), and a Platform API. The Shortcut Platform API lets teams submit spreadsheet-automation jobs, poll status, download generated workbooks, upload context files, list agent skills, and export organization usage data programmatically using API-key bearer authentication.
image: https://shortcut.ai/og-image.png
layout: provider
modified: '2026-07-19'
name: Fundamental Research Labs
nav: Providers
network: true
overview: 'Fundamental Research Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Spreadsheets API, and Usage API. Tagged areas include Company, Artificial Intelligence, Spreadsheets, Excel, and Financial Modeling.


  The Fundamental Research Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fundamental Research Labs'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 26 more developer resources.'
plans:
- name: Fundamental Research Labs Plans
  plan_count: 4
  slug: fundamental-research-labs-plans
random_paper: 0
rate_limits:
- limit_count: 5
  name: Fundamental Research Labs Rate Limits
  slug: fundamental-research-labs-rate-limits
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.7
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fundamental-research-labs/refs/heads/main/screenshots/fundamental-research-labs-2026-07-25T215308.png
security:
- kind: authentication
  name: Fundamental Research Labs Authentication
  slug: fundamental-research-labs-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fundamental Research Labs Domain Security
  slug: fundamental-research-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fundamental-research-labs
tags:
- Company
- Artificial Intelligence
- Spreadsheets
- Excel
- Financial Modeling
- Agents
- Automation
- Productivity
- Data Analysis
website: https://fundamentalresearchlabs.ai
---
