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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/3cx/plans/3cx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3cx-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/3cx/conformance/3cx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/3cx-conformance.yml
- group: auth
  href: https://artifacts.apis.io/3cx/well-known/3cx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/3cx-security.txt
- group: agent
  href: https://artifacts.apis.io/3cx/well-known/3cx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3cx-well-known.yml
- group: other
  href: https://artifacts.apis.io/3cx/hosts/3cx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3cx-hosts.yml
- group: other
  href: https://artifacts.apis.io/3cx/vendors/3cx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3cx-vendors.yml
- group: build
  href: https://artifacts.apis.io/3cx/packages/3cx-packages.yml
  title: ''
  type: SDKs
  url: packages/3cx-packages.yml
- group: build
  href: https://artifacts.apis.io/3cx/packages/3cx-packages.yml
  title: ''
  type: Packages
  url: packages/3cx-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.3cx.com/blog/news/register-on-forum/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.3cx.com/blog/releases/v18-u8/
- group: company
  title: ''
  type: Blog
  url: https://www.3cx.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.3cx.com/docs/manual/create-extensions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/3cx
- group: auth
  href: https://artifacts.apis.io/3cx/security/3cx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3cx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.3cx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.3cx.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.3cx.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.3cx.com/contact/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.3cx.com/developer/
coverage:
  checked: '2026-10-26'
  detail: The developer portal URL https://www.3cx.com/developer/ returns 404, indicating no public API program.
  evidence:
  - status: 404
    url: https://www.3cx.com/developer/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: 3CX provides a unified communications solution offering a software‑based IP PBX, video conferencing, live chat, and AI‑enhanced features such as an AI Receptionist and call transcription. The platform serves businesses of all sizes, enabling on‑premises, cloud, or hybrid deployments with robust call‑center reporting and integration capabilities.
image: https://www.3cx.com/wp-content/uploads/2026/05/OG-Home-Page-X-1200x675-v1.png
layout: provider
modified: '2026-10-26'
name: 3CX
nav: Providers
network: true
overview: '3CX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, VoIP, Artificial Intelligence, and Unified Communications.


  3CX''s developer surface includes signup flow, changelog, engineering blog, getting-started guide, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: 3Cx Plans Pricing
  plan_count: 42
  slug: 3cx-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Cx Domain Security
  slug: 3cx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 3cx
tags:
- Company
- Communications
- VoIP
- Artificial Intelligence
- Unified Communications
website: https://www.3cx.com/
---
