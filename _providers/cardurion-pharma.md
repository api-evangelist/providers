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
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cardurion-pharma/refs/heads/main/well-known/cardurion-pharma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardurion-pharma-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cardurion-pharma/refs/heads/main/hosts/cardurion-pharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardurion-pharma-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cardurion-pharma/refs/heads/main/vendors/cardurion-pharma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardurion-pharma-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cardurion.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://cardurion.com/about-cardurion/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cardurion-pharma/refs/heads/main/security/cardurion-pharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardurion-pharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardurion.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardurion.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardurion.com/terms
- group: operate
  title: ''
  type: Support
  url: https://cardurion.com/contact-us
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found despite probing known hosts and documentation pages.
  evidence:
  - status: 200
    url: https://cardurion.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cardurion Pharma is a cardiovascular-focused biopharmaceutical company developing novel therapeutics for heart disease. It translates expertise in cardiovascular signaling pathways into groundbreaking treatments, acquiring assets, discovering new targets, and advancing programs such as PDE9 and CaMKII inhibitors. The company aims to address unmet patient needs through innovative drug candidates and expanded access programs, with a pipeline spanning multiple therapeutic areas.
layout: provider
modified: '2026-10-07'
name: Cardurion Pharma
nav: Providers
network: true
overview: 'Cardurion Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Cardiovascular, Therapeutics, and Drug Development.


  Cardurion Pharma''s developer surface includes support and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardurion Pharma Domain Security
  slug: cardurion-pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardurion-pharma
tags:
- Company
- Biopharma
- Cardiovascular
- Therapeutics
- Drug Development
website: https://cardurion.com
---
