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
  href: https://raw.githubusercontent.com/api-evangelist/constancetherapeutics/refs/heads/main/hosts/constancetherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constancetherapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/constancetherapeutics/refs/heads/main/vendors/constancetherapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constancetherapeutics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constancetherapeutics.com/utility/terms-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://constancetherapeutics.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/constancetherapeutics/refs/heads/main/security/constancetherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constancetherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constancetherapeutics.com
coverage:
  checked: '2026-10-10'
  detail: The company website provides no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://constancetherapeutics.com
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Constancetherapeutics is a vertically integrated cannabis therapeutics company producing standardized, science‑based whole‑plant extracts. Since 2008 it has focused on quality, evidence‑based options and offers a range of CBD‑rich products through its online shop, serving thousands of customers and advancing insurance reimbursement initiatives for seniors.
image: https://cdn.prod.website-files.com/686b504b1f4531c18a7e5001/686f92948cfd7b3f409e6c5f_273d14f2cf609d36b3b2303ab74113e4_Thumbnail.avif
layout: provider
modified: '2026-10-10'
name: Constancetherapeutics
nav: Providers
network: true
overview: Constancetherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cannabis, Therapeutics, CBD, and Health.
random_paper: 11
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constancetherapeutics Domain Security
  slug: constancetherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: constancetherapeutics
tags:
- Company
- Cannabis
- Therapeutics
- CBD
- Health
website: https://constancetherapeutics.com
---
