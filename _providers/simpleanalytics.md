---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · 14-day trial
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - https://www.simpleanalytics.com/pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Simpleanalytics Agentic Access
  operation_count: 5
  slug: simpleanalytics-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://queue.simpleanalyticscdn.com
  baseurl_source: declared
  description: The Events API from Simple Analytics — server-side collection of custom events and page views, with customer-defined metadata, posted unauthenticated to the collection queue.
  name: Simple Analytics Events API
  slug: simpleanalytics-events-api
- baseURL: https://simpleanalytics.com
  baseurl_source: declared
  description: The Export API from Simple Analytics — raw, unsampled data point export (page views and events) as JSON or CSV over a date range, with per-field selection.
  name: Simple Analytics Export API
  slug: simpleanalytics-export-api
- baseURL: https://simpleanalytics.com
  baseurl_source: declared
  description: The Stats API from Simple Analytics — the aggregated dashboard statistics (pageviews, visitors, histogram, pages, countries, referrers, UTM and device breakdowns) as JSON for any tracked hostname.
  name: Simple Analytics Stats API
  slug: simpleanalytics-stats-api
- baseURL: https://simpleanalytics.com
  baseurl_source: declared
  description: The Websites API from Simple Analytics — the Admin surface for listing the websites in an account and adding a new one with timezone, visibility and label.
  name: Simple Analytics Websites API
  slug: simpleanalytics-websites-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Simple Analytics Events API
  slug: open-simpleanalytics-events-api
- collection_type: open
  name: Simple Analytics Events Export API
  slug: open-simpleanalytics-export-api
- collection_type: open
  name: Simple Analytics Events Stats API
  slug: open-simpleanalytics-stats-api
- collection_type: open
  name: Simple Analytics Events Websites API
  slug: open-simpleanalytics-websites-api
- collection_type: open
  name: Simple Analytics API
  slug: open-simpleanalytics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simpleanalytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpleanalytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpleanalytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simpleanalytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simpleanalytics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simpleanalytics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simpleanalytics-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simpleanalytics.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.simpleanalytics.com/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.simpleanalytics.com/roadmap
- group: design
  title: ''
  type: Conformance
  url: conformance/simpleanalytics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.simpleanalytics.com/gdpr-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/simpleanalytics-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/simpleanalytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/simpleanalytics-packages.yml
- group: design
  title: ''
  type: Components
  url: components/simpleanalytics-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/simpleanalytics-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/simpleanalytics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simpleanalytics-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://simpleanalytics.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simpleanalytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simpleanalytics
- group: company
  title: ''
  type: Website
  url: https://www.simpleanalytics.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.simpleanalytics.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simpleanalytics.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simpleanalytics.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.simpleanalytics.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.simpleanalytics.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simpleanalytics.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.simpleanalytics.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.simpleanalytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simpleanalytics.com/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simpleanalytics.com/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/simpleanalytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simpleanalytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simpleanalytics-finops.yml
created: '2026-06-21'
description: Simple Analytics is a privacy-first, cookieless web analytics platform built and hosted in the European Union by Simple Analytics B.V. in the Netherlands. It collects no personal data, sets no cookies, stores no IP addresses and needs no consent banner, while exposing a REST API surface to pull aggregated dashboard statistics, export raw unsampled data points (page views and events) to warehouses and BI tools, collect custom events server-side from backends and mobile apps, and administer the websites in an account. Public websites can be read anonymously on both read APIs, and a large first-party plugin library installs the tracking script across common frameworks and CMSes.
finops:
- name: Simpleanalytics Finops
  service_category: Analytics
  slug: simpleanalytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simpleanalytics.png
layout: provider
modified: '2026-08-13'
name: Simple Analytics
nav: Providers
network: true
overview: 'Simple Analytics publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Export API, Stats API, and 1 more. Tagged areas include Analytics, Web Analytics, Privacy, Cookieless, and GDPR.


  Simple Analytics'' developer surface includes authentication, changelog, sandbox, engineering blog, documentation, API reference, getting-started guide, and 30 more developer resources.'
plans:
- name: Simpleanalytics Plans Pricing
  plan_count: 3
  slug: simpleanalytics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Simpleanalytics Rate Limits
  slug: simpleanalytics-rate-limits
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 74.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 63.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simpleanalytics/refs/heads/main/screenshots/simpleanalytics-2026-08-17T080419.png
security:
- kind: authentication
  name: Simpleanalytics Authentication
  slug: simpleanalytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Simpleanalytics Domain Security
  slug: simpleanalytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Simpleanalytics Trust Center
  slug: simpleanalytics-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, PCI DSS
slug: simpleanalytics
tags:
- Analytics
- Web Analytics
- Privacy
- Cookieless
- GDPR
- Event
- Data Export
- Europe
website: https://www.simpleanalytics.com
---
