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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Leeo Insurance Services Agentic Access
  operation_count: 7
  slug: leeo-insurance-services-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- baseURL: https://api.leeoinsurance.com/api/v1
  baseurl_source: declared
  description: Daily and weekly aggregated driver scorecards.
  name: LEEO Insurance Services Aggregates API
  slug: leeo-insurance-services-aggregates-api
- baseURL: https://api.leeoinsurance.com/api/v1
  baseurl_source: declared
  description: Fleet driver roster.
  name: LEEO Insurance Services Drivers API
  slug: leeo-insurance-services-drivers-api
- baseURL: https://api.leeoinsurance.com/api/v1
  baseurl_source: declared
  description: Generated fleet report links.
  name: LEEO Insurance Services Reports API
  slug: leeo-insurance-services-reports-api
- baseURL: https://api.leeoinsurance.com/api/v1
  baseurl_source: declared
  description: Trip lists, trip detail, paths, and driving events.
  name: LEEO Insurance Services Trips API
  slug: leeo-insurance-services-trips-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LEEO Fleet Telematics Aggregates API
  slug: open-leeo-insurance-services-aggregates-api
- collection_type: open
  name: LEEO Fleet Telematics Aggregates Drivers API
  slug: open-leeo-insurance-services-drivers-api
- collection_type: open
  name: LEEO Fleet Telematics Aggregates Reports API
  slug: open-leeo-insurance-services-reports-api
- collection_type: open
  name: LEEO Fleet Telematics Aggregates Trips API
  slug: open-leeo-insurance-services-trips-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/leeo-insurance-services-fleet-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leeoinsurance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leeoinsurance.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leeoinsurance.com/leeo-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leeoinsurance.com/
- group: operate
  title: ''
  type: Support
  url: https://leeoinsurance.com/contact
- group: company
  title: ''
  type: Blog
  url: https://leeoinsurance.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fairmatic
- group: start
  title: ''
  type: Login
  url: https://app.fairmatic.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leeoinsurance.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leeoinsurance.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://leeoinsurance.com/
- group: build
  title: ''
  type: Packages
  url: packages/leeo-insurance-services-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leeo-insurance-services-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leeo-insurance-services-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leeo-insurance-services-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leeo-insurance-services-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leeo-insurance-services-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leeo-insurance-services-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leeo-insurance-services-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leeo-insurance-services-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/leeo-insurance-services-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leeo-insurance-services-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leeo-insurance-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leeo-insurance-services-domain-security.yml
created: '2026-07-17'
description: LEEO Insurance Services is a San Francisco-based managing general agent (MGA) for commercial auto insurance, founded in 2017 and known as Fairmatic until its December 2025 rebrand. LEEO underwrites and prices fleet policies using telematics collected from drivers' phones through its mobile SDK, applying machine learning across underwriting, pricing, and claims, and rewarding safer driving with renewal credits and cashback. It writes fleet classes including non-emergency medical transport, light business auto, and last-mile delivery, selling through brokers. LEEO exposes a read-only REST Fleet Telematics API returning the driver roster, trip histories, trip paths and driving events, and daily and weekly driver safety scorecards, plus native SDKs for Android, iOS, React Native, and MAUI. The company has raised $91M and is backed by Battery Ventures, Foundation Capital, and Aquiline Technology Growth.
image: https://framerusercontent.com/images/YggCBRfzpd8IYRlJTG6UlpdiYQ.png
layout: provider
modified: '2026-07-19'
name: LEEO Insurance Services
nav: Providers
network: true
overview: 'LEEO Insurance Services publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Aggregates API, Drivers API, Reports API, and 1 more. Tagged areas include Company, Insurance, Insurtech, Commercial Auto Insurance, and Telematics.


  LEEO Insurance Services'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 19 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 15.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leeo-insurance-services/refs/heads/main/screenshots/leeo-insurance-services-2026-07-25T224822.png
security:
- kind: authentication
  name: Leeo Insurance Services Authentication
  slug: leeo-insurance-services-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Leeo Insurance Services Domain Security
  slug: leeo-insurance-services-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leeo-insurance-services
tags:
- Company
- Insurance
- Insurtech
- Commercial Auto Insurance
- Telematics
- Fleet Management
- Driving Behavior
- Risk Management
- Managing General Agent
- Mobile SDK
website: https://leeoinsurance.com/
---
