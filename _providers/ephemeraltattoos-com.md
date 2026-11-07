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
- group: other
  href: https://artifacts.apis.io/ephemeraltattoos-com/hosts/ephemeraltattoos-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ephemeraltattoos-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ephemeraltattoos-com/vendors/ephemeraltattoos-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ephemeraltattoos-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ephemeraltattoos-com/security/ephemeraltattoos-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ephemeraltattoos-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ephemeraltattoos.com/
- group: company
  title: ''
  type: Blog
  url: https://ephemeral.tattoo/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ephemeral.tattoo/privacy-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://ephemeral.tattoo/disclaimer/
coverage:
  checked: '2026-10-29'
  detail: Probing known API subdomains returned no OpenAPI/Swagger spec (404 or no response).
  evidence:
  - status: 404
    url: https://api.ephemeral.tattoo/openapi.json
  - status: 0
    url: https://api.ephemeraltattoos.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Ephemeral Solutions creates made-to-fade tattoo ink that naturally fades over time, offering a safe, FDA‑approved alternative to permanent tattoos. Founded by NYU Tandon Ph.D. researchers, the company has iterated its formula over years to achieve fine‑line shading and consistent fade durations. Operating from Brooklyn, NY, Ephemeral partners with licensed tattoo artists to provide black‑ink tattoos that last months instead of years, while developing future products like radiotherapy‑grade FadeMark and next‑gen ink formulations.
image: https://ephemeral.tattoo/assets/icons/logo-traditional-playful.svg
layout: provider
modified: '2026-10-29'
name: Ephemeral Solutions
nav: Providers
network: true
overview: 'Ephemeral Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tattoo, Biotechnology, Health, Startups, and Cosmetics.


  Ephemeral Solutions'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ephemeraltattoos-com/ephemeraltattoos-com-2026-11-03T131559.png
security:
- kind: domain-security
  name: Ephemeraltattoos Com Domain Security
  slug: ephemeraltattoos-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ephemeraltattoos-com
tags:
- Tattoo
- Biotechnology
- Health
- Startups
- Cosmetics
- Company
website: https://ephemeraltattoos.com/
---
