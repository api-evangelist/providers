---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Plausible Agentic Access
  operation_count: 18
  slug: plausible-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 8
apis:
- description: The CustomProps API from Plausible — 2 operation(s) for customprops.
  name: Plausible CustomProps API
  slug: plausible-customprops-api
- description: Submit pageviews and custom events.
  name: Plausible Events API
  slug: plausible-events-api
- description: The Goals API from Plausible — 2 operation(s) for goals.
  name: Plausible Goals API
  slug: plausible-goals-api
- description: The Guests API from Plausible — 2 operation(s) for guests.
  name: Plausible Guests API
  slug: plausible-guests-api
- description: Run analytics queries against site data.
  name: Plausible Query API
  slug: plausible-query-api
- description: The SharedLinks API from Plausible — 1 operation(s) for sharedlinks.
  name: Plausible SharedLinks API
  slug: plausible-sharedlinks-api
- description: The Sites API from Plausible — 2 operation(s) for sites.
  name: Plausible Sites API
  slug: plausible-sites-api
- description: The Teams API from Plausible — 1 operation(s) for teams.
  name: Plausible Teams API
  slug: plausible-teams-api
artifact_total: 17
collections:
- collection_type: open
  name: Plausible Events API
  slug: open-plausible-events
- collection_type: open
  name: Plausible Sites API
  slug: open-plausible-sites
- collection_type: open
  name: Plausible Stats API
  slug: open-plausible-stats
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plausible-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plausible-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plausible-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plausible-analytics
- group: company
  title: ''
  type: Website
  url: https://plausible.io
- group: docs
  title: ''
  type: Documentation
  url: https://plausible.io/docs
- group: docs
  title: ''
  type: APIDocumentation
  url: https://plausible.io/docs/stats-api
- group: start
  title: ''
  type: GettingStarted
  url: https://plausible.io/docs/add-website
- group: company
  title: ''
  type: Blog
  url: https://plausible.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://plausible.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/plausible/analytics
- group: start
  title: ''
  type: Login
  url: https://plausible.io/login
- group: start
  title: ''
  type: Signup
  url: https://plausible.io/register
- group: operate
  title: ''
  type: Support
  url: https://plausible.io/contact
- group: other
  title: ''
  type: SelfHosted
  url: https://plausible.io/self-hosted-web-analytics
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/plausible/analytics/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plausible.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plausible.io/privacy
- group: other
  title: ''
  type: DataPolicy
  url: https://plausible.io/data-policy
created: '2026-03-26'
description: Plausible is an open source, privacy-friendly web analytics platform designed as a lightweight alternative to Google Analytics. It provides essential website traffic metrics without using cookies or collecting personal data, making it compliant with GDPR, CCPA, and other privacy regulations out of the box. It can be self-hosted or used as a cloud service.
finops:
- name: Plausible Finops
  service_category: Analytics
  slug: plausible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plausible.png
layout: provider
modified: '2026-05-19'
name: Plausible
nav: Providers
network: true
overview: 'Plausible publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CustomProps API, Events API, Goals API, and 5 more. Tagged areas include Analytics, Cookie-Free, GDPR, Open Source, and Privacy.


  Plausible''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, GitHub presence, signup flow, and 12 more developer resources.'
plans:
- name: Plausible Plans Pricing
  plan_count: 4
  slug: plausible-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 3
  name: Plausible Rate Limits
  slug: plausible-rate-limits
score:
  band: developing
  composite: 52.9
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 52.3
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/screenshots/plausible-2026-06-20T191759.png
security:
- kind: authentication
  name: Plausible Authentication
  slug: plausible-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plausible Domain Security
  slug: plausible-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plausible
tags:
- Analytics
- Cookie-Free
- GDPR
- Open Source
- Privacy
- Web Analytics
website: https://plausible.io
---
