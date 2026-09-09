---
access_model:
  confidence: high
  label: Enterprise — sales-gated, no published pricing
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans/dow-jones-developer-platform-plans-pricing.yml
  - https://developer.dowjones.com/request-trial/
  trial: true
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
    error_semantics: verified
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
  score: 41.5
  scored_at: '2026-09-08'
api_count: 9
apis:
- description: The Dow Jones Developer Platform is the umbrella developer surface for Dow Jones' news, business intelligence, market data and risk-and-compliance products. It covers three API families — Factiva, New
  name: Dow Jones Developer Platform
  slug: dow-jones-developer-platform
- baseURL: https://api.dowjones.com
  baseurl_source: declared
  description: 'Search Dow Jones Newswires real-time content with DJN taxonomy expressions and retrieve the linked articles by Dow Jones Resource Name. The same endpoints serve the standard Real-Time licence and the '
  name: Dow Jones Newswires Real-Time API
  slug: newswires-real-time-api
- baseURL: https://api.dowjones.com
  baseurl_source: declared
  description: Retrieve the entitled Dow Jones content collections and the articles inside them. This is the one Newswires flow Dow Jones permits an application to run on a schedule rather than on human action, subj
  name: Dow Jones Newswires Top Stories API
  slug: newswires-top-stories-api
- baseURL: https://api.dowjones.com
  baseurl_source: declared
  description: Search and retrieve Dow Jones economic, corporate, treasury and IPO calendar events, with a full set of taxonomy endpoints for the event codes, event classes, series codes, countries, regions, languag
  name: Dow Jones Calendar Live API
  slug: calendar-live-api
- baseURL: https://api.dowjones.com/content
  baseurl_source: declared
  description: 'The Factiva content workflow surface: full-text and metadata search across the Factiva archive, reference resolution and binary retrieval, alerts, newsletter editions and NewsPlus collections, plus sp'
  name: Factiva Content API
  slug: factiva-content-api
- baseURL: https://api.dowjones.com
  baseurl_source: declared
  description: List the newsletters an account is entitled to, read a newsletter's metadata, and walk its editions. Published as OpenAPI 3.0.2 and the only Dow Jones contract that declares the JSON:API media type ap
  name: Factiva Newsletters API
  slug: factiva-newsletters-api
- baseURL: https://api-thirdparty.riskcenter.dowjones.com
  baseurl_source: declared
  description: Manage third parties, their properties and their monitored entities inside Dow Jones RiskCenter — the third-party risk-management product in the Risk & Compliance family. This is the only write surfac
  name: Dow Jones RiskCenter Third Party Platform API
  slug: riskcenter-third-party-api
- description: 'The original Factiva integration surface, in production since 2000 and still published: an XML/SOAP 1.1 web-service suite exposing Search, Retrieval, Taxonomy, Membership, Registration, Newsstand, Tra'
  name: Factiva Developer Kit (SOAP)
  slug: factiva-developer-kit
artifact_total: 17
asyncapis:
- description: ''
  name: Dow Jones Developer Platform Factiva Streams Events
  slug: dow-jones-developer-platform-factiva-streams-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.dowjones.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dowjones.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dowjones.com/documents/site-docs-getting_started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dowjones.com/documents/site-docs-getting_started-api_essentials
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dowjones.com/documents/site-docs-getting_started-quick_start
- group: operate
  title: ''
  type: Support
  url: https://developer.dowjones.com/support-ticket-create
- group: start
  title: ''
  type: SignUp
  url: https://developer.dowjones.com/request-trial/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dowjones
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/dj-cse/workspace/devportal-factiva-products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dowjones.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dowjones.com/privacy-notice/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dow-jones-developer-platform-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.dowjones.com/documents/site-docs-getting_started-deprecation_and_sunset_policies
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dow-jones-developer-platform-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dow-jones-developer-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dow-jones-developer-platform-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dow-jones-developer-platform-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dow-jones-developer-platform-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dow-jones-developer-platform-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dow-jones-developer-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/dow-jones-developer-platform-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dow-jones-developer-platform-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/dow-jones-developer-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dow-jones-developer-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dow-jones-developer-platform-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/dow-jones-developer-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dow-jones-developer-platform-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dow-jones-developer-platform-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dow-jones-developer-platform-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dow-jones-developer-platform-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dow-jones-developer-platform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dow-jones-developer-platform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dow-jones-developer-platform-finops.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dow-jones-developer-platform-mcp.yml
- group: other
  title: ''
  type: X-EventSurface
  url: asyncapi/dow-jones-developer-platform-factiva-streams-events.yml
created: '2025-03-01'
description: 'Dow Jones is a financial news and information provider that publishes The Wall Street Journal, Barron''s, MarketWatch and Financial News, and operates professional information services including Factiva, Dow Jones Newswires and Dow Jones Risk & Compliance. The Developer Platform is the API and feed surface for that content: real-time newswires search and article retrieval, Factiva news search and analytics, economic and IPO calendars, company and executive data, and sanctions, adverse-media and third-party screening. Dow Jones publishes machine-readable contracts for ten surfaces — nine OpenAPI/Swagger documents served from its own developer portal and a WSDL 1.1 Factiva Developer Kit with 208 SOAP operations — behind an OAuth 2.0 identity service requiring a two-step token exchange. Access is entitlement-based: no self-serve signup, no published pricing, and Newswires and Risk & Compliance applications must pass certification before serving users.'
finops:
- name: Dow Jones Developer Platform Finops
  service_category: API
  slug: dow-jones-developer-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dow-jones-developer-platform.png
layout: provider
modified: '2026-09-07'
name: Dow Jones Developer Platform
nav: Providers
network: true
overview: 'Dow Jones Developer Platform publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Dow Jones Developer Platform, Dow Jones Newswires Real-Time API, Dow Jones Newswires Top Stories API, and 4 more. Tagged areas include Business Data, Compliance, Financial, Market Data, and News.


  The Dow Jones Developer Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dow Jones Developer Platform''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 29 more developer resources.'
plans:
- name: Dow Jones Developer Platform Plans Pricing
  plan_count: 0
  slug: dow-jones-developer-platform-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Dow Jones Developer Platform Rate Limits
  slug: dow-jones-developer-platform-rate-limits
scopes:
- name: Dow Jones Developer Platform Scopes
  scope_count: 0
  slug: dow-jones-developer-platform-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 73.2
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 65.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 86.7
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dow-jones-developer-platform/refs/heads/main/screenshots/dow-jones-developer-platform-2026-06-20T180207.png
security:
- kind: authentication
  name: Dow Jones Developer Platform Authentication
  slug: dow-jones-developer-platform-authentication
  summary_line: oauth2/openIdConnect/http/apiKey · 4 schemes
- kind: domain-security
  name: Dow Jones Developer Platform Domain Security
  slug: dow-jones-developer-platform-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dow Jones Developer Platform Vulnerability Disclosure
  slug: dow-jones-developer-platform-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Dow Jones Developer Platform Trust Center
  slug: dow-jones-developer-platform-trust-center
  summary_line: ISO/IEC 27001, ISAE 3000 (Revised) — Sanctions Assurance, Dow Jones Risk & Compliance Annual Data Quality Report
slug: dow-jones-developer-platform
tags:
- Business Data
- Compliance
- Financial
- Market Data
- News
- Risk and Compliance
- Screening
- Sanctions
website: https://www.dowjones.com
---
