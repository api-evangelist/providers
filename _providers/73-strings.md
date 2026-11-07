---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: 73 Strings Agentic Access
  operation_count: 23
  slug: 73-strings-agentic-access
  summary_line: 23 operations · 5 acting
api_count: 6
apis:
- baseURL: https://api-accord-eut-73strings.azure-api.net/assetinfo
  baseurl_source: declared
  description: The **Asset Info APIs**, a RESTful service on 73 Strings, provides detailed company insights, enabling efficient portfolio management, investment analysis, and seamless data retrieval across an organi
  name: 73 Strings Asset Info API
  slug: 73-strings-asset-info-api
- baseURL: https://api-accord-eut-73strings.azure-api.net/assetinfo
  baseurl_source: declared
  description: The **Documents APIs**, a RESTful service on 73 Strings, provides a comprehensive information of the uploaded documents affiliated with the company in the funds across an organization in the 73 String
  name: 73 Strings Documents API
  slug: 73-strings-documents-api
- baseURL: https://api-accord-eut-73strings.azure-api.net/assetinfo
  baseurl_source: declared
  description: 'The **Financial Data APIs**, a RESTful service on 73 Strings, allows to retrieve comprehensive information of attributes and their values on various cash flow dates in several tags of the Financials, '
  name: 73 Strings Financial Data API
  slug: 73-strings-financial-data-api
- baseURL: https://api-accord-eut-73strings.azure-api.net/assetinfo
  baseurl_source: declared
  description: The **Qualitative Data APIs**, a RESTful service on the 73 Strings platform, provide structured access to narrative-driven company insights, enabling retrieval of qualitative analysis data such as str
  name: 73 Strings Qualitative Data API
  slug: 73-strings-qualitative-data-api
- baseURL: https://api-accord-eut-73strings.azure-api.net/assetinfo
  baseurl_source: declared
  description: The <b>Transaction APIs</b> enable external enterprise customers to <b>ingest and retrieve transaction ledger records</b> within the <b>73 Strings platform</b>.<br><br>These APIs are intended for <b>c
  name: 73 Strings Transaction API
  slug: 73-strings-transaction-api-api
- baseURL: https://api-accord-eut-73strings.azure-api.net/assetinfo
  baseurl_source: declared
  description: The **Captable APIs**, a RESTful service on 73 Strings, provides comprehensive capital table data including securities, equity, cash positions, and key financial metrics for entities within an organiz
  name: 73 Strings cap table API
  slug: 73-strings-cap-table-api
artifact_total: 22
collections:
- collection_type: open
  name: Asset Info API
  slug: open-73-strings-asset-info-api
- collection_type: open
  name: Captable API
  slug: open-73-strings-captable-api
- collection_type: open
  name: Documents API
  slug: open-73-strings-documents-api
- collection_type: open
  name: Financial Data API
  slug: open-73-strings-financial-data-api
- collection_type: open
  name: Qualitative Data API
  slug: open-73-strings-qualitative-data-api
- collection_type: open
  name: Transaction Transaction API API
  slug: open-73-strings-transaction-api-api
common:
- group: auth
  href: https://artifacts.apis.io/73-strings/security/73-strings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/73-strings-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/73-strings/agentic-access/73-strings-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/73-strings-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/73-strings/authentication/73-strings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/73-strings-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.73strings.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-accord-eut-73strings.developer.azure-api.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api-accord-eut-73strings.developer.azure-api.net/apis
- group: docs
  title: ''
  type: APIReference
  url: https://api-accord-eut-73strings.developer.azure-api.net/apis
- group: start
  title: ''
  type: SignUp
  url: https://api-accord-eut-73strings.developer.azure-api.net/signup
- group: start
  title: ''
  type: Login
  url: https://api-accord-eut-73strings.developer.azure-api.net/signin
- group: operate
  title: ''
  type: Support
  url: mailto:support@73strings.com
- group: company
  title: ''
  type: Blog
  url: https://www.73strings.com/insights/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/73Strings
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.73strings.com/terms-and-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.73strings.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.73strings.com/resources/about/
- group: design
  href: https://artifacts.apis.io/73-strings/conventions/73-strings-conventions.yml
  title: ''
  type: Conventions
  url: conventions/73-strings-conventions.yml
- group: design
  href: https://artifacts.apis.io/73-strings/errors/73-strings-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/73-strings-problem-types.yml
- group: design
  href: https://artifacts.apis.io/73-strings/lifecycle/73-strings-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/73-strings-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/73-strings/conformance/73-strings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/73-strings-conformance.yml
