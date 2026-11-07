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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cerula-care/hosts/cerula-care-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cerula-care-hosts.yml
- group: other
  href: https://artifacts.apis.io/cerula-care/vendors/cerula-care-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cerula-care-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cerula-care/security/cerula-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerula-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cerulacare.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://cerulacare.com/#model
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@cerulacare.com
coverage:
  checked: '2026-10-08'
  detail: Home page returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://cerulacare.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Cerula Care provides integrated psycho‑oncology collaborative care for health systems and oncology practices. It embeds expert psychosocial support into cancer treatment workflows, improving patient outcomes and unlocking reimbursable collaborative‑care billing codes. The company combines clinical expertise with AI‑driven models to deliver coordinated mental‑health services, reporting outcomes and revenue for providers.
image: https://cerulacare.com/assets/cerula-care-logo-C0ioTcwm.png
layout: provider
modified: '2026-10-07'
name: Cerula Care
nav: Providers
network: true
overview: 'Cerula Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Behavioral Health, Oncology, and Collaborative Care.


  Cerula Care''s developer surface includes getting-started guide and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 6.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cerula-care/cerula-care-2026-11-03T123734.png
security:
- kind: domain-security
  name: Cerula Care Domain Security
  slug: cerula-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cerula-care
tags:
- Company
- Healthcare
- Behavioral Health
- Oncology
- Collaborative Care
website: https://cerulacare.com/
---
