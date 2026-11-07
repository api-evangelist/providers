---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- description: Beamline UI provides a component library API documented at https://beamline.io/docs. No public machine‑readable contract was found; the MCP endpoint requires a text/event‑stream accept header, which i
  name: Beamline UI API
  slug: beamline-ui-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/beamline-io/plans/beamline-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beamline-io-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/beamline-io/cli/beamline-io-cli.yml
  title: ''
  type: CLI
  url: cli/beamline-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/beamline-io/changelog/beamline-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beamline-io-changelog.yml
- group: agent
  href: https://artifacts.apis.io/beamline-io/llms/beamline-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beamline-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/beamline-io/well-known/beamline-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beamline-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/beamline-io/hosts/beamline-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beamline-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/beamline-io/vendors/beamline-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beamline-io-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dprvda
- group: operate
  title: ''
  type: ChangeLog
  url: https://beamline.io/changelog
- group: start
  title: ''
  type: SignUp
  url: https://beamline.io/components/signup-form
- group: start
  title: ''
  type: Login
  url: https://beamline.io/components/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://beamline.io/docs/customize#interface-sound-media-and-voice
- group: auth
  href: https://artifacts.apis.io/beamline-io/security/beamline-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beamline-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beamline.io/
- group: docs
  title: ''
  type: Documentation
  url: https://beamline.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://beamline.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beamline.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beamline.io/privacy
- group: company
  title: ''
  type: About
  url: https://beamline.io/about
- group: operate
  title: ''
  type: Contact
  url: https://beamline.io/contact
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found after probing common spec endpoints on api.beamline.io.
  evidence:
  - status: 0
    url: https://api.beamline.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Beamline UI provides a library of polished, editable React components and complete screens for building custom applications. Offering over 200 components and 50 full-screen templates, it targets SaaS apps, trading tools, dashboards, and AI workspaces. Based in Kyiv, Ukraine, the platform emphasizes responsive design, motion, and micro‑interactions, with a focus on developer productivity and seamless integration.
image: https://beamline.io/components/og.png?v=8902d2c750
layout: provider
modified: '2026-11-02'
name: Beamline UI
nav: Providers
network: true
overview: 'Beamline UI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include UI, React, Components, Software-as-a-Service, and Open Source.


  Beamline UI''s developer surface includes CLI, changelog, signup flow, getting-started guide, documentation, pricing, and 14 more developer resources.'
plans:
- name: Beamline Io Plans Pricing
  plan_count: 2
  slug: beamline-io-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ukraine
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beamline Io Domain Security
  slug: beamline-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: beamline-io
tags:
- UI
- React
- Components
- Software-as-a-Service
- Open Source
website: https://beamline.io/
---
