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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rpc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rpc.net
- group: docs
  title: ''
  type: Documentation
  url: https://www.rpc.net/services
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.rpc.net
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rpc/refs/heads/main/vocabulary/rpc-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rpc/refs/heads/main/json-ld/rpc-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.rpc.net/feed/
created: '2025-01-01'
description: RPC, Inc. is an oilfield services company providing specialized well services to independent and major oil and gas companies engaged in the exploration, production, and development of oil and gas properties. Operating through subsidiaries including Cudd Energy Services, Patterson Services, Spinnaker Oilwell Services, and Thru Tubing Solutions, RPC offers pressure pumping, wireline, downhole tools, coiled tubing, cementing, snubbing, nitrogen services, well control, rental tools, and tubular services. RPC does not currently offer a public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rpc.png
json_schemas:
- name: RPC Well Service
  property_count: 11
  slug: rpc-well-service
jsonld:
- class_count: 0
  name: Rpc Context
  property_count: 15
  slug: rpc-context
layout: provider
modified: '2026-05-02'
name: RPC
nav: Providers
network: true
overview: 'RPC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Oilfield Services, Energy, Oil and Gas, Well Services, and Pressure Pumping.


  The RPC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RPC''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
press:
- date: '2026-05-25'
  title: 'AI Technologies in Legal Practice: Revolutionizing Law Firms'
  url: https://rpcgrowthstrategies.com/blogs/post/10-ai-assisted-legal-tech-vendors-delivering-reliable-productivity-to-law-firms/
- date: '2026-05-25'
  title: AI legal services & compliance experts
  url: https://www.rpclegal.com/expertise/solutions/artificial-intelligence/
- date: '2026-05-25'
  title: Preliminary Guidelines on the Use of Artificial Intelligence ...
  url: https://www.njcourts.gov/sites/default/files/notices/2024/01/n240125a.pdf
- date: '2026-05-25'
  title: 2024-April-Report-and-Recommendations-of-the-Task- ...
  url: https://nysba.org/wp-content/uploads/2022/03/2024-April-Report-and-Recommendations-of-the-Task-Force-on-Artificial-Intelligence.pdf?srsltid=AfmBOoq_4FkgcXCrzUgvch379a_WyTvhOtROIDI9lFhLCSDedX0DkDJv
- date: ''
  title: RPC launches Porter, its in-house AI assistant built to ...
  url: https://www.rpclegal.com/press-and-media/rpc-launches-porter
random_paper: 10
rules:
- effective_rule_count: 5
  extends: []
  name: RPC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rpc-jsonschema-spectral-rules
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 43.3
    catalog_earned_first_party: 0.0
    catalog_gap: 71.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rpc/refs/heads/main/screenshots/rpc-2026-06-20T193232.png
security:
- kind: domain-security
  name: Rpc Domain Security
  slug: rpc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rpc
tags:
- Oilfield Services
- Energy
- Oil and Gas
- Well Services
- Pressure Pumping
- Fortune 1000
website: https://www.rpc.net
---
