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
  trial: false
  try_now: true
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Buttondown Agentic Access
  operation_count: 14
  slug: buttondown-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 6
apis:
- description: The Emails API from Buttondown — 2 operation(s) for emails.
  name: Buttondown Emails API
  slug: buttondown-emails-api
- description: The Newsletters API from Buttondown — 1 operation(s) for newsletters.
  name: Buttondown Newsletters API
  slug: buttondown-newsletters-api
- description: The Subscribers API from Buttondown — 2 operation(s) for subscribers.
  name: Buttondown Subscribers API
  slug: buttondown-subscribers-api
- description: The Tags API from Buttondown — 2 operation(s) for tags.
  name: Buttondown Tags API
  slug: buttondown-tags-api
- description: The Webhooks API from Buttondown — 1 operation(s) for webhooks.
  name: Buttondown Webhooks API
  slug: buttondown-webhooks-api
- description: The Buttondown hosted newsletter platform provides a markdown-based composition experience, subscriber management, delivery infrastructure, analytics, monetization via paid subscriptions, team collabo
  name: Buttondown Newsletter Platform
  slug: newsletter-platform
artifact_total: 14
collections:
- collection_type: open
  name: Buttondown API
  slug: open-buttondown
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buttondown-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buttondown-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buttondown-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buttondown-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buttondown
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buttondown
- group: company
  title: ''
  type: Website
  url: https://buttondown.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buttondown.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://buttondown.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://buttondown.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://buttondown.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.buttondown.com/changelog
- group: operate
  title: ''
  type: Support
  url: mailto:support@buttondown.email
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.buttondown.com/llms.txt
created: '2026-04-23'
description: Buttondown is an independent email newsletter platform for creators and businesses, offering a markdown editor, automations, paid subscriptions, analytics, team collaboration, and a feature-complete REST API for programmatic management of subscribers, emails, newsletters, and related resources.
finops:
- name: Buttondown Finops
  service_category: API
  slug: buttondown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buttondown.png
layout: provider
modified: '2026-07-25'
name: Buttondown
nav: Providers
network: true
overview: 'Buttondown publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Emails API, Newsletters API, Subscribers API, and 2 more. Tagged areas include Analytics, Automations, Email, Markdown, and Newsletters.


  Buttondown''s developer surface includes authentication, documentation, pricing, engineering blog, changelog, support, and 8 more developer resources.'
plans:
- name: Buttondown Plans Pricing
  plan_count: 3
  slug: buttondown-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Buttondown Rate Limits
  slug: buttondown-rate-limits
score:
  band: thin
  composite: 34.8
  delta: -9.4
  facets:
    commercial_clarity: 26.3
    contract_quality: 52.2
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/buttondown/refs/heads/main/screenshots/buttondown-2026-06-20T173820.png
security:
- kind: authentication
  name: Buttondown Authentication
  slug: buttondown-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Buttondown Domain Security
  slug: buttondown-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buttondown Vulnerability Disclosure
  slug: buttondown-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: buttondown
tags:
- Analytics
- Automations
- Email
- Markdown
- Newsletters
- Paid Subscriptions
- SaaS
- Subscribers
website: https://buttondown.com/
---
