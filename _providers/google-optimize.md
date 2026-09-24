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
- description: API for managing Google Optimize experiments, variants, and accessing optimization data. Sunset on September 30, 2023. Migrate to Google Analytics 4 experiments or third-party A/B testing tools.
  name: Google Optimize API (Sunset)
  slug: optimize-api
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/security/google-optimize-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-optimize-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/security/google-optimize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-optimize-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://support.google.com/optimize/answer/12979939
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/analytics/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.google.com/analytics/terms/us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/well-known/google-optimize-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-optimize-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/well-known/google-optimize-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-optimize-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/lifecycle/google-optimize-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-optimize-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.google.com/optimize/answer/12979939
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/packages/google-optimize-packages.yml
  title: ''
  type: Packages
  url: packages/google-optimize-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/llms/google-optimize-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-optimize-llms.txt
coverage:
  checked: '2026-09-12'
  detail: Google Optimize and Optimize 360 were sunset on 2023-09-30 and the product is now a tombstone — developers.google.com/optimize and optimize.google.com both redirect in full to a single Help Center sunset notice, the documented base https://www.googleapis.com/optimize/v1 returns 404, and Google's own API Discovery directory listed 530 services on 2026-09-12 with no Optimize entry among them.
  evidence:
  - status: 200
    url: https://developers.google.com/optimize
  - status: 404
    url: https://www.googleapis.com/optimize/v1
  - status: 404
    url: https://optimize.googleapis.com/
  - status: 200
    url: https://www.googleapis.com/discovery/v1/apis?name=optimize
  - status: 200
    url: https://support.google.com/optimize/answer/12979939
  reason: defunct
  state: none
created: '2024-01-01'
description: Google Optimize was a website optimization and A/B testing tool that helped businesses test variations of web pages and personalize experiences. Google Optimize and Optimize 360 were sunset on September 30, 2023. Google recommends migrating to Google Analytics 4 with built-in A/B testing or third-party tools.
features:
- description: Test two or more variants of a web page to determine which performs better. Service sunset September 30, 2023.
  name: A/B Testing (Sunset)
- description: Test combinations of multiple page elements simultaneously. Service sunset September 30, 2023.
  name: Multivariate Testing (Sunset)
- description: Test entirely different pages against each other. Service sunset September 30, 2023.
  name: Redirect Tests (Sunset)
- description: Deliver targeted experiences to specific audience segments. Service sunset September 30, 2023.
  name: Personalization (Sunset)
- description: Native integration with Google Analytics for experiment targeting and reporting. Service sunset September 30, 2023.
  name: Google Analytics Integration (Sunset)
- description: WYSIWYG editor for creating test variants without code changes. Service sunset September 30, 2023.
  name: Visual Editor (Sunset)
finops:
- name: Google Optimize Finops
  service_category: API
  slug: google-optimize-finops
image: https://www.gstatic.com/images/branding/product/1x/optimize_48dp.png
layout: provider
modified: '2026-09-12'
name: Google Optimize
nav: Providers
network: true
overview: 'Google Optimize publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include A/B Testing, Analytics, Deprecated, Experimentation, and Google.


  The Google Optimize catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Optimize''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Google Optimize Plans Pricing
  plan_count: 0
  slug: google-optimize-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Google Optimize Rate Limits
  slug: google-optimize-rate-limits
rules:
- effective_rule_count: 13
  extends: []
  name: Google Optimize API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: google-optimize-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/google-optimize/refs/heads/main/screenshots/google-optimize-2026-06-20T182219.png
security:
- kind: domain-security
  name: Google Optimize Domain Security
  slug: google-optimize-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Google Optimize Vulnerability Disclosure
  slug: google-optimize-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-optimize
solutions:
- description: Free A/B testing tool sunset September 30, 2023. Migrate to GA4 experiments or third-party tools.
  name: Google Optimize (Sunset)
- description: Enterprise A/B testing tool sunset September 30, 2023. Part of Google Marketing Platform.
  name: Google Optimize 360 (Sunset)
tags:
- A/B Testing
- Analytics
- Deprecated
- Experimentation
- Google
- Optimization
- Personalization
- Defunct
use_cases:
- description: Test landing page variations to improve conversion rates. (Service sunset)
  name: Landing Page Optimization
- description: Test call-to-action button text, color, and placement. (Service sunset)
  name: CTA Testing
- description: Show different content to different audience segments. (Service sunset)
  name: Content Personalization
- description: Test checkout process variations to reduce abandonment. (Service sunset)
  name: Checkout Flow Optimization
website: https://www.google.com/
---
