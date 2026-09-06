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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for managing employees, schedules, timesheets, locations, leave, tasks, and sales metrics in the Deputy workforce management platform. Authentication is handled via OAuth 2.0 or a permanent a
  name: Deputy Public API
  slug: public-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/deputy-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deputy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deputy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deputy.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deputy.com/deputy-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.deputy.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.deputy.com/docs/getting-started-with-the-deputy-api
- group: auth
  title: ''
  type: Authentication
  url: https://developer.deputy.com/docs/using-oauth-20
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deputy.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://once.deputy.com/signup/
- group: start
  title: ''
  type: Login
  url: https://once.deputy.com/login/
- group: operate
  title: ''
  type: Support
  url: https://help.deputy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.deputy.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deputy.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deputy.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deputy.com/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deputydev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deputy-com
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/deputyapp
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.deputy.com/llms.txt
created: '2026-05-11'
description: Deputy is an API-first workforce management platform that handles employee scheduling, time and attendance tracking, timesheets, leave management, task delegation, and team communications for businesses with hourly workers. The platform integrates with payroll, HR, and point of sale systems and exposes most of its product surface area via a public REST API. The Deputy API uses OAuth 2.0 or permanent token authentication and provides JSON endpoints for employees, schedules, timesheets, locations, sales metrics, and more.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deputy.png
layout: provider
modified: '2026-05-11'
name: Deputy
nav: Providers
network: true
overview: 'Deputy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Workforce Management, Employee Scheduling, Time and Attendance, Timesheets, and Human Resources.


  Deputy''s developer surface includes documentation, getting-started guide, authentication, pricing, signup flow, support, engineering blog, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 22.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deputy/refs/heads/main/screenshots/deputy-2026-06-20T180004.png
security:
- kind: domain-security
  name: Deputy Domain Security
  slug: deputy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deputy Vulnerability Disclosure
  slug: deputy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Deputy Trust Center
  slug: deputy-trust-center
  summary_line: SOC 2, ISO 27001
slug: deputy
tags:
- Workforce Management
- Employee Scheduling
- Time and Attendance
- Timesheets
- Human Resources
- Shift Planning
website: https://www.deputy.com
---
