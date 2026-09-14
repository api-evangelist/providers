---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/varsity-tutors-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.varsitytutors.com/
- group: company
  title: ''
  type: Blog
  url: https://www.varsitytutors.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.varsitytutors.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.varsitytutors.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.varsitytutors.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/varsitytutors
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/varsity-tutors-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/varsity-tutors-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/varsity-tutors-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/varsity-tutors-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/varsity-tutors-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: 'Varsity Tutors runs a real first-party API gateway at api.varsitytutors.com (its responses carry `server: vt-apigw`), but its robots.txt reads `Allow: /vtwa/v1/link_blocks_directory/lookup` then `Disallow: /` — the gateway exists only to serve the company''s own web and mobile clients, and the company publishes no developer portal, API reference, SDK or machine-readable contract on any of its four first-party hosts; its sole documented third-party integration is a Clever app-gallery listing in which Varsity Tutors CONSUMES Clever''s Instant Login and Secure Sync rostering APIs rather than exposing one of its own.'
  evidence:
  - status: 200
    url: https://api.varsitytutors.com/robots.txt
  - status: 404
    url: https://api.varsitytutors.com/openapi.json
  - status: 403
    url: https://api.varsitytutors.com/graphql
  - status: 404
    url: https://www.varsitytutors.com/.well-known/agent-card.json
  - status: 404
    url: https://developer.varsitytutors.com/
  - status: 404
    url: https://docs.varsitytutors.com/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Varsity Tutors, a Nerdy company (NYSE: NRDY), is a St. Louis based live online learning platform that connects K-12, college, graduate and professional learners with expert instructors for private one-on-one tutoring, small-group and large-format live classes, test preparation, practice tests and diagnostics across more than 3,000 subjects. Alongside its direct-to-consumer memberships it sells Varsity Tutors for Schools to school districts, and it ships an AI-enhanced learning surface at ai.varsitytutors.com. The company operates a production API gateway at api.varsitytutors.com that serves its own web and mobile clients, but it publishes no public developer portal, API reference or machine-readable contract; its only documented third-party integration surface is its Clever app-gallery listing, which provides Clever Instant Login SSO and Clever Secure Sync rostering to districts.'
image: https://www.varsitytutors.com/favicon.ico
layout: provider
modified: '2026-09-02'
name: Varsity Tutors
nav: Providers
network: true
overview: 'Varsity Tutors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Tutoring.


  Varsity Tutors'' developer surface includes engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Varsity Tutors Plans Pricing
  plan_count: 0
  slug: varsity-tutors-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Varsity Tutors Rate Limits
  slug: varsity-tutors-rate-limits
security:
- kind: domain-security
  name: Varsity Tutors Domain Security
  slug: varsity-tutors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: varsity-tutors
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Test Preparation
- K-12
- Live Classes
- Rostering
- Single Sign-On
- Artificial Intelligence
website: https://www.varsitytutors.com/
---
