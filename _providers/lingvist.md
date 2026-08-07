---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The OAuth 2.0 protected API behind the Lingvist learning platform. Lingvist publishes no reference documentation for it; the authorization, token and user-profile endpoints are documented in Lingvist'
  name: Lingvist Learn API
  slug: learn-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://lingvist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lingvist.com/help/
- group: operate
  title: ''
  type: Support
  url: https://lingvist.com/help/
- group: company
  title: ''
  type: Blog
  url: https://lingvist.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lingvist.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://learn.lingvist.com/#register
- group: start
  title: ''
  type: Login
  url: https://learn.lingvist.com/#signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lingvist.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lingvist.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lingvist
- group: company
  title: ''
  type: About
  url: https://lingvist.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://lingvist.com/contact/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lingvist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lingvist-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lingvist-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lingvist-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lingvist-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lingvist-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/lingvist-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lingvist-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lingvist-domain-security.yml
created: '2026-07-17'
description: Lingvist is an Estonian education technology company building an AI-powered language-learning platform that uses machine learning, language statistics and spaced repetition to teach the vocabulary a learner actually needs. It was founded by Mait Müntel, a physicist who worked on the Higgs boson discovery team at CERN and built the first prototype to teach himself French. Lingvist maps each learner's knowledge in real time and adapts course material to them individually, offering 60+ courses across 15+ languages, a Custom Decks feature that turns a learner's own words or texts into a course, and a Lingvist for Business offering. Lingvist does not operate a public, self-serve API program - no developer portal, API reference or machine-readable specification is published. It does run an OAuth 2.0 protected API at api.lingvist.com whose endpoints are publicly documented only through Lingvist's own open-source NodeBB single-sign-on plugin, with client credentials arranged directly
  with Lingvist rather than self-registered.
image: https://lingvist.com/assets/images/resized/1200/lingvist.jpg
layout: provider
modified: '2026-07-19'
name: Lingvist
nav: Providers
network: true
overview: 'Lingvist publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Language Learning, EdTech, and Artificial Intelligence.


  Lingvist''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 15 more developer resources.'
random_paper: 89
scopes:
- name: Lingvist Scopes
  scope_count: 1
  slug: lingvist-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 25.0
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lingvist/refs/heads/main/screenshots/lingvist-2026-07-25T225247.png
security:
- kind: authentication
  name: Lingvist Authentication
  slug: lingvist-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lingvist Domain Security
  slug: lingvist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lingvist
tags:
- Company
- Education
- Language Learning
- EdTech
- Artificial Intelligence
- Machine Learning
- Spaced Repetition
- Mobile
- Estonia
- Consumer
website: https://lingvist.com/
---
