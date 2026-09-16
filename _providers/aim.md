---
access_model:
  confidence: medium
  label: Dealer / direct sales only — no self-serve signup or public pricing
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-15'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Blog
  url: https://aim.vision/news
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aim/refs/heads/main/rate-limits/aim-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aim-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aim/refs/heads/main/packages/aim-packages.yml
  title: ''
  type: Packages
  url: packages/aim-packages.yml
- group: company
  title: ''
  type: Website
  url: https://aim.vision/
- group: company
  title: ''
  type: About
  url: https://aim.vision/about
- group: operate
  title: ''
  type: FAQ
  url: https://aim.vision/faqs
- group: company
  title: ''
  type: News
  url: https://aim.vision/news
- group: company
  title: ''
  type: Careers
  url: https://aim.vision/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aim.vision/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aim.vision/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aim-intelligent-machines
- group: company
  title: ''
  type: Twitter
  url: https://x.com/scale_earth
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aim/refs/heads/main/llms/aim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aim-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aim/refs/heads/main/security/aim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aim-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aim/refs/heads/main/plans/aim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aim-plans-pricing.yml
coverage:
  checked: '2026-09-14'
  detail: AIM Intelligent Machines sells an autonomous-earthmoving retrofit kit through equipment dealers, and its entire public web surface is the eight marketing and legal pages listed in its own sitemap.xml — there is no docs, api, developer or app subdomain (all fail to resolve), no GitHub organization, and every contract and .well-known path probed on aim.vision and www.aim.vision returns a hard 404.
  evidence:
  - status: 200
    url: https://aim.vision/sitemap.xml
  - status: 0
    url: https://docs.aim.vision/
  - status: 0
    url: https://api.aim.vision/
  - status: 404
    url: https://aim.vision/openapi.json
  - status: 404
    url: https://aim.vision/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/aim-intelligent-machines
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: AIM (AIM Intelligent Machines) is a Redmond, Washington robotics and artificial-intelligence company building autonomous earthmoving for mining, construction and defense. Its plug-and-play retrofit kit converts existing heavy equipment — excavators, bulldozers, haul trucks — into self-operating machines regardless of make, model, size or age, while preserving the OEM warranty, pairing rugged onboard hardware and 360-degree camera-based perception with a tablet-based control interface and a "Site Intelligence" analytics dashboard for remote fleet tasking, terrain mapping and productivity reporting. Founded in 2021 by engineers from Waymo, SpaceX, Google, Tesla, Apple, Microsoft, Trimble and Hexagon, AIM is backed by General Catalyst (partners Quentin Clark and Max Rimpel), Khosla Ventures, DCVC, Human Capital, Ironspring Ventures and Mantis, and has announced a strategic partnership with Komatsu and a LiDAR partnership with Ouster. AIM sells through equipment dealers rather than
  a self-serve product, and as of this pass publishes no public developer program, API reference, SDK or machine-readable contract of any kind — its entire public web surface is eight marketing and legal pages.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aim.png
layout: provider
modified: '2026-09-14'
name: AIM Intelligent Machines
nav: Providers
network: true
overview: 'AIM Intelligent Machines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Robotics, Autonomy, and Heavy Equipment.


  AIM Intelligent Machines'' developer surface includes engineering blog, FAQ, product news, and 12 more developer resources.'
plans:
- name: Aim Plans Pricing
  plan_count: 0
  slug: aim-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aim Rate Limits
  slug: aim-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aim Domain Security
  slug: aim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aim
tags:
- Company
- Artificial Intelligence
- Robotics
- Autonomy
- Heavy Equipment
- Earthmoving
- Mining
- Construction
- Defense
- Startup
- General Catalyst Portfolio
website: https://aim.vision/
---
