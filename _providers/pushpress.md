---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Pushpress Agentic Access
  operation_count: 45
  slug: pushpress-agentic-access
  summary_line: 45 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Programmatic API key management.
  name: PushPress ApiKeys API
  slug: pushpress-apikeys-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Scheduled one-on-one or small-group appointments.
  name: PushPress Appointments API
  slug: pushpress-appointments-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Marketing / lead-source attributions for a customer.
  name: PushPress Attributions API
  slug: pushpress-attributions-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Class, appointment, event, and open-facility check-ins.
  name: PushPress Checkins API
  slug: pushpress-checkins-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Scheduled classes and class types.
  name: PushPress Classes API
  slug: pushpress-classes-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: The gym / business (company) the API key is scoped to.
  name: PushPress Company API
  slug: pushpress-company-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Gym members and leads (customers).
  name: PushPress Customers API
  slug: pushpress-customers-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Customer enrollments in membership plans.
  name: PushPress Enrollments API
  slug: pushpress-enrollments-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Gym events (workshops, competitions, socials).
  name: PushPress Events API
  slug: pushpress-events-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Invitations for members or staff to join the gym on PushPress.
  name: PushPress Invitations API
  slug: pushpress-invitations-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Transactional email, SMS, push, and in-app notifications.
  name: PushPress Messages API
  slug: pushpress-messages-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Membership and billing plans offered by the gym.
  name: PushPress Plans API
  slug: pushpress-plans-api
- baseURL: https://api.pushpress.com/v3
  baseurl_source: declared
  description: Platform webhook subscriptions for real-time events.
  name: PushPress Webhooks API
  slug: pushpress-webhooks-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PushPress Platform ApiKeys API
  slug: open-pushpress-apikeys-api
- collection_type: open
  name: PushPress Platform ApiKeys Appointments API
  slug: open-pushpress-appointments-api
- collection_type: open
  name: PushPress Platform ApiKeys Attributions API
  slug: open-pushpress-attributions-api
- collection_type: open
  name: PushPress Platform ApiKeys Checkins API
  slug: open-pushpress-checkins-api
- collection_type: open
  name: PushPress Platform ApiKeys Classes API
  slug: open-pushpress-classes-api
- collection_type: open
  name: PushPress Platform ApiKeys Company API
  slug: open-pushpress-company-api
- collection_type: open
  name: PushPress Platform ApiKeys Customers API
  slug: open-pushpress-customers-api
- collection_type: open
  name: PushPress Platform ApiKeys Enrollments API
  slug: open-pushpress-enrollments-api
- collection_type: open
  name: PushPress Platform ApiKeys Events API
  slug: open-pushpress-events-api
- collection_type: open
  name: PushPress Platform ApiKeys Invitations API
  slug: open-pushpress-invitations-api
- collection_type: open
  name: PushPress Platform ApiKeys Messages API
  slug: open-pushpress-messages-api
- collection_type: open
  name: PushPress Platform ApiKeys Plans API
  slug: open-pushpress-plans-api
- collection_type: open
  name: PushPress Platform ApiKeys Webhooks API
  slug: open-pushpress-webhooks-api
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
random_paper: 18
rate_limits:
- limit_count: 2
  name: Pushpress Rate Limits
  slug: pushpress-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pushpress/refs/heads/main/screenshots/pushpress-2026-09-02T152346.png
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
- Software-as-a-Service
- Webhook
website: https://www.pushpress.com
---
