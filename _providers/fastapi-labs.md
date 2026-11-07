---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/fastapi-labs/plans/fastapi-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastapi-labs-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/fastapi-labs/authentication/fastapi-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fastapi-labs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fastapi-labs/well-known/fastapi-labs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fastapi-labs-security.txt
- group: agent
  href: https://artifacts.apis.io/fastapi-labs/well-known/fastapi-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fastapi-labs-well-known.yml
- group: other
  href: https://artifacts.apis.io/fastapi-labs/hosts/fastapi-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastapi-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/fastapi-labs/vendors/fastapi-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastapi-labs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastapicloud.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastapicloud.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/fastapi-labs/security/fastapi-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastapi-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastapicloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fastapicloud.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://fastapicloud.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastapicloud
- group: operate
  title: ''
  type: Support
  url: https://fastapicloud.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://fastapicloud.com/pricing
created: '2026-10-23'
description: FastAPI Labs, operating as FastAPI Cloud, provides a developer‑focused platform that lets you deploy FastAPI applications with a single command. Backed by Sequoia Capital, the service offers zero‑config global infrastructure, automatic scaling, and built‑in metrics, targeting both human developers and AI agents. It integrates with popular tools, supports custom domains, and emphasizes security with HTTPS by default.
image: https://fastapicloud.com/social-preview.png
layout: provider
modified: '2026-10-23'
name: FastAPI Labs
nav: Providers
network: true
overview: 'FastAPI Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Platform, Cloud, Python, and Open Source.


  FastAPI Labs'' developer surface includes authentication, documentation, engineering blog, support, pricing, and 10 more developer resources.'
plans:
- name: Fastapi Labs Plans Pricing
  plan_count: 2
  slug: fastapi-labs-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 48.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fastapi-labs/fastapi-labs-2026-11-03T131855.png
security:
- kind: authentication
  name: Fastapi Labs Authentication
  slug: fastapi-labs-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fastapi Labs Domain Security
  slug: fastapi-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fastapi-labs
tags:
- Company
- API Platform
- Cloud
- Python
- Open Source
website: https://fastapicloud.com/
---
