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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tinyfish Agentic Access
  operation_count: 20
  slug: tinyfish-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 4
apis:
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: Browser automation endpoints for executing tasks on websites
  name: TinyFish Automation API
  slug: tinyfish-automation-api
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: Endpoints for retrieving automation run data
  name: TinyFish Runs API
  slug: tinyfish-runs-api
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: The TinyFish Browser API API from TinyFish — 1 operation(s) for tinyfish browser api.
  name: TinyFish TinyFish Browser API API
  slug: tinyfish-tinyfish-browser-api-api
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: The TinyFish Fetch API API from TinyFish — 1 operation(s) for tinyfish fetch api.
  name: TinyFish TinyFish Fetch API API
  slug: tinyfish-tinyfish-fetch-api-api
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: The TinyFish Search API API from TinyFish — 1 operation(s) for tinyfish search api.
  name: TinyFish TinyFish Search API API
  slug: tinyfish-tinyfish-search-api-api
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: The Usage API from TinyFish — 1 operation(s) for usage.
  name: TinyFish Usage API
  slug: tinyfish-usage-api
- baseURL: https://agent.tinyfish.ai
  baseurl_source: declared
  description: Vault credential management endpoints for connecting password managers and managing stored credentials
  name: TinyFish Vault API
  slug: tinyfish-vault-api
artifact_total: 20
asyncapis:
- description: ''
  name: Tinyfish Agent Webhooks
  slug: tinyfish-agent-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TinyFish Browser Automation API
  slug: open-tinyfish-automation-api
- collection_type: open
  name: TinyFish Browser Automation Runs API
  slug: open-tinyfish-runs-api
- collection_type: open
  name: TinyFish Browser Automation TinyFish Browser API API
  slug: open-tinyfish-tinyfish-browser-api-api
- collection_type: open
  name: TinyFish Browser Automation TinyFish Fetch API API
  slug: open-tinyfish-tinyfish-fetch-api-api
- collection_type: open
  name: TinyFish Browser Automation TinyFish Search API API
  slug: open-tinyfish-tinyfish-search-api-api
- collection_type: open
  name: TinyFish Browser Automation Usage API
  slug: open-tinyfish-usage-api
- collection_type: open
  name: TinyFish Browser Automation Vault API
  slug: open-tinyfish-vault-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tinyfish-browser-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tinyfish.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tinyfish.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tinyfish.ai/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tinyfish.ai/quick-start
- group: start
  title: ''
  type: Quickstart
  url: https://docs.tinyfish.ai/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://agent.tinyfish.ai/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://pricing.tinyfish.ai/
- group: company
  title: ''
  type: Blog
  url: https://blog.tinyfish.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tinyfish-io
- group: operate
  title: ''
  type: Support
  url: https://form.typeform.com/to/Ivk0DVRA
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tinyfish.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tinyfish.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://tinyfish.instatus.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tinyfish-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tinyfish-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tinyfish-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tinyfish-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tinyfish-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tinyfish-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tinyfish-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tinyfish-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tinyfish-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tinyfish-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tinyfish-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tinyfish-agent-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tinyfish-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tinyfish-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tinyfish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tinyfish.ai/
created: '2026-07-17'
description: 'TinyFish provides enterprise infrastructure for AI web agents — a unified platform that lets AI systems interact with the live web at scale. It ships four API surfaces: a Web Agent Automation API that turns natural-language goals into browser automations on real websites (sync, async, SSE-streaming, and batch), a Search API returning structured JSON from browser-rendered results, a Fetch API that converts rendered pages to clean markdown/JSON/HTML, and a Browser API for cloud CDP browser sessions with stealth/anti-bot capabilities. All APIs authenticate with an X-API-Key header, are documented at docs.tinyfish.ai with published OpenAPI specs and an llms.txt, and are exposed to assistants through an official hosted MCP server. TinyFish is the company behind the open-source AgentQL project and is backed by ICONIQ Capital.'
image: https://www.tinyfish.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: TinyFish MCP Server
  slug: tinyfish-mcp-server
modified: '2026-07-21'
name: TinyFish
nav: Providers
network: true
overview: 'TinyFish publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Automation API, Runs API, TinyFish Browser API API, and 4 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Web Automation, and Web Scraping.


  The TinyFish catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TinyFish''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, pricing, engineering blog, and 24 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 65.8
    developer_ergonomics: 67.3
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tinyfish/refs/heads/main/screenshots/tinyfish-2026-08-17T082359.png
security:
- kind: authentication
  name: Tinyfish Authentication
  slug: tinyfish-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tinyfish Domain Security
  slug: tinyfish-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tinyfish
tags:
- Company
- Artificial Intelligence
- AI Agents
- Web Automation
- Web Scraping
- Search
- Browser Automation
- MCP
- Data Extraction
website: https://www.tinyfish.ai/
---
