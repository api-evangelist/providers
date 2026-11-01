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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/infuseai-io/well-known/infuseai-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infuseai-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/infuseai-io/vendors/infuseai-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infuseai-io-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/infuseai-io/plans/infuseai-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infuseai-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/infuseai-io/changelog/infuseai-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infuseai-io-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://reccehq.com/
- group: design
  href: https://artifacts.apis.io/infuseai-io/conformance/infuseai-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infuseai-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/infuseai-io/llms/infuseai-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infuseai-io-llms.txt
- group: other
  href: https://artifacts.apis.io/infuseai-io/hosts/infuseai-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infuseai-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reccehq.com/statements/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://reccehq.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reccehq.com/statements/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://reccehq.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://reccehq.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://blog.reccehq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reccehq.com/
- group: auth
  href: https://artifacts.apis.io/infuseai-io/security/infuseai-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/infuseai-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/infuseai-io/security/infuseai-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infuseai-io-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://infuseai.io
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: InfuseAI is an AI-driven data review platform that helps software teams understand how code changes impact their data pipelines. By providing automated data validation, lineage tracking, and impact analysis, InfuseAI enables developers and data engineers to approve changes with confidence, reducing risk and improving data quality. Backed by 500 Global, the company focuses on integrating seamlessly into CI/CD workflows and supporting modern data stack tools.
image: https://reccehq.com/assets/images/recce-og-image.avif
layout: provider
modified: '2026-10-21'
name: InfuseAI
nav: Providers
network: true
overview: 'InfuseAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, DataReview, CI/CD, and DataQuality.


  InfuseAI''s developer surface includes changelog, pricing, engineering blog, documentation, and 13 more developer resources.'
plans:
- name: Infuseai Io Plans Pricing
  plan_count: 3
  slug: infuseai-io-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Infuseai Io Domain Security
  slug: infuseai-io-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Infuseai Io Trust Center
  slug: infuseai-io-trust-center
  summary_line: SOC 2
slug: infuseai-io
tags:
- Company
- AI
- DataReview
- CI/CD
- DataQuality
---
