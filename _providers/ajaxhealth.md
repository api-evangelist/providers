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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ajaxhealth/refs/heads/main/hosts/ajaxhealth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ajaxhealth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ajaxhealth/refs/heads/main/vendors/ajaxhealth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ajaxhealth-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ajaxhealth.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://ajaxhealth.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://ajaxhealth.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ajaxhealth/refs/heads/main/security/ajaxhealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ajaxhealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ajaxhealth.com
coverage:
  checked: 2026-09-23
  detail: Home page provides no machine-readable API specification or documentation.
  evidence:
  - status: 200
    url: https://ajaxhealth.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: Ajaxhealth is a global investment firm focused on building and scaling high-quality healthcare businesses. It partners with industry leaders to innovate in medical technology, supporting companies through growth capital and strategic guidance. The firm operates across multiple locations including Menlo Park, New York, Austin, and Los Angeles, and engages in activities such as investing, mentorship, and fostering collaborations to advance healthcare solutions.
image: https://ajaxhealth.com/wp-content/uploads/team-cta.png
layout: provider
modified: '2026-09-23'
name: Ajaxhealth
nav: Providers
network: true
overview: Ajaxhealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Investment, Healthcare, MedTech, Venture Capital, and Company.
random_paper: 16
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ajaxhealth Domain Security
  slug: ajaxhealth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ajaxhealth
tags:
- Investment
- Healthcare
- MedTech
- Venture Capital
- Company
website: https://ajaxhealth.com
---
