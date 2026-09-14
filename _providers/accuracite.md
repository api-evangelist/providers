---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
api_count: 1
apis:
- description: 'Synchronous REST API for citation verification and claim-to-source lookup. Two operations, both POST and both keyed by an X-API-Key header: /api/v1/verify checks a citation string (or a bare URL, or a'
  name: AccuraCite API
  slug: accuracite-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://accuracite.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accuracite-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accuracite-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/accuracite-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accuracite-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accuracite-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accuracite-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accuracite-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accuracite-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accuracite-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accuracite-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://accuracite.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://accuracite.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://accuracite.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://accuracite.com/blog
- group: operate
  title: ''
  type: Support
  url: https://accuracite.com/feedback
- group: start
  title: ''
  type: SignUp
  url: https://accuracite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accuracite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accuracite.com/privacy
created: '2026-08-31'
description: 'AccuraCite verifies bibliographies and finds real citations, catching AI-hallucinated references before they are published. Every citation supplied as raw text, BibTeX, RIS or an uploaded PDF is checked against eight academic indexes -- OpenAlex, Crossref, Semantic Scholar, PubMed, DBLP, arXiv, CORE and Google Scholar -- and returned as verified, mismatch or not_found, with the matched bibliographic record and a field-level list of what disagreed. A second surface runs the other direction: given a claim, it returns real papers whose abstracts actually support it rather than papers whose titles merely look related. Both are exposed over a small synchronous REST API (POST /api/v1/verify and POST /api/v1/generate) keyed by an X-API-Key header and metered from a shared monthly credit pool. AccuraCite is a solo-founder product built by a computer-science PhD after finding fabricated citations in a co-authored, partly AI-drafted paper.'
image: https://accuracite.com/static/img/og-image.png
layout: provider
modified: '2026-08-31'
name: AccuraCite
nav: Providers
network: true
overview: 'AccuraCite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Citations, Research, Bibliography, Academic, and Verification.


  AccuraCite''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 12 more developer resources.'
plans:
- name: Accuracite Plans Pricing
  plan_count: 5
  slug: accuracite-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Accuracite Rate Limits
  slug: accuracite-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/screenshots/accuracite-2026-09-02T144112.png
security:
- kind: authentication
  name: Accuracite Authentication
  slug: accuracite-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Accuracite Domain Security
  slug: accuracite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accuracite
tags:
- Citations
- Research
- Bibliography
- Academic
- Verification
- AI Safety
website: https://accuracite.com/
---
