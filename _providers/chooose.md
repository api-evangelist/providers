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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chooose/refs/heads/main/llms/chooose-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chooose-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chooose/refs/heads/main/hosts/chooose-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chooose-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chooose/refs/heads/main/vendors/chooose-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chooose-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chooose.today/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chooose.today/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chooose/refs/heads/main/security/chooose-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chooose-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chooose.today
coverage:
  checked: '2026-10-08'
  detail: Attempts to fetch OpenAPI spec at known API host returned no content.
  evidence:
  - status: 0
    url: https://api.chooose.today/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chooose provides a purpose‑built software platform for scaling Sustainable Aviation Fuel (SAF) programs. Their end‑to‑end solution helps aviation and freight companies plan, procure, report, and manage SAF initiatives, integrating tools for carbon accounting, supplier engagement, and regulatory compliance. The platform is used by industry leaders to accelerate SAF adoption and meet climate targets.
image: https://cdn.sanity.io/images/ea9ydig4/production/2a635a982f40c1a9247b8a975138309112bf0423-2401x1260.jpg?rect=1,0,2400,1260&w=1200&h=630&fit=crop&auto=format
layout: provider
modified: '2026-10-08'
name: Chooose
nav: Providers
network: true
overview: Chooose is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sustainable Aviation Fuel, Climate Tech, Software Platform, and Aviation.
random_paper: 4
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Chooose Domain Security
  slug: chooose-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chooose
tags:
- Company
- Sustainable Aviation Fuel
- Climate Tech
- Software Platform
- Aviation
website: https://www.chooose.today
---
