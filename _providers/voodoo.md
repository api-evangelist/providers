---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The HTTP backend behind Voodoo's Publishing Platform (Publidash), the dashboard partner studios use to submit prototypes, run tests, and read analytics, monetization and IAP figures. The host is named
  name: Voodoo Publishing Platform API
  slug: voodoo-publishing-platform
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voodoo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voodoo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://voodoo.io/publishing
- group: operate
  title: ''
  type: Support
  url: https://voodoo.io/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://voodoo.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://voodoo.io/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VoodooTeam
- group: start
  title: ''
  type: SignUp
  url: https://voodoo.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voodoo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voodoo.io/privacy
- group: build
  title: ''
  type: Packages
  url: packages/voodoo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/voodoo-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/voodoo-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/voodoo-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voodoo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voodoo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voodoo-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/voodoo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voodoo-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voodoo-llms.txt
created: '2026-09-04'
description: 'Voodoo is a Paris-based mobile games and apps company founded in 2013 by Alexandre Yazdi and Laurent Ritter. It develops and publishes free-to-play mobile titles (Paper.io, Hole.io, Helix Jump, Mob Control), operates a partner publishing programme used by thousands of external studios, runs an in-house mobile ad network (Voodoo ADN) and an advertising business selling interstitial, rewarded and in-game inventory across roughly 150 million monthly active users, and owns the social apps BeReal and Wizz. Its developer-facing surface is a partner platform rather than a public API: the Publishing Platform (Publidash) dashboard, its auth-gated backend at v2-publidash-api.voodoo.io, and first-party mobile ad SDKs distributed through CocoaPods, Swift Package Manager and a Voodoo-hosted Maven repository.'
image: https://framerusercontent.com/images/cKiSnoz2B6fJXIxssj9GA1gg.jpg
layout: provider
modified: '2026-09-04'
name: Voodoo
nav: Providers
network: true
overview: 'Voodoo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Mobile Games, Mobile Apps, and Advertising.


  Voodoo''s developer surface includes support, engineering blog, signup flow, changelog, sandbox, and 15 more developer resources.'
plans:
- name: Voodoo Plans Pricing
  plan_count: 0
  slug: voodoo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Voodoo Rate Limits
  slug: voodoo-rate-limits
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 24.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Voodoo Domain Security
  slug: voodoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voodoo
tags:
- Company
- Gaming
- Mobile Games
- Mobile Apps
- Advertising
- Ad Network
- Game Publishing
- Mobile SDK
- Monetization
- Social Apps
website: https://voodoo.io/
---
