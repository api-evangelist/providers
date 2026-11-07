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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Doro Mind mental health platform, documented at the Getting Started page.
  name: Doro Mind API
  slug: doro-mind-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/doro-mind/hosts/doro-mind-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doro-mind-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://doromind.com/about/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doromind
- group: auth
  href: https://artifacts.apis.io/doro-mind/security/doro-mind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doro-mind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doromind.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doromind.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://doromind.com/about/story
- group: operate
  title: ''
  type: Support
  url: https://doromind.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doromind.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doromind.com/terms-of-service
- group: company
  title: ''
  type: Website
  url: https://doromind.com/
coverage:
  checked: '2026-10-24'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://doromind.com/resources/blog
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Doro Mind is a U.S.-based mental health care startup that provides family‑centered treatment and support for serious mental illnesses such as schizophrenia, psychosis, and bipolar disorder. Operating as a public benefit corporation, it offers clinical coordination, medication management (including Clozapine), and virtual care across New York, Connecticut, and California, with nationwide virtual support. The platform combines expert psychiatric care with resources for families, aiming to improve recovery outcomes and reduce hospitalizations.
image: https://doromind.com/images/doro-mind-default-og.png
layout: provider
modified: '2026-10-24'
name: Doro Mind
nav: Providers
network: true
overview: 'Doro Mind is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Startups, Public-benefit, and Telehealth.


  Doro Mind''s developer surface includes documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 58.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 15.9
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/doro-mind/doro-mind-2026-11-03T130941.png
security:
- kind: domain-security
  name: Doro Mind Domain Security
  slug: doro-mind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doro-mind
tags:
- Company
- Mental Health
- Startups
- Public-benefit
- Telehealth
website: https://doromind.com/
---
