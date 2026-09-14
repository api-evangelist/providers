---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Horoscope Api Agentic Access
  operation_count: 3
  slug: horoscope-api-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://freehoroscopeapi.com/api/v1
  baseurl_source: declared
  description: Horoscope predictions by zodiac sign
  name: Horoscope API Horoscope API
  slug: horoscope-api-horoscope-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Horoscope API
  slug: open-horoscope-api-horoscope-api
- collection_type: open
  name: Horoscope API
  slug: open-horoscope-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/horoscope-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/horoscope-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://freehoroscopeapi.com
created: '2025-01-07'
description: The Horoscope API offers a versatile solution for accessing daily, weekly, and monthly horoscope predictions tailored to each zodiac sign. With intuitive endpoints, developers can seamlessly integrate astrological insights into their applications, delivering accurate and personalized horoscope data in JSON format.
finops:
- name: Horoscope Api Finops
  service_category: API
  slug: horoscope-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/horoscope-api.png
layout: provider
modified: '2026-05-19'
name: Horoscope API
nav: Providers
network: true
overview: 'Horoscope API publishes 1 API on the [APIs.io](https://apis.io/) network: Horoscope API. Tagged areas include Astrology, Content, Horoscope, and Zodiac.


  The Horoscope API catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Horoscope Api Plans Pricing
  plan_count: 3
  slug: horoscope-api-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Horoscope Api Rate Limits
  slug: horoscope-api-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Horoscope API API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: horoscope-api-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/horoscope-api/refs/heads/main/screenshots/horoscope-api-2026-06-20T182833.png
security:
- kind: domain-security
  name: Horoscope Api Domain Security
  slug: horoscope-api-domain-security
  summary_line: TLSv1.3
slug: horoscope-api
tags:
- Astrology
- Content
- Horoscope
- Zodiac
website: https://freehoroscopeapi.com
---
