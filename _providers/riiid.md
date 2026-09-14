---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - '{''url'': ''https://www.riiid.com'', ''status'': 301, ''note'': ''declared website redirects to https://corp.socra.ai/ — a different registrable domain (riiid.com -> socra.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://www.riiid.com
  baseurl_source: spec
  description: Riiid's adaptive learning engine analyzes learner interaction data in real time to recommend personalized study paths and content. It is delivered inside Riiid/Socra products (Santa) and to partners v
  name: Riiid Adaptive Learning
  slug: adaptive-learning
- baseURL: https://www.riiid.com
  baseurl_source: spec
  description: Proprietary deep knowledge tracing and score-prediction models (built on 100M+ student interactions, the EdNet dataset) estimate a learner's mastery and predict test outcomes in real time. Exposed thr
  name: Riiid Knowledge Tracing
  slug: knowledge-tracing
- baseURL: https://www.riiid.com
  baseurl_source: spec
  description: Santa is Riiid's consumer AI tutor app for standardized English tests (TOEIC, and TOEFL via an ETS content partnership). It is distributed as iOS / Android mobile applications with no documented publi
  name: Riiid Santa
  slug: santa
- baseURL: https://www.riiid.com
  baseurl_source: spec
  description: B2B / AI-as-a-Service (R.Inside) engagements that embed Riiid's adaptive learning and knowledge-tracing AI into partner education platforms. Access is sales-led and contract-based via partnership@socr
  name: Riiid Partner Solutions
  slug: partner-solutions
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Riiid API
  slug: open-riiid
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riiid-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riiid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/riiid
- group: company
  title: ''
  type: Website
  url: https://www.riiid.com
- group: docs
  title: ''
  type: Documentation
  url: https://corp.socra.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/riiid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/riiid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/riiid-finops.yml
created: '2026-06-21'
description: Riiid (now operating as Socra AI) is an AI education technology company whose proprietary deep-knowledge-tracing and score-prediction models power adaptive learning. Its consumer product Santa (AI TOEIC / TOEFL test prep) and its R.Inside AI-as-a-Service offering bring real-time student modeling to partners. Riiid does not publish a public, self-serve developer API; its AI is delivered through B2B partner integrations and packaged products.
finops:
- name: Riiid Finops
  service_category: AI and Machine Learning
  slug: riiid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riiid.png
layout: provider
modified: '2026-06-21'
name: Riiid
nav: Providers
network: true
overview: 'Riiid publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Adaptive Learning, Knowledge Tracing, Santa, and 1 more. Tagged areas include Artificial Intelligence, Education, Adaptive Learning, Knowledge Tracing, and EdTech.


  Riiid''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Riiid Plans Pricing
  plan_count: 2
  slug: riiid-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Riiid Rate Limits
  slug: riiid-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/riiid/refs/heads/main/screenshots/riiid-2026-09-02T153824.png
security:
- kind: domain-security
  name: Riiid Domain Security
  slug: riiid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riiid
tags:
- Artificial Intelligence
- Education
- Adaptive Learning
- Knowledge Tracing
- EdTech
website: https://www.riiid.com
---
