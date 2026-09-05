---
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.amazonscraperapi.com
  baseurl_source: declared
  description: REST/JSON API for single-product (ASIN) extraction, search results, and async batch scraping across 20 Amazon marketplaces. API key auth via ?api_key= query parameter; only HTTP 2xx responses are bill
  name: Amazon Scraper REST API
  slug: amazon-scraper-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Amazon Scraper Api Webhooks
  slug: amazon-scraper-api-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://amazonscraperapi.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-scraper-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-scraper-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-scraper-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amazon-scraper-api-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-scraper-api-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-scraper-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-scraper-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-scraper-api-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-scraper-api-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-scraper-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-scraper-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-scraper-api-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://amazonscraperapi.com/docs/changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-scraper-api-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-scraper-api-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-scraper-api-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-scraper-api-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amazon-scraper-api-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amazon-scraper-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amazon-scraper-api-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.amazonscraperapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://amazonscraperapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://amazonscraperapi.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:info@amazonscraperapi.com
- group: company
  title: ''
  type: Blog
  url: https://amazonscraperapi.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChocoData-com
- group: commercial
  title: ''
  type: Pricing
  url: https://amazonscraperapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.amazonscraperapi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amazonscraperapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amazonscraperapi.com/privacy
created: '2026-07-16'
description: REST/JSON API for extracting structured Amazon product, search, and batch data across 20 marketplaces, with key-based authentication, official SDKs, a CLI, and a local MCP server. Operated independently under the ChocoData namespace; not affiliated with Amazon.com, Inc.
layout: provider
mcp_servers:
- description: ''
  name: Amazon Scraper API MCP Server
  slug: amazon-scraper-api-mcp-server
modified: '2026-09-03'
name: Amazon Scraper API
nav: Providers
network: true
overview: 'Amazon Scraper API publishes 1 API on the [APIs.io](https://apis.io/) network: Amazon Scraper REST API. Tagged areas include Web Scraping, Data Extraction, E-Commerce Data, Amazon, and marketplace data.


  The Amazon Scraper API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Amazon Scraper API''s developer surface includes authentication, changelog, CLI, API reference, getting-started guide, support, engineering blog, and 25 more developer resources.'
plans:
- name: Amazon Scraper Api Plans Pricing
  plan_count: 5
  slug: amazon-scraper-api-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Amazon Scraper Api Rate Limits
  slug: amazon-scraper-api-rate-limits
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.7
    developer_ergonomics: 78.6
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 68.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 61.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-scraper-api/refs/heads/main/screenshots/amazon-scraper-api-2026-07-25T200010.png
security:
- kind: authentication
  name: Amazon Scraper Api Authentication
  slug: amazon-scraper-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Amazon Scraper Api Domain Security
  slug: amazon-scraper-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amazon-scraper-api
tags:
- Web Scraping
- Data Extraction
- E-Commerce Data
- Amazon
- marketplace data
- Product Intelligence
- Price Monitoring
- Competitor Research
- MCP
- Agent Tooling
website: https://amazonscraperapi.com
---
