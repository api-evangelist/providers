---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 8
apis:
- baseURL: https://porter.revinate.com
  baseurl_source: declared
  description: The Hotel Sets API from Revinate — 4 operation(s) for hotel sets.
  name: Revinate Hotel Sets API
  slug: revinate-hotel-sets-api
- baseURL: https://porter.revinate.com
  baseurl_source: declared
  description: The Hotels API from Revinate — 11 operation(s) for hotels.
  name: Revinate Hotels API
  slug: revinate-hotels-api
- baseURL: https://porter.revinate.com
  baseurl_source: declared
  description: The Languages API from Revinate — 2 operation(s) for languages.
  name: Revinate Languages API
  slug: revinate-languages-api
- baseURL: https://porter.revinate.com
  baseurl_source: declared
  description: The Review Sites API from Revinate — 2 operation(s) for review sites.
  name: Revinate Review Sites API
  slug: revinate-review-sites-api
- baseURL: https://porter.revinate.com
  baseurl_source: declared
  description: The Reviews API from Revinate — 2 operation(s) for reviews.
  name: Revinate Reviews API
  slug: revinate-reviews-api
- baseURL: https://porter.revinate.com
  baseurl_source: declared
  description: The Widget Reviews API from Revinate — 1 operation(s) for widget reviews.
  name: Revinate Widget Reviews API
  slug: revinate-widget-reviews-api
artifact_total: 13
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/revinate-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/revinate-porter-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.revinate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://porter.revinate.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://porter.revinate.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://porter.revinate.com/documentation#api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://porter.revinate.com/documentation#introduction
- group: operate
  title: ''
  type: Support
  url: https://www.revinate.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.revinate.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revinate
- group: start
  title: ''
  type: Login
  url: https://www.revinate.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revinate.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revinate.com/website-privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.revinate.com/
- group: auth
  title: ''
  type: Compliance
  url: security/revinate-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revinate-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revinate-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/revinate-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revinate-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/revinate-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revinate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revinate-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revinate-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/revinate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revinate-rate-limits.yml
created: '2026-08-26'
description: Revinate is a hospitality technology company providing a Guest Data Platform and CRM for hotels — unifying guest profiles from property-management systems, then driving direct revenue through email marketing, a voice/call-center product, a virtual concierge, and reputation and guest-feedback management. Revinate states it powers 950 million-plus guest profiles and $17.2 billion in direct revenue for over 12,500 hotels worldwide. Its public developer surface is the Porter API — a read-only REST API for structured review data covering 100-plus review sites, exposing hotels, hotel sets, reviews, competitor reviews, review-volume and rating snapshots, survey email statistics, and hospitality-specific sentiment analysis broken out by topic category.
image: https://www.revinate.com/wp-content/uploads/2022/09/revinate-logo-400px.png
layout: provider
modified: '2026-08-26'
name: Revinate
nav: Providers
network: true
overview: 'Revinate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Hotel Sets API, Hotels API, Languages API, and 3 more. Tagged areas include Hospitality, Hotels, Reviews, Reputation Management, and Guest Data Platform.


  Revinate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Revinate Plans Pricing
  plan_count: 0
  slug: revinate-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Revinate Rate Limits
  slug: revinate-rate-limits
scopes:
- name: Revinate Scopes
  scope_count: 0
  slug: revinate-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/revinate/refs/heads/main/screenshots/revinate-2026-09-02T153723.png
security:
- kind: authentication
  name: Revinate Authentication
  slug: revinate-authentication
  summary_line: apiKey/openIdConnect · 4 schemes
- kind: domain-security
  name: Revinate Domain Security
  slug: revinate-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Revinate Vulnerability Disclosure
  slug: revinate-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Revinate Trust Center
  slug: revinate-trust-center
  summary_line: trust center published
slug: revinate
tags:
- Hospitality
- Hotels
- Reviews
- Reputation Management
- Guest Data Platform
- CRM
- Sentiment Analysis
- Travel
- Marketing
- Customer Feedback
website: https://www.revinate.com/
---
