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
- description: Assesses weather condition in specific locations
  name: Yandex.Weather
  slug: yandexweather
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-weather-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yandex-weather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yandex.com/dev/weather/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Assesses weather condition in specific locations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yandex-weather.png
layout: provider
modified: '2026-05-28'
name: Yandex.Weather
nav: Providers
network: true
overview: Yandex.Weather publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/yandex-weather/refs/heads/main/screenshots/yandex-weather-2026-06-20T201723.png
security:
- kind: domain-security
  name: Yandex Weather Domain Security
  slug: yandex-weather-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Yandex Weather Vulnerability Disclosure
  slug: yandex-weather-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yandex-weather
tags:
- Weather
- Public APIs
website: https://yandex.com/dev/weather/
---
