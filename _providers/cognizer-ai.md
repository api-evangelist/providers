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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognizer-ai/refs/heads/main/vendors/cognizer-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognizer-ai-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognizer-ai/refs/heads/main/hosts/cognizer-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognizer-ai-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.cognizer.ai/hc/en-us
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognizer-ai/refs/heads/main/security/cognizer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognizer-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cognizer.ai
coverage:
  checked: '2026-10-09'
  detail: The main site https://cognizer.ai returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 202
    url: https://cognizer.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cognizer Inc is a contract intelligence AI vendor serving enterprises, SaaS vendors, and legal service providers. Their Agentic AI platform discovers contracts and structures key data elements, streamlining business processes and enabling informed decision making. Based in Pleasanton, California, Cognizer focuses on advanced contract intelligence challenges using cutting‑edge AI technology.
layout: provider
modified: '2026-10-09'
name: Cognizer AI
nav: Providers
network: true
overview: 'Cognizer AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Contract Intelligence, Software-as-a-Service, and Legal Tech.


  Cognizer AI''s developer surface includes support and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 4.0
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
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognizer Ai Domain Security
  slug: cognizer-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cognizer-ai
tags:
- Company
- Artificial Intelligence
- Contract Intelligence
- Software-as-a-Service
- Legal Tech
website: https://cognizer.ai
---
