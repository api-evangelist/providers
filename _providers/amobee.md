---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: REST API for managing cross-channel advertising campaigns including advertisers, insertion orders, line items, packages, creatives, and ads across programmatic channels. Authentication uses OAuth2 cli
  name: Amobee Campaign API
  slug: amobee-campaign-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The env-vars-test-controller API from Amobee — 1 operation(s) for env-vars-test-controller.
  name: Amobee Env Vars Test Controller API
  slug: amobee-env-vars-test-controller-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The gateway-swagger-controller API from Amobee — 2 operation(s) for gateway-swagger-controller.
  name: Amobee Gateway Swagger Controller API
  slug: amobee-gateway-swagger-controller-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The health-check API from Amobee — 1 operation(s) for health-check.
  name: Amobee Health Check API
  slug: amobee-health-check-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The ip-controller API from Amobee — 1 operation(s) for ip-controller.
  name: Amobee Ip Controller API
  slug: amobee-ip-controller-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The tcf-disclosure-controller API from Amobee — 2 operation(s) for tcf-disclosure-controller.
  name: Amobee Tcf Disclosure Controller API
  slug: amobee-tcf-disclosure-controller-api
artifact_total: 13
collections:
- collection_type: open
  name: OpenAPI definition
  slug: open-amobee-services
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amobee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amobee-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amobee.com/trust/master-service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amobee.com/trust/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.amobee.com/
- group: start
  title: ''
  type: Login
  url: https://platform.amobee.com/app/account/index.htm
- group: auth
  title: ''
  type: Security
  url: security/amobee-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amobee-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amobee-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/amobee-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amobee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amobee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amobee-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amobee-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/amobee-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/amobee-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amobee-services-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amobee-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Amobee
coverage:
  checked: '2026-08-12'
  detail: Amobee is now operated as Nexxen and its developer surface went with the rebrand — the Platform API reference at services.amobee.com/campaign/v3/doc/ returns 404 while the OAuth token endpoint and DSP console still serve existing customers, and the remaining reference lives in a Zendesk help center that refuses anonymous requests (403, Help Center API 401).
  evidence:
  - status: 404
    url: https://services.amobee.com/campaign/v3/doc/
  - status: 403
    url: https://help.amobee.com/hc/en-us
  - status: 401
    url: https://help.amobee.com/api/v2/help_center/en-us/categories.json
  - status: 405
    url: https://services.amobee.com/accounts/v1/api/token
  - status: 200
    url: https://services.amobee.com/v3/api-docs
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: Amobee (now Nexxen) is a digital advertising platform offering REST APIs for managing cross-channel programmatic campaigns, audience targeting, data management, and advertising analytics. The platform enables advertisers and agencies to plan, activate, and measure media across display, video, mobile, social, and TV channels through a unified DSP.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amobee.png
layout: provider
modified: '2026-08-12'
name: Amobee
nav: Providers
network: true
overview: 'Amobee publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Env Vars Test Controller API, Gateway Swagger Controller API, Health Check API, and 2 more. Tagged areas include Digital Advertising, DSP, Programmatic, Campaign Management, and Audience Targeting.


  Amobee''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 8
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/screenshots/amobee-2026-06-20T171938.png
security:
- kind: authentication
  name: Amobee Authentication
  slug: amobee-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Amobee Domain Security
  slug: amobee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amobee Vulnerability Disclosure
  slug: amobee-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amobee
tags:
- Digital Advertising
- DSP
- Programmatic
- Campaign Management
- Audience Targeting
- Data Management Platform
- AdTech
- Samsung Ads
website: https://www.amobee.com/
---
