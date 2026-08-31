---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
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
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
