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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/streamline/plans/streamline-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/streamline-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/streamline/conformance/streamline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/streamline-conformance.yml
- group: agent
  href: https://artifacts.apis.io/streamline/well-known/streamline-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/streamline-well-known.yml
- group: other
  href: https://artifacts.apis.io/streamline/hosts/streamline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/streamline-hosts.yml
- group: other
  href: https://artifacts.apis.io/streamline/vendors/streamline-vendors.yml
  title: ''
  type: Vendors
  url: vendors/streamline-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.streamline.ai/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.streamline.ai/support
- group: auth
  title: ''
  type: Security
  url: https://www.streamline.ai/product/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.streamline.ai/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.streamline.ai/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.streamline.ai/resources/guides
- group: auth
  href: https://artifacts.apis.io/streamline/security/streamline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/streamline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.streamline.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.streamline.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.streamline.ai/resources/blog
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.streamline.ai/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Streamline AI provides a legal front‑door and intake automation platform for in‑house legal teams. It streamlines request management, workflow automation, matter management, analytics, dynamic document generation, and AI‑powered features like email intake, knowledge bot, and contract intelligence, helping legal operations scale efficiently.
image: https://cdn.prod.website-files.com/621f27e1e4e9f9673a3ff93e/69f9fba722606e606eab1be8_main-og-banner.webp
layout: provider
modified: '2026-10-25'
name: Streamline
nav: Providers
network: true
overview: 'Streamline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Automation, Artificial Intelligence, Workflows, and Document Generation.


  Streamline''s developer surface includes support, getting-started guide, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Streamline Plans Pricing
  plan_count: 2
  slug: streamline-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/streamline/streamline-2026-11-03T143924.png
security:
- kind: domain-security
  name: Streamline Domain Security
  slug: streamline-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: streamline
tags:
- Legal Tech
- Automation
- Artificial Intelligence
- Workflows
- Document Generation
website: https://www.streamline.ai/
---
