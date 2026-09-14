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
api_count: 1
apis:
- description: OffenderList provides security and information-focused organizations API access, batch requests, remote access, and internal access to a national sex offender database.
  name: OffenderList
  slug: offenderlist
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offenderlist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://offenderlist.us/
- group: company
  title: ''
  type: Blog
  url: https://offenderlist.us/feed/
created: '2024-11-13'
description: OffenderList is a comprehensive online platform that provides information about individuals who have been convicted of criminal offenses. The website allows users to search for offenders based on various criteria such as name, location, or offense type. OffenderList provides important details about each offender, including their mugshot, charges, conviction date, and sentence length. OffenderList provides security and information-focused organizations API access, batch requests, remote access, and internal access to a national sex offender database.
finops:
- name: Offenderlist Finops
  service_category: API
  slug: offenderlist-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/offenderlist.png
layout: provider
modified: '2026-04-28'
name: OffenderList
nav: Providers
network: true
overview: 'OffenderList publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sex Offenders, Public Safety, and Criminal Records.


  OffenderList''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Offenderlist Plans Pricing
  plan_count: 3
  slug: offenderlist-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Offenderlist Rate Limits
  slug: offenderlist-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/offenderlist/refs/heads/main/screenshots/offenderlist-2026-06-20T190626.png
security:
- kind: domain-security
  name: Offenderlist Domain Security
  slug: offenderlist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: offenderlist
tags:
- Sex Offenders
- Public Safety
- Criminal Records
website: https://offenderlist.us/
---
