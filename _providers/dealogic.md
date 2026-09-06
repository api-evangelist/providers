---
access_model:
  confidence: high
  label: Licensed - contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://iongroup.com/analytics/data-portal/request-info/
  - https://dealogic.com/request-a-demo/
  - https://iongroup.com/analytics/data-portal/apis-data-feeds/dealogic-origination-data-feed/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-09-05'
api_count: 8
apis:
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: 'OData v4 read API over Dealogic''s SPAC (special purpose acquisition company) dataset: SPAC entries and their listings, IPO syndicate, attorneys, auditors, lockups and promote schedules, company manage'
  name: Dealogic Analytics SPAC API
  slug: dealogic-analytics-spac-api
- baseURL: https://bank.analytics.dealogic.com/
  baseurl_source: declared
  description: 'Read API returning Dealogic bank-profile analytics for a given bank identifier: overall bank ranking plus rankings by region, industry and product, top deals, recently completed deals and pipeline dea'
  name: Dealogic Analytics Bank API
  slug: dealogic-analytics-bank-api
- baseURL: https://company.analytics.dealogic.com/
  baseurl_source: declared
  description: 'Read API returning Dealogic company-profile analytics for a given company identifier: banking relationships and their momentum, top banks by investment-banking revenue and by lending volume, a drill-d'
  name: Dealogic Analytics Company API
  slug: dealogic-analytics-company-api
- baseURL: https://sponsor.analytics.dealogic.com/
  baseurl_source: declared
  description: 'Read API returning Dealogic financial-sponsor analytics for a given sponsor identifier: investment activity over time, portfolio-company entries and exits, banking relationships ranked by fees and by '
  name: Dealogic Analytics Sponsor API
  slug: dealogic-analytics-sponsor-api
- baseURL: https://api.reporting.dealogic.com/
  baseurl_source: declared
  description: 'Report-execution API over Dealogic''s reporting engine: fetch a saved report definition by report id, execute a report for a given valid-dates type, and execute a report with additional criteria or wit'
  name: Dealogic Reporting API
  slug: dealogic-reporting-api
- baseURL: https://api.reporting.cortex.dealogic.com/
  baseurl_source: declared
  description: 'Report-execution API for the Dealogic Cortex platform (v1.2): retrieve the criteria available for a report id, execute a report by report id and valid-dates type, execute a report with extended criter'
  name: Cortex Reporting API
  slug: cortex-reporting-api
- baseURL: https://api.profiles.dealogic.com/
  baseurl_source: declared
  description: 'Deal- and market-profile API served from Dealogic infrastructure: DCM and loan deal profiles by deal id, US leveraged-finance market profiles for high yield (priced deals, in-market deals, secondary p'
  name: IONA Profiles API
  slug: iona-profiles-api
- description: 'File-based bulk data feed of Dealogic''s investment banking content: over 2 million transactions since 1995 across Equity Capital Markets, Debt Capital Markets, syndicated loans and M&A, plus 1.1 milli'
  name: Dealogic Primary Market Deals & Entities Feed
  slug: dealogic-primary-market-deals-entities-feed
artifact_total: 16
asyncapis:
- description: ''
  name: Dealogic Events
  slug: dealogic-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealogic-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dealogic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dealogic
- group: company
  title: ''
  type: Website
  url: https://www.dealogic.com/
- group: start
  title: ''
  type: Login
  url: https://cortex.dealogic.com/
- group: other
  title: ''
  type: X-Product-InvestmentBanking
  url: https://www.dealogic.com/our-platforms/investment-banking/
- group: other
  title: ''
  type: X-Product-InvestmentManagers
  url: https://www.dealogic.com/our-platforms/investment-managers/
- group: other
  title: ''
  type: X-Product-Corporations
  url: https://www.dealogic.com/our-platforms/corporations/
- group: operate
  title: ''
  type: Contact
  url: https://www.dealogic.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://dealogic.com/llms.txt
