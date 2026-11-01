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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/hiretofu-com/plans/hiretofu-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hiretofu-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/hiretofu-com/llms/hiretofu-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hiretofu-com-llms.txt
- group: other
  href: https://artifacts.apis.io/hiretofu-com/hosts/hiretofu-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hiretofu-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hiretofu-com/vendors/hiretofu-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hiretofu-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hiretofu.com/privacyPolicy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hiretofu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.hiretofu.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hiretofu.com/
- group: auth
  href: https://artifacts.apis.io/hiretofu-com/security/hiretofu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hiretofu-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hiretofu.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://hiretofu.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Tofu offers AI‑driven candidate fraud detection, deepfake detection, and resume screening for recruiting and security teams. The platform connects to an applicant tracking system (ATS) and flags identity theft, impersonation, synthetic identities, deepfakes, and proxy interviewers across the hiring funnel. It provides a Fraud API and Deepfake API for platforms and a Chrome extension for recruiter verification.
image: https://www.hiretofu.com/brand/og-image.png
layout: provider
modified: '2026-10-24'
name: Tofu
nav: Providers
network: true
overview: 'Tofu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include fraud detection, deepfake detection, recruiting, security, and ATS integration.


  Tofu''s developer surface includes pricing, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Hiretofu Com Plans Pricing
  plan_count: 3
  slug: hiretofu-com-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hiretofu Com Domain Security
  slug: hiretofu-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hiretofu-com
tags:
- fraud detection
- deepfake detection
- recruiting
- security
- ATS integration
- AI screening
website: https://hiretofu.com/
---
