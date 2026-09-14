---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swing-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swingtherapeutics.com/
- group: operate
  title: ''
  type: Support
  url: https://swingtherapeutics.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://swingtherapeutics.com/resources/
- group: company
  title: ''
  type: BlogRSS
  url: https://swingtherapeutics.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://swingtherapeutics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swingtherapeutics.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swing-therapeutics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/swing-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swing-therapeutics-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: 'Swing Therapeutics ships one regulated end-user product — Stanza, a prescription-only digital therapeutic dispensed to patients as a native iOS/Android app — and has no developer program of any kind: api., developer. and docs.swingtherapeutics.com are all NXDOMAIN, no GitHub organization exists, and the full STEP 0b contract-discovery probe set 404s on every host the company controls.'
  evidence:
  - status: 404
    url: https://swingtherapeutics.com/openapi.json
  - status: 404
    url: https://swingtherapeutics.com/.well-known/api-catalog
  - status: 404
    url: https://app.swingtherapeutics.com/openapi.json
  - status: 404
    url: https://www.swing.care/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/swingtherapeutics
  - status: 200
    url: https://swingtherapeutics.com/for-clinicians/
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: Swing Therapeutics is a San Francisco digital therapeutics company founded in 2019 that develops evidence-based, smartphone-delivered treatments for chronic illness. Its lead product, Stanza, is a 12-week prescription digital therapeutic delivering Acceptance and Commitment Therapy (ACT) for the management of fibromyalgia symptoms in adults, and in 2023 it became the first digital therapeutic to receive FDA De Novo marketing authorization for that indication. Stanza is prescribed by clinicians and dispensed to patients as a native iOS/Android application; the company also operates Swing Care, a virtual fibromyalgia clinic offering physician visits, medication management and coaching. Swing Therapeutics and Swing Care were acquired by XRHealth in July 2026. The company publishes no public API, developer portal, SDK or machine-readable specification — its software is delivered exclusively as a regulated end-user therapy, and it is an API consumer (its clinical operations run on
  the Healthie EHR API) rather than an API provider.
image: https://swingtherapeutics.com/wp-content/uploads/2021/08/SWI_Favicon_L1R1@2x.png
layout: provider
modified: '2026-08-29'
name: Swing Therapeutics
nav: Providers
network: true
overview: 'Swing Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Therapeutics, Health, Healthcare, and Digital Health.


  Swing Therapeutics'' developer surface includes support, engineering blog, and 8 more developer resources.'
plans:
- name: Swing Therapeutics Plans Pricing
  plan_count: 0
  slug: swing-therapeutics-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Swing Therapeutics Rate Limits
  slug: swing-therapeutics-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/swing-therapeutics/refs/heads/main/screenshots/swing-therapeutics-2026-09-02T161408.png
security:
- kind: domain-security
  name: Swing Therapeutics Domain Security
  slug: swing-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: swing-therapeutics
tags:
- Company
- Digital Therapeutics
- Health
- Healthcare
- Digital Health
- Fibromyalgia
- Chronic Pain
- Behavioral Health
- Prescription Digital Therapeutic
- Telemedicine
- Mobile Application
- No Public API
website: https://swingtherapeutics.com/
---
