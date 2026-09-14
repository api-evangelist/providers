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
- description: Use geocoding to get an object's coordinates from its address
  name: Yandex.Maps Geocoder
  slug: yandexmaps-geocoder
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-maps-geocoder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yandex-maps-geocoder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yandex.com/dev/maps/geocoder
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Use geocoding to get an object's coordinates from its address
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yandex-maps-geocoder.png
layout: provider
modified: '2026-05-28'
name: Yandex.Maps Geocoder
nav: Providers
network: true
overview: Yandex.Maps Geocoder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/yandex-maps-geocoder/refs/heads/main/screenshots/yandex-maps-geocoder-2026-06-20T201723.png
security:
- kind: domain-security
  name: Yandex Maps Geocoder Domain Security
  slug: yandex-maps-geocoder-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Yandex Maps Geocoder Vulnerability Disclosure
  slug: yandex-maps-geocoder-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yandex-maps-geocoder
tags:
- Geocoding
- Public APIs
website: https://yandex.com/dev/maps/geocoder
---
