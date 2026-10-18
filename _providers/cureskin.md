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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: No public machine‑readable API contract discovered; the site provides a pricing page but no OpenAPI/GraphQL spec.
  name: Cureskin API
  slug: cureskin-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cureskin/refs/heads/main/plans/cureskin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cureskin-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cureskin/refs/heads/main/llms/cureskin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cureskin-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cureskin/refs/heads/main/hosts/cureskin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cureskin-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cureskin.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cureskin
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cureskin/refs/heads/main/security/cureskin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cureskin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cureskin.com
- group: company
  title: ''
  type: About
  url: https://cureskin.com/about-cureskin/
- group: docs
  title: ''
  type: Documentation
  url: https://cureskin.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cureskin.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cureskin.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://cureskin.com/contact/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://cureskin.com
  - status: 403
    url: https://equityzen.com/company/cureskin
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Cureskin is an AI‑powered dermatology and hair‑care platform founded in 2017 in Bengaluru, India. It offers a mobile app that provides free AI skin and hair analysis, connects users with board‑certified dermatologists, and delivers personalized, prescription‑strength treatment kits. The service combines machine‑learning diagnostics with clinician oversight to address conditions such as acne, hair loss, and skin aging, aiming to make professional dermatological care accessible and continuous for everyday health needs.
image: https://cureskin.com/wp-content/uploads/2025/08/send.png
layout: provider
modified: '2026-10-12'
name: Cureskin
nav: Providers
network: true
overview: 'Cureskin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Dermatology, Skincare, and Hair Care.


  Cureskin''s developer surface includes pricing, documentation, and 10 more developer resources.'
plans:
- name: Cureskin Plans Pricing
  plan_count: 1
  slug: cureskin-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cureskin Domain Security
  slug: cureskin-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: cureskin
tags:
- Company
- Artificial Intelligence
- Dermatology
- Skincare
- Hair Care
website: https://cureskin.com
---
