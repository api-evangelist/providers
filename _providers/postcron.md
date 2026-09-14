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
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://postcron.com
- group: company
  title: ''
  type: Blog
  url: https://postcron.com/en/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://postcron.com/en/blog/feed
- group: commercial
  title: ''
  type: Pricing
  url: https://postcron.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://postcron.com/app/
- group: operate
  title: ''
  type: HelpCenter
  url: https://postcron.com/en/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postcron.com/en/terms_conditions_privacy_policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postcron.com/en/terms_conditions_privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postcron
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postcron-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postcron-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/postcron-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postcron-rate-limits.yml
coverage:
  checked: '2026-08-13'
  detail: Postcron ships only an end-user scheduling app — there is no developer portal, API reference, spec, SDK or webhook surface anywhere on postcron.com, and the two hosts that do answer (postcron.com/api/ and api.postcron.com/api/v1/) are the web app's own undocumented backends, which reject every unauthenticated call with "You need send a token".
  evidence:
  - status: 404
    url: https://postcron.com/en/api
  - status: 401
    url: https://postcron.com/api/
  - status: 404
    url: https://api.postcron.com/openapi.json
  - status: 404
    url: https://postcron.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Postcron is a social media scheduling and publishing tool that lets marketers, agencies, and small businesses plan, schedule, and automatically publish content across Instagram, Facebook, X (Twitter), LinkedIn, Pinterest, and TikTok from a single dashboard. It supports bulk uploading up to 1,000 posts from Excel or Google Docs, multi-account and team management, automatic image watermarking, a browser extension, and mobile apps for iOS and Android. Originally a Y Combinator / 500 Global-backed startup, Postcron is a consumer- and SMB-facing publishing product; it exposes an internal application API used by its own clients but does not publish a documented public developer API, OpenAPI specification, SDKs, or a developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postcron.png
layout: provider
modified: '2026-08-13'
name: Postcron
nav: Providers
network: true
overview: 'Postcron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social-Media, Social Media Scheduling, Publishing, and Marketing.


  Postcron''s developer surface includes engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Postcron Plans Pricing
  plan_count: 0
  slug: postcron-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Postcron Rate Limits
  slug: postcron-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/postcron/refs/heads/main/screenshots/postcron-2026-09-02T151826.png
security:
- kind: domain-security
  name: Postcron Domain Security
  slug: postcron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postcron
tags:
- Company
- Social-Media
- Social Media Scheduling
- Publishing
- Marketing
- Content Management
- Software-as-a-Service
website: https://postcron.com
---
