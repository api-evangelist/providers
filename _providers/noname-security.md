---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://nonamesecurity.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.akamai.com/products/api-security — a different registrable domain (nonamesecurity.com -> akamai.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 4
apis:
- description: The Noname API Security Platform provides comprehensive API security through discovery, posture management, runtime protection, and active testing. It discovers all APIs across the organization, detec
  name: Noname API Security Platform
  slug: api-security-platform
- description: Noname API Discovery provides complete visibility into all APIs across an organization, including managed, unmanaged, shadow, and legacy APIs. It automatically catalogs APIs, classifies sensitive data
  name: Noname API Discovery
  slug: api-discovery
- description: Noname Runtime Protection uses AI and machine learning to detect and block API attacks in real time, including data leakage, policy violations, suspicious behavior, and targeted attacks on APIs.
  name: Noname Runtime Protection
  slug: runtime-protection
- description: Noname Active Testing enables organizations to test APIs for vulnerabilities and misconfigurations before they reach production, integrating into CI/CD pipelines for shift-left API security testing.
  name: Noname Active Testing
  slug: active-testing
artifact_total: 8
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/akamai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noname-security-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nonamesec
- group: company
  title: ''
  type: Website
  url: https://nonamesecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nonamesecurity.com/
- group: company
  title: ''
  type: Blog
  url: https://nonamesecurity.com/blog
- group: company
  title: ''
  type: About
  url: https://nonamesecurity.com/company
- group: company
  title: ''
  type: Partners
  url: https://nonamesecurity.com/partners
- group: start
  title: ''
  type: Login
  url: https://app.nonamesecurity.com/
- group: operate
  title: ''
  type: Contact
  url: https://nonamesecurity.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nonamesecurity/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/NonameSecurity
created: '2026-03-26'
description: Noname Security (acquired by Akamai in 2024) is an API security platform that provides complete API discovery, posture management, runtime protection, and active testing capabilities. The platform helps organizations discover all APIs including shadow and rogue APIs, detect misconfigurations and vulnerabilities, and protect against API-based attacks across their entire API estate.
finops:
- name: Noname Security Finops
  service_category: API
  slug: noname-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/noname-security.png
layout: provider
modified: '2026-04-28'
name: Noname Security
nav: Providers
network: true
overview: 'Noname Security publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Discovery, API Security, API Testing, Developer Tools, and Posture Management.


  Noname Security''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Noname Security Plans Pricing
  plan_count: 3
  slug: noname-security-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Noname Security Rate Limits
  slug: noname-security-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/noname-security/refs/heads/main/screenshots/noname-security-2026-06-20T190402.png
security:
- kind: domain-security
  name: Noname Security Domain Security
  slug: noname-security-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: noname-security
tags:
- API Discovery
- API Security
- API Testing
- Developer Tools
- Posture Management
- Runtime Protection
- Shadow APIs
website: https://nonamesecurity.com
---
