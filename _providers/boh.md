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
  href: https://raw.githubusercontent.com/api-evangelist/boh/refs/heads/main/llms/boh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boh-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boh/refs/heads/main/hosts/boh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boh-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boh/refs/heads/main/vendors/boh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boh-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boh/refs/heads/main/security/boh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boh.ai/
- group: company
  title: ''
  type: Blog
  url: https://boh.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://boh.ai/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boh.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boh.ai/privacy-policy
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI or other machine-readable contract found at https://api.boh.ai/openapi.json (no response).
  evidence:
  - status: 0
    url: https://api.boh.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Boh provides a comprehensive partner solution for restaurant repairs, maintenance, and compliance across Southern California. It coordinates vendor services, handles emergency repairs, and manages compliance documentation, helping restaurant operators reduce downtime and operational costs. The platform offers a wide range of services from HVAC and refrigeration repair to fire suppression maintenance, ensuring kitchens stay operational and meet regulatory standards.
image: https://boh.ai/og-default.png
layout: provider
modified: '2026-10-12'
name: Boh
nav: Providers
network: true
overview: 'Boh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Maintenance, Compliance, and Repair.


  Boh''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.0
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
    developer_ergonomics: 7.1
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
  name: Boh Domain Security
  slug: boh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boh
tags:
- Company
- Restaurant
- Maintenance
- Compliance
- Repair
website: https://boh.ai/
---
