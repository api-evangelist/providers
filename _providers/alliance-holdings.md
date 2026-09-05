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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alliance-holdings-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alliance-holdings-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.arlp.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.arlp.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arlp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arlp.com/privacy-statement/
coverage:
  checked: '2026-09-04'
  detail: Alliance Holdings GP, L.P. was absorbed into Alliance Resource Partners in the 2018 simplification transaction and its own host ahgp.com no longer resolves (NXDOMAIN on the apex, certificate-name mismatch on www), so the only surface left to probe is the successor's twelve-page WordPress corporate site at www.arlp.com — which has no developer section, returns 404 for /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and every /.well-known/ path, and whose full Yoast page sitemap lists no documentation, reference or portal page at all.
  evidence:
  - status: 404
    url: https://www.arlp.com/openapi.json
  - status: 404
    url: https://www.arlp.com/.well-known/api-catalog
  - status: 200
    url: https://www.arlp.com/page-sitemap.xml
  - status: 0
    url: https://ahgp.com
  reason: defunct
  state: none
created: '2026-03-24'
description: 'Alliance Holdings GP, L.P. (AHGP) was a limited partnership formed to own and control Alliance Resource Management GP, LLC, the managing general partner of Alliance Resource Partners, L.P. (ARLP), the second largest coal producer in the eastern United States. AHGP held a general partner interest, incentive distribution rights, and a direct stake in ARLP common units. In 2018 AHGP was absorbed into ARLP in a simplification transaction and ceased to exist as a separate public entity. ARLP (NASDAQ: ARLP) continues as a diversified energy company earning income from coal production and from coal, oil and gas mineral royalties. Alliance Holdings never maintained a public developer API program and neither does the surviving entity. The legacy ahgp.com host no longer resolves and alliancecoal.com redirects to www.arlp.com; probes on 2026-09-04 of arlp.com, www.arlp.com and investor.arlp.com found no OpenAPI, GraphQL, AsyncAPI, gRPC, WSDL, MCP, agent card, or served /.well-known/ document.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alliance-holdings.png
layout: provider
modified: '2026-09-04'
name: Alliance Holdings
nav: Providers
network: true
overview: Alliance Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Coal, Mining, Natural Resources, and Financial-Services.
random_paper: 4
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/alliance-holdings/refs/heads/main/screenshots/alliance-holdings-2026-07-25T195655.png
security:
- kind: domain-security
  name: Alliance Holdings Domain Security
  slug: alliance-holdings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alliance-holdings
tags:
- Energy
- Coal
- Mining
- Natural Resources
- Financial-Services
- Holding Company
website: https://www.arlp.com
---
