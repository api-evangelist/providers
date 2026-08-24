---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://support.inmobi.com/choice/getting-started-cmp/inmobi-cmp-premium
  - plans/inmobi-plans-pricing.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: Automates download of app inventory performance data for InMobi publishers. A single POST to /v3.0/reporting/publisher takes a reportRequest envelope of metrics (adRequests, adImpressions, clicks, ear
  name: InMobi Publisher Reporting API
  slug: inmobi-publisher-reporting-api
- description: Manages InMobi monetization inventory — the apps and placements a publisher monetizes through InMobi — without clicking through the dashboard. Apps are listed, fetched, created and patched at /rest/ap
  name: InMobi Ad Management API
  slug: inmobi-ad-management-api
- description: Asynchronous spend reporting for InMobi DSP advertisers. A bearer token is minted from clientId/clientSecret at POST /auth/token (8-hour validity), then a report is created at POST /reports/network, /
  name: InMobi DSP Cost API
  slug: inmobi-dsp-cost-api
- description: Lets a publisher request InMobi ads from its own servers rather than through the client SDK, using the InMobi ad-request/ad-response contract at /showad/v3.1. The caller is identified by an InMobi Pro
  name: InMobi Server-to-Server Ad Request API
  slug: inmobi-server-to-server-ad-request-api
- description: InMobi's programmatic ad exchange, integrated by demand-side platforms over the IAB OpenRTB 2.5 protocol. InMobi publishes its own delta specification ("InMobi Open RTB 2.5 Specification Version 4.3")
  name: InMobi Exchange (OpenRTB 2.5)
  slug: inmobi-exchange-openrtb
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/inmobi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inmobi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inmobi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.inmobi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.inmobi.com/monetize
- group: docs
  title: ''
  type: APIReference
  url: https://support.inmobi.com/monetize/inmobi-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://support.inmobi.com/monetize
- group: operate
  title: ''
  type: Support
  url: https://support.inmobi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InMobi
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.inmobi.com/inmobi-now
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/inmobi-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://www.inmobi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://support.inmobi.com/choice/getting-started-cmp/inmobi-cmp-premium
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inmobi.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inmobi.com/website-privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://publisher.inmobi.com/
- group: start
  title: ''
  type: SignUp
  url: https://publisher.inmobi.com/signup
- group: auth
  title: ''
  type: Compliance
  url: https://www.inmobi.com/trust-center/
- group: auth
  title: ''
  type: Security
  url: https://www.inmobi.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/inmobi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/inmobi-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inmobi-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inmobi-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/inmobi-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inmobi-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inmobi-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inmobi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inmobi-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inmobi-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/inmobi-plans-pricing.yml
created: '2026-07-17'
description: InMobi is a global advertising technology and mobile marketing platform headquartered in Bengaluru, India, and backed by SoftBank Vision Fund. It positions itself as the intelligence layer of the consumer internet, connecting brands and consumers across mobile apps and the open web. InMobi's enterprise platforms include InMobi Advertising for brand building, app growth and ad monetization; the InMobi Exchange, a programmatic OpenRTB 2.5 ad exchange for demand-side platforms; InMobi DSP performance solutions; and InMobi CMP (Choice), an IAB TCF-certified consent management platform. InMobi operates four documented, live REST APIs — the Publisher Reporting API 3.0 for inventory performance data, the Ad Management API for managing apps and placements, the DSP Cost API for asynchronous spend reporting, and a Server-to-Server Ad Request API — alongside native mobile ad SDKs for Android (Maven Central) and iOS (CocoaPods and Swift Package Manager). No OpenAPI, AsyncAPI, OAuth server
  or REST client library is published for any of them. Consumer brands include Glance and the 1Weather app.
image: https://github.com/InMobi.png
layout: provider
modified: '2026-08-12'
name: InMobi
nav: Providers
network: true
overview: 'InMobi publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Advertising, AdTech, and Mobile.


  InMobi''s developer surface includes documentation, API reference, getting-started guide, support, changelog, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Inmobi Plans Pricing
  plan_count: 2
  slug: inmobi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Inmobi Rate Limits
  slug: inmobi-rate-limits
score:
  band: developing
  composite: 45.1
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 45.1
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inmobi/refs/heads/main/screenshots/inmobi-2026-07-25T222451.png
security:
- kind: authentication
  name: Inmobi Authentication
  slug: inmobi-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Inmobi Domain Security
  slug: inmobi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Inmobi Trust Center
  slug: inmobi-trust-center
  summary_line: TAG Certified Against Fraud, IAB Tech Lab, IAB TCF (certified CMP vendor), MMA, GDPR, CCPA
slug: inmobi
tags:
- Company
- Enterprise
- Advertising
- AdTech
- Mobile
- Monetization
- Programmatic
- OpenRTB
- SDK
- Consent Management
- DSP
- Reporting
website: https://www.inmobi.com/
---
