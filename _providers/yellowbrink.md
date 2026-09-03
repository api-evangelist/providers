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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yellowbrink-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yellowbrink-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.yellowbrink.com/
coverage:
  checked: '2026-09-02'
  detail: YellowBrink is a community platform, not a software vendor — its site is a white-labelled Innoloft LoftOS single-page app that answers 200 with the identical 12,016-byte HTML shell for every path probed (including /openapi.json and every /.well-known/*), and the only API behind it, api.innoloft.com, belongs to Innoloft and returns 401 anonymously.
  evidence:
  - status: 200
    url: https://www.yellowbrink.com/openapi.json
  - status: 200
    url: https://www.yellowbrink.com/.well-known/agent-card.json
  - status: 401
    url: https://api.innoloft.com/openapi.json
  - status: 200
    url: https://www.yellowbrink.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: YellowBrink is a Netherlands-based, vendor-neutral community platform for open health data, founded by Jan de Lange and Bouwe Koopal to connect healthcare professionals, vendors, researchers and policymakers working with open standards such as openEHR, HL7 FHIR, OMOP and SNOMED CT. The name pairs the Yellow Pages — showing who builds what — with "brink", the Dutch word for the village square where a community gathers. It runs weekly webinars in cooperation with openEHR NL, country and topic special-interest groups, and discussion and co-creation rooms, hosts "The Brink" partner and meeting area at the EHRCON26 conference in Amsterdam, and is developing a postdoctoral European Master of Data Availability programme with European universities and hospital systems. The platform is a white-labelled Innoloft LoftOS tenant; YellowBrink itself publishes no public API, SDK or developer program.
layout: provider
modified: '2026-09-02'
name: YellowBrink
nav: Providers
network: true
overview: YellowBrink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Health Data, openEHR, and Interoperability.
random_paper: 5
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Yellowbrink Domain Security
  slug: yellowbrink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: yellowbrink
tags:
- Company
- Health Care
- Health Data
- openEHR
- Interoperability
- Standards
- Community
- Education
- Events
- Netherlands
website: https://www.yellowbrink.com/
---
