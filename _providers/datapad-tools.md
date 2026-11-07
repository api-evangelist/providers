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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documented on the developer portal.
  name: Data Pad API
  slug: data-pad-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/datapad-tools/hosts/datapad-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datapad-tools-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datapad.tools/developer/
- group: auth
  href: https://artifacts.apis.io/datapad-tools/security/datapad-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datapad-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datapad.tools/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI or other machine‑readable contract found despite a public developer portal.
  evidence:
  - status: 200
    url: https://datapad.tools/developer/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Data Pad provides a free suite of in‑browser tools for editing, validating and transforming healthcare and business data formats such as HL7 v2, HIPAA X12, EDIFACT, CSV, JSON, XML, PDF, DICOM images and more. Users can split, merge, de‑identify, generate synthetic test data and perform metadata editing, all directly in the browser with no data leaving the client device.
image: https://datapad.tools/opengraph-image?c8af2e6488cba51c
layout: provider
modified: '2026-11-05'
name: Data Pad
nav: Providers
network: true
overview: Data Pad is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Tools, Healthcare, Business, Open Source, and Free.
random_paper: 5
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datapad Tools Domain Security
  slug: datapad-tools-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datapad-tools
tags:
- Data Tools
- Healthcare
- Business
- Open Source
- Free
website: https://datapad.tools/
---
