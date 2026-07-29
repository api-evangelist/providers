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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Pushpress Agentic Access
  operation_count: 45
  slug: pushpress-agentic-access
  summary_line: 45 operations · 16 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Programmatic API key management.
  name: PushPress ApiKeys API
  slug: pushpress-apikeys-api
- description: Scheduled one-on-one or small-group appointments.
  name: PushPress Appointments API
  slug: pushpress-appointments-api
- description: Marketing / lead-source attributions for a customer.
  name: PushPress Attributions API
  slug: pushpress-attributions-api
- description: Class, appointment, event, and open-facility check-ins.
  name: PushPress Checkins API
  slug: pushpress-checkins-api
- description: Scheduled classes and class types.
  name: PushPress Classes API
  slug: pushpress-classes-api
- description: The gym / business (company) the API key is scoped to.
  name: PushPress Company API
  slug: pushpress-company-api
- description: Gym members and leads (customers).
  name: PushPress Customers API
  slug: pushpress-customers-api
- description: Customer enrollments in membership plans.
  name: PushPress Enrollments API
  slug: pushpress-enrollments-api
- description: Gym events (workshops, competitions, socials).
  name: PushPress Events API
  slug: pushpress-events-api
- description: Invitations for members or staff to join the gym on PushPress.
  name: PushPress Invitations API
  slug: pushpress-invitations-api
- description: Transactional email, SMS, push, and in-app notifications.
  name: PushPress Messages API
  slug: pushpress-messages-api
- description: Membership and billing plans offered by the gym.
  name: PushPress Plans API
  slug: pushpress-plans-api
- description: Platform webhook subscriptions for real-time events.
  name: PushPress Webhooks API
  slug: pushpress-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: PushPress Platform API
  slug: open-pushpress
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pushpress-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pushpress-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pushpress-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PushPress
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pushpress
- group: company
  title: ''
  type: Website
  url: https://www.pushpress.com
- group: docs
  title: ''
  type: Documentation
  url: https://ppe.apidocumentation.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/pushpress-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pushpress-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pushpress-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pushpress.com/blog
created: '2026-07-12'
description: PushPress is a gym and fitness business management platform covering membership management, billing and payments, class and appointment scheduling, check-ins, CRM, and a member app. The PushPress Platform API is a REST API (base https://api.pushpress.com/v3) that lets developers read and manage customers (members), check-ins, appointments, classes, events, plan enrollments, membership plans, invitations, and transactional messaging, and subscribe to platform webhooks for real-time events. Requests are authenticated with an API key in the API-KEY header and scoped to a single gym location with a company-id header.
finops:
- name: Pushpress Finops
  service_category: Business Management Software
  slug: pushpress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pushpress.png
layout: provider
modified: '2026-07-12'
name: PushPress
nav: Providers
network: true
overview: 'PushPress publishes 13 APIs on the [APIs.io](https://apis.io/) network, including ApiKeys API, Appointments API, Attributions API, and 10 more. Tagged areas include Fitness, Gym Management, Membership Management, Fitness Software, and Class Scheduling.


  PushPress'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pushpress Plans Pricing
  plan_count: 5
  slug: pushpress-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Pushpress Rate Limits
  slug: pushpress-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pushpress Authentication
  slug: pushpress-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pushpress Domain Security
  slug: pushpress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pushpress
tags:
- Fitness
- Gym Management
- Membership Management
- Fitness Software
- Class Scheduling
- Billing
- CRM
- Wellness
- SaaS
- Webhooks
website: https://www.pushpress.com
---
