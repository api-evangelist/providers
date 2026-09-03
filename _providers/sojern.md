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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://sojern.com
- group: company
  title: ''
  type: About
  url: https://www.sojern.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.sojern.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sojern.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sojern.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sojern.com/legal
- group: operate
  title: ''
  type: Support
  url: https://www.sojern.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://sojernportal.zendesk.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://sojernportal.zendesk.com/hc/en-us/categories/17486414747028-Getting-Started
- group: docs
  title: ''
  type: Documentation
  url: https://www.sojern.com/legal/partner-documentation
- group: start
  title: ''
  type: Login
  url: https://portal.sojern.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sojern
- group: auth
  title: ''
  type: Compliance
  url: https://www.sojern.com/privacy
- group: design
  title: ''
  type: Conformance
  url: conformance/sojern-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sojern-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sojern-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sojern-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sojern-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: 'Sojern runs no developer program at all — api.sojern.com is live but 404s every spec path, the only public technical document is a legal "Technology Specifications for Partners" page describing a JavaScript pixel and a server-to-server postback, and the sole machine-readable contract is the customer portal''s Hasura GraphQL backend, which answers anonymous callers with "introspection is disabled for role: anonymous".'
  evidence:
  - status: 404
    url: https://api.sojern.com/openapi.json
  - status: 200
    url: https://portal.sojern.com/backend/v1/graphql
  - status: 404
    url: https://www.sojern.com/.well-known/agent-card.json
  - status: 200
    url: https://sojernportal.zendesk.com/api/v2/help_center/articles/search.json?query=api
  - status: 200
    url: https://www.sojern.com/legal/partner-documentation
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Sojern is an AI-powered digital marketing platform built for the hospitality and travel industry. Powered by the Sojern Traveler Ecosystem, it unifies real-time traveler intent data, AI-driven audience predictions, and multichannel media activation across display, social, video, connected TV, SEM, metasearch, email, and native channels to help hotels, destinations, attractions, airlines, and agencies drive direct bookings, improve ROI, and grow guest loyalty. The platform spans audiences, creative services, activation, optimization, measurement, and attribution, plus guest-experience tools. Sojern publishes no public developer program: there is no developer portal, no API reference and no machine-readable contract. Its integration surface is the partner-side Sojern Universal Pixel and server-to-server postback described in its Technology Specifications for Partners, while the customer portal is backed by an authenticated GraphQL endpoint whose introspection is disabled for
  anonymous callers. This is a company profile in the API Evangelist network.'
image: https://cdn.prod.website-files.com/62f4d9f104e0675aa0d8401e/63a3caf0ed595569eb075b4d_Hotels-11.webp
layout: provider
modified: '2026-08-12'
name: Sojern
nav: Providers
network: true
overview: 'Sojern is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hospitality, Marketing, and Advertising.


  Sojern''s developer surface includes engineering blog, pricing, support, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Sojern Plans Pricing
  plan_count: 7
  slug: sojern-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Sojern Rate Limits
  slug: sojern-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.5
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sojern/refs/heads/main/screenshots/sojern-2026-09-02T160103.png
security:
- kind: domain-security
  name: Sojern Domain Security
  slug: sojern-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sojern
tags:
- Company
- Travel
- Hospitality
- Marketing
- Advertising
- AdTech
- MarTech
- Travel Marketing
- Audiences
- Data
website: https://sojern.com
---
