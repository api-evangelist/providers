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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Halesis provides an efficient language model platform for developers, offering chat completions and integration tools.
  name: Halesis API
  slug: halesis-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/halesis/refs/heads/main/plans/halesis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/halesis-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/halesis/refs/heads/main/well-known/halesis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/halesis-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/halesis/refs/heads/main/hosts/halesis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/halesis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/halesis/refs/heads/main/vendors/halesis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/halesis-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://halesis.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.halesis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://halesis.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://halesis.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://halesis.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/halesis
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/halesis/refs/heads/main/security/halesis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/halesis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://halesis.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.halesis.com/api-docs
coverage:
  checked: '2026-10-12'
  detail: API documentation is a Next.js SPA that returns HTML shells without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://app.halesis.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: 'Halesis is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.halesis.com/website-files/summary_large_image.jpg
layout: provider
modified: '2026-10-12'
name: Halesis
nav: Providers
network: true
overview: 'Halesis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Language Model Platform, Developers, AI Integration, and Chat Completions.


  Halesis'' developer surface includes pricing, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Halesis Plans Pricing
  plan_count: 3
  slug: halesis-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 39.3
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Halesis Domain Security
  slug: halesis-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: halesis
tags:
- Language Model Platform
- Developers
- AI Integration
- Chat Completions
website: https://halesis.com
---
