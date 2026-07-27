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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Donorbox Agentic Access
  operation_count: 7
  slug: donorbox-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: Fundraising campaigns.
  name: Donorbox Campaigns API
  slug: donorbox-campaigns-api
- description: One-time and recurring donation transactions.
  name: Donorbox Donations API
  slug: donorbox-donations-api
- description: Donor/supporter profiles.
  name: Donorbox Donors API
  slug: donorbox-donors-api
- description: Ticketed fundraising events.
  name: Donorbox Events API
  slug: donorbox-events-api
- description: Recurring donation subscriptions.
  name: Donorbox Plans API
  slug: donorbox-plans-api
- description: Event ticket purchase transactions.
  name: Donorbox Purchases API
  slug: donorbox-purchases-api
- description: Individual event tickets.
  name: Donorbox Tickets API
  slug: donorbox-tickets-api
artifact_total: 16
collections:
- collection_type: open
  name: Donorbox API
  slug: open-donorbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/donorbox-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/donorbox-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/donorbox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donorbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/donorbox-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/donorbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/donorbox
- group: company
  title: ''
  type: Website
  url: https://donorbox.org
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/donorbox/donorbox-api/wiki
- group: commercial
  title: ''
  type: Plans
  url: plans/donorbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/donorbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/donorbox-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://donorbox.org/nonprofit-blog/feed/
created: '2026-07-03'
description: Donorbox is an online donation and fundraising platform for nonprofits, offering branded donation forms, recurring giving, peer-to-peer campaigns, event ticketing, memberships, and text-to-give. Its REST API (an add-on available on Pro and Premium plans) exposes read-only access to Campaigns, Donations, Plans (recurring donation subscriptions), Donors, Events, Tickets, and Ticket Purchases, authenticated with HTTP Basic Auth using an organization email and API key, with custom webhooks available as an alternative to polling.
finops:
- name: Donorbox Finops
  service_category: Nonprofit Fundraising and Payments
  slug: donorbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donorbox.png
layout: provider
modified: '2026-07-03'
name: Donorbox
nav: Providers
network: true
overview: 'Donorbox publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Donations API, Donors API, and 4 more. Tagged areas include Nonprofit, Fundraising, Donations, Payments, and Recurring Giving.


  Donorbox''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Donorbox Plans Pricing
  plan_count: 4
  slug: donorbox-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 2
  name: Donorbox Rate Limits
  slug: donorbox-rate-limits
score:
  band: thin
  composite: 43.1
  delta: 2.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donorbox/refs/heads/main/screenshots/donorbox-2026-07-25T212301.png
security:
- kind: authentication
  name: Donorbox Authentication
  slug: donorbox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Donorbox Domain Security
  slug: donorbox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Donorbox Vulnerability Disclosure
  slug: donorbox-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Donorbox Trust Center
  slug: donorbox-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: donorbox
tags:
- Nonprofit
- Fundraising
- Donations
- Payments
- Recurring Giving
- Event Ticketing
website: https://donorbox.org
---
