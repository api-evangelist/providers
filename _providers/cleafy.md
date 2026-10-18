---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Cleafy fraud detection platform
  name: Cleafy API
  slug: cleafy-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleafy/refs/heads/main/well-known/cleafy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleafy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleafy/refs/heads/main/hosts/cleafy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleafy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleafy/refs/heads/main/vendors/cleafy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleafy-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cleafy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cleafy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleafy/refs/heads/main/security/cleafy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleafy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleafy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cleafy.com/resources/documents
- group: company
  title: ''
  type: Blog
  url: https://www.cleafy.com/news
- group: operate
  title: ''
  type: Support
  url: https://support.cleafy.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3993512.fs1.hubspotusercontent-na1.net/hubfs/3993512/CLEAFY/Downloadable%20Resources/Legal%20Documentation/Website%20Terms%20of%20Use_2024.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/31282315
coverage:
  checked: '2026-10-08'
  detail: Documentation pages are client‑side rendered SPAs, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.cleafy.com/document-category/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Cleafy is a Milan‑based cybersecurity company founded in 2014, providing an AI‑powered fraud detection and prevention platform for banks and financial institutions. Its solution monitors web, mobile and API sessions in real time to detect and stop online banking fraud, account takeover, and other digital threats, serving clients across EMEA, the Americas and Asia.
image: https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/6a0efcff2c6691f08cd0b4a4_1bd9910d2177fcb870cb14173c4149f1_Homepage_Nyx_Opengraph.avif
layout: provider
modified: '2026-10-08'
name: Cleafy
nav: Providers
network: true
overview: 'Cleafy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Fraud Prevention, Banking, and Artificial Intelligence.


  Cleafy''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 18.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleafy Domain Security
  slug: cleafy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cleafy
tags:
- Company
- Cybersecurity
- Fraud Prevention
- Banking
- Artificial Intelligence
website: https://www.cleafy.com
---
