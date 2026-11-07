---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cradlewise/llms/cradlewise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cradlewise-llms.txt
- group: auth
  href: https://artifacts.apis.io/cradlewise/well-known/cradlewise-help-center-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cradlewise-help-center-security.txt
- group: agent
  href: https://artifacts.apis.io/cradlewise/well-known/cradlewise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cradlewise-well-known.yml
- group: other
  href: https://artifacts.apis.io/cradlewise/hosts/cradlewise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cradlewise-hosts.yml
- group: other
  href: https://artifacts.apis.io/cradlewise/vendors/cradlewise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cradlewise-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cradlewise
- group: auth
  href: https://artifacts.apis.io/cradlewise/security/cradlewise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cradlewise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cradlewise.com/
- group: company
  title: ''
  type: Blog
  url: https://cradlewise.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://cradlewise.com/en-US
- group: operate
  title: ''
  type: Support
  url: https://help-center.cradlewise.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cradlewise.com/en-US/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cradlewise.com/en-US/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://cradlewise.com/en-US/financing
- group: start
  title: ''
  type: SignUp
  url: https://cradlewise.com/en-US
- group: start
  title: ''
  type: GettingStarted
  url: https://cradlewise.com/en-US
- group: docs
  title: ''
  type: APIReference
  url: https://cradlewise.com/en-US
coverage:
  checked: '2026-10-11'
  detail: The main website is a JavaScript‑rendered Next.js app, and attempts to fetch OpenAPI files from the API host returned 403, with no machine‑readable spec discovered.
  evidence:
  - status: 403
    url: https://api.cradlewise.com/openapi.json
  - status: 200
    url: https://cradlewise.com/en-US
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Cradlewise offers an all‑in‑one smart bassinet and crib that converts from a newborn bassinet to a toddler crib for up to 24 months. It includes a built‑in baby monitor, sound machine, and sleep‑tracking features, aiming to simplify nighttime care for parents. The product integrates IoT sensors and a companion app to provide real‑time insights and soothing sounds, positioning Cradlewise at the intersection of baby care and smart home technology.
image: https://assets.cradlewise.com/images/index/meta-image-cng-new.jpg
layout: provider
modified: '2026-10-11'
name: Cradlewise
nav: Providers
network: true
overview: 'Cradlewise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Baby, Smart Home, IoT, and Parenting.


  Cradlewise''s developer surface includes engineering blog, documentation, support, pricing, signup flow, getting-started guide, API reference, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 55.4
    operational_transparency: 13.2
  previous_composite: 23.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cradlewise/cradlewise-2026-11-03T125514.png
security:
- kind: domain-security
  name: Cradlewise Domain Security
  slug: cradlewise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cradlewise
tags:
- Company
- Baby
- Smart Home
- IoT
- Parenting
website: https://cradlewise.com/
---
