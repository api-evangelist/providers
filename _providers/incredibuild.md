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
- description: Standard REST APIs exposed by the Incredibuild Coordinator for managing build groups and users, and a Build History API that returns build telemetry as JSON. Requests authenticate with a custom API ke
  name: Incredibuild Build Group & Build History API
  slug: incredibuild-build-group-build-history-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incredibuild-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/incredibuild-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/incredibuild-conventions.yml
- group: company
  title: ''
  type: Website
  url: https://www.incredibuild.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.incredibuild.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.incredibuild.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.incredibuild.com/win/latest/windows/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.incredibuild.com/site_landing/download_docs_center.htm
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.incredibuild.com/win/latest/windows/release_notes.html
- group: company
  title: ''
  type: Blog
  url: https://www.incredibuild.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.incredibuild.com/support
- group: start
  title: ''
  type: SignUp
  url: https://app.incredibuild.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.incredibuild.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.incredibuild.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.incredibuild.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IncrediBuild
created: '2026-07-17'
description: Incredibuild is a development acceleration platform that speeds up developer and CI/CD builds using distributed processing and build caching. Its universal acceleration layer parallelizes compilation and other tasks across idle CPUs on-premises and in the cloud, removes redundant work with organization-wide caching, and surfaces pipeline bottlenecks through observability dashboards. Products include Build Cache, Distributed Processing, Observability, Build Runner (managed CI runners), Build Guard (audit-ready SBOMs), and Islo (an AI sandbox for coding agents). Incredibuild exposes a set of Build Group REST APIs for managing build groups and users on the Coordinator, plus a Build History API that returns build telemetry as JSON for dashboards and analysis. It serves gaming, automotive, semiconductor, embedded, financial services, and medtech teams, and is natively embedded in Visual Studio. Backed by Insight Partners.
image: https://www.incredibuild.com/wp-content/themes/incredibuild/assets/images/logo.svg
layout: provider
modified: '2026-07-19'
name: Incredibuild
nav: Providers
network: true
overview: 'Incredibuild publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Build Acceleration, Continuous Integration, and Distributed Computing.


  Incredibuild''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, support, and 9 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 27.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incredibuild/refs/heads/main/screenshots/incredibuild-2026-07-25T222249.png
security:
- kind: authentication
  name: Incredibuild Authentication
  slug: incredibuild-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Incredibuild Domain Security
  slug: incredibuild-domain-security
  summary_line: TLSv1.3 · DMARC
slug: incredibuild
tags:
- Company
- DevOps
- Build Acceleration
- Continuous Integration
- Distributed Computing
- Build Cache
- Developer Tools
- CI/CD
website: https://www.incredibuild.com/
---
