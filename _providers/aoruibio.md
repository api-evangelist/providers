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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation for AULBIO platform services.
  name: AULBIO API
  slug: aulbio-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aoruibio/refs/heads/main/hosts/aoruibio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aoruibio-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aoruibio/refs/heads/main/security/aoruibio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aoruibio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aulbio.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aulbio.com/etc/agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aulbio.com/etc/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://aulbio.com/main/index.html
coverage:
  checked: 2026-09-25
  detail: The provider's website aulbio.com returns a JavaScript shell, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://aulbio.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Aoruibio, operating under the brand AULBIO, is a South Korean biotechnology company focused on innovative microsphere drug delivery technology called EXTENNA. It provides platform services for long‑acting therapeutics, partnering with pharmaceutical firms to develop injectable, long‑acting products. The company emphasizes smart manufacturing systems, R&D pipelines, and global collaborations to advance bio‑healthcare solutions.
image: http://aulbio.com/og.jpg
layout: provider
modified: '2026-09-25'
name: Aoruibio
nav: Providers
network: true
overview: 'Aoruibio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Healthcare, Drug Delivery, Platform, and South Korea.


  Aoruibio''s developer surface includes documentation and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aoruibio Domain Security
  slug: aoruibio-domain-security
  summary_line: TLSv1.2 · HSTS
slug: aoruibio
tags:
- Biotechnology
- Healthcare
- Drug Delivery
- Platform
- South Korea
website: https://aulbio.com
---
