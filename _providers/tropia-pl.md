---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.tropia.pl
  baseurl_source: declared
  description: Programistyczny dostęp do danych rejestrowych KRS, powiązań, sprawozdań finansowych, pomocy publicznej i kontraktów publicznych.
  name: tropia.pl API
  slug: tropia-pl-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/tropia-pl/conformance/tropia-pl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tropia-pl-conformance.yml
- group: other
  href: https://artifacts.apis.io/tropia-pl/overlays/tropia-pl-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/tropia-pl-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/tropia-pl/llms/tropia-pl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tropia-pl-llms.txt
- group: other
  href: https://artifacts.apis.io/tropia-pl/hosts/tropia-pl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tropia-pl-hosts.yml
- group: other
  href: https://artifacts.apis.io/tropia-pl/vendors/tropia-pl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tropia-pl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tropia-pl/security/tropia-pl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tropia-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tropia.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://tropia.pl/api/dokumentacja
- group: docs
  title: ''
  type: APIReference
  url: https://api.tropia.pl/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tropia.pl/regulamin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tropia.pl/polityka-prywatnosci
- group: commercial
  title: ''
  type: Pricing
  url: https://tropia.pl/premium/kup
created: '2026-10-20'
description: Tropia.pl provides programmatic access to Polish public register data, including company registration (KRS), relationships, financial statements, public aid, and public contracts. The API offers a prepaid model where request costs are returned in response headers, with free error responses for not‑found entities. Documentation and authentication details are available on the site, and the service targets developers needing comprehensive corporate data for analysis and compliance.
image: https://tropia.pl/og-home-v1.png
layout: provider
modified: '2026-10-20'
name: tropia-pl
nav: Providers
network: true
overview: 'tropia-pl is listed with 1 API on the [APIs.io](https://apis.io/) network: tropia.pl API. Tagged areas include Company, API, Data, Poland, and Finance.


  tropia-pl''s developer surface includes documentation, API reference, pricing, and 9 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 36.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tropia Pl Domain Security
  slug: tropia-pl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tropia-pl
tags:
- Company
- API
- Data
- Poland
- Finance
- Public-Records
website: https://tropia.pl/
---
