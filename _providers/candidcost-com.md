---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CandidCost provides cost estimation APIs.
  name: CandidCost API
  slug: candidcost-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/candidcost-com/llms/candidcost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/candidcost-com-llms.txt
- group: other
  href: https://artifacts.apis.io/candidcost-com/hosts/candidcost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/candidcost-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/candidcost-com/vendors/candidcost-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/candidcost-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://candidcost.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candidcost.com/privacy
- group: auth
  href: https://artifacts.apis.io/candidcost-com/security/candidcost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/candidcost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://candidcost.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing documented API endpoints.
  evidence:
  - status: 200
    url: https://candidcost.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CandidCost provides free homebuying tools built on public U.S. government data, offering transparent cost calculations, fee fairness checks, and qualification assistance. All numbers are sourced, no lender referrals, and user information is never sold. The service is owned by Vaspera Capital, an AI product studio.
layout: provider
modified: '2026-11-04'
name: CandidCost
nav: Providers
network: true
overview: CandidCost is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Home Buying, Real Estate, Finance, Data, and Transparency.
random_paper: 0
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Candidcost Com Domain Security
  slug: candidcost-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: candidcost-com
tags:
- Home Buying
- Real Estate
- Finance
- Data
- Transparency
website: https://candidcost.com/
---
