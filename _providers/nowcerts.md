---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Nowcerts Agentic Access
  operation_count: 21
  slug: nowcerts-agentic-access
  summary_line: 21 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.nowcerts.com/api
  baseurl_source: declared
  description: Obtain and refresh bearer tokens.
  name: NowCerts Authentication API
  slug: nowcerts-authentication-api
- baseURL: https://api.nowcerts.com/api
  baseurl_source: declared
  description: Carrier, underwriter, and line-of-business reference data.
  name: NowCerts Carriers API
  slug: nowcerts-carriers-api
- baseURL: https://api.nowcerts.com/api
  baseurl_source: declared
  description: Policy endorsements and their financial detail.
  name: NowCerts Endorsements API
  slug: nowcerts-endorsements-api
- baseURL: https://api.nowcerts.com/api
  baseurl_source: declared
  description: Insureds and prospects (customers), their contacts, and related data.
  name: NowCerts Insureds API
  slug: nowcerts-insureds-api
- baseURL: https://api.nowcerts.com/api
  baseurl_source: declared
  description: Policies, coverages, and quotes.
  name: NowCerts Policies API
  slug: nowcerts-policies-api
- baseURL: https://api.nowcerts.com/api
  baseurl_source: declared
  description: Tasks, task work groups, and to-do workflow.
  name: NowCerts Tasks API
  slug: nowcerts-tasks-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NowCerts Authentication API
  slug: open-nowcerts-authentication-api
- collection_type: open
  name: NowCerts Authentication Carriers API
  slug: open-nowcerts-carriers-api
- collection_type: open
  name: NowCerts Authentication Endorsements API
  slug: open-nowcerts-endorsements-api
- collection_type: open
  name: NowCerts Authentication Insureds API
  slug: open-nowcerts-insureds-api
- collection_type: open
  name: NowCerts Authentication Policies API
  slug: open-nowcerts-policies-api
- collection_type: open
  name: NowCerts Authentication Tasks API
  slug: open-nowcerts-tasks-api
- collection_type: open
  name: NowCerts API
  slug: open-nowcerts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nowcerts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nowcerts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nowcerts-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/momentumamp
- group: company
  title: ''
  type: Website
  url: https://www.nowcerts.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.nowcerts.com/Help
- group: commercial
  title: ''
  type: Plans
  url: plans/nowcerts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nowcerts-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nowcerts-finops.yml
created: '2026-07-10'
description: NowCerts (rebranded to Momentum AMP, but the API is still served from api.nowcerts.com) is a cloud insurance agency management system (AMS) for independent agencies. It exposes a documented REST API that lets agencies and their integration partners import, update, and retrieve their own book of business - insureds and prospects, policies and coverages, carriers and underwriters, endorsements and commissions, tasks and workflow, drivers, vehicles, properties, claims, certificates of insurance, notes, SMS, and payments. The API is token-authenticated and reachable by any NowCerts agency whose account has the "API Integration" agent role assigned; API integrations are gated to the Professional tier and above. Endpoints are documented on the public ASP.NET Web API help page at api.nowcerts.com/Help and are widely used through Zapier and partner integrations.
finops:
- name: Nowcerts Finops
  service_category: Insurance Agency Management Software
  slug: nowcerts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nowcerts.png
layout: provider
modified: '2026-07-10'
name: NowCerts
nav: Providers
network: true
overview: 'NowCerts publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Carriers API, Endorsements API, and 3 more. Tagged areas include Insurance, Insurtech, Agency Management System, AMS, and Policies.


  NowCerts'' developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Nowcerts Plans Pricing
  plan_count: 4
  slug: nowcerts-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Nowcerts Rate Limits
  slug: nowcerts-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/nowcerts/refs/heads/main/screenshots/nowcerts-2026-08-07T185637.png
security:
- kind: authentication
  name: Nowcerts Authentication
  slug: nowcerts-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nowcerts Domain Security
  slug: nowcerts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nowcerts
tags:
- Insurance
- Insurtech
- Agency Management System
- AMS
- Policies
- Insureds
- Certificates of Insurance
- REST
website: https://www.nowcerts.com
---
