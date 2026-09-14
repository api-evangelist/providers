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
- description: Provides information about parcels in transport for Sweden and Denmark
  name: PostNord
  slug: postnord
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/postnord-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postnord-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.postnord.com/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provides information about parcels in transport for Sweden and Denmark
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postnord.png
layout: provider
modified: '2026-05-28'
name: PostNord
nav: Providers
network: true
overview: PostNord publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tracking and Public APIs.
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/postnord/refs/heads/main/screenshots/postnord-2026-06-20T192014.png
security:
- kind: domain-security
  name: Postnord Domain Security
  slug: postnord-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Postnord Vulnerability Disclosure
  slug: postnord-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: postnord
tags:
- Tracking
- Public APIs
website: https://developer.postnord.com/api
---
