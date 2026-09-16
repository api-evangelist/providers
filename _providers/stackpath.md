---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.stackpath.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/security/stackpath-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackpath-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/packages/stackpath-packages.yml
  title: ''
  type: Packages
  url: packages/stackpath-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/packages/stackpath-packages.yml
  title: ''
  type: SDKs
  url: packages/stackpath-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/cli/stackpath-cli.yml
  title: ''
  type: CLI
  url: cli/stackpath-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/lifecycle/stackpath-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stackpath-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/plans/stackpath-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackpath-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/rate-limits/stackpath-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stackpath-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/llms/stackpath-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stackpath-llms.txt
coverage:
  checked: '2026-08-29'
  detail: StackPath ceased operations in June 2024 and was dissolved; every API and developer host - api., gateway., developer., docs., control. and status.stackpath.com - has been withdrawn from DNS, the github.com/stackpath organization returns 404, and www.stackpath.com serves an 835-byte empty black placeholder page.
  evidence:
  - status: 200
    url: https://www.stackpath.com/
  - status: 0
    url: https://developer.stackpath.com/docs/en/getting-started/
  - status: 0
    url: https://gateway.stackpath.com/
  - status: 404
    url: https://api.github.com/orgs/stackpath
  - status: 404
    url: https://www.stackpath.com/.well-known/security.txt
  - status: 404
    url: https://www.stackpath.com/llms.txt
  reason: defunct
  state: none
created: '2026-08-29'
description: StackPath was an American edge computing platform provider headquartered in Dallas, Texas, founded in 2015 by SoftLayer co-founder Lance Crosby. It sold CDN, WAF/WAAP, DNS, SSL, object storage, edge compute (containers and VMs), serverless scripting and monitoring as a single edge platform, driven by a public REST API at gateway.stackpath.com with OAuth2 client-credentials auth and per-service OpenAPI definitions. The company exited the CDN business in 2023 (roughly 100 enterprise CDN contracts went to Akamai), sold its web application and API protection assets to Gcore in March 2024, then announced in June 2024 that it was ceasing operations and liquidating its remaining assets. All StackPath API, developer-portal, control-panel and status hosts have since been withdrawn from DNS and the company no longer publishes any machine-readable API contract.
layout: provider
modified: '2026-09-15'
name: StackPath
nav: Providers
network: true
overview: 'StackPath is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edge Computing, Content Delivery Network, Web Application Firewall, and DNS.


  StackPath''s developer surface includes CLI and 8 more developer resources.'
plans:
- name: Stackpath Plans Pricing
  plan_count: 0
  slug: stackpath-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Stackpath Rate Limits
  slug: stackpath-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/stackpath/refs/heads/main/screenshots/stackpath-2026-09-02T160712.png
security:
- kind: domain-security
  name: Stackpath Domain Security
  slug: stackpath-domain-security
  summary_line: TLSv1.3 · HSTS
slug: stackpath
tags:
- Company
- Edge Computing
- Content Delivery Network
- Web Application Firewall
- DNS
- Object Storage
- Serverless
- Defunct
website: https://www.stackpath.com/
---
