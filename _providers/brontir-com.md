---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/brontir-com/plans/brontir-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brontir-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/brontir-com/cli/brontir-com-cli.yml
  title: ''
  type: CLI
  url: cli/brontir-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/brontir-com/authentication/brontir-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brontir-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/brontir-com/conformance/brontir-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brontir-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brontir-com/llms/brontir-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brontir-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brontir-com/well-known/brontir-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brontir-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brontir-com/hosts/brontir-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brontir-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brontir.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brontir.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://brontir.com/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://brontir.com/setup
- group: auth
  href: https://artifacts.apis.io/brontir-com/security/brontir-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brontir-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brontir.com/
- group: docs
  title: ''
  type: Documentation
  url: https://brontir.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://brontir.com/pricing
created: '2026-11-03'
description: BRONTIR provides live web research integration for Claude and ChatGPT, delivering structured public data from social media, reviews, YouTube, maps, and stores with source attribution. It offers free credits on signup and tiered paid plans for higher usage, operating as a web application hosted at brontir.com.
image: https://brontir.com/og-image.png?v=2
layout: provider
modified: '2026-11-03'
name: BRONTIR
nav: Providers
network: true
overview: 'BRONTIR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Integration, Web Research, Public Data, and Software-as-a-Service.


  BRONTIR''s developer surface includes CLI, authentication, getting-started guide, documentation, pricing, and 10 more developer resources.'
plans:
- name: Brontir Com Plans Pricing
  plan_count: 4
  slug: brontir-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Brontir Com Authentication
  slug: brontir-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Brontir Com Domain Security
  slug: brontir-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brontir-com
tags:
- Artificial Intelligence
- Data Integration
- Web Research
- Public Data
- Software-as-a-Service
website: https://brontir.com/
---
