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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automed/refs/heads/main/hosts/automed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automed-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automed/refs/heads/main/vendors/automed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automed-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.automed.tech/auth/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automed/refs/heads/main/security/automed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.automed.tech
coverage:
  checked: 2026-09-26
  detail: Automed's website provides login and registration pages but no public developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://www.automed.tech
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Automed provides an AI‑powered medication safety platform that combines smart dispensing, connected monitoring, and predictive insights to ensure patients take the right medication at the right time across home, hospital, and pharmacy settings. The solution offers closed‑loop verification, adherence visibility for care teams, and predictive analytics to close the gap between prescribed and actually taken medication.
layout: provider
modified: '2026-09-26'
name: Automed
nav: Providers
network: true
overview: Automed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, Medication, Adherence, and Platform.
random_paper: 3
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automed Domain Security
  slug: automed-domain-security
  summary_line: TLSv1.3 · HSTS
slug: automed
tags:
- Healthcare
- Artificial Intelligence
- Medication
- Adherence
- Platform
website: https://www.automed.tech
---
