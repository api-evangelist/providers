---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bespree provides AI-powered job seeker tools but does not expose a public API.
  name: Bespree API
  slug: bespree-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bespree-com/plans/bespree-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bespree-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bespree-com/changelog/bespree-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bespree-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/bespree-com/llms/bespree-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bespree-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bespree-com/hosts/bespree-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bespree-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bespree-com/vendors/bespree-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bespree-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bespree.com/changelog
- group: auth
  href: https://artifacts.apis.io/bespree-com/security/bespree-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bespree-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bespree.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bespree.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://bespree.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bespree.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bespree.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://bespree.com/help
created: '2026-11-02'
description: Bespree provides AI-powered tools for job seekers, including resume building, cover letter generation, interview practice, and local job search. The platform offers a free account with no credit card required, aiming to streamline the job application process through automation and personalization.
image: https://bespree.com/og-image.jpg
layout: provider
modified: '2026-11-02'
name: Bespree
nav: Providers
network: true
overview: 'Bespree is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Job Search, Resume Builder, and CoverLetter.


  Bespree''s developer surface includes changelog, documentation, pricing, support, and 9 more developer resources.'
plans:
- name: Bespree Com Plans Pricing
  plan_count: 2
  slug: bespree-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Bespree Com Rate Limits
  slug: bespree-com-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bespree Com Domain Security
  slug: bespree-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bespree-com
tags:
- Company
- Artificial Intelligence
- Job Search
- Resume Builder
- CoverLetter
website: https://bespree.com/
---
