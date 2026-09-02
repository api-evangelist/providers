---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The workflow list, detail and execution surface behind Osly, as documented by the company's own first-party TypeScript SDK. Two REST reads (GET /workflows, GET /workflows/{id}) authenticated with an X
  name: Osly Workflow API (PocketFlow)
  slug: osly-workflow-api-pocketflow
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osly.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.alore.ai/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/HrZutaq46t
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osly-ai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/osly_ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Osly-AI
- group: company
  title: ''
  type: Blog
  url: https://blog.osly.ai/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.osly.ai/rss/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Osly-AI/Pocketflow-SDK#readme
- group: build
  title: ''
  type: Packages
  url: packages/osly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/osly-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/osly-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osly-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osly-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osly-problem-types.yml
- group: other
  title: ''
  type: EventCatalog
  url: events/osly-workflow-events.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osly-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/osly-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/osly-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/osly-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osly-llms.txt
created: '2026-07-17'
description: Osly is an AI workflow automation platform (a product of Alore AI) that lets startups and prosumers build N8N-based AI workflows from natural language, with no coding required. Users describe automations in plain English to generate email sequences, lead categorization and personalized outreach, spin up internal dashboard UIs, and connect 50+ apps including HubSpot, Salesforce, Google Drive, Notion, LinkedIn and Shopify. Osly was surfaced as a portfolio company of 500 Global and added to the API Evangelist network. It publishes no developer portal, no API documentation and no OpenAPI; the only machine-readable description of its API is the company's own first-party TypeScript SDK in github.com/Osly-AI, which documents an X-API-Key REST surface plus a Socket.IO execution stream at api.pocketflow.ai — the company's prior brand domain, since pocketflow.ai redirects to osly.ai. As of 2026-08-14 every application and API host in the estate (app.osly.ai, api.osly.ai, api.pocketflow.ai,
  app.alore.ai) returns Cloudflare 522; only the marketing site and blog respond.
image: https://www.osly.ai/favicon.ico
layout: provider
modified: '2026-08-14'
name: Osly
nav: Providers
network: true
overview: 'Osly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Workflow-Automation, No-Code, and Agents.


  Osly''s developer surface includes signup flow, support, engineering blog, documentation, CLI, authentication, and 17 more developer resources.'
plans:
- name: Osly Plans Pricing
  plan_count: 0
  slug: osly-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Osly Rate Limits
  slug: osly-rate-limits
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 17.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/osly/refs/heads/main/screenshots/osly-2026-08-07T191006.png
security:
- kind: authentication
  name: Osly Authentication
  slug: osly-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Osly Domain Security
  slug: osly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: osly
tags:
- Company
- Artificial Intelligence
- Workflow-Automation
- No-Code
- Agents
- Lead Generation
- Productivity
- Integration
- Low-Code
website: https://osly.ai/
---
