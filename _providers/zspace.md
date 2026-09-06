---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'The zSpace Core SDK is a native C API (documented as native_sdk_4.0) that lets an application drive a zSpace display: it loads the SDK runtime, detects connected peripherals, and exposes fourteen API '
  name: zSpace Core SDK (Native C API)
  slug: zspace-core-sdk
- description: The web API behind the zSpace developer portal and account surface, served from api.zspace.com/v2 and named as apiUrlV2 in the portal's own published runtime configuration. It is a Node/NestJS service
  name: zSpace Developer Portal API (v2)
  slug: zspace-developer-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://zspace.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zspace.com/assets/sdk-manual/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zspace.com/assets/sdk-manual/modules.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zspace
- group: company
  title: ''
  type: Blog
  url: https://blog.zspace.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zspace.com/s/
- group: operate
  title: ''
  type: Community
  url: https://dev-community.zspace.com/
- group: start
  title: ''
  type: SignUp
  url: https://login.zspace.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.zspace.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zspace-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zspace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zspace-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zspace-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zspace-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/zspace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zspace-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zspace-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zspace-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zspace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zspace-problem-types.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zspace-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zspace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zspace-rate-limits.yml
created: '2026-09-05'
description: 'zSpace, Inc. (Nasdaq: ZSPC) builds AR/VR learning technology for K-12, career and technical education, and higher education — glasses-free 3D laptops and all-in-one displays (Inspire, Imagine, AIO Pro) paired with a stylus, head tracking, and a catalog of curriculum-aligned applications, models and simulations. Its developer surface is centered on the zSpace Core SDK, a native C API plus a Unity plugin that gives applications access to the display''s stereo frustum, coordinate spaces, tracker devices and targets, stylus buttons, LED and haptics. A first-party developer portal at developer.zspace.com fronts an authenticated web API at api.zspace.com/v2 and a Keycloak OpenID Connect identity provider at auth.zspace.com; product release notes for roughly thirty applications are published from a public updates.zspace.com bucket. zSpace is a publicly traded company (Nasdaq: ZSPC) headquartered in San Jose, California with more than 70 patents, and reports over 2,400 U.S. school,
  technical-center, community-college and university customers.'
image: https://cdn.zspace.com/website-images/zspace-logo.png
layout: provider
modified: '2026-09-05'
name: zSpace
nav: Providers
network: true
overview: 'zSpace publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Augmented Reality, Virtual Reality, and EdTech.


  zSpace''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, changelog, and 17 more developer resources.'
plans:
- name: Zspace Plans Pricing
  plan_count: 0
  slug: zspace-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Zspace Rate Limits
  slug: zspace-rate-limits
scopes:
- name: Zspace Scopes
  scope_count: 0
  slug: zspace-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Zspace Authentication
  slug: zspace-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Zspace Domain Security
  slug: zspace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zspace
tags:
- Company
- Education
- Augmented Reality
- Virtual Reality
- EdTech
- Hardware
- 3D
- Simulation
- Career and Technical Education
- Developer SDK
website: https://zspace.com/
---
