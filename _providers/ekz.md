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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/ekz/well-known/ekz-ekz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ekz-ekz-security.txt
- group: auth
  href: https://artifacts.apis.io/ekz/security/ekz-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ekz-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ekz/llms/ekz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ekz-llms.txt
- group: auth
  href: https://artifacts.apis.io/ekz/well-known/ekz-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ekz-www-security.txt
- group: auth
  href: https://artifacts.apis.io/ekz/well-known/ekz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ekz-security.txt
- group: agent
  href: https://artifacts.apis.io/ekz/well-known/ekz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ekz-well-known.yml
- group: other
  href: https://artifacts.apis.io/ekz/hosts/ekz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ekz-hosts.yml
- group: other
  href: https://artifacts.apis.io/ekz/vendors/ekz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ekz-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ekz.ch/client-setup
- group: start
  title: ''
  type: Login
  url: https://my.ekz.ch/website/login
- group: company
  title: ''
  type: Blog
  url: https://www.ekz.ch/fr/clients-professionnels/solutions-energetiques/blog/premiere-a-geneve.html
- group: auth
  href: https://artifacts.apis.io/ekz/security/ekz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ekz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ekz/security/ekz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ekz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ekz.ch/
coverage:
  checked: '2026-10-27'
  detail: No machine‑readable API specification was found; attempts to fetch OpenAPI files from api.ekz.ch returned errors.
  evidence:
  - status: error
    url: https://api.ekz.ch/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: EKZ (Elektrizitätswerk des Kantons Zürich) is a Swiss energy provider offering electricity, gas, solar, heat and e‑mobility solutions for residential and business customers. The company focuses on sustainable, climate‑friendly energy services, digital customer portals, and comprehensive support. EKZ operates nationwide in the Zurich canton, providing tariffs, installations, and energy consulting through its online platforms.
image: https://www.ekz.ch/.imaging/mte/ekz/open-graph/dam/ekz/bildpool/headerbilder_Inhaltseiten/Header_Inhaltseite_3200x1120_flat_single.jpg/jcr:content/Header_Inhaltseite_3200x1120_flat_single.jpg
layout: provider
modified: '2026-10-27'
name: EKZ
nav: Providers
network: true
overview: 'EKZ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Switzerland, Renewable, and CustomerPortal.


  EKZ''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ekz Domain Security
  slug: ekz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ekz Vulnerability Disclosure
  slug: ekz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ekz
tags:
- Energy
- Utilities
- Switzerland
- Renewable
- CustomerPortal
website: https://ekz.ch/
---
