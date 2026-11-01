---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Scarlet compliance platform
  name: Scarlet API
  slug: scarlet-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/scarletcomply-com/hosts/scarletcomply-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scarletcomply-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/scarletcomply-com/security/scarletcomply-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scarletcomply-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scarlet.cc/
- group: docs
  title: ''
  type: Documentation
  url: https://www.scarlet.cc/mission
- group: company
  title: ''
  type: Blog
  url: https://www.scarlet.cc/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scarlet.cc/legal/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scarlet.cc/legal/privacy-policy
coverage:
  detail: Homepage is a JavaScript‑rendered single‑page app, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://www.scarlet.cc/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Scarlet provides AI medical device certification services, helping innovators bring AI-driven healthcare technologies to market quickly and compliantly. By acting as a Notified Body, Scarlet streamlines regulatory approval under EU MDR and other frameworks, offering guidance, audits, and continuous support to ensure devices meet safety and performance standards. Their platform integrates with developers to accelerate certification, reduce time-to-market, and maintain compliance throughout product updates.
image: https://framerusercontent.com/assets/pOOYU5LKBkcB9VJnN6W1QbmPCSA.svg
layout: provider
modified: '2026-10-22'
name: Scarlet
nav: Providers
network: true
overview: 'Scarlet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, MedicalDevice, Certification, and NotifiedBody.


  Scarlet''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Scarletcomply Com Rate Limits
  slug: scarletcomply-com-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scarletcomply Com Domain Security
  slug: scarletcomply-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scarletcomply-com
tags:
- Company
- AI
- MedicalDevice
- Certification
- NotifiedBody
website: https://www.scarlet.cc/
---
