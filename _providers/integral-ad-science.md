---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 1
apis:
- description: 'RESTful API that exposes IAS viewability, fraud and brand safety metrics for a customer''s own business applications. Job-oriented: POST /report submits a JSON ReportRequest describing teams, date rang'
  name: IAS Reporting API
  slug: ias-reporting-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integral-ad-science-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/integral-ad-science-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/integral-ad-science-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/integral-ad-science-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/integral-ad-science-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/integral-ad-science-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/integral-ad-science-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/integral-ad-science-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/integral-ad-science-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/integral-ad-science-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/integral-ad-science-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/integral-ad-science-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/integral-ad-science-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://helpcenter.integralplatform.com/article/developers-center
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://helpcenter.integralplatform.com/topics/release-notes
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.integralplatform.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://integralads.com/ias-legal-portal/ias-signal-platform-authorized-user-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://integralads.com/ias-privacy-data-management/policies/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://integralads.com/ias-legal-portal/
- group: start
  title: ''
  type: Login
  url: https://reporting.integralplatform.com/spa/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/integralads
- group: company
  title: ''
  type: Website
  url: https://integralads.com
- group: other
  title: ''
  type: IASAgent
  url: https://integralads.com/ias-agent/
- group: other
  title: ''
  type: ResponsibleAI
  url: https://integralads.com/responsible-ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.integralplatform.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.integralads.com/en-US/home
- group: other
  title: ''
  type: Platform
  url: https://reporting.integralplatform.com/spa/login
- group: other
  title: ''
  type: Prebid-RTD
  url: https://docs.prebid.org/dev-docs/modules/iasRtdProvider.html
- group: other
  title: ''
  type: Prebid-Bidder
  url: https://docs.prebid.org/dev-docs/bidders/ias.html
- group: other
  title: ''
  type: SalesforceConnector
  url: https://help.salesforce.com/s/articleView?id=mktg.mcidp_data_streams_api_connect_integral.htm&language=en_US&type=5
- group: company
  title: ''
  type: Newsroom
  url: https://integralads.com/about-ias/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://integralads.com/insider/
- group: company
  title: ''
  type: About
  url: https://integralads.com/about-ias/
- group: company
  title: ''
  type: Careers
  url: https://integralads.com/about-ias/careers/
- group: company
  title: ''
  type: Investors
  url: https://investors.integralads.com/
- group: operate
  title: ''
  type: Contact
  url: https://integralads.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integral-ad-science
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/integralads
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@integralads
coverage:
  checked: '2026-08-12'
  detail: 'Integral Ad Science runs a real, live REST API estate — data.integralplatform.com answers a bearer request with the documented OAuth error "invalid_token: Access token expired" — but between 2024 and 2026 IAS moved every developer article (reporting-api, segment-api-guide, custom-segment-retrieval-api-guide, multimedia-classification-api, gaming-api, admantx-api-guide, auto-tag-light-api, partner-measurement-api-implementation-guide) behind the IAS Signal customer login, leaving only a Developers Center index page that renders with requiredRoles ["loggedIn"] and serves an empty body to anonymous clients.'
  evidence:
  - status: 200
    url: https://helpcenter.integralplatform.com/article/developers-center
  - status: 404
    url: https://helpcenter.integralplatform.com/article/reporting-api
  - status: 401
    url: https://data.integralplatform.com/report
  - status: 404
    url: https://data.integralplatform.com/.well-known/oauth-authorization-server
  reason: customer-only-docs
  state: gated
created: '2026-05-25'
description: 'Integral Ad Science (NASDAQ: IAS) is a New York-based global ad verification and digital media measurement company. IAS provides technology and data that measures the quality, viewability, ad fraud, brand safety and suitability, contextual targeting, and attention performance of digital advertising across CTV and video, the open web, social platforms, mobile and in-app, and digital audio. Its products serve advertisers and agencies, publishers, and ad-tech platforms with proprietary capabilities including Quality Impressions, Total Visibility, Total Media Quality, Context Control, and the IAS Agent platform for generative-AI-era brand safety. IAS does operate a documented REST API estate on data.integralplatform.com — the Reporting API (viewability, fraud and brand safety metrics as asynchronous CSV report jobs), Segment API, Custom Segment Retrieval, Partner Measurement, Multimedia Classification, Gaming, ADmantX semantic analysis, Auto Tag Light and Automated Tagging — but
  it publishes no OpenAPI specification, no self-serve credentials and, since 2025, no publicly readable API reference: the IAS Developers Center and every developer article now render only for logged-in IAS Signal customers. Authentication is OAuth 2.0 password grant with client credentials issued by an IAS representative. Customer access to IAS data and measurement is otherwise delivered through enterprise integrations with DSPs, SSPs, ad servers, social platforms, and walled gardens, plus the IAS Signal reporting platform, header-bidding modules (Prebid IAS RTD provider and bidder adapter), and partner connectors such as the Salesforce Marketing Cloud Intelligence (Datorama) IAS connector. The company''s GitHub organization (github.com/integralads) is primarily internal tooling, forks, and ad-tech ecosystem contributions rather than a documented developer SDK surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/integral-ad-science.png
layout: provider
modified: '2026-08-12'
name: Integral Ad Science
nav: Providers
network: true
overview: 'Integral Ad Science publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Ad Verification, Ad Measurement, Brand Safety, and Ad Fraud.


  Integral Ad Science''s developer surface includes authentication, changelog, release notes, support, legal docs, engineering blog, YouTube channel, and 32 more developer resources.'
plans:
- name: Integral Ad Science Plans Pricing
  plan_count: 0
  slug: integral-ad-science-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Integral Ad Science Rate Limits
  slug: integral-ad-science-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 26.9
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/integral-ad-science/refs/heads/main/screenshots/integral-ad-science-2026-06-20T183425.png
security:
- kind: authentication
  name: Integral Ad Science Authentication
  slug: integral-ad-science-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Integral Ad Science Domain Security
  slug: integral-ad-science-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Integral Ad Science Trust Center
  slug: integral-ad-science-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISMS Statement of Applicability
slug: integral-ad-science
tags:
- Advertising
- Ad Verification
- Ad Measurement
- Brand Safety
- Ad Fraud
- Viewability
- Contextual Targeting
- Attention Measurement
- CTV
- Connected TV
- Video Advertising
- Programmatic
- Header Bidding
- Prebid
- AdTech
- Marketing
- Media Quality
website: https://integralads.com
---
