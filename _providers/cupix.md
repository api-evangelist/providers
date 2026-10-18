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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cupix/refs/heads/main/hosts/cupix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cupix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cupix/refs/heads/main/vendors/cupix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cupix-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cupix.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cupix.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cupix.com/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cupix/refs/heads/main/security/cupix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cupix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cupix.com
coverage:
  checked: '2026-10-12'
  detail: OpenAPI endpoint https://app.cupix.com/openapi.json returns HTML instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://app.cupix.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Cupix provides an AI‑powered 4D digital twin platform that transforms 360° video, laser scans, drone imagery and BIM data into detailed, measurable 3‑D models. It enables construction, oil & gas, manufacturing, and government teams to visualize, track progress, verify designs, and collaborate remotely, reducing site visits and rework while improving productivity and safety.
image: https://cdn.prod.website-files.com/60a1d24dc3ad906020ec0b79/6a9d748706be28b14a2df4d8_meta%20graph%20image-home-100.jpg
layout: provider
modified: '2026-10-12'
name: Cupix
nav: Providers
network: true
overview: 'Cupix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Spatial Intelligence, Digital Twin, and Artificial Intelligence.


  Cupix''s developer surface includes pricing and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Cupix Domain Security
  slug: cupix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cupix
tags:
- Company
- Construction
- Spatial Intelligence
- Digital Twin
- Artificial Intelligence
website: https://www.cupix.com
---
