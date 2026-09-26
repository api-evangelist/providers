---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiwo/refs/heads/main/llms/aiwo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiwo-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiwo/refs/heads/main/well-known/aiwo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiwo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiwo/refs/heads/main/vendors/aiwo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiwo-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiwo/refs/heads/main/security/aiwo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiwo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiwo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiwo.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiwo.com/pages/aiwo-terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://aiwo.com/blogs/blog
created: '2026-09-22'
description: Aiwo Limited is a science‑driven longevity hub offering advanced health screenings, personalized treatment plans, tailored supplements, and wellness therapies. Their platform combines cutting‑edge diagnostics with AI‑powered insights to help adults improve health, energy, and lifespan.
layout: provider
modified: '2026-09-22'
name: Aiwo
nav: Providers
network: true
overview: 'Aiwo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Longevity, Wellness, Diagnostics, and Artificial Intelligence.


  Aiwo''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 9.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiwo Domain Security
  slug: aiwo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiwo
tags:
- Health
- Longevity
- Wellness
- Diagnostics
- Artificial Intelligence
website: https://aiwo.com/
---
