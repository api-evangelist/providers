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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cell-ed.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cell-ed/refs/heads/main/hosts/cell-ed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cell-ed-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cell-ed/refs/heads/main/vendors/cell-ed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cell-ed-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cell-ed.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cell-ed.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.cell-ed.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cell-Ed
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cell-ed/refs/heads/main/security/cell-ed-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cell-ed-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cell-ed/refs/heads/main/security/cell-ed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cell-ed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cell-ed.com
coverage:
  checked: '2026-10-07'
  detail: Developer portal at https://dev.cell-ed.com/ provides documentation but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 0
    url: https://api.cell-ed.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cell-Ed provides mobile-first, micro‑learning courses that help adults develop essential literacy, digital, and life‑skill competencies. Their platform delivers 3‑minute lessons via smartphone, WhatsApp, and web, targeting workers with limited time. Partnering with organizations like EnGen, Cell‑Ed creates pathways to employment, offering courses in language, academic, work, and life skills, while also supplying employers with upskilled talent.
image: http://static1.squarespace.com/static/69c50f951a134d54994796f0/t/69c51d2c4694333b2a927835/1774525740630/Cell-ed_Logo_high.png?format=1500w
layout: provider
modified: '2026-10-07'
name: Cell-Ed
nav: Providers
network: true
overview: 'Cell-Ed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, MobileLearning, WorkforceDevelopment, MicroLearning, and SkillBuilding.


  Cell-Ed''s developer surface includes documentation and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cell Ed Domain Security
  slug: cell-ed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cell Ed Trust Center
  slug: cell-ed-trust-center
  summary_line: SOC 2, HIPAA
slug: cell-ed
tags:
- Education
- MobileLearning
- WorkforceDevelopment
- MicroLearning
- SkillBuilding
- Company
website: https://www.cell-ed.com
---
