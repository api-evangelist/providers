---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Loopme Agentic Access
  operation_count: 3
  slug: loopme-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- baseURL: https://loopme.me/api/s2s
  baseurl_source: declared
  description: 'LoopMe''s server-to-server ad request endpoint. A third-party ad server, exchange or mediation platform sends a GET describing the device, app and user, and LoopMe returns an MRAID ad payload (ad HTML '
  name: LoopMe S2S Ad Serving API
  slug: loopme-ad-serving-api
- baseURL: https://reports.loopme.com/api/v1
  baseurl_source: declared
  description: The Advertiser Reporting API from LoopMe — 1 operation(s) for advertiser reporting.
  name: LoopMe Advertiser Reporting API
  slug: loopme-advertiser-reporting-api
- baseURL: https://reports.loopme.com/api/v1
  baseurl_source: declared
  description: The Publisher Reporting API from LoopMe — 1 operation(s) for publisher reporting.
  name: LoopMe Publisher Reporting API
  slug: loopme-publisher-reporting-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LoopMe S2S Ad Request API
  slug: open-loopme-ad-serving-api
- collection_type: open
  name: LoopMe Reporting Ad Serving Advertiser Reporting API
  slug: open-loopme-advertiser-reporting-api
- collection_type: open
  name: LoopMe Reporting Ad Serving Publisher Reporting API
  slug: open-loopme-publisher-reporting-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loopme-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.loopme.cool/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.loopme.cool/
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.loopme.cool/publishers/reporting-api
- group: company
  title: ''
  type: Blog
  url: https://loopme.ai/news-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.loopme.io/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loopme
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.loopme.com/privacy-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.loopme.com/legal-centre/terms-of-use
- group: build
  title: ''
  type: SDKs
  url: packages/loopme-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/loopme-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loopme-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loopme-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loopme-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loopme-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/loopme-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loopme-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loopme-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/loopme-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loopme-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/loopme-request-ad-s2s.md
- group: commercial
  title: ''
  type: Plans
  url: plans/loopme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loopme-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/loopme-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loopme-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://legal.loopme.com/privacy-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/loopme-trust-center.yml
- group: design
  title: ''
  type: Components
  url: components/loopme-components.yml
- group: start
  title: ''
  type: Login
  url: https://loopme.ai/product-logins/
created: '2026-07-17'
description: LoopMe is a global brand-performance advertising platform that uses AI to bring brands into mobile and CTV apps. Its products span an AI-powered intelligent marketplace, PurchaseLoop outcome-based brand advertising, the Chartboost in-app monetization platform, and an Audience & Measurement Platform (AMP). For developers, LoopMe exposes a REST Reporting API for publisher (app/site) and advertiser (campaign) statistics, a server-to-server (S2S) ad request API, first-party United SDKs for Android and iOS, and a Prebid.js header-bidding adapter. LoopMe is backed by HV Capital and headquartered in the UK.
image: https://loopme.ai/wp-content/themes/loopme/assets/images/logo.svg
layout: provider
modified: '2026-08-13'
name: LoopMe
nav: Providers
network: true
overview: 'LoopMe publishes 3 APIs on the [APIs.io](https://apis.io/) network: S2S Ad Serving API, Advertiser Reporting API, and Publisher Reporting API. Tagged areas include Company, Advertising, AdTech, Mobile Advertising, and CTV.


  LoopMe''s developer surface includes documentation, API reference, engineering blog, support, authentication, changelog, sandbox, and 23 more developer resources.'
plans:
- name: Loopme Plans Pricing
  plan_count: 0
  slug: loopme-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Loopme Rate Limits
  slug: loopme-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/loopme/refs/heads/main/screenshots/loopme-2026-08-17T121137.png
security:
- kind: authentication
  name: Loopme Authentication
  slug: loopme-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loopme Domain Security
  slug: loopme-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Loopme Trust Center
  slug: loopme-trust-center
  summary_line: ePrivacyseal, TAG registered (Trustworthy Accountability Group)
slug: loopme
tags:
- Company
- Advertising
- AdTech
- Mobile Advertising
- CTV
- Reporting
- Programmatic
- Ai Enterprise Software
- SDK
website: https://wiki.loopme.cool/
---
