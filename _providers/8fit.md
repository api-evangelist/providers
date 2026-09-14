---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://8fit.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.withings.com/en-us — a different registrable domain (8fit.com -> withings.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/8fit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/8fit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8fit-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/8fit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/8fit-security.txt
- group: company
  title: ''
  type: Website
  url: https://8fit.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://8fit.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://8fit.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://8fit.com/articles/
- group: start
  title: ''
  type: SignUp
  url: https://8fit.com/signup/
- group: start
  title: ''
  type: Login
  url: https://8fit.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://8fit.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://8fit.com/privacy/
created: '2026-07-17'
description: 8fit is a consumer health and fitness application offering personalized home workout programs (HIIT, boxing, Pilates, yoga, and meditation), custom healthy meal and nutrition plans, and holistic wellness guidance built around sustainable habit-building rather than quick fixes. Founded in Berlin and surfaced in the API Evangelist network as a portfolio company of Creandum, 8fit reached more than 40 million downloads before being acquired by Withings (a Gilde Healthcare portfolio company) in February 2022. Withings announced the discontinuation of the standalone 8fit app effective June 26, 2026, folding its nutrition and activity content into the Withings app and Withings+ service. 8fit is a mobile/web consumer app and does not publish a public developer API; this profile captures its public web, security, and identity surface.
image: https://images.ctfassets.net/90pc6zknij8o/QKISIkVdSR3h8d2wmF2tc/62dc9226c81562cffdd0a4418fe69904/web_link_image.png
layout: provider
modified: '2026-07-17'
name: 8fit
nav: Providers
network: true
overview: '8fit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fitness, Health, and Wellness.


  8fit''s developer surface includes support, engineering blog, signup flow, and 10 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/8fit/refs/heads/main/screenshots/8fit-2026-07-25T181241.png
security:
- kind: domain-security
  name: 8Fit Domain Security
  slug: 8fit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 8Fit Vulnerability Disclosure
  slug: 8fit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 8fit
tags:
- Company
- Consumer
- Fitness
- Health
- Wellness
- Nutrition
- Mobile App
website: https://8fit.com/
---
