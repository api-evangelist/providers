---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
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
- group: design
  href: https://artifacts.apis.io/allurion-technologies/conformance/allurion-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allurion-technologies-conformance.yml
- group: other
  href: https://artifacts.apis.io/allurion-technologies/hosts/allurion-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allurion-technologies-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allurion.com/en-us/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allurion.com/en-us/privacy-policy
- group: auth
  href: https://artifacts.apis.io/allurion-technologies/security/allurion-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allurion-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.allurion.com
coverage:
  checked: '2026-10-05'
  detail: The public website provides only marketing pages with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.allurion.com/en-us/start-your-journey
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Allurion Technologies develops non‑surgical weight‑loss solutions, including the FDA‑approved Allurion Smart Capsule and gastric balloon systems. Their platform offers virtual care suites, professional resources, and a partner program to help clinics deliver effective, minimally invasive treatments for obesity. The company focuses on innovative, patient‑centric technology to improve health outcomes and support sustainable weight management.
layout: provider
modified: '2026-09-24'
name: Allurion Technologies
nav: Providers
network: true
overview: Allurion Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weight Loss, Medical Devices, Healthcare, and Technology.
random_paper: 15
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 11.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/allurion-technologies/allurion-technologies-2026-11-03T120656.png
security:
- kind: domain-security
  name: Allurion Technologies Domain Security
  slug: allurion-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allurion-technologies
tags:
- Company
- Weight Loss
- Medical Devices
- Healthcare
- Technology
- Obesity
website: https://www.allurion.com
---
