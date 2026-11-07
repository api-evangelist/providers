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
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Constants provides a platform for creating user digital twins to simulate and analyze product decisions.
  name: Constants API
  slug: constants-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/constants-io/vendors/constants-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constants-io-vendors.yml
- group: agent
  href: https://artifacts.apis.io/constants-io/llms/constants-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/constants-io-llms.txt
- group: other
  href: https://artifacts.apis.io/constants-io/a2a/constants-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/constants-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/constants-io/well-known/constants-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/constants-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/constants-io/hosts/constants-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constants-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.constants.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.constants.io/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.constants.io/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.constants.io/
- group: auth
  href: https://artifacts.apis.io/constants-io/security/constants-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constants-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.constants.io/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are served as markdown but require rendering to discover contracts, none were found.
  evidence:
  - status: 200
    url: https://docs.constants.io/introduction.md
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Constants provides a platform for creating user digital twins to simulate and analyze product decisions. Their service lets teams run quick simulations of user behavior on websites or apps, generating reports on conversion, hesitation points, and actionable insights within about 20 minutes. The platform includes features like test files, reports, credit‑based simulation usage, and integrations with Discord, Google, and email for authentication. It aims to help product teams make data‑driven decisions efficiently.
image: https://www.constants.io/_testing/og-image.png?v=20261002
layout: provider
modified: '2026-11-04'
name: Constants
nav: Providers
network: true
overview: 'Constants is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Twin, Simulation, Product Analytics, and User Behavior.


  Constants'' developer surface includes getting-started guide, documentation, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constants Io Domain Security
  slug: constants-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: constants-io
tags:
- Company
- Digital Twin
- Simulation
- Product Analytics
- User Behavior
website: https://www.constants.io/
---
