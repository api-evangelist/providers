---
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadarena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acadarena.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acadarena.com/privacypolicy
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/acadarenagg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Arclight-Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acadarena
- group: company
  title: ''
  type: Twitter
  url: https://x.com/acadarena
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/acadarenagg
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://equityzen.com/company/acadarena
- group: build
  title: ''
  type: Packages
  url: packages/acadarena-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acadarena-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acadarena-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acadarena-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: AcadArena ships student-facing campus gaming programs and a Next.js marketing site with no developer, API or documentation section anywhere in its navigation; the only API hostname it ever named, api.acadarena.com, is now a dangling CNAME to a deleted DigitalOcean app that does not resolve, and the Supabase project the website itself calls rejects anonymous requests.
  evidence:
  - status: 200
    url: https://www.acadarena.com/
  - status: 404
    url: https://www.acadarena.com/llms.txt
  - status: 404
    url: https://www.acadarena.com/.well-known/api-catalog
  - status: 401
    url: https://aatesefpjfdqshisyriz.supabase.co/rest/v1/
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: AcadArena is a Philippine campus gaming and esports company founded in 2019 by Ariane Lim, Kevin Hoang and Justin Banusin, and trades today as a brand owned by AcadArena Digital Education Solutions OPC. It builds student communities around games across high-school and college campuses in the Philippines and Southeast Asia, running the AcadArena Alliance student-club accreditation network, an Incubator that helps students stand up a club on a campus that has none, the Buffs marketplace that supplies loot and sponsorship for campus events, an Alliance for Teachers practice community for moderators and educators, and collegiate competitions. The company has served hundreds of schools, has been the Philippine collegiate licensee for Riot Games titles, and raised a $3.5M seed round. Its public surface is a Next.js marketing site backed by a key-gated Supabase project; AcadArena publishes no developer portal, API reference, SDK or machine-readable contract, and the api.acadarena.com
  hostname it once used now resolves only to a dangling CNAME.
image: https://www.acadarena.com/assets/logo/acadarena_logo.png
layout: provider
modified: '2026-09-06'
name: AcadArena
nav: Providers
network: true
overview: AcadArena is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Gaming, Education, and Community.
plans:
- name: Acadarena Plans Pricing
  plan_count: 0
  slug: acadarena-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Acadarena Rate Limits
  slug: acadarena-rate-limits
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 6.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acadarena Domain Security
  slug: acadarena-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: acadarena
tags:
- Company
- Esports
- Gaming
- Education
- Community
- Events
- Students
- Sponsorship
- Philippines
- Southeast Asia
website: https://www.acadarena.com/
---
