---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Bitvore Agentic Access
  operation_count: 121
  slug: bitvore-agentic-access
  summary_line: 121 operations · 53 acting
api_count: 12
apis:
- baseURL: https://api.bitvore.com/muni/alerts/
  baseurl_source: declared
  description: Alerts API
  name: Bitvore Alert API API
  slug: bitvore-alert-api-api
- baseURL: https://api.bitvore.com/bondapi/
  baseurl_source: declared
  description: Municipal Bond API
  name: Bitvore Bond API
  slug: bitvore-bond-api
- baseURL: https://api.bitvore.com/corpnews/
  baseurl_source: declared
  description: Corp News API
  name: Bitvore Corporate News API
  slug: bitvore-corporate-news-api
- baseURL: https://api.bitvore.com/v2/corp/
  baseurl_source: declared
  description: Export Files and Reports
  name: Bitvore Datasets API API
  slug: bitvore-datasets-api-api
- baseURL: https://api.bitvore.com/econnews/
  baseurl_source: declared
  description: Economic News API
  name: Bitvore Economic News API
  slug: bitvore-economic-news-api
- baseURL: https://api.bitvore.com/entityapi/
  baseurl_source: declared
  description: Entity API
  name: Bitvore Entity API
  slug: bitvore-entity-api
- baseURL: https://api.bitvore.com/v2/corp/
  baseurl_source: declared
  description: Financial Filings, Submissions and Summaries
  name: Bitvore Filings API API
  slug: bitvore-filings-api-api
- baseURL: https://api.bitvore.com/financialfiling/
  baseurl_source: declared
  description: Financial Filings API
  name: Bitvore Financial Filings API
  slug: bitvore-financial-filings-api
- baseURL: https://api.bitvore.com/idapi/
  baseurl_source: declared
  description: Identification API
  name: Bitvore Identification API
  slug: bitvore-identification-api
- baseURL: https://api.bitvore.com/intelapi/
  baseurl_source: declared
  description: Intelligence API
  name: Bitvore Intel API
  slug: bitvore-intel-api
- baseURL: https://api.bitvore.com/muni/api/
  baseurl_source: declared
  description: Municipal API
  name: Bitvore Muni API API
  slug: bitvore-muni-api-api
- baseURL: https://api.bitvore.com/muninews/
  baseurl_source: declared
  description: Muni News API
  name: Bitvore Muni News API
  slug: bitvore-muni-news-api
- baseURL: https://api.bitvore.com/v2/
  baseurl_source: declared
  description: Precision and Economic News
  name: Bitvore News API API
  slug: bitvore-news-api-api
- baseURL: https://api.bitvore.com/oauth/
  baseurl_source: declared
  description: Bitvore OAuth2 Authorization Server API
  name: Bitvore O Auth2 API
  slug: bitvore-oauth2-api
- baseURL: https://api.bitvore.com/v2/corp/
  baseurl_source: declared
  description: Organization Details and Search
  name: Bitvore Organizations API API
  slug: bitvore-organizations-api-api
- baseURL: https://api.bitvore.com/portfolioapi/
  baseurl_source: declared
  description: Portfolio API
  name: Bitvore Portfolio API
  slug: bitvore-portfolio-api
- baseURL: https://api.bitvore.com/v2/
  baseurl_source: declared
  description: Manage Organization-based Portfolios
  name: Bitvore Portfolios API API
  slug: bitvore-portfolios-api-api
- baseURL: https://api.bitvore.com/v2/corp/
  baseurl_source: declared
  description: Organization Scores
  name: Bitvore Sentiment Scores API API
  slug: bitvore-sentiment-scores-api-api
- baseURL: https://api.bitvore.com/sentimentscores/
  baseurl_source: declared
  description: Company Sentiment Score API
  name: Bitvore Sentiment Scores API
  slug: bitvore-sentiment-scores-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deprecated Custom Alert API API
  slug: open-bitvore-alert-api-api
- collection_type: open
  name: Deprecated Custom Bond API
  slug: open-bitvore-bond-api
- collection_type: open
  name: Bitvore Legacy Corporate News API
  slug: open-bitvore-corporate-news-api
- collection_type: open
  name: Corporate Datasets API API
  slug: open-bitvore-datasets-api-api
- collection_type: open
  name: Bitvore Legacy Economic News API
  slug: open-bitvore-economic-news-api
- collection_type: open
  name: Bitvore Legacy Entity API
  slug: open-bitvore-entity-api
- collection_type: open
  name: Corporate Filings API API
  slug: open-bitvore-filings-api-api
