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
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cakap/refs/heads/main/llms/cakap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cakap-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cakap/refs/heads/main/hosts/cakap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cakap-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cakap/refs/heads/main/vendors/cakap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cakap-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://cakap.com/kelas-korporasi/leadership/
- group: company
  title: ''
  type: Blog
  url: https://blog.cakap.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cakap/refs/heads/main/security/cakap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cakap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cakap.com/
coverage:
  checked: '2026-10-06'
  detail: Cakap's public website provides human‑readable information but no machine‑readable API specification was discovered.
  evidence:
  - status: 200
    url: https://cakap.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Cakap is an Indonesian ed‑tech platform offering online language learning courses, corporate training, and AI‑driven workflow automation. It provides a mobile app and web portal for English, Mandarin, Japanese, Korean, and other languages, serving students, professionals, and enterprises across Southeast Asia.
image: https://cakap.com/wp-content/uploads/2019/11/Cakap.com-ID-FI.jpg
layout: provider
modified: '2026-10-06'
name: Cakap
nav: Providers
network: true
overview: 'Cakap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EdTech, LanguageLearning, OnlineEducation, and SoutheastAsia.


  Cakap''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 4.3
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
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cakap Domain Security
  slug: cakap-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cakap
tags:
- Company
- EdTech
- LanguageLearning
- OnlineEducation
- SoutheastAsia
website: https://cakap.com/
---
