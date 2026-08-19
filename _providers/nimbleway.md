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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Nimbleway Agentic Access
  operation_count: 42
  slug: nimbleway-agentic-access
  summary_line: 42 operations · 22 acting
api_count: 11
apis:
- description: The Agents API from Nimbleway — 7 operation(s) for agents.
  name: Nimbleway Agents API
  slug: nimbleway-agents-api
- description: The Crawl API from Nimbleway — 2 operation(s) for crawl.
  name: Nimbleway Crawl API
  slug: nimbleway-crawl-api
- description: The Domain Knowledge API from Nimbleway — 1 operation(s) for domain knowledge.
  name: Nimbleway Domain Knowledge API
  slug: nimbleway-domain-knowledge-api
- description: The Extract API from Nimbleway — 3 operation(s) for extract.
  name: Nimbleway Extract API
  slug: nimbleway-extract-api
- description: The Fast SERP API from Nimbleway — 1 operation(s) for fast serp.
  name: Nimbleway Fast SERP API
  slug: nimbleway-fast-serp-api
- description: The Jobs API from Nimbleway — 9 operation(s) for jobs.
  name: Nimbleway Jobs API
  slug: nimbleway-jobs-api
- description: The Map API from Nimbleway — 1 operation(s) for map.
  name: Nimbleway Map API
  slug: nimbleway-map-api
- description: The Media API from Nimbleway — 2 operation(s) for media.
  name: Nimbleway Media API
  slug: nimbleway-media-api
- description: The Search API from Nimbleway — 1 operation(s) for search.
  name: Nimbleway Search API
  slug: nimbleway-search-api
- description: The SERP API from Nimbleway — 3 operation(s) for serp.
  name: Nimbleway SERP API
  slug: nimbleway-serp-api
- description: The Tasks API from Nimbleway — 6 operation(s) for tasks.
  name: Nimbleway Tasks API
  slug: nimbleway-tasks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nimble SDK Agents API
  slug: open-nimbleway-agents-api
- collection_type: open
  name: Nimble SDK Agents Crawl API
  slug: open-nimbleway-crawl-api
- collection_type: open
  name: Nimble SDK Agents Domain Knowledge API
  slug: open-nimbleway-domain-knowledge-api
- collection_type: open
  name: Nimble SDK Agents Extract API
  slug: open-nimbleway-extract-api
- collection_type: open
  name: Nimble SDK Agents Fast SERP API
  slug: open-nimbleway-fast-serp-api
- collection_type: open
  name: Nimble SDK Agents Jobs API
  slug: open-nimbleway-jobs-api
- collection_type: open
  name: Nimble SDK Agents Map API
  slug: open-nimbleway-map-api
- collection_type: open
  name: Nimble SDK Agents Media API
  slug: open-nimbleway-media-api
- collection_type: open
  name: Nimble SDK Agents Search API
  slug: open-nimbleway-search-api
- collection_type: open
  name: Nimble SDK Agents SERP API
  slug: open-nimbleway-serp-api
- collection_type: open
  name: Nimble SDK Agents Tasks API
  slug: open-nimbleway-tasks-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nimbleway.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nimbleway.com/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nimbleway.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nimbleway.com/api-reference/introduction
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/nimbleway-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/nimbleway-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nimbleway-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nimbleway-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nimbleway-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nimbleway-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nimbleway-openapi-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nimbleway-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nimbleway.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nimbleway-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nimbleway-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nimbleway.com/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/nimbleway-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nimbleway-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nimbleway-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nimbleway-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nimbleway-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nimbleway-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nimbleway-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nimbleway-cli.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nimbleway
- group: company
  title: ''
  type: Blog
  url: https://www.nimbleway.com/blog
- group: operate
  title: ''
  type: Support
  url: https://portal.usepylon.com/nimble
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nimbleway.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://online.nimbleway.com/signup
- group: start
  title: ''
  type: Login
  url: https://online.nimbleway.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nimbleway.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nimbleway.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://nimbleway.com
created: '2026-07-17'
description: Nimble (Nimbleway) is a real-time web data intelligence platform that turns any public web page into structured, analysis-ready data at scale. Its AI-Native SDK exposes Search, Extract, Map, Crawl, SERP, Media Download, and Web Search Agents over a single REST API (https://sdk.nimbleway.com/v1), plus a managed Jobs layer for recurring, scheduled collection. Nimble ships first-party Python, TypeScript, Go (CLI), LangChain, Scrapy, and Vercel AI SDK libraries, an official Model Context Protocol server, and native connectors for Databricks, Snowflake, Azure, and Claude. The platform is SOC 2, GDPR, and CCPA compliant. Originally added to the API Evangelist network as a Norwest Venture Partners portfolio lead, now enriched from Nimble's public developer surface.
image: https://logo.clearbit.com/nimbleway.com
layout: provider
mcp_servers:
- description: ''
  name: nimbleway-mcp.yml
  slug: nimbleway-mcpyml
modified: '2026-07-20'
name: Nimbleway
nav: Providers
network: true
overview: 'Nimbleway publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Crawl API, Domain Knowledge API, and 8 more. Tagged areas include Company, Web Data, Web Scraping, Data Extraction, and Web Search.


  Nimbleway''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, CLI, engineering blog, and 27 more developer resources.'
random_paper: 74
rate_limits:
- limit_count: 2
  name: Nimbleway Rate Limits
  slug: nimbleway-rate-limits
score:
  band: strong
  composite: 56.6
  delta: -2.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 55.6
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nimbleway/refs/heads/main/screenshots/nimbleway-2026-08-07T185313.png
security:
- kind: authentication
  name: Nimbleway Authentication
  slug: nimbleway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nimbleway Domain Security
  slug: nimbleway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nimbleway Trust Center
  slug: nimbleway-trust-center
  summary_line: SOC 2, GDPR
slug: nimbleway
tags:
- Company
- Web Data
- Web Scraping
- Data Extraction
- Web Search
- Proxies
- AI Agents
- Model Context Protocol
website: https://nimbleway.com
---
