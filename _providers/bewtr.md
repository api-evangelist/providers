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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bewtr/refs/heads/main/conformance/bewtr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bewtr-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bewtr/refs/heads/main/hosts/bewtr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bewtr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bewtr/refs/heads/main/vendors/bewtr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bewtr-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bewtr/refs/heads/main/security/bewtr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bewtr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bewtr.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bewtr.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.bewtr.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bewtr.com/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://www.bewtr.com/mcp
  - status: 403
    url: https://equityzen.com/company/bewtr
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bewtr (BE WTR) is a premium sustainable water brand offering still and sparkling bottled water in circular premium glass packaging. The company focuses on local sourcing, high‑quality taste, and environmental stewardship, providing a range of products such as AQTiV FILTER, DUO, ONE, COMBI, and TOWER systems. Their mission emphasizes zero waste and circularity, positioning BE WTR as a leader in sustainable premium water solutions worldwide.
image: https://www.bewtr.com/hubfs/BE%20WTR%20Logo.png
layout: provider
modified: '2026-09-28'
name: Bewtr
nav: Providers
network: true
overview: 'Bewtr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Sustainability, Premium, and BottledWater.


  Bewtr''s developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bewtr Domain Security
  slug: bewtr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bewtr
tags:
- Company
- Water
- Sustainability
- Premium
- BottledWater
- Circular Economy
website: https://www.bewtr.com
---
