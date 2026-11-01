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
api_count: 1
apis:
- description: Instacash (Instacash PE) provides financial services API as described on their developer portal.
  name: Instacash PE API
  slug: instacash-pe-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://reevalua.com/
- group: agent
  href: https://artifacts.apis.io/instacash-pe/llms/instacash-pe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instacash-pe-llms.txt
- group: other
  href: https://artifacts.apis.io/instacash-pe/hosts/instacash-pe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instacash-pe-hosts.yml
- group: other
  href: https://artifacts.apis.io/instacash-pe/vendors/instacash-pe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instacash-pe-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reevalua.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reevalua.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://reevalua.com/blog
- group: auth
  href: https://artifacts.apis.io/instacash-pe/security/instacash-pe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/instacash-pe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/instacash-pe/security/instacash-pe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instacash-pe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instacash.pe
coverage:
  checked: '2026-10-25'
  detail: Developer portal redirects to reevalua.com with JavaScript‑rendered pages, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://reevalua.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: 'PreAuth (Instacash) is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by 500-global) and added to the network as a stub for full-pipeline profiling.'
image: https://reevalua.com/img/new/thumb-b2c.png
layout: provider
modified: '2026-10-25'
name: PreAuth (Instacash)
nav: Providers
network: true
overview: 'PreAuth (Instacash) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  PreAuth (Instacash)''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Instacash Pe Domain Security
  slug: instacash-pe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Instacash Pe Trust Center
  slug: instacash-pe-trust-center
  summary_line: SOC 2, ISO 27001
slug: instacash-pe
tags:
- Company
website: https://instacash.pe
---
