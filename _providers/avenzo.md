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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation for Avenzo Therapeutics (no machine‑readable spec found)
  name: Avenzo Therapeutics API
  slug: avenzo-therapeutics-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avenzo/refs/heads/main/conformance/avenzo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avenzo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avenzo/refs/heads/main/llms/avenzo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avenzo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avenzo/refs/heads/main/hosts/avenzo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avenzo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avenzo/refs/heads/main/vendors/avenzo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avenzo-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://avenzotx.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avenzo/refs/heads/main/security/avenzo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avenzo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avenzotx.com/
- group: company
  title: ''
  type: About
  url: https://avenzotx.com/about-us/
- group: docs
  title: ''
  type: Documentation
  url: https://avenzotx.com/pipeline-and-science/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avenzotx.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avenzotx.com/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://forgeglobal.com/avenzo_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Avenzo Therapeutics is a biotechnology company focused on developing next‑generation oncology therapies. The firm aims to transform cancer treatment through innovative drug development, targeting solid tumors with validated targets. It maintains a pipeline of clinical trials and scientific research, and engages investors and partners to advance its mission.
image: https://avenzotx.com/wp-content/uploads/avenzo-facebook-card-scaled.jpg
layout: provider
modified: '2026-09-26'
name: Avenzo Therapeutics
nav: Providers
network: true
overview: 'Avenzo Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Oncology, Therapeutics, Clinical Trials, and Innovation.


  Avenzo Therapeutics'' developer surface includes documentation and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avenzo Domain Security
  slug: avenzo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avenzo
tags:
- Biotechnology
- Oncology
- Therapeutics
- Clinical Trials
- Innovation
website: https://avenzotx.com/
---
