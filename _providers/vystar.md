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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.vystarcu.org/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vystar-credit-union
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vystar-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vystar-llms.txt
created: '2026-07-23'
description: 'VyStar Credit Union is a member-owned, not-for-profit financial cooperative headquartered in Jacksonville, Florida. Founded in 1952 as Jax Navy Federal Credit Union to serve military members at Naval Air Station Jacksonville and renamed VyStar in 2002, it is one of the largest credit unions in the United States, with roughly $14 billion in assets, more than 950,000 members, and approximately 80 branches across Florida and Georgia. It is state-chartered and federally insured by the NCUA. Like most US credit unions, VyStar publishes no public, first-party developer API program: there is no live developer portal, no downloadable OpenAPI or Swagger definition, and no documented first-party data-access API. Consumer-permissioned account data is shared with third parties through financial-data aggregators rather than a documented open API, and the United States has no single mandated open-banking contract. VyStar''s open-finance posture is therefore aggregator-mediated, with the
  emerging CFPB Section 1033 Personal Financial Data Rights rule as the relevant regulatory horizon.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T15:30:00Z'
name: VyStar Credit Union
nav: Providers
network: true
overview: VyStar Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Credit Union, United States, and Open Finance.
random_paper: 9
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Vystar Domain Security
  slug: vystar-domain-security
  summary_line: TLSv1.2 · DMARC
slug: vystar
tags:
- Financial-Services
- Banking
- Credit Union
- United States
- Open Finance
- Consumer Finance
- Data Aggregation
website: https://www.vystarcu.org/
---
