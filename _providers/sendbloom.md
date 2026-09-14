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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendbloom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendbloom.com
created: '2026-07-17'
description: sendbloom was surfaced as a portfolio company of Slow Ventures and added to the API Evangelist network as a stub for enrichment. An enrichment probe on 2026-07-21 found sendbloom.com parked on a Namecheap parking IP with no live HTTPS site (it 302-redirects to a non-resolving host); no docs, developer, or api subdomain resolves and no public API surface exists. Google Workspace MX and a legacy email-SaaS SPF record (Intercom + Mandrill) remain, indicating a dormant/defunct provider rather than an active API. Kept as a lead; no artifacts beyond a probed domain-security profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendbloom.png
layout: provider
modified: '2026-07-21'
name: sendbloom
nav: Providers
network: true
overview: sendbloom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 18
security:
- kind: domain-security
  name: Sendbloom Domain Security
  slug: sendbloom-domain-security
  summary_line: no transport/DNS hardening detected
slug: sendbloom
tags:
- Company
website: https://sendbloom.com
---
