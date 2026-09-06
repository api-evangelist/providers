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
- description: Programmatic access to per-game data (character, ranking, match, and metadata) for Nexon titles. Authenticated with a per-application API key sent in the x-nxopen-api-key HTTP header. Versioned resour
  name: NEXON Open API
  slug: nexon-open-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.nexon.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.nexon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.nexon.com/guide/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.nexon.com/guide/request-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://openapi.nexon.com/guide/prepare-in-advance/
- group: start
  title: ''
  type: SignUp
  url: https://openapi.nexon.com/my-application/create-app/
- group: operate
  title: ''
  type: Support
  url: https://openapi.nexon.com/support/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openapi.nexon.com/support/terms/
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexon-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexon-inc-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexon-inc-domain-security.yml
created: '2026-07-17'
description: Nexon (operated by Nexon Korea Co., Ltd.) is a global video game publisher whose NEXON Open API platform at openapi.nexon.com gives developers programmatic access to per-game data such as character, ranking, and match information. Requests are authenticated with a per-application API key sent in the x-nxopen-api-key HTTP header and served from open.api.nexon.com; the developer portal provides application registration, usage analytics, per-game API references, and integration guides.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nexon-inc.png
layout: provider
modified: '2026-07-20'
name: Nexon Inc
nav: Providers
network: true
overview: 'Nexon Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Video Games, and Game Data.


  Nexon Inc''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 5 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexon-inc/refs/heads/main/screenshots/nexon-inc-2026-08-07T185157.png
security:
- kind: authentication
  name: Nexon Inc Authentication
  slug: nexon-inc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nexon Inc Domain Security
  slug: nexon-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexon-inc
tags:
- Company
- Consumer
- Gaming
- Video Games
- Game Data
- Developer API
- OpenAPI
website: http://www.nexon.net/
---
