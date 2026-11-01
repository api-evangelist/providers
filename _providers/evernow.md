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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/evernow/llms/evernow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evernow-llms.txt
- group: other
  href: https://artifacts.apis.io/evernow/hosts/evernow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evernow-hosts.yml
- group: other
  href: https://artifacts.apis.io/evernow/vendors/evernow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evernow-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evernow.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.evernow.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evernow.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.evernow.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://help.evernow.com/
- group: auth
  href: https://artifacts.apis.io/evernow/security/evernow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evernow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evernow.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.evernow.com/mcp
  - status: 200
    url: https://www.evernow.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Evernow provides expert menopause care, treatments, and prescription services through a telehealth platform. Users can access personalized medical guidance, hormone therapy, and symptom management online, supported by licensed clinicians. The service emphasizes evidence‑based approaches, privacy, and convenient digital access, aiming to improve quality of life for women navigating menopause. Evernow’s platform integrates scheduling, secure messaging, and prescription delivery, reflecting a modern, patient‑centered healthcare solution.
image: https://cdn.prod.website-files.com/62039cc91acccd69bbc3274f/6234821b71fe6f2a89a8ec47_OG-min.webp
layout: provider
modified: '2026-10-22'
name: Evernow
nav: Providers
network: true
overview: 'Evernow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Menopause, Telehealth, and Women''s Health.


  Evernow''s developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Evernow Domain Security
  slug: evernow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evernow
tags:
- Company
- Health
- Menopause
- Telehealth
- Women's Health
website: https://www.evernow.com/
---
