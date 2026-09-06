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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plans-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plans.app/
- group: start
  title: ''
  type: SignUp
  url: https://plans.app/signup
- group: start
  title: ''
  type: Login
  url: https://platform.plans.app/login
- group: operate
  title: ''
  type: StatusPage
  url: https://plans.hyperping.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plans.app/legal/terms-and-conditions-en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plans.app/legal/privacy-policy-en
- group: company
  title: ''
  type: Careers
  url: https://plans.app/careers
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plans-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plans-well-known.yml
created: '2026-07-17'
description: Plans (plans.app, formerly lun.energy) is a climate-technology company focused on decarbonising the built world. It removes the friction that stands in the way of transitioning homes to low-carbon energy faster, letting professionals capture building data on a mobile device, analyze it, and produce retrofit / energy plans — "capture, analyze, plan, all in your pocket." A web platform (platform.plans.app) and a Chrome extension support the workflow, and the product is offered across English, Danish, and French markets. Plans is backed by Partech. No public developer API has been identified during enrichment; the platform is a login-gated single-page application and the site exposes no OpenAPI, SDKs, docs, or developer portal.
image: https://plans.app/apple-touch-icon.png
layout: provider
modified: '2026-07-20'
name: Plans
nav: Providers
network: true
overview: 'Plans is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Energy, Decarbonization, and Built World.


  Plans'' developer surface includes signup flow and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plans/refs/heads/main/screenshots/plans-2026-09-02T151418.png
security:
- kind: domain-security
  name: Plans Domain Security
  slug: plans-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plans
tags:
- Company
- Climate
- Energy
- Decarbonization
- Built World
- Home Retrofit
- Construction Tech
- Sustainability
website: https://plans.app/
---
