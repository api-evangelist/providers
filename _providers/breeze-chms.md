---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Breeze Chms Agentic Access
  operation_count: 47
  slug: breeze-chms-agentic-access
  summary_line: 47 operations
api_count: 1
apis:
- description: Account summary and activity log.
  name: Breeze ChMS Account API
  slug: breeze-chms-account-api
- description: Check-in / check-out attendance and eligibility.
  name: Breeze ChMS Attendance API
  slug: breeze-chms-attendance-api
- description: Events, calendars, and locations.
  name: Breeze ChMS Events API
  slug: breeze-chms-events-api
- description: Forms, form fields, and form entries.
  name: Breeze ChMS Forms API
  slug: breeze-chms-forms-api
- description: Contribution funds.
  name: Breeze ChMS Funds API
  slug: breeze-chms-funds-api
- description: Contributions (giving records).
  name: Breeze ChMS Giving API
  slug: breeze-chms-giving-api
- description: Members, contacts, custom profile fields, and families.
  name: Breeze ChMS People API
  slug: breeze-chms-people-api
- description: Pledge campaigns and pledges.
  name: Breeze ChMS Pledges API
  slug: breeze-chms-pledges-api
- description: Tags, tag folders, and tag assignment.
  name: Breeze ChMS Tags API
  slug: breeze-chms-tags-api
- description: Volunteers and volunteer roles for events.
  name: Breeze ChMS Volunteers API
  slug: breeze-chms-volunteers-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Breeze ChMS Account API
  slug: open-breeze-chms-account-api
- collection_type: open
  name: Breeze ChMS Account Attendance API
  slug: open-breeze-chms-attendance-api
- collection_type: open
  name: Breeze ChMS Account Events API
  slug: open-breeze-chms-events-api
- collection_type: open
  name: Breeze ChMS Account Forms API
  slug: open-breeze-chms-forms-api
- collection_type: open
  name: Breeze ChMS Account Funds API
  slug: open-breeze-chms-funds-api
- collection_type: open
  name: Breeze ChMS Account Giving API
  slug: open-breeze-chms-giving-api
- collection_type: open
  name: Breeze ChMS Account People API
  slug: open-breeze-chms-people-api
- collection_type: open
  name: Breeze ChMS Account Pledges API
  slug: open-breeze-chms-pledges-api
- collection_type: open
  name: Breeze ChMS Account Tags API
  slug: open-breeze-chms-tags-api
- collection_type: open
  name: Breeze ChMS Account Volunteers API
  slug: open-breeze-chms-volunteers-api
- collection_type: open
  name: Breeze ChMS API
  slug: open-breeze-chms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/breeze-chms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breeze-chms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/breeze-chms-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/breeze-chms
- group: company
  title: ''
  type: Website
  url: https://www.breezechms.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.breezechms.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/breeze-chms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/breeze-chms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/breeze-chms-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://get.tithe.ly/blog/rss.xml
created: '2026-07-03'
description: Breeze ChMS is church management software (breezechms.com) for small and mid-sized churches, covering people/membership, tags and groups, events and calendars, check-ins and attendance, online and text giving, funds, pledge campaigns, custom forms, and volunteer scheduling. Breeze publishes a documented REST API scoped to each church subdomain (https://{subdomain}.breezechms.com/api), authenticated with an account API key sent in the Api-Key HTTP header. All API operations are HTTP GET requests with query-string parameters, and the API is rate limited to roughly 20 requests per minute.
finops:
- name: Breeze Chms Finops
  service_category: Church Management Software (SaaS)
  slug: breeze-chms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/breeze-chms.png
layout: provider
modified: '2026-07-03'
name: Breeze ChMS
nav: Providers
network: true
overview: 'Breeze ChMS publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Attendance API, Events API, and 7 more. Tagged areas include Church Management, ChMS, Non-Profit, Giving, and Membership.


  Breeze ChMS''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Breeze Chms Plans Pricing
  plan_count: 2
  slug: breeze-chms-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Breeze Chms Rate Limits
  slug: breeze-chms-rate-limits
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breeze-chms/refs/heads/main/screenshots/breeze-chms-2026-07-25T203746.png
security:
- kind: authentication
  name: Breeze Chms Authentication
  slug: breeze-chms-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Breeze Chms Domain Security
  slug: breeze-chms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breeze-chms
tags:
- Church Management
- ChMS
- Non-Profit
- Giving
- Membership
- Event
- Faith
website: https://www.breezechms.com
---
