---
access_model:
  confidence: medium
  label: Sales-led
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.flytedesk.com/
  - https://rfp.flytedesk.com/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The first-party GraphQL API behind the flytedesk application — the campus advertising marketplace covering suppliers (campus media organizations), campuses, buyers, audiences, ad shops, campaigns, ads
  name: FlyteDesk GraphQL API
  slug: flytedesk-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flytedesk-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flytedesk-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/flytedesk-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/flytedesk-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flytedesk-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.flytedesk.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flytedesk.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flytedesk.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flytedesk.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.flytedesk.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.flytedesk.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flytedesk
- group: start
  title: ''
  type: Login
  url: https://platform.flytedesk.com/auth/users/sign_in
created: '2026-07-17'
description: flytedesk is the campus advertising platform that connects national brands with college media across the United States. Founded in 2015 in Boulder, Colorado, it operates the largest network of campus media in the US, letting advertisers create, book, manage, and measure national campaigns across print, digital, email newsletters, social, influencer, radio, and out-of-home channels reaching millions of college students. For college publishers and campus media organizations, its self-serve platform provides tools to build, manage, and monetize their media ecosystem, along with an Audience Builder for targeting. flytedesk is backed by Techstars. The company publishes no developer portal, no API reference and no SDK, but it does operate a first-party GraphQL API at api.app.flytedesk.com with introspection enabled, so its full 374-type schema is publicly readable and is captured here.
image: https://cdn.prod.website-files.com/69a96def413819b7db64de8c/69c65e8608f9f4200cad70f3_Homepage_1.png
layout: provider
modified: '2026-08-12'
name: FlyteDesk
nav: Providers
network: true
overview: 'FlyteDesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Media, Campus Media, and College Advertising.


  FlyteDesk''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Flytedesk Plans Pricing
  plan_count: 0
  slug: flytedesk-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Flytedesk Rate Limits
  slug: flytedesk-rate-limits
score:
  band: thin
  composite: 30.0
  delta: 18.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 43.2
    developer_ergonomics: 13.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 11.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/flytedesk/refs/heads/main/screenshots/flytedesk-2026-07-25T214857.png
security:
- kind: authentication
  name: Flytedesk Authentication
  slug: flytedesk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Flytedesk Domain Security
  slug: flytedesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flytedesk
tags:
- Company
- Advertising
- Media
- Campus Media
- College Advertising
- Marketing
- AdTech
- GraphQL
- Media Buying
- Higher Education
website: https://www.flytedesk.com/
---
