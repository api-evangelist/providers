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
api_count: 2
apis:
- description: REST API for managing Zscaler Internet Access policies, URL filtering, cloud sandbox, DLP, location and user provisioning, and reporting on web traffic and threats across the Zscaler Cloud platform.
  name: Zscaler Internet Access (ZIA) API
  slug: zia-api
- description: REST API for managing Zscaler Private Access (ZPA) configurations including segment groups, application segments, connector groups, SCIM provisioning, policies, and access logs.
  name: Zscaler Private Access (ZPA) API
  slug: zpa-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zscaler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zscaler-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zscaler
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zscaler
- group: company
  title: ''
  type: Website
  url: https://www.zscaler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zscaler.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zscaler.com/pricing-and-plans
- group: start
  title: ''
  type: Signup
  url: https://www.zscaler.com/products/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.zscaler.com/blogs
created: '2026-05-11'
description: Zscaler is a cloud security platform delivering Zero Trust Exchange services including Zscaler Internet Access (ZIA), Zscaler Private Access (ZPA), and Zscaler Digital Experience (ZDX). Zscaler exposes REST APIs across its product suite for configuration, policy management, and reporting, authenticated via API keys, OAuth 2.0, or session-based authentication depending on the product and cloud (zsapi).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zscaler.png
layout: provider
modified: '2026-05-11'
name: Zscaler
nav: Providers
network: true
overview: 'Zscaler publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Security, Zero Trust, SASE, Network Security, and SWG.


  Zscaler''s developer surface includes documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/screenshots/zscaler-2026-06-20T201955.png
security:
- kind: domain-security
  name: Zscaler Domain Security
  slug: zscaler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zscaler Vulnerability Disclosure
  slug: zscaler-vulnerability-disclosure
  summary_line: Bugcrowd
slug: zscaler
tags:
- Cloud Security
- Zero Trust
- SASE
- Network Security
- SWG
website: https://www.zscaler.com/
---
