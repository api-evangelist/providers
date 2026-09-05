---
access_model:
  confidence: high
  label: Paid, sales-assisted, API access separately entitled
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.salesforce.com/marketing/analytics/pricing/
  - https://developers.datorama.com/docs/manage/introduction/
  - '{''url'': ''https://datorama.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.salesforce.com/marketing/analytics/?redirect=datorama.com&bc=DB — a different registrable domain (datorama.com -> salesforce.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST API to set up, manage and administer a Marketing Cloud Intelligence (Datorama) account — accounts, workspaces, users, permission sets, data streams, connectors, data source authentications, bucke
  name: Intelligence Platform API
  slug: intelligence-platform-api
- description: Synchronous JSON query API for reading harmonized Marketing Cloud Intelligence (Datorama) data out into any other platform, including all classifications and calculations. POST /v1/query and POST /v1/
  name: Intelligence Query API
  slug: intelligence-query-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://datorama.com
- group: other
  title: ''
  type: Product
  url: https://www.salesforce.com/marketing/analytics/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.datorama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.datorama.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.datorama.com/docs/manage/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.datorama.com/docs/build/apps/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/s/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/marketing/analytics/pricing/
- group: start
  title: ''
  type: Login
  url: https://platform.datorama.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/products/Datorama
- group: auth
  title: ''
  type: Security
  url: https://security.salesforce.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.salesforce.com/en/services/marketing-cloud-intelligence
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/datorama-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/datorama-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/datorama-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datorama-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datorama-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datorama-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/datorama-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datorama-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/datorama-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/datorama-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/datorama-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datorama-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/datorama-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/datorama-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/datorama-cli.yml
- group: design
  title: ''
  type: Components
  url: components/datorama-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datorama-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datorama-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datorama-domain-security.yml
created: '2026-07-17'
description: 'Datorama was a cloud-based marketing intelligence and analytics platform founded in 2012 in Tel Aviv and New York. It unified marketing, advertising, and sales data from thousands of disparate sources into a single AI-powered reporting and dashboarding layer, using its "Genius" machine learning engine to automate data harmonization across ad, social, web, and CRM APIs. Salesforce acquired Datorama in August 2018 for a reported ~$800 million and rebranded it as Salesforce Marketing Cloud Intelligence. The marketing, pricing, legal, trust and support surfaces have moved to salesforce.com, but the developer surface is still live on the original domain: a Gatsby developer portal at developers.datorama.com documents an Intelligence Platform API and a synchronous Query API on https://api.datorama.com/v1, both authenticated with a per-user personal access token in an Authorization header, both rate limited per user (60 platform req/min, 200 query req/min, 20,000 calls/day UTC) with
  X-PlatformRateLimit-*, X-QueryRateLimit-* and X-DailyQuota-* response headers, plus an asynchronous Reporting API for large exports, a header-switched sandbox mode, an Apps JavaScript SDK and a `dato` CLI on npm, a custom-connector framework, and — new in July 2026 — a first-party MCP server (@datorama/mci-mcp-sdk) that proxies MCP JSON-RPC to a tenant /api/mcp endpoint using an OAuth2 service-account key. No OpenAPI, AsyncAPI, GraphQL SDL, llms.txt, /.well-known/ document or A2A agent card is published anywhere on the surface. This profile entered the API Evangelist network as a lightspeed-venture-partners portfolio lead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datorama.png
layout: provider
mcp_servers:
- description: ''
  name: Datorama MCP Server
  slug: datorama-mcp-server
modified: '2026-08-12'
name: Datorama
nav: Providers
network: true
overview: 'Datorama publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Marketing, Marketing Intelligence, and Advertising.


  Datorama''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, changelog, and 26 more developer resources.'
plans:
- name: Datorama Plans Pricing
  plan_count: 2
  slug: datorama-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Datorama Rate Limits
  slug: datorama-rate-limits
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 76.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 46.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datorama/refs/heads/main/screenshots/datorama-2026-07-25T211413.png
security:
- kind: authentication
  name: Datorama Authentication
  slug: datorama-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Datorama Domain Security
  slug: datorama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datorama Vulnerability Disclosure
  slug: datorama-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Datorama Trust Center
  slug: datorama-trust-center
  summary_line: SOC 2, SOC 3, C5 (ISAE 3000), UK Cyber Essentials, UK Cyber Essentials Plus, Spain ENS High, EU Processor Binding Corporate Rules
slug: datorama
tags:
- Company
- Analytics
- Marketing
- Marketing Intelligence
- Advertising
- Data
- Business Intelligence
- Reporting
- Salesforce
- Marketing Analytics
- Data Harmonization
- Dashboards
- MCP
website: https://datorama.com
---
