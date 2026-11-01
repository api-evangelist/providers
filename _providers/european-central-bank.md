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
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/european-central-bank/well-known/european-central-bank-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/european-central-bank-www-security.txt
- group: agent
  href: https://artifacts.apis.io/european-central-bank/well-known/european-central-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/european-central-bank-well-known.yml
- group: other
  href: https://artifacts.apis.io/european-central-bank/hosts/european-central-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/european-central-bank-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://data.ecb.europa.eu/privacy-statement-ecb-data-portal
- group: company
  title: ''
  type: Newsroom
  url: https://www.ecb.europa.eu/press/calendars/statscal/html/index.en.html
- group: start
  title: ''
  type: Login
  url: https://data.ecb.europa.eu/user/login
- group: auth
  href: https://artifacts.apis.io/european-central-bank/security/european-central-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/european-central-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.ecb.europa.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://data.ecb.europa.eu/help/api/overview
- group: company
  title: ''
  type: Blog
  url: https://data.ecb.europa.eu/ecb-data-blog
- group: operate
  title: ''
  type: Support
  url: https://data.ecb.europa.eu/help/api/overview
coverage:
  checked: '2026-10-27'
  detail: The ECB Data Portal provides HTML documentation but no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://data.ecb.europa.eu/help/api/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: The European Central Bank (ECB) Data Portal provides access to a wide range of statistical data, economic indicators, and financial datasets published by the ECB. It offers APIs and downloadable resources for researchers, analysts, and developers to integrate official euro area data into applications, dashboards, and analytical tools. The portal includes macroeconomic statistics, monetary policy information, and market data, supporting transparency and data-driven decision making.
layout: provider
modified: '2026-10-27'
name: ECB Data Portal
nav: Providers
network: true
overview: 'ECB Data Portal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Banking, European Union, Economic Data, and Statistics.


  ECB Data Portal''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: European Central Bank Domain Security
  slug: european-central-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: european-central-bank
tags:
- Finance
- Banking
- European Union
- Economic Data
- Statistics
- Open Data
website: https://data.ecb.europa.eu/
---
