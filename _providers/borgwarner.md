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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/borgwarner-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/borgwarner
- group: company
  title: ''
  type: Website
  url: https://www.borgwarner.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.borgwarner.com/investors
- group: company
  title: ''
  type: Newsroom
  url: https://www.borgwarner.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.borgwarner.com/careers
- group: other
  title: ''
  type: Sustainability
  url: https://www.borgwarner.com/sustainability
- group: company
  title: ''
  type: Blog
  url: https://www.borgwarner.com/newsroom/press-releases
- group: agent
  title: ''
  type: WellKnown
  url: well-known/borgwarner-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/borgwarner-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/borgwarner-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/borgwarner-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/borgwarner-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/borgwarner-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/borgwarner-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.borgwarner.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.borgwarner.com/docs/default-source/legal-documents/us-privacy-policy.pdf
coverage:
  checked: '2026-09-04'
  detail: BorgWarner sells propulsion hardware to vehicle OEMs under negotiated supply programs and machine-to-machine integration runs over supplier EDI (X12/EDIFACT), not HTTP — api., developer. and docs.borgwarner.com do not resolve, and the only API-shaped surface on the domain is the Sitefinity CMS OData v4 service at /api/default, which 401s to anonymous callers.
  evidence:
  - status: 401
    url: https://www.borgwarner.com/api/default/$metadata
  - status: 404
    url: https://www.borgwarner.com/openapi.json
  - status: 200
    url: https://www.borgwarner.com/.well-known/oauth-authorization-server
  - status: 404
    url: https://api.github.com/orgs/borgwarner
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: BorgWarner is a global automotive supplier designing and manufacturing propulsion systems, thermal management, battery systems, charging solutions, and power electronics for combustion, hybrid, and electric vehicles. The company accelerates the world's transition to clean, efficient mobility across passenger and commercial vehicle markets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/borgwarner.png
layout: provider
modified: '2026-09-04'
name: BorgWarner
nav: Providers
network: true
overview: 'BorgWarner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Connected Vehicles, Clean Mobility, Electric Vehicles, and Propulsion Systems.


  BorgWarner''s developer surface includes engineering blog, authentication, and 15 more developer resources.'
plans:
- name: Borgwarner Plans Pricing
  plan_count: 0
  slug: borgwarner-plans-pricing
press:
- date: '2026-05-25'
  title: BorgWarner Partners with Manufacture 2030 to Reduce ...
  url: https://www.borgwarner.com/newsroom/press-releases/2024/03/06/borgwarner-partners-with-manufacture-2030-to-reduce-supply-chain-emissions
- date: '2026-05-25'
  title: We're excited to introduce our all new Turbine Generator ...
  url: https://www.instagram.com/p/DUoA8sFkgPc/
- date: '2026-05-25'
  title: BorgWarner Reports 2025 Results and Provides 2026 ...
  url: https://www.borgwarner.com/newsroom/press-releases/2026/02/11/borgwarner-reports-2025-results-and-provides-2026-guidance--returned-approximately--630-million-to-shareholders-in-2025--strategically-enters-data-center-market-with-turbine-generator-system-award
- date: '2026-05-25'
  title: BorgWarner Strategically Enters Data Center Market with ...
  url: https://www.prnewswire.com/news-releases/borgwarner-strategically-enters-data-center-market-with-power-generation-solution-award-302684780.html
- date: '2026-05-25'
  title: BorgWarner Strategically Enters Data Center Market with ...
  url: https://www.borgwarner.com/newsroom/press-releases/2026/02/11/borgwarner-strategically-enters-data-center-market-with-power-generation-solution-award
random_paper: 10
rate_limits:
- limit_count: 0
  name: Borgwarner Rate Limits
  slug: borgwarner-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/borgwarner/refs/heads/main/screenshots/borgwarner-2026-06-20T173610.png
security:
- kind: authentication
  name: Borgwarner Authentication
  slug: borgwarner-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Borgwarner Domain Security
  slug: borgwarner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: borgwarner
tags:
- Automotive
- Connected Vehicles
- Clean Mobility
- Electric Vehicles
- Propulsion Systems
- Fortune 500
website: https://www.borgwarner.com
---
