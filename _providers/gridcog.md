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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://security.gridcog.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gridcog/refs/heads/main/well-known/gridcog-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gridcog-my-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gridcog/refs/heads/main/well-known/gridcog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gridcog-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gridcog/refs/heads/main/hosts/gridcog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gridcog-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gridcog/refs/heads/main/vendors/gridcog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gridcog-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.gridcog.com/industries/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gridcog/refs/heads/main/security/gridcog-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gridcog-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gridcog/refs/heads/main/security/gridcog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gridcog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gridcog.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gridcog.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.gridcog.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gridcog.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gridcog.com/legal/user-terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://www.gridcog.com/profile
- group: operate
  title: ''
  type: Support
  url: https://my.gridcog.com
coverage:
  checked: '2026-10-13'
  detail: Documentation pages render only minimal text and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://my.gridcog.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Gridcog provides intelligent energy decision software that enables large‑scale asset developers, consultants, energy majors, and e‑mobility planners to accurately evaluate and design utility‑scale hybrid, co‑located, and EV charging projects. Their platform offers multi‑market, multi‑site, and multi‑asset simulation tools, delivering transparent, reliable modeling for commercial and industrial energy projects. Gridcog’s solutions help clients assess feasibility, optimize designs, and accelerate investment decisions in the clean energy transition.
image: https://cdn.prod.website-files.com/63078873858838fe95a00d2d/6385bd0b39e0d66f366d28c1_Home-OG%20(1).webp
layout: provider
modified: '2026-10-13'
name: Gridcog
nav: Providers
network: true
overview: 'Gridcog is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Software, Cleantech, and Modeling.


  Gridcog''s developer surface includes pricing, engineering blog, signup flow, support, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gridcog Domain Security
  slug: gridcog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Gridcog Trust Center
  slug: gridcog-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: gridcog
tags:
- Company
- Energy
- Software
- Cleantech
- Modeling
website: https://www.gridcog.com
---