- group: other
  title: ''
  type: X-Product-SyndicateSalesTradingResearch
  url: https://dealogic.com/platform/syndicate-str/
- group: auth
  title: ''
  type: X-Product-ComplianceManager
  url: https://dealogic.com/product/compliancemanager/
- group: other
  title: ''
  type: X-Platform
  url: https://dealogic.com/platform/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://iongroup.com/analytics/data-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://iongroup.com/analytics/data-portal/apis-data-feeds/
- group: docs
  title: ''
  type: APIReference
  url: https://iongroup.com/analytics/data-portal/apis-data-feeds/spac-api/documentation/low-level-documentation/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealogic.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealogic.com/privacy-policy/
- group: commercial
  title: ''
  type: Privacy
  url: https://dealogic.com/data-privacy/
- group: operate
  title: ''
  type: Support
  url: https://dealogic.com/about-us/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://dealogic.com/insights/
- group: operate
  title: ''
  type: PressReleases
  url: https://dealogic.com/about-us/press/
- group: start
  title: ''
  type: SignUp
  url: https://iongroup.com/analytics/data-portal/request-info/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dealogic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/dealogic-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dealogic-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dealogic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dealogic-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/dealogic-login-dealogic-com-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dealogic-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dealogic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dealogic-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dealogic-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dealogic-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dealogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealogic-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/dealogic-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dealogic-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dealogic-llms.txt
created: '2024-01-20'
description: 'Dealogic is a global provider of content and software for the capital markets — deal management, analytics, league tables and compliance — used by investment banks, syndicate and sales/trading desks, investment managers and corporates, and is part of ION Analytics. Its platforms are Cortex, Dealogic Connect, Analytics and ComplianceManager. Dealogic runs no developer portal of its own: its APIs are catalogued on the ION Analytics Data Portal, and eight OpenAPI 3.0.1 documents covering 153 operations are served from Dealogic''s own Swagger UIs on spac/bank/company/sponsor.analytics.dealogic.com, api.reporting.dealogic.com, api.reporting.cortex.dealogic.com and api.profiles.dealogic.com. The SPAC API is OData v4; the rest are plain REST. All are read-only and gated by OAuth 2.0 at login.dealogic.com with one ''dealogic'' scope — no self-service signup, no published pricing, no SDK. Bulk delivery is the Primary Market Deals & Entities Feed: XML over secure FTP or a service bus.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dealogic.png
layout: provider
modified: '2026-09-05'
name: Dealogic
nav: Providers
network: true
overview: 'Dealogic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics SPAC API, Analytics Bank API, Analytics Company API, and 4 more. Tagged areas include Analytics, Capital Markets, Compliance, Deal Management, and Debt Capital Markets.


  The Dealogic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dealogic''s developer surface includes documentation, API reference, privacy policy, support, engineering blog, signup flow, authentication, and 33 more developer resources.'
plans:
- name: Dealogic Plans Pricing
  plan_count: 0
  slug: dealogic-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Dealogic Rate Limits
  slug: dealogic-rate-limits
scopes:
- name: Dealogic Scopes
  scope_count: 4
  slug: dealogic-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 37.3
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 39.4
    developer_ergonomics: 54.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/screenshots/dealogic-2026-06-20T175743.png
security:
- kind: authentication
  name: Dealogic Authentication
  slug: dealogic-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Dealogic Domain Security
  slug: dealogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dealogic Vulnerability Disclosure
  slug: dealogic-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Dealogic Trust Center
  slug: dealogic-trust-center
  summary_line: ISO/IEC 27001
slug: dealogic
tags:
- Analytics
- Capital Markets
- Compliance
- Deal Management
- Debt Capital Markets
- Equity Capital Markets
- Finance
- Financial Data
- Investment Banking
- League Tables
- M&A
- OData
- Private Equity
- Reporting
- SPAC
- Syndicated Loans
website: https://www.dealogic.com/
---
