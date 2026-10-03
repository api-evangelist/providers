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
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/hosts/quietforge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quietforge-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/vendors/quietforge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quietforge-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/security/quietforge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quietforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quietforge.studio/
- group: docs
  title: ''
  type: Documentation
  url: https://qf-api.quietforge-studio.workers.dev/
coverage:
  checked: '2026-09-28'
  detail: The provider's documentation site returns HTML and no machine‑readable OpenAPI or other contract files were found.
  evidence:
  - status: 200
    url: https://quietforge.studio/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Quietforge Docs API (Quietforge Studio) provides a suite of AI‑run document processing services hosted on Cloudflare Workers. It offers endpoints for converting documents between formats, extracting PDF text, rendering web pages to images or PDFs, generating Sudoku puzzles and books, and advanced typesetting of manuscripts. Pricing is per‑call, with transparent USD rates, and includes a searchable index of x402 pay‑per‑call services on Base blockchain. The platform emphasizes developer-friendly JSON APIs and integrates with on‑chain payment protocols.
layout: provider
modified: '2026-09-27'
name: Quietforge Docs API (Quietforge Studio)
nav: Providers
network: true
overview: 'Quietforge Docs API (Quietforge Studio) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Document Processing, Cloudflare Workers, Software-as-a-Service, and Business Automation.


  Quietforge Docs API (Quietforge Studio)''s developer surface includes documentation and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 4
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Quietforge Domain Security
  slug: quietforge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quietforge
tags:
- Artificial Intelligence
- Document Processing
- Cloudflare Workers
- Software-as-a-Service
- Business Automation
website: https://quietforge.studio/
---
