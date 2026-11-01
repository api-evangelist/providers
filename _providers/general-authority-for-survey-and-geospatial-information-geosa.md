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
  href: https://artifacts.apis.io/general-authority-for-survey-and-geospatial-information-geosa/hosts/general-authority-for-survey-and-geospatial-information-geosa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/general-authority-for-survey-and-geospatial-information-geosa-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geosa.gov.sa/ar/controlAndcompliance/Pages/terms.aspx
- group: start
  title: ''
  type: Sandbox
  url: https://geo-licensing.geosa.gov.sa/Landing/service/sandbox/ar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geosa.gov.sa/ar/controlAndcompliance/Pages/privacypolicy.aspx
- group: company
  title: ''
  type: Newsroom
  url: https://geosa.gov.sa/ar/mediacenter/news/Pages/default.aspx
- group: auth
  href: https://artifacts.apis.io/general-authority-for-survey-and-geospatial-information-geosa/security/general-authority-for-survey-and-geospatial-information-geosa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/general-authority-for-survey-and-geospatial-information-geosa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geosa.gov.sa/
- group: docs
  title: ''
  type: Documentation
  url: https://geosa.gov.sa/en/Pages/default.aspx
coverage:
  checked: '2026-10-26'
  detail: The provider's site returns SharePoint HTML for attempted OpenAPI URLs, indicating docs are rendered via JavaScript/SharePoint and no machine‑readable spec is available.
  evidence:
  - status: 200
    url: https://geosa.gov.sa/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: General Authority for Survey and Geospatial Information (GEOSA) is the Saudi Arabian governmental authority responsible for national surveying, mapping, and geospatial data management. It oversees the collection, analysis, and dissemination of geospatial information to support urban planning, infrastructure development, environmental monitoring, and public services. GEOSA provides geospatial datasets, standards, and services to government agencies, private sector partners, and researchers, fostering data-driven decision making across the Kingdom.
image: https://geosa.gov.sa/_layouts/15/geosa/dgadesign/img/Logo-geosa-rgb.png
layout: provider
modified: '2026-10-26'
name: General Authority for Survey and Geospatial Information (GEOSA)
nav: Providers
network: true
overview: 'General Authority for Survey and Geospatial Information (GEOSA) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Geospatial, Surveying, and Saudi-Arabia.


  General Authority for Survey and Geospatial Information (GEOSA)''s developer surface includes sandbox, documentation, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: General Authority For Survey And Geospatial Information Geosa Domain Security
  slug: general-authority-for-survey-and-geospatial-information-geosa-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: general-authority-for-survey-and-geospatial-information-geosa
tags:
- Company
- Government
- Geospatial
- Surveying
- Saudi-Arabia
website: https://geosa.gov.sa/
---
