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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/x4-pharmaceuticals/hosts/x4-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/x4-pharmaceuticals-hosts.yml
- group: other
  href: https://artifacts.apis.io/x4-pharmaceuticals/vendors/x4-pharmaceuticals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/x4-pharmaceuticals-vendors.yml
- group: auth
  href: https://artifacts.apis.io/x4-pharmaceuticals/security/x4-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/x4-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.x4pharma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.x4pharma.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.x4pharma.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.x4pharma.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.x4pharma.com/compliance-ethics/
coverage:
  checked: '2026-10-23'
  detail: X4 Pharmaceuticals is a biotech company with no public developer API.
  evidence:
  - status: 200
    url: https://www.x4pharma.com/
  reason: not-a-software-company
  state: none
created: '2026-10-22'
description: X4 Pharmaceuticals develops and commercializes innovative therapies for rare immune system diseases. It has received U.S. approval for mavorixafor (XOLREMDI®) and is advancing it in a global Phase 3 trial. Headquartered in Boston, Massachusetts, X4 is publicly traded on Nasdaq under the symbol XFOR. The company focuses on patients with unmet needs, delivering progress through its Rare Resolve program.
layout: provider
modified: '2026-10-22'
name: X4 Pharmaceuticals
nav: Providers
network: true
overview: 'X4 Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Rare Diseases, and Clinical Trials.


  X4 Pharmaceuticals'' developer surface includes documentation and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: X4 Pharmaceuticals Domain Security
  slug: x4-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: x4-pharmaceuticals
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Rare Diseases
- Clinical Trials
website: https://www.x4pharma.com/
---
