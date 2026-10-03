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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biomeme/refs/heads/main/llms/biomeme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biomeme-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biomeme/refs/heads/main/well-known/biomeme-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/biomeme-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biomeme/refs/heads/main/well-known/biomeme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biomeme-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biomeme/refs/heads/main/hosts/biomeme-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biomeme-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biomeme/refs/heads/main/vendors/biomeme-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biomeme-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.biomeme.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biomeme.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://biomeme.com/about/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.biomeme.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biomeme/refs/heads/main/security/biomeme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biomeme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biomeme.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.biomeme.com
- group: company
  title: ''
  type: Blog
  url: https://blog.biomeme.com
coverage:
  checked: '2026-09-28'
  detail: Developer portal renders HTML only, no machine‑readable OpenAPI or other contract found.
  evidence:
  - status: 200
    url: https://portal.biomeme.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Biomeme provides mobile CBRN biodefense and point‑of‑care molecular diagnostic solutions. Their platform enables rapid testing for infectious diseases, antimicrobial resistance, and health monitoring across military, public health, and research sectors. Biomeme’s products include handheld PCR devices, assay kits, and a cloud‑based data platform for real‑time results and analytics.
layout: provider
modified: '2026-09-28'
name: Biomeme
nav: Providers
network: true
overview: 'Biomeme is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Biotechnology, Healthcare, and Molecular Testing.


  Biomeme''s developer surface includes support, documentation, engineering blog, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biomeme Domain Security
  slug: biomeme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biomeme
tags:
- Company
- Diagnostics
- Biotechnology
- Healthcare
- Molecular Testing
- CBRN
website: https://biomeme.com/
---
