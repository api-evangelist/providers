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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: API for managing Google Optimize experiments, variants, and accessing optimization data. Sunset on September 30, 2023. Migrate to Google Analytics 4 experiments or third-party A/B testing tools.
  name: Google Optimize API (Sunset)
  slug: optimize-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-optimize-vulnerability-disclosure.yml
- group: auth
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
modified: '2026-04-28'
name: Google Optimize
nav: Providers
network: true
overview: 'Google Optimize publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include A/B Testing, Analytics, Deprecated, Experimentation, and Google.


  The Google Optimize catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Optimize''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Google Optimize Plans Pricing
  plan_count: 3
  slug: google-optimize-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Google Optimize Rate Limits
  slug: google-optimize-rate-limits
rules:
- name: Google Optimize API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: google-optimize-spectral-rules
score:
  band: thin
  composite: 28.5
  delta: -3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 27.1
    operational_transparency: 31.6
  previous_composite: 31.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Sunset
use_cases:
- description: Test landing page variations to improve conversion rates. (Service sunset)
  name: Landing Page Optimization
- description: Test call-to-action button text, color, and placement. (Service sunset)
  name: CTA Testing
- description: Show different content to different audience segments. (Service sunset)
  name: Content Personalization
- description: Test checkout process variations to reduce abandonment. (Service sunset)
  name: Checkout Flow Optimization
---
