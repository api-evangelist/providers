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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amberstone-biosciences/refs/heads/main/hosts/amberstone-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amberstone-biosciences-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amberstone-biosciences/refs/heads/main/security/amberstone-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amberstone-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://amberstonebio.com/
- group: company
  title: ''
  type: About
  url: http://amberstonebio.com/web/about.php
- group: operate
  title: ''
  type: Contact
  url: http://amberstonebio.com/web/contact.php
- group: docs
  title: ''
  type: Documentation
  url: http://amberstonebio.com/web/science.php
coverage:
  checked: 2026-09-24
  detail: The provider's documentation pages are HTML with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://amberstonebio.com/web/science.php
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Amberstone Biosciences Inc. discovers transformative immunotherapeutics, focusing on tumor‑activated T‑MATE™ technology to develop precise, safe cancer treatments. The company pioneers next‑gen immunotherapies that trigger immune responses only in tumors, minimizing harm to healthy tissue. Their pipeline spans innovative antibody‑drug conjugates and novel biologics aimed at solid tumors, leveraging proprietary platforms to unlock therapeutic potential previously deemed undruggable.
layout: provider
modified: '2026-09-24'
name: Amberstone Biosciences
nav: Providers
network: true
overview: 'Amberstone Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Immunotherapy, Cancer, and Therapeutics.


  Amberstone Biosciences'' developer surface includes documentation and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amberstone Biosciences Domain Security
  slug: amberstone-biosciences-domain-security
  summary_line: TLSv1.2
slug: amberstone-biosciences
tags:
- Company
- Biotechnology
- Immunotherapy
- Cancer
- Therapeutics
website: http://amberstonebio.com/
---
