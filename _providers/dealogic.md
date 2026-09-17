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
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-09-16'
api_count: 16
apis:
- description: 'File-based bulk data feed of Dealogic''s investment banking content: over 2 million transactions since 1995 across Equity Capital Markets, Debt Capital Markets, syndicated loans and M&A, plus 1.1 milli'
  name: Dealogic Primary Market Deals & Entities Feed
  slug: dealogic-primary-market-deals-entities-feed
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Admin API from Dealogic — 1 operation(s) for admin.
  name: Dealogic Admin API
  slug: dealogic-admin-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Data API from Dealogic — 27 operation(s) for data.
  name: Dealogic Data API
  slug: dealogic-data-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The DcmDeal API from Dealogic — 1 operation(s) for dcmdeal.
  name: Dealogic Dcm Deal API
  slug: dealogic-dcmdeal-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Entity Navigation API from Dealogic — 44 operation(s) for entity navigation.
  name: Dealogic Entity Navigation API
  slug: dealogic-entity-navigation-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The LevfinMarketUpdate API from Dealogic — 16 operation(s) for levfinmarketupdate.
  name: Dealogic Levfin Market Update API
  slug: dealogic-levfinmarketupdate-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The LoanDeal API from Dealogic — 1 operation(s) for loandeal.
  name: Dealogic Loan Deal API
  slug: dealogic-loandeal-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The OrganizationSpacProfile API from Dealogic — 8 operation(s) for organizationspacprofile.
  name: Dealogic Organization Spac Profile API
  slug: dealogic-organizationspacprofile-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Related Entities API from Dealogic — 32 operation(s) for related entities.
  name: Dealogic Related Entities API
  slug: dealogic-related-entities-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The ReportData API from Dealogic — 7 operation(s) for reportdata.
  name: Dealogic Report Data API
  slug: dealogic-reportdata-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Root Entity API from Dealogic — 1 operation(s) for root entity.
  name: Dealogic Root Entity API
  slug: dealogic-root-entity-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Spac Admin API from Dealogic — 4 operation(s) for spac admin.
  name: Dealogic Spac Admin API
  slug: dealogic-spac-admin-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Spac Reader API from Dealogic — 1 operation(s) for spac reader.
  name: Dealogic Spac Reader API
  slug: dealogic-spac-reader-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Spac Writer API from Dealogic — 9 operation(s) for spac writer.
  name: Dealogic Spac Writer API
  slug: dealogic-spac-writer-api
- baseURL: https://spac.analytics.dealogic.com/
  baseurl_source: declared
  description: The Test API from Dealogic — 1 operation(s) for test.
  name: Dealogic Test API
  slug: dealogic-test-api
artifact_total: 23
asyncapis:
- description: ''
  name: Dealogic Events
  slug: dealogic-events
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-analytics-spac-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-analytics-spac-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-analytics-spac-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-analytics-spac-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-analytics-bank-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-analytics-bank-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-analytics-company-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-analytics-company-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-analytics-sponsor-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-analytics-sponsor-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-reporting-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-cortex-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-cortex-reporting-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/overlays/dealogic-iona-profiles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dealogic-iona-profiles-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/security/dealogic-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/security/dealogic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dealogic-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/conformance/dealogic-conformance.yml
  title: ''
  type: Compliance
  url: conformance/dealogic-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/conformance/dealogic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealogic-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/authentication/dealogic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dealogic-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/scopes/dealogic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dealogic-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/well-known/dealogic-login-dealogic-com-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/dealogic-login-dealogic-com-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/well-known/dealogic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealogic-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/conventions/dealogic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dealogic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/errors/dealogic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dealogic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/data-model/dealogic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealogic-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/lifecycle/dealogic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dealogic-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/plans/dealogic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dealogic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/rate-limits/dealogic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dealogic-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/packages/dealogic-packages.yml
  title: ''
  type: Packages
  url: packages/dealogic-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/mcp/dealogic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dealogic-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealogic/refs/heads/main/llms/dealogic-llms.txt
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
overview: 'Dealogic publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Data API, Dcm Deal API, and 11 more. Tagged areas include Analytics, Capital Markets, Compliance, Deal Management, and Debt Capital Markets.


  The Dealogic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dealogic''s developer surface includes documentation, API reference, privacy policy, support, engineering blog, signup flow, authentication, and 41 more developer resources.'
plans:
- name: Dealogic Plans Pricing
  plan_count: 0
  slug: dealogic-plans-pricing
random_paper: 10
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
  composite: 42.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 45.7
    developer_ergonomics: 54.2
    discoverability: 66.7
    operational_transparency: 2.6
  previous_composite: 41.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
