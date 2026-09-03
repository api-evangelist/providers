---
access_model:
  confidence: high
  label: Freemium — instant 24-hour key, no signup; $7/mo Supporter tier
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://gate.crawl4ai.com/ (#pricing)
  - https://gate.crawl4ai.com/llms.txt
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: 'The hosted Crawl4AI API. One key, plain JSON, one fast endpoint per job: POST /scrape turns a URL into clean Markdown or HTML, GET /search runs a browser-free multi-engine web search, GET /answer retu'
  name: Crawl4AI Cloud API
  slug: crawl4ai
- description: The versioned Crawl4AI cloud surface the first-party Cloud SDKs and the Claude Code plugin call. Covers POST /v1/markdown, /v1/screenshot (screenshot and PDF capture), /v1/extract (auto, LLM or reusab
  name: Crawl4AI Cloud v1 API
  slug: crawl4ai-v1
- description: The Apache-2.0 API server that ships inside the crawl4ai project and the unclecode/crawl4ai Docker image, serving on port 11235 on infrastructure the operator runs. Exposes /crawl, /crawl/stream, /cra
  name: Crawl4AI Self-Hosted API
  slug: crawl4ai-docker
artifact_total: 11
asyncapis:
- description: ''
  name: Crawl4Ai Webhooks
  slug: crawl4ai-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/unclecode/crawl4ai-cloud-sdk/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://crawl4ai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gate.crawl4ai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crawl4ai.com
- group: docs
  title: ''
  type: APIReference
  url: https://gate.crawl4ai.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crawl4ai.com/core/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://docs.crawl4ai.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/jP8KfhDhyN
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unclecode
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/unclecode/crawl4ai
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/unclecode/crawl4ai/blob/main/ROADMAP.md
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crawl4ai
- group: commercial
  title: ''
  type: Pricing
  url: https://gate.crawl4ai.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://gate.crawl4ai.com/dashboard/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gate.crawl4ai.com/legal/#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gate.crawl4ai.com/legal/#privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://unclecode.github.io/crawl4ai-status/
- group: commercial
  title: ''
  type: Plans
  url: plans/crawl4ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crawl4ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crawl4ai-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/crawl4ai-platform-gateway-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/crawl4ai-platform-gateway-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crawl4ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crawl4ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crawl4ai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/crawl4ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crawl4ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crawl4ai-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crawl4ai-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crawl4ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crawl4ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crawl4ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crawl4ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/crawl4ai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crawl4ai-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crawl4ai-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crawl4ai-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crawl4ai-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crawl4ai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crawl4ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/crawl4ai-vulnerability-disclosure.yml
created: '2026-03-27'
description: Crawl4AI is an open-source, Apache-2.0 web crawler and scraper built to turn any URL into clean, LLM-ready data — Markdown, typed JSON, screenshots, PDFs, or a map of every URL on a domain. Operated by CONTEXT4AI PTE LTD of Singapore and created by Hossein Tohidi (@unclecode), the project pairs a 79,000-star Python library and self-hostable Docker API server with a hosted Cloud API at gate.crawl4ai.com that serves scrape, search, answer, extract and bulk-job endpoints from three regions, plus a live remote MCP server that exposes the same capabilities to agents as five native tools. Self-hosting is free and unmetered; the hosted tier is free at 5,000 searches and 1,000 scrapes a month.
finops:
- name: Crawl4Ai Finops
  service_category: API
  slug: crawl4ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crawl4ai.png
layout: provider
mcp_servers:
- description: Crawl4AI ships a hosted, streamable-HTTP MCP server at https://gate.crawl4ai.com/mcp that exposes the Cloud API as five native agent tools. tools/list answers ANONYMOUSLY — the full tool set with comp
  name: Crawl4AI Cloud MCP Server
  slug: crawl4ai-cloud-mcp-server
modified: '2026-08-29'
name: Crawl4AI
nav: Providers
network: true
overview: 'Crawl4AI publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Automation, Web Crawling, Web Scraping, Data Extraction, and Search.


  The Crawl4AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crawl4AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Crawl4Ai Plans Pricing
  plan_count: 4
  slug: crawl4ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 8
  name: Crawl4Ai Rate Limits
  slug: crawl4ai-rate-limits
score:
  band: strong
  composite: 66.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 97.4
  previous_composite: 66.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crawl4ai/refs/heads/main/screenshots/crawl4ai-2026-06-20T175215.png
security:
- kind: authentication
  name: Crawl4Ai Authentication
  slug: crawl4ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Crawl4Ai Domain Security
  slug: crawl4ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Crawl4Ai Vulnerability Disclosure
  slug: crawl4ai-vulnerability-disclosure
  summary_line: disclosure policy published
slug: crawl4ai
tags:
- AI Automation
- Web Crawling
- Web Scraping
- Data Extraction
- Search
- LLM Tooling
- Agents
- MCP
- Open-Source
website: https://crawl4ai.com
---