- collection_type: open
  name: Bitvore Legacy Financial Filings API
  slug: open-bitvore-financial-filings-api
- collection_type: open
  name: Bitvore Legacy Identification API
  slug: open-bitvore-identification-api
- collection_type: open
  name: Deprecated Custom Intel API
  slug: open-bitvore-intel-api
- collection_type: open
  name: Deprecated Custom Muni API API
  slug: open-bitvore-muni-api-api
- collection_type: open
  name: Bitvore Legacy Muni News API
  slug: open-bitvore-muni-news-api
- collection_type: open
  name: Bitvore News API API
  slug: open-bitvore-news-api-api
- collection_type: open
  name: Security O Auth2 API
  slug: open-bitvore-oauth2-api
- collection_type: open
  name: Corporate Organizations API API
  slug: open-bitvore-organizations-api-api
- collection_type: open
  name: Bitvore Legacy Portfolio API
  slug: open-bitvore-portfolio-api
- collection_type: open
  name: Bitvore Portfolios API API
  slug: open-bitvore-portfolios-api-api
- collection_type: open
  name: Corporate Sentiment Scores API API
  slug: open-bitvore-sentiment-scores-api-api
- collection_type: open
  name: Bitvore Legacy Sentiment Scores API
  slug: open-bitvore-sentiment-scores-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitvore-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bitvore-corporate-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bondwave.com/muni-news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bitvore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bitvore.com/v2/docs/api-reference
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bitvore.com/v2/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bitvore.com/v2/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.bitvore.com/get-access
- group: operate
  title: ''
  type: Support
  url: mailto:support@bitvore.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitvore
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.bitvore.com/v2/release
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bitvore-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.bitvore.com/v2/release
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitvore-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitvore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitvore-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitvore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitvore-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitvore-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitvore-data-model.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitvore-dataset-export-schema.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitvore-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bitvore-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitvore-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitvore-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitvore-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitvore-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bitvore-tool-crosswalk.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bitvore-signals.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://developer.bitvore.com/v2/docs/api-reference/signals
- group: company
  title: ''
  type: Blog
  url: https://bondwave.com/posts-archive/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bondwave.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bondwave.com/legal-information/
created: '2026-08-07'
description: 'Bitvore Corp. builds Cellenus, an AI/NLP platform that reads unstructured public text — global news, press releases, SEC filings and proxy statements, earnings-call transcripts — and turns it into structured material business events, signals, trended sentiment, and growth and risk scores. Coverage spans 500,000+ surveilled companies across 60,000+ sources, sold as two separately licensed datasets: Cellenus Corporate Intelligence (corporate and economic news, organizations, financial filings, sentiment scores) and Cellenus Municipal (municipal bond news by CUSIP, location, FIPS and sector), with an ESG signal and scoring layer over both. Access is by REST API, bulk dataset and changeset exports, and a Microsoft-certified Power Platform connector. Bitvore''s fixed-income data-analytics unit was acquired by BondWave in November 2024; bitvore.com now redirects to bondwave.com/muni-news/, while developer.bitvore.com and api.bitvore.com remain live and serving the Cellenus API surface.'
image: https://conn-afd-prod-endpoint-bmc9bqahasf3grgk.b01.azurefd.net/u/shgogna/version-mismatches-special-train/1.0.1670.3520/bitvorecellenus/icon.png
layout: provider
modified: '2026-08-14'
name: Bitvore
nav: Providers
network: true
overview: 'Bitvore publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Alert API API, Bond API, Corporate News API, and 16 more. Tagged areas include Financial Data, Market Intelligence, Alternative Data, News API, and NLP.


  Bitvore''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, changelog, authentication, and 27 more developer resources.'
plans:
- name: Bitvore Plans Pricing
  plan_count: 0
  slug: bitvore-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Bitvore Rate Limits
  slug: bitvore-rate-limits
scopes:
- name: Bitvore Scopes
  scope_count: 1
  slug: bitvore-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.1
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitvore/refs/heads/main/screenshots/bitvore-2026-08-07T162558.png
security:
- kind: authentication
  name: Bitvore Authentication
  slug: bitvore-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Bitvore Domain Security
  slug: bitvore-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitvore
tags:
- Financial Data
- Market Intelligence
- Alternative Data
- News API
- NLP
- ESG
- Municipal Bonds
- Credit Risk
- Company Data
- Sentiment Analysis
- Unstructured Data
- Fixed Income
website: https://bondwave.com/muni-news/
---
