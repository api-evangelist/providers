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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/naturstrom/llms/naturstrom-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/naturstrom-llms.txt
- group: other
  href: https://artifacts.apis.io/naturstrom/hosts/naturstrom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/naturstrom-hosts.yml
- group: auth
  href: https://artifacts.apis.io/naturstrom/security/naturstrom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/naturstrom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://naturstrom.de/
- group: company
  title: ''
  type: Blog
  url: https://www.naturstrom.de/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.naturstrom.de/service/kontakt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.naturstrom.de/datenschutz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.naturstrom.de/agb
coverage:
  checked: '2026-10-28'
  detail: Attempts to fetch common OpenAPI and GraphQL endpoints returned 404, indicating no machine‑readable specification is published.
  evidence:
  - status: 404
    url: https://www.naturstrom.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Naturstrom AG is a German energy provider that supplies 100 % renewable electricity, green gas, heating solutions and e‑mobility services to residential and business customers. The company emphasizes sustainability, offers transparent tariffs, and operates under the corporate headquarters in Düsseldorf. It provides customer portals for account management and publishes information about its services, pricing, terms, and privacy policies on its public website.
image: https://www.naturstrom.de/Privatkunden/_processed_/f/0/csm_naturstrom_privatkunden_strom_header_a77030f48b.jpg
layout: provider
modified: '2026-10-28'
name: Naturstrom
nav: Providers
network: true
overview: 'Naturstrom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Renewable, Electricity, Germany, and Sustainability.


  Naturstrom''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 15
scopes:
- name: Naturstrom Scopes
  scope_count: 0
  slug: naturstrom-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Naturstrom Authentication
  slug: naturstrom-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Naturstrom Domain Security
  slug: naturstrom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: naturstrom
tags:
- Energy
- Renewable
- Electricity
- Germany
- Sustainability
- Company
website: https://naturstrom.de/
---
