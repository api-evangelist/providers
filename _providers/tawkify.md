---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tawkify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tawkify.com/
- group: operate
  title: ''
  type: Support
  url: https://tawkify.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://tawkify.com/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://tawkify.com/how-it-works
- group: company
  title: ''
  type: Blog
  url: https://tawkify.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.tawkify.com/onboarding
- group: start
  title: ''
  type: Login
  url: https://app.tawkify.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.tawkify.com/agreement/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.tawkify.com/agreement/privacypolicy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tawkify
- group: company
  title: ''
  type: Press
  url: https://tawkify.com/press
- group: commercial
  title: ''
  type: Plans
  url: plans/tawkify-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tawkify-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Tawkify sells human matchmaking as an end-user consumer service and ships no developer surface at all - api.tawkify.com, developer.tawkify.com and docs.tawkify.com do not resolve, the marketing site's 94-URL sitemap contains no developer or reference page, and the only customer application (app.tawkify.com) is a robots-disallowed private Next.js app that 404s every spec, GraphQL, MCP, agent-card and well-known path probed.
  evidence:
  - status: 0
    url: https://api.tawkify.com/
  - status: 0
    url: https://developer.tawkify.com/
  - status: 404
    url: https://tawkify.com/openapi.json
  - status: 404
    url: https://app.tawkify.com/graphql
  - status: 404
    url: https://app.tawkify.com/.well-known/agent-card.json
  - status: 200
    url: https://app.tawkify.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: Tawkify is a US personalized matchmaking service that pairs paying clients with a trained human matchmaker rather than offering a self-service dating app. Founded in 2012 and headquartered in San Francisco, the company screens and hand-selects introductions from a network of several million singles, arranges curated first dates, and collects structured feedback after each match. Packages are sold by consultation through a client experience specialist instead of a published price list. Tawkify operates a consumer web application at app.tawkify.com for onboarding, profiles and match feedback, but publishes no public API, developer portal, SDK or machine-readable contract of any kind; its engineering surface is entirely internal.
image: https://tawkify.com/api/og
layout: provider
modified: '2026-08-29'
name: Tawkify
nav: Providers
network: true
overview: 'Tawkify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Matchmaking, Online Dating, Relationships, and Consumer Services.


  Tawkify''s developer surface includes support, getting-started guide, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Tawkify Plans Pricing
  plan_count: 0
  slug: tawkify-plans-pricing
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/tawkify/refs/heads/main/screenshots/tawkify-2026-09-02T162616.png
security:
- kind: domain-security
  name: Tawkify Domain Security
  slug: tawkify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tawkify
tags:
- Company
- Matchmaking
- Online Dating
- Relationships
- Consumer Services
- Personal Services
- Concierge
website: https://tawkify.com/
---
