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
- group: design
  href: https://artifacts.apis.io/beme-health/conformance/beme-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beme-health-conformance.yml
- group: other
  href: https://artifacts.apis.io/beme-health/hosts/beme-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beme-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/beme-health/vendors/beme-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beme-health-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hazel.co/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hazel.co/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.hazel.co/news
- group: start
  title: ''
  type: GettingStarted
  url: https://hazel.co/get-started
- group: auth
  href: https://artifacts.apis.io/beme-health/security/beme-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beme-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hazel.co/
coverage:
  checked: '2026-09-27'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://my.hazel.co/openapi.json
  - status: 200
    url: https://my.hazel.co/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: BeMe Health, operating under the brand Hazel Health, provides K‑12 telehealth services, offering virtual mental and physical health care for students through school district partnerships. The company focuses on equitable access to pediatric care, integrating therapy, medical consultations, and wellness resources via its online platform.
image: https://cdn.prod.website-files.com/6726adae0a7647e5cdcb00e3/68474e66e54ff774a3c054b2_hazel-og.jpg
layout: provider
modified: '2026-09-27'
name: BeMe Health
nav: Providers
network: true
overview: 'BeMe Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Telehealth, K-12, Education, and Pediatrics.


  BeMe Health''s developer surface includes getting-started guide and 8 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/beme-health/beme-health-2026-10-11T101844.png
security:
- kind: domain-security
  name: Beme Health Domain Security
  slug: beme-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beme-health
tags:
- Health
- Telehealth
- K-12
- Education
- Pediatrics
website: https://www.hazel.co/
---
