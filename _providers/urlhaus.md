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
api_count: 1
apis:
- description: Bulk queries and Download Malware Samples
  name: URLhaus
  slug: urlhaus
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/urlhaus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urlhaus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urlhaus-api.abuse.ch/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Bulk queries and Download Malware Samples
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urlhaus.png
layout: provider
modified: '2026-05-28'
name: URLhaus
nav: Providers
network: true
overview: URLhaus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti Malware and Public APIs.
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/urlhaus/refs/heads/main/screenshots/urlhaus-2026-06-20T200529.png
security:
- kind: domain-security
  name: Urlhaus Domain Security
  slug: urlhaus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Urlhaus Vulnerability Disclosure
  slug: urlhaus-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: urlhaus
tags:
- Anti Malware
- Public APIs
website: https://urlhaus-api.abuse.ch/
---
