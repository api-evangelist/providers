---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The Nativo API V3 is the platform REST API for the Nativo advertising platform. It exposes CRUD trafficking resources (advertisers, campaigns, budgets, ads, creatives, placements, targeting parameters
  name: Nativo API V3
  slug: nativo-api-v3
- description: A BETA GET endpoint that returns a Nativo native display ad as a programmatic response so a publisher can render the ad in its own technology rather than through the Nativo tag or SDK. The request req
  name: Nativo Ad Serving API (BETA)
  slug: nativo-ad-serving-api
artifact_total: 7
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/life360/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nativo-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://ads.life360.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ads.life360.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.nativo.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.nativo.com/reference/general
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.nativo.com/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://support.nativo.com/en/
- group: company
  title: ''
  type: Blog
  url: https://ads.life360.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/life360-oss
- group: start
  title: ''
  type: SignUp
  url: https://ads.life360.com/get-a-demo
- group: start
  title: ''
  type: Login
  url: https://admin.nativo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ads.life360.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ads.life360.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nativo.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nativo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nativo-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nativo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nativo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nativo-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nativo-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nativo-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/nativo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nativo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nativo-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nativo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/nativo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nativo-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nativo-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nativo-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nativo-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: security/nativo-vulnerability-disclosure.yml
created: '2026-08-26'
description: Nativo is a native advertising and content-distribution technology company (El Segundo, California) that runs a native ad exchange and licenses a white-label ad server used by publishers to sell and serve sponsored content, native display, native video and story ad formats across a network of more than 20,000 apps and sites. Its platform spans an SSP, a curation marketplace, a self-serve buying console, a SaaS ad renderer, and the SPARC and Brand Rank products. Nativo was acquired by Life360 and the acquisition closed on 5 January 2026; the corporate site now resolves to ads.life360.com ("Life360 Ads featuring Nativo"), while the developer surface remains on nativo.com hosts. The public developer surface is a REST Nativo API V3 at api.nativo.com/v3 covering advertisers, campaigns, budgets, ads, creatives, placements, targeting and six reporting resources; a BETA Ad Serving API on jadserve.postrelease.com; and first-party mobile ad SDKs for iOS, Android and React Native.
image: https://cdn.prod.website-files.com/62348aef92bf092b84891591/6297b07786c9a646645a6a52_Nativo-Open-Graph.png
layout: provider
modified: '2026-08-26'
name: Nativo
nav: Providers
network: true
overview: 'Nativo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Native Advertising, and Programmatic Advertising.


  Nativo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Nativo Plans Pricing
  plan_count: 0
  slug: nativo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Nativo Rate Limits
  slug: nativo-rate-limits
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nativo/refs/heads/main/screenshots/nativo-2026-09-02T150725.png
security:
- kind: authentication
  name: Nativo Authentication
  slug: nativo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Nativo Domain Security
  slug: nativo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nativo Vulnerability Disclosure
  slug: nativo-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: nativo
tags:
- Company
- Advertising
- AdTech
- Native Advertising
- Programmatic Advertising
- Supply Side Platform
- Ad Serving
- Marketing
- Publishing
- Reporting
- Mobile SDK
website: https://ads.life360.com/
---