- group: design
  href: https://artifacts.apis.io/73-strings/data-model/73-strings-data-model.yml
  title: ''
  type: DataModel
  url: data-model/73-strings-data-model.yml
- group: operate
  href: https://artifacts.apis.io/73-strings/rate-limits/73-strings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/73-strings-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/73-strings/plans/73-strings-plans.yml
  title: ''
  type: Plans
  url: plans/73-strings-plans.yml
- group: agent
  href: https://artifacts.apis.io/73-strings/mcp/73-strings-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/73-strings-mcp.yml
- group: build
  href: https://artifacts.apis.io/73-strings/mcp/73-strings-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/73-strings-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/73-strings/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/73-strings/llms/73-strings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/73-strings-llms.txt
- group: other
  href: https://artifacts.apis.io/73-strings/overlays/73-strings-asset-info-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/73-strings-asset-info-overlay.yaml
- group: other
  href: https://artifacts.apis.io/73-strings/overlays/73-strings-captable-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/73-strings-captable-overlay.yaml
- group: other
  href: https://artifacts.apis.io/73-strings/overlays/73-strings-documents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/73-strings-documents-overlay.yaml
- group: other
  href: https://artifacts.apis.io/73-strings/overlays/73-strings-financial-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/73-strings-financial-data-overlay.yaml
- group: other
  href: https://artifacts.apis.io/73-strings/overlays/73-strings-qualitative-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/73-strings-qualitative-data-overlay.yaml
- group: other
  href: https://artifacts.apis.io/73-strings/overlays/73-strings-transaction-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/73-strings-transaction-api-overlay.yaml
created: '2026-08-05'
description: 73 Strings is an AI-powered financial technology company serving alternative asset managers in private equity, private credit, venture capital, infrastructure and multi-strategy funds. Its platform digitises the valuation and portfolio-monitoring lifecycle for illiquid assets through three products — 73 Value (audit-ready equity and credit valuations), 73 Monitor (portfolio monitoring and analytics) and 73 Extract (AI extraction of unstructured private-market documents into structured data). 73 Strings exposes a REST API surface through Microsoft Azure API Management developer portals, covering asset information, cap tables, documents, financial data, qualitative data and transaction-ledger ingestion, all authenticated with a subscription key and scoped by organization and user identifiers. The company is headquartered in Paris with offices in London, New York, San Francisco, Singapore, Riyadh, Abu Dhabi, Bengaluru and Hyderabad, and is backed by Blackstone, Goldman Sachs, Hamilton
  Lane, Golub Capital and Broadhaven.
finops:
- has_sources: true
  method: derived
  name: 73 Strings Finops
  primary_unit: ''
  service_category: ''
  slug: 73-strings-finops
  template: true
image: https://backend.73strings.com/wp-content/uploads/73-Intelligence_image-1.png
layout: provider
modified: '2026-09-16'
name: 73 Strings
nav: Providers
network: true
overview: '73 Strings publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset Info API, Documents API, Financial Data API, and 3 more. Tagged areas include Private Markets, Valuation, Portfolio Monitoring, Private Equity, and Private Credit.


  The 73 Strings catalog on APIs.io includes 1 Spectral governance ruleset.


  73 Strings'' developer surface includes authentication, documentation, API reference, signup flow, support, engineering blog, and 26 more developer resources.'
plans:
- name: 73 Strings Plans
  plan_count: 4
  slug: 73-strings-plans
random_paper: 17
rate_limits:
- limit_count: 5
  name: 73 Strings Rate Limits
  slug: 73-strings-rate-limits
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: 73 Strings API Rules
  rule_count: 71
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 13
  slug: 73-strings-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 47.0
    discoverability: 71.4
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/73-strings/73-strings-2026-08-07T160710.png
security:
- kind: authentication
  name: 73 Strings Authentication
  slug: 73-strings-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 73 Strings Domain Security
  slug: 73-strings-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Assemble a cap table and diligence pack for a portfolio company
  slug: 73-strings-captable-and-diligence-pack
- name: Ingest a transaction ledger in bulk
  slug: 73-strings-ingest-transaction-ledger
- name: Pull financials for a portfolio company
  slug: 73-strings-pull-portfolio-financials
slug: 73-strings
tags:
- Private Markets
- Valuation
- Portfolio Monitoring
- Private Equity
- Private Credit
- Venture Capital
- Alternative Assets
- Financial Data
- Data Extraction
- Fintech
- Asset Management
- Azure API Management
website: https://www.73strings.com/
---
