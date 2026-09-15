---
access_model:
  confidence: high
  label: API access add-on, contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developers.madkudu.com/getting-started/usage-and-credits
  - https://developers.madkudu.com/readme.md
  - '{''url'': ''https://madkudu.com/'', ''status'': 301, ''note'': ''declared website redirects to https://hginsights.com/ — a different registrable domain (madkudu.com -> hginsights.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-09-14'
api_count: 2
apis:
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Accounts API from MadKudu — 3 operation(s) for accounts.
  name: MadKudu Accounts API
  slug: madkudu-accounts-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The AI API from MadKudu — 1 operation(s) for ai.
  name: MadKudu AI API
  slug: madkudu-ai-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Companies API from MadKudu — 1 operation(s) for companies.
  name: MadKudu Companies API
  slug: madkudu-companies-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Enrichment API from MadKudu — 1 operation(s) for enrichment.
  name: MadKudu Enrichment API
  slug: madkudu-enrichment-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Ingestion API from MadKudu — 3 operation(s) for ingestion.
  name: MadKudu Ingestion API
  slug: madkudu-ingestion-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Job Changes API from MadKudu — 1 operation(s) for job changes.
  name: MadKudu Job Changes API
  slug: madkudu-job-changes-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Lookup API from MadKudu — 2 operation(s) for lookup.
  name: MadKudu Lookup API
  slug: madkudu-lookup-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Organisation API from MadKudu — 2 operation(s) for organisation.
  name: MadKudu Organisation API
  slug: madkudu-organisation-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Persons API from MadKudu — 3 operation(s) for persons.
  name: MadKudu Persons API
  slug: madkudu-persons-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Search API from MadKudu — 2 operation(s) for search.
  name: MadKudu Search API
  slug: madkudu-search-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Sourcing API from MadKudu — 3 operation(s) for sourcing.
  name: MadKudu Sourcing API
  slug: madkudu-sourcing-api
- baseURL: https://madapi.madkudu.com
  baseurl_source: declared
  description: The Utilities API from MadKudu — 1 operation(s) for utilities.
  name: MadKudu Utilities API
  slug: madkudu-utilities-api
artifact_total: 18
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/overlays/madkudu-madapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/madkudu-madapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/overlays/madkudu-legacy-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/madkudu-legacy-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://madkudu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.madkudu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.madkudu.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.madkudu.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.madkudu.com/getting-started/quickstart
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/mcp/madkudu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/madkudu-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/mcp/madkudu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/madkudu-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MadKudu
- group: operate
  title: ''
  type: Support
  url: mailto:support@madkudu.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.madkudu.com/
- group: company
  title: ''
  type: Blog
  url: https://madkudu.com/blog
- group: start
  title: ''
  type: Login
  url: https://msi.madkudu.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hginsights.com/product/pricing-guide/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hginsights.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hginsights.com/privacy-page/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.madkudu.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/authentication/madkudu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/madkudu-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/errors/madkudu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/madkudu-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/conventions/madkudu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/madkudu-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/lifecycle/madkudu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/madkudu-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/data-model/madkudu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/madkudu-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/sandbox/madkudu-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/madkudu-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/conformance/madkudu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/madkudu-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/security/madkudu-trust-center.yml
  title: ''
  type: Compliance
  url: security/madkudu-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/security/madkudu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/madkudu-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/security/madkudu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/madkudu-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/packages/madkudu-packages.yml
  title: ''
  type: Packages
  url: packages/madkudu-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/packages/madkudu-packages.yml
  title: ''
  type: SDKs
  url: packages/madkudu-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/plans/madkudu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/madkudu-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/rate-limits/madkudu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/madkudu-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/llms/madkudu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/madkudu-llms.txt
created: '2026-07-17'
description: MadKudu is a predictive lead scoring and account intelligence platform for B2B sales and marketing teams, using AI-driven propensity modeling and dynamic scoring across fit, intent, and engagement signals to surface high-propensity accounts and people. Its developer surface (MadAPI) programmatically exposes account and person lookup, enrichment, activity, search, sourcing discovery, AI web search, organisation endpoints and a "coming soon" custom ingestion API, alongside a legacy Scoring API and a hosted Model Context Protocol (MCP) server for AI agents. MadKudu publishes OpenAPI 3.1.0 for both surfaces, but only as per-operation blocks embedded in its GitBook reference — no spec document is served. MadKudu was acquired by HG Insights in 2025; the docs are now titled "HG Platform API" and API access is contact-sales. Originally backed by Partech and Techstars.
image: https://cdn.prod.website-files.com/6107b1101d4d3e748743f234/65f31ad2b4ac6cf0cb8bd691_og-img.png
layout: provider
mcp_servers:
- description: ''
  name: MadMCP
  slug: madmcp
modified: '2026-08-14'
name: MadKudu
nav: Providers
network: true
overview: 'MadKudu publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AI API, Companies API, and 9 more. Tagged areas include Company, Applicative Saas, Sales Intelligence, Lead Scoring, and Predictive Analytics.


  MadKudu''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 27 more developer resources.'
plans:
- name: Madkudu Plans Pricing
  plan_count: 0
  slug: madkudu-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Madkudu Rate Limits
  slug: madkudu-rate-limits
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 70.8
    discoverability: 75.9
    operational_transparency: 39.5
  previous_composite: 51.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/screenshots/madkudu-2026-07-25T225833.png
security:
- kind: authentication
  name: Madkudu Authentication
  slug: madkudu-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Madkudu Domain Security
  slug: madkudu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Madkudu Trust Center
  slug: madkudu-trust-center
  summary_line: SOC 2 Type 2, CAIQ, SIG Lite
slug: madkudu
tags:
- Company
- Applicative Saas
- Sales Intelligence
- Lead Scoring
- Predictive Analytics
- Account Intelligence
- Data Enrichment
- MCP
- Agents
- Go-To-Market
website: https://madkudu.com/
---
