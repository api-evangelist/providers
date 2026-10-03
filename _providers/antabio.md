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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antabio/refs/heads/main/hosts/antabio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antabio-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antabio.com/legal-notice
- group: company
  title: ''
  type: Newsroom
  url: https://antabio.com/news
- group: other
  title: ''
  type: Leadership
  url: https://antabio.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antabio/refs/heads/main/security/antabio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antabio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antabio.com
coverage:
  checked: 2026-09-25
  detail: The Antabio website serves only HTML pages with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://antabio.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Antabio is a biotechnology company focused on developing innovative antimicrobial therapies to combat resistant infections. The firm leverages advanced peptide engineering and proprietary platforms to create novel treatments aimed at addressing the growing global challenge of antimicrobial resistance. Antabio engages in research collaborations, clinical development, and seeks partnerships to bring its pipeline candidates to market, targeting both hospital and community settings.
layout: provider
modified: '2026-09-25'
name: Antabio
nav: Providers
network: true
overview: Antabio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Antimicrobial, Healthcare, Pharma, and Company.
random_paper: 8
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Antabio Domain Security
  slug: antabio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: antabio
tags:
- Biotechnology
- Antimicrobial
- Healthcare
- Pharma
- Company
website: https://antabio.com
---
