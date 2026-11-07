---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer portal provides API reference and integration guides for EasyDial's communication platform.
  name: EasyDial API
  slug: easydial-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.easydial.io/trust
- group: other
  href: https://artifacts.apis.io/easydial/hosts/easydial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easydial-hosts.yml
- group: auth
  href: https://artifacts.apis.io/easydial/security/easydial-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/easydial-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/easydial/security/easydial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easydial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.easydial.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.easydial.io/api-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.easydial.io/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.easydial.io
- group: operate
  title: ''
  type: Support
  url: https://www.easydial.io/contact.php
- group: company
  title: ''
  type: Blog
  url: https://www.easydial.io/blog
coverage:
  checked: '2026-10-24'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.easydial.io/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: EasyDial provides a comprehensive suite of cloud‑based contact‑center and unified communications solutions, including omnichannel call handling, AI‑driven chatbots, voice bots, WhatsApp messaging, audio conferencing, and broadcasting tools. Targeting enterprises across health, telecom, banking, e‑commerce, education and finance sectors, the platform integrates with Microsoft Teams, CRM systems and offers professional services, gateway‑as‑a‑service and managed services. EasyDial emphasizes affordable, scalable pricing and a developer‑friendly API for real‑time communications.
layout: provider
modified: '2026-10-24'
name: Easydial
nav: Providers
network: true
overview: 'Easydial is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Artificial Intelligence, Unified Communications, and Contact Center.


  Easydial''s developer surface includes documentation, getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 15.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/easydial/easydial-2026-11-03T131232.png
security:
- kind: domain-security
  name: Easydial Domain Security
  slug: easydial-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Easydial Trust Center
  slug: easydial-trust-center
  summary_line: SOC 2, GDPR
slug: easydial
tags:
- Company
- Communications
- Artificial Intelligence
- Unified Communications
- Contact Center
website: https://www.easydial.io
---
