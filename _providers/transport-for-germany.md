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
- description: Deutsche Bahn (DB) API
  name: Transport for Germany
  slug: transport-for-germany
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transport-for-germany-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-for-germany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://data.deutschebahn.com/dataset/api-fahrplan
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Deutsche Bahn (DB) API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transport-for-germany.png
layout: provider
modified: '2026-05-28'
name: Transport for Germany
nav: Providers
network: true
overview: Transport for Germany publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/transport-for-germany/refs/heads/main/screenshots/transport-for-germany-2026-06-20T195702.png
security:
- kind: domain-security
  name: Transport For Germany Domain Security
  slug: transport-for-germany-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transport For Germany Vulnerability Disclosure
  slug: transport-for-germany-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: transport-for-germany
tags:
- Transportation
- Public APIs
website: http://data.deutschebahn.com/dataset/api-fahrplan
---
