---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-committee-on-statistical-methodology-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-committee-on-statistical-methodology-llms.txt
- group: company
  title: ''
  type: Website
  url: https://statspolicy.gov/FCSM/
- group: other
  title: ''
  type: Conference
  url: https://nces.ed.gov/FCSM/
- group: other
  title: ''
  type: Conference
  url: https://fcsmconf.org/
- group: operate
  title: ''
  type: Contact
  url: mailto:StatsPolicyGov@omb.eop.gov
coverage:
  checked: '2026-09-09'
  detail: FCSM is an OMB-chartered interagency methodology committee whose published output is PDF guidance (A Framework for Data Quality, the AI-Ready Extension); its site statspolicy.gov answers HTTP 200 with one identical 31,432-byte HTML shell for /openapi.json, /llms.txt and a nonsense control path alike, and every /.well-known/ path on statspolicy.gov, fcsm.gov and the legacy nces.ed.gov host returns 404.
  evidence:
  - status: 200
    url: https://statspolicy.gov/openapi.json
  - status: 200
    url: https://statspolicy.gov/this-path-does-not-exist-xyz123
  - status: 404
    url: https://statspolicy.gov/.well-known/api-catalog
  - status: 404
    url: https://fcsm.gov/.well-known/agent-card.json
  - status: 404
    url: https://nces.ed.gov/openapi.json
  - status: 200
    url: https://statspolicy.gov/integrations
  reason: not-a-software-company
  state: none
created: '2024-12-03'
description: 'The Federal Committee on Statistical Methodology (FCSM) is an interagency committee, chartered by the Office of Management and Budget and supported by the OMB Statistical Policy Office, dedicated to improving the quality of U.S. Federal statistics. FCSM publishes methodology guidance, standards and conference proceedings — including A Framework for Data Quality — and convenes subcommittees and an annual research and policy conference. It is a policy and methodology body, not a data publisher: it does not operate or document a public developer API, and the statistical data itself is published by its member agencies under their own domains.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-committee-on-statistical-methodology.png
layout: provider
modified: '2026-09-09'
name: Federal Committee on Statistical Methodology
nav: Providers
network: true
overview: Federal Committee on Statistical Methodology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Statistical Methodology, Statistics, Data Quality, and Government.
random_paper: 2
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Federal Committee On Statistical Methodology Domain Security
  slug: federal-committee-on-statistical-methodology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-committee-on-statistical-methodology
tags:
- Federal-Government
- Statistical Methodology
- Statistics
- Data Quality
- Government
website: https://statspolicy.gov/FCSM/
---
