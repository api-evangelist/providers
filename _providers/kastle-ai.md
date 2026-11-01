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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/kastle-ai/well-known/kastle-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kastle-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/kastle-ai/hosts/kastle-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kastle-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/kastle-ai/vendors/kastle-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kastle-ai-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.kastle.ai/
- group: auth
  href: https://artifacts.apis.io/kastle-ai/security/kastle-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kastle-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kastle.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kastle.ai
created: '2026-10-22'
description: Kastle AI provides an AI‑driven platform that automates the full loan lifecycle, keeping originations, fulfillment, and servicing moving 24/7. Built for regulated financial work, it connects to existing banking and loan systems, offering agents that handle tasks from application intake to post‑closing management, improving efficiency and compliance across the loan process.
image: https://framerusercontent.com/images/nWHdKftAnklKiPSskgcJquexg.png
layout: provider
modified: '2026-10-22'
name: Kastle AI
nav: Providers
network: true
overview: 'Kastle AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, FinTech, Loan, Automation, and Platform.


  Kastle AI''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kastle Ai Domain Security
  slug: kastle-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kastle-ai
tags:
- AI
- FinTech
- Loan
- Automation
- Platform
website: https://kastle.ai
---
