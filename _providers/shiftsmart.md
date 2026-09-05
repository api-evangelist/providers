---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'The private REST API backing the Shiftsmart worker and manager applications. Probing confirms a live FeathersJS service at api.shiftsmart.com: an unauthenticated GET /health returns 200, service colle'
  name: Shiftsmart Platform API
  slug: shiftsmart-platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://shiftsmart.com/
- group: company
  title: ''
  type: Blog
  url: https://shiftsmart.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.shiftsmart.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shiftsmartinc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shiftsmart.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shiftsmart.com/employer-terms-of-service
- group: commercial
  title: ''
  type: PartnerTermsOfService
  url: https://shiftsmart.com/partner-terms-of-service
- group: company
  title: ''
  type: News
  url: https://shiftsmart.com/news
- group: company
  title: ''
  type: Careers
  url: https://shiftsmart.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://shiftsmart.com/contact
- group: build
  title: ''
  type: Packages
  url: packages/shiftsmart-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shiftsmart-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/shiftsmart-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shiftsmart-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/shiftsmart_stock/
created: '2026-08-02'
description: Shiftsmart is a workforce management and flexible-labor platform that connects enterprises and government agencies with a community of independent workers across more than 50 countries. The platform covers the full labor lifecycle — sourcing workers from profiles carrying credentials and performance metrics, onboarding and training them into custom labor pools, building optimized schedules from rules and templates, dispatching shifts by in-app notification or SMS, tracking GPS-verified attendance and productivity, and paying workers within 24 hours via real-time debit transfers and payroll integrations. Shiftsmart also runs location-level audits, mystery shopping and compliance programs on top of the same labor network. The platform is delivered through worker and manager mobile applications backed by a private REST API at api.shiftsmart.com; Shiftsmart publishes no public developer portal, API reference, or machine-readable specification.
image: https://cdn.prod.website-files.com/602a3f3e454f14956d14543a/6660192ccef2360b51721359_Shiftsmart%20Webclip.png
layout: provider
modified: '2026-08-02'
name: Shiftsmart
nav: Providers
network: true
overview: 'Shiftsmart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Staffing, Scheduling, and Labor Marketplace.


  Shiftsmart''s developer surface includes engineering blog, support, product news, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shiftsmart/refs/heads/main/screenshots/shiftsmart-2026-09-02T155203.png
security:
- kind: authentication
  name: Shiftsmart Authentication
  slug: shiftsmart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shiftsmart Domain Security
  slug: shiftsmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shiftsmart
tags:
- Company
- Workforce Management
- Staffing
- Scheduling
- Labor Marketplace
- Human Resources
- Gig Economy
- Workforce
- Payments
- Field Services
website: https://shiftsmart.com/
---
