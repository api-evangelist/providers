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
api_count: 1
apis:
- description: API for accessing patient data index, providing health record information.
  name: Patientdataindex (PDI)
  slug: patientdataindex-pdi
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ehalsomyndigheten/refs/heads/main/llms/ehalsomyndigheten-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ehalsomyndigheten-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ehalsomyndigheten/refs/heads/main/hosts/ehalsomyndigheten-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ehalsomyndigheten-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ehalsomyndigheten/refs/heads/main/vendors/ehalsomyndigheten-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ehalsomyndigheten-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.ehalsomyndigheten.se/om-ehalsomyndigheten/om-oss/register-och-databaser/
- group: company
  title: ''
  type: Newsroom
  url: https://www.ehalsomyndigheten.se/om-ehalsomyndigheten/om-oss/press/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ehalsomyndigheten.se/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ehalsomyndigheten
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ehalsomyndigheten/refs/heads/main/security/ehalsomyndigheten-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ehalsomyndigheten-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ehalsomyndigheten.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.ehalsomyndigheten.se/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: E-hälsomyndigheten, the Swedish eHealth Agency, is a governmental authority responsible for national digital health infrastructure, including services such as the National Drug List, Prescription Monitoring, and digital health records. It provides public information, guidelines, and APIs to support healthcare professionals, private individuals, and organizations in accessing health data, medication information, and digital health services across Sweden.
image: https://www.ehalsomyndigheten.se/logo.png
layout: provider
modified: '2026-10-12'
name: E-halsomyndigheten (Swedish eHealth Agency)
nav: Providers
network: true
overview: 'E-halsomyndigheten (Swedish eHealth Agency) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eHealth, Sweden, Government, and Digital Health.


  E-halsomyndigheten (Swedish eHealth Agency)''s developer surface includes signup flow, documentation, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ehalsomyndigheten Domain Security
  slug: ehalsomyndigheten-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ehalsomyndigheten
tags:
- Company
- eHealth
- Sweden
- Government
- Digital Health
website: https://www.ehalsomyndigheten.se/
---
