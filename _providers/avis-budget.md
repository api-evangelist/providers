---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://stage.abgapiservices.com
  baseurl_source: declared
  description: 'REST API (v2) for the Avis, Budget and Payless rental car brands: keyword search of rental locations, vehicle availability and rate shopping (including inclusive rates, coupons, memberships and second'
  name: Avis Budget Group Rental Cars API
  slug: avis-budget-group-rental-cars-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.avisbudgetgroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.avis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.avis.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.avis.com/apis/rental-cars/versions/2fd66e15-44a2-4bc2-a96e-84b56a19c903
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.avis.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.avis.com/guides
- group: operate
  title: ''
  type: Support
  url: https://developer.avis.com/support
- group: operate
  title: ''
  type: Contact
  url: https://developer.avis.com/contact-us
- group: operate
  title: ''
  type: IssueTracker
  url: https://developer.avis.com/report-bug
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.avis.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://developer.avis.com/register
- group: start
  title: ''
  type: Login
  url: https://developer.avis.com/login
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/1524765/SzKWudFC
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.avis.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.avis.com/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avisbudgetgroup.com/home/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avisbudgetgroup.com/home/privacy-policy
- group: operate
  title: ''
  type: PressReleases
  url: https://www.avisbudgetgroup.com/home/news-and-media/press-release
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avisbudgetgroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avis-budget-group/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/security/avis-budget-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avis-budget-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/well-known/avis-budget-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avis-budget-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/llms/avis-budget-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avis-budget-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/llms/avis-budget-avis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avis-budget-avis-com-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/conformance/avis-budget-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avis-budget-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/plans/avis-budget-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avis-budget-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/components/avis-budget-components.yml
  title: ''
  type: Components
  url: components/avis-budget-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/sandbox/avis-budget-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/avis-budget-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/rate-limits/avis-budget-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avis-budget-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/lifecycle/avis-budget-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/avis-budget-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/lifecycle/avis-budget-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avis-budget-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/changelog/avis-budget-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avis-budget-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/conventions/avis-budget-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avis-budget-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/authentication/avis-budget-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avis-budget-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/scopes/avis-budget-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/avis-budget-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-01-01'
description: 'Avis Budget Group (NASDAQ: CAR) is a global provider of vehicle rental and mobility solutions operating the Avis, Budget, Budget Truck, Payless and Zipcar brands across roughly 11,000 rental locations in about 180 countries. The Avis Budget Group Developer Portal (developer.avis.com, a Kong-hosted portal) publishes the Rental Cars 2.0.0 REST API — location keyword search, vehicle availability and rate shopping, reservation create/view/modify/cancel, and location-specific terms and conditions — for travel, airline, OTA and partner applications, secured with OAuth 2.0 client credentials and gated behind partner sign-up and ABG approval. A white-label car rental booking solution is offered alongside the API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avis-budget.png
layout: provider
modified: '2026-09-18'
name: Avis Budget Group
nav: Providers
network: true
overview: 'Avis Budget Group publishes 1 API on the [APIs.io](https://apis.io/) network: Rental Cars API. Tagged areas include Fortune 500, Car Rental, Travel, Mobility, and Fleet Management.


  Avis Budget Group''s developer surface includes documentation, API reference, getting-started guide, support, changelog, signup flow, sandbox, and 29 more developer resources.'
plans:
- name: Avis Budget Plans Pricing
  plan_count: 0
  slug: avis-budget-plans-pricing
press:
- date: ''
  title: Cars & The Cloud
  url: https://ir.avisbudgetgroup.com/node/28796/pdf
- date: ''
  title: Avis Announces Google Home Integration with Artificial Intelligence ...
  url: https://avisbudgetgroup.gcs-web.com/news-releases/news-release-details/avis-announces-google-home-integration-artificial-intelligence
- date: ''
  title: Press Releases
  url: https://ir.avisbudgetgroup.com/press-releases?mobile=1&page=20
- date: ''
  title: Avis Budget Group Drives Forward Connected Car Innovation ...
  url: https://ir.powerfleet.com/press-releases/detail/295/avis-budget-group-drives-forward-connected-car-innovation
- date: ''
  title: Avis Budget Group's Strategy For AI, Innovation, And ...
  url: https://www.forbes.com/sites/peterhigh/2024/11/07/avis-budget-groups-strategy-for-ai-innovation-and-customer-focus/
random_paper: 15
rate_limits:
- limit_count: 0
  name: Avis Budget Rate Limits
  slug: avis-budget-rate-limits
scopes:
- name: Avis Budget Scopes
  scope_count: 0
  slug: avis-budget-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 48.3
    developer_ergonomics: 25.6
    discoverability: 75.9
    operational_transparency: 10.5
  previous_composite: 31.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/avis-budget/refs/heads/main/screenshots/avis-budget-2026-07-25T201946.png
security:
- kind: authentication
  name: Avis Budget Authentication
  slug: avis-budget-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Avis Budget Domain Security
  slug: avis-budget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avis-budget
tags:
- Fortune 500
- Car Rental
- Travel
- Mobility
- Fleet Management
- Transportation
- Reservations
- Vehicle Rental
- Partner API
- Hospitality
website: https://www.avisbudgetgroup.com/
---
