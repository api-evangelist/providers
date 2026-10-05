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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomtech/refs/heads/main/hosts/bloomtech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloomtech-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomtech/refs/heads/main/vendors/bloomtech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloomtech-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://admissions.bloomtech.com/s/login/SelfRegister
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomtech/refs/heads/main/security/bloomtech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomtech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bloomtech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bloomtech.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomtech.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomtech.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomtech.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.bloomtech.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloominstituteoftechnology
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bloomtech.com/tuition/options
coverage:
  checked: '2026-09-29'
  detail: OpenAPI endpoint https://api.bloomtech.com/openapi.json returned HTTP 530 with no spec.
  evidence:
  - status: 530
    url: https://api.bloomtech.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Bloom Institute of Technology (BloomTech) is an online coding bootcamp offering full‑stack web development and AI‑focused courses. Founded to provide low‑risk, high‑impact pathways to tech careers, it boasts over 4,000 graduates since 2017, an 86% job placement rate in 2022, and a tuition‑refund guarantee. The platform combines flexible part‑time and full‑time options, AI‑enhanced learning, and corporate upskilling solutions for diverse learners.
image: https://cdn.prod.website-files.com/613baa7ad4f394142e65cb73/63052986d3eeaf5b3312dff9_home_opengraph.jpg
layout: provider
modified: '2026-09-29'
name: BloomTech
nav: Providers
network: true
overview: 'BloomTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Coding Bootcamp, Developer Training, AI‑Integrated Learning, Career Support, and Deferred Tuition.


  BloomTech''s developer surface includes engineering blog, documentation, support, pricing, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloomtech Domain Security
  slug: bloomtech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomtech
tags:
- Coding Bootcamp
- Developer Training
- AI‑Integrated Learning
- Career Support
- Deferred Tuition
website: https://www.bloomtech.com/
---
