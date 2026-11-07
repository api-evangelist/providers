---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Voxist API provides speech‑to‑text, translation, and voice‑agent capabilities as described in the developer documentation.
  name: Voxist API
  slug: voxist-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/voxist/plans/voxist-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voxist-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/voxist/well-known/voxist-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voxist-well-known.yml
- group: other
  href: https://artifacts.apis.io/voxist/hosts/voxist-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voxist-hosts.yml
- group: other
  href: https://artifacts.apis.io/voxist/vendors/voxist-vendors.yml
  title: ''
  type: Vendors
  url: vendors/voxist-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.voxist.com/en/platform/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Voxist
- group: auth
  href: https://artifacts.apis.io/voxist/security/voxist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voxist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voxist.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.voxist.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.voxist.com/en/voxist-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.voxist.com/en/voxist-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.voxist.com/en/solutions/developers
- group: operate
  title: ''
  type: Support
  url: https://www.voxist.com/en/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voxist.com/en/solutions/enterprise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iubenda.com/terms-and-conditions/63464178
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/63464178
coverage:
  checked: '2026-10-27'
  detail: The developer documentation page loads content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.voxist.com/en/voxist-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Voxist provides Speech AI solutions built in Europe, offering products such as Voxcept for enterprise knowledge capture, Voxlive for real‑time translation, Voxlingo for multilingual call handling, Voxreply smart voicemail, and Voxmemo for meeting dictation. Their developer platform includes the Voxist API, enabling integration of speech‑to‑text, translation, and AI‑driven voice agents into applications. The company focuses on privacy‑first, European‑hosted AI services for contact centers, enterprises, and developers.
layout: provider
modified: '2026-10-27'
name: Voxist
nav: Providers
network: true
overview: 'Voxist is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Speech AI, Voice Technology, European, and Enterprise.


  Voxist''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 11 more developer resources.'
plans:
- name: Voxist Plans Pricing
  plan_count: 3
  slug: voxist-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/voxist/voxist-2026-11-03T145937.png
security:
- kind: domain-security
  name: Voxist Domain Security
  slug: voxist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: voxist
tags:
- Company
- Speech AI
- Voice Technology
- European
- Enterprise
website: https://voxist.com/
---
