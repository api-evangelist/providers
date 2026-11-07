---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AppScreenStudio provides a free online App Store and Google Play screenshot generator with AI assistance.
  name: AppScreenStudio API
  slug: appscreenstudio-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appscreenstudio-com/plans/appscreenstudio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appscreenstudio-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/appscreenstudio-com/llms/appscreenstudio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appscreenstudio-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appscreenstudio-com/well-known/appscreenstudio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appscreenstudio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/appscreenstudio-com/hosts/appscreenstudio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appscreenstudio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appscreenstudio-com/vendors/appscreenstudio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appscreenstudio-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appscreenstudio.com/terms
- group: auth
  href: https://artifacts.apis.io/appscreenstudio-com/security/appscreenstudio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appscreenstudio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appscreenstudio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.appscreenstudio.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appscreenstudio.com/en/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appscreenstudio.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:help@appscreenstudio.com
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://www.appscreenstudio.com/openapi.json
  - status: could not resolve host
    url: https://api.appscreenstudio.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AppScreenStudio provides a free online App Store and Google Play screenshot generator for iOS and Android developers. Users can upload raw app captures, customize templates, and export store‑ready screenshots in all required sizes with a single click. The platform integrates AI agents like Claude, Code, and Gemini to assist design, and offers a large library of free and premium templates, serving over 9,400 developers and ASO specialists. It aims to simplify app store listing creation without needing design tools.
image: https://www.appscreenstudio.com/opengraph-image.webp
layout: provider
modified: '2026-11-01'
name: AppScreenStudio
nav: Providers
network: true
overview: 'AppScreenStudio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AppScreenStudio, ScreenshotGenerator, Mobile Development, and AI Integration.


  AppScreenStudio''s developer surface includes engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Appscreenstudio Com Plans Pricing
  plan_count: 1
  slug: appscreenstudio-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appscreenstudio Com Domain Security
  slug: appscreenstudio-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: appscreenstudio-com
tags:
- AppScreenStudio
- ScreenshotGenerator
- Mobile Development
- AI Integration
website: https://appscreenstudio.com/
---
