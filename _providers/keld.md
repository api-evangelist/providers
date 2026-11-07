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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://keld.co/security
- group: design
  href: https://artifacts.apis.io/keld/conformance/keld-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keld-conformance.yml
- group: agent
  href: https://artifacts.apis.io/keld/llms/keld-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keld-llms.txt
- group: other
  href: https://artifacts.apis.io/keld/hosts/keld-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keld-hosts.yml
- group: other
  href: https://artifacts.apis.io/keld/vendors/keld-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keld-vendors.yml
- group: build
  href: https://artifacts.apis.io/keld/packages/keld-packages.yml
  title: ''
  type: SDKs
  url: packages/keld-packages.yml
- group: build
  href: https://artifacts.apis.io/keld/packages/keld-packages.yml
  title: ''
  type: Packages
  url: packages/keld-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keld.co/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://keld.co/status
- group: start
  title: ''
  type: SignUp
  url: https://keld.co/signup
- group: auth
  title: ''
  type: Security
  url: https://keld.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keld.co/privacy
- group: company
  title: ''
  type: Blog
  url: https://keld.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://keld.co/docs
- group: auth
  href: https://artifacts.apis.io/keld/security/keld-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/keld-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/keld/security/keld-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keld.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://keld.co/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'Keld is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by founder-collective) and added to the network as a stub for full-pipeline profiling.'
image: https://keld.co/assets/logos/keld-og-card.png?v=90a6d12d6c
layout: provider
modified: '2026-10-24'
name: Keld
nav: Providers
network: true
overview: 'Keld is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Inference, Marketplace, Model Marketplace, and Enterprise AI.


  Keld''s developer surface includes signup flow, engineering blog, getting-started guide, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 37.5
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.9
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
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/keld/keld-2026-11-03T134347.png
security:
- kind: domain-security
  name: Keld Domain Security
  slug: keld-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Keld Trust Center
  slug: keld-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: keld
tags:
- Inference
- Marketplace
- Model Marketplace
- Enterprise AI
website: https://keld.co/
---
