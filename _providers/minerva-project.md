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
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minerva-project-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.minervaproject.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.minervaproject.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.minervaproject.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.minervaproject.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/minervaproject
- group: start
  title: ''
  type: SignUp
  url: https://forum.minervaproject.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.minervaproject.com/mp-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.minervaproject.com/mp-privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.minervaproject.com/mp-security
- group: design
  title: ''
  type: Conformance
  url: conformance/minerva-project-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/minerva-project-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/minerva-project-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/minerva-project-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/minerva-project-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/minerva-project-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Minerva Project ships Forum as an end-user learning platform licensed to partner institutions and reached through a browser behind per-institution SSO — its own sitemap lists no developer, documentation or pricing page, api.minervaproject.com and developer.minervaproject.com do not resolve, and every OpenAPI/GraphQL/MCP/agent-card path probed on minervaproject.com, forum.minervaproject.com and help.minervaproject.com returned 404.
  evidence:
  - status: 404
    url: https://www.minervaproject.com/openapi.json
  - status: 404
    url: https://forum.minervaproject.com/openapi.json
  - status: 404
    url: https://help.minervaproject.com/.well-known/agent-card.json
  - status: 200
    url: https://www.minervaproject.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Minerva Project is a San Francisco based education company founded in 2012 that partners with universities, secondary schools and corporate academies to redesign their academic programs around active learning, and delivers that redesign on Forum, its own purpose-built synchronous learning platform. Forum runs live seminars for up to hundreds of concurrent learners with breakout groups, shared whiteboards, polls, tagged video recordings, TalkTime engagement analytics, and assessment against explicit learning outcomes. The company also incubated Minerva University and the Minerva Baccalaureate. Minerva Project sells institutional partnerships and a licensed platform, not a developer product: as of this profiling pass it publishes no public API, no developer portal, and no machine-readable contract, and Forum access is provisioned per partner institution behind SSO.'
image: https://cdn.prod.website-files.com/692097cb0554e89f100a2d98/699365f874c8a3ea7bbac155_MinervaProject-home.jpg
layout: provider
modified: '2026-08-25'
name: Minerva Project
nav: Providers
network: true
overview: 'Minerva Project is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Higher Education, and Learning Platform.


  Minerva Project''s developer surface includes documentation, support, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Minerva Project Plans Pricing
  plan_count: 0
  slug: minerva-project-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Minerva Project Rate Limits
  slug: minerva-project-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/minerva-project/refs/heads/main/screenshots/minerva-project-2026-09-02T150743.png
security:
- kind: domain-security
  name: Minerva Project Domain Security
  slug: minerva-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Minerva Project Vulnerability Disclosure
  slug: minerva-project-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Minerva Project Trust Center
  slug: minerva-project-trust-center
  summary_line: SOC 2 Type II, GDPR, FERPA
slug: minerva-project
tags:
- Company
- Education
- EdTech
- Higher Education
- Learning Platform
- Active Learning
- Virtual Classroom
- Assessment
- Learning Analytics
website: https://www.minervaproject.com/
---
