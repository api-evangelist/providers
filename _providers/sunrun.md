---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: The Sunrun API provides access to platform services and data for enterprise integration and automation.
  name: Sunrun API
  slug: sunrun-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sunrun-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunrun-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SunRun
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sunrun
- group: company
  title: ''
  type: Website
  url: https://www.sunrun.com
created: '2026-04-19'
description: Sunrun is a major US corporation and Fortune 1000 company. The Sunrun API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Sunrun Finops
  service_category: Residential Solar & Storage
  slug: sunrun-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sunrun.png
layout: provider
modified: '2026-04-19'
name: Sunrun
nav: Providers
network: true
overview: Sunrun publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Residential Solar and Clean Energy.
plans:
- name: Sunrun Plans Pricing
  plan_count: 1
  slug: sunrun-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Sunrun Rate Limits
  slug: sunrun-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/sunrun/refs/heads/main/screenshots/sunrun-2026-06-20T194705.png
security:
- kind: domain-security
  name: Sunrun Domain Security
  slug: sunrun-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sunrun Vulnerability Disclosure
  slug: sunrun-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sunrun
tags:
- Residential Solar
- Clean Energy
website: https://www.sunrun.com
---
