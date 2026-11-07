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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bucket-co/plans/bucket-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bucket-co-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://reflag.com/security
- group: agent
  href: https://artifacts.apis.io/bucket-co/llms/bucket-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bucket-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/bucket-co/well-known/bucket-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bucket-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/bucket-co/hosts/bucket-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bucket-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/bucket-co/vendors/bucket-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bucket-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reflag.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://reflag.com/security
- group: build
  title: ''
  type: SDKs
  url: https://reflag.com/glossary/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reflag.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://reflag.com/pricing
- group: other
  title: ''
  type: Leadership
  url: https://reflag.com/glossary/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reflagcom
- group: operate
  title: ''
  type: ChangeLog
  url: https://reflag.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://reflag.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://reflag.com/changelog/introducing-feature-onboarding-funnel
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bucket.co/
- group: auth
  href: https://artifacts.apis.io/bucket-co/security/bucket-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bucket-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bucket-co/security/bucket-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bucket-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bucket.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://bucket.co/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: 'Bucket is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by creandum) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/68a872edf3df6064de547670/68e674a70f2a92f3a26d3296_reflag-og-home%20(2)-min.png
layout: provider
modified: '2026-10-22'
name: Bucket
nav: Providers
network: true
overview: 'Bucket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Feature Flags, Software-as-a-Service, Developer Tools, SDK, and Integration.


  Bucket''s developer surface includes pricing, changelog, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Bucket Co Plans Pricing
  plan_count: 3
  slug: bucket-co-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 47.3
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bucket-co/bucket-co-2026-11-03T122721.png
security:
- kind: domain-security
  name: Bucket Co Domain Security
  slug: bucket-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bucket Co Trust Center
  slug: bucket-co-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: bucket-co
tags:
- Feature Flags
- Software-as-a-Service
- Developer Tools
- SDK
- Integration
website: https://bucket.co/
---
