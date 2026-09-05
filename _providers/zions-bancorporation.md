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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zions-bancorporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zionsbancorporation.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zionsbank.com/business/treasury/treasury-internet-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zions-bancorporation
created: '2026-07-23'
description: 'Zions Bancorporation, National Association is a nationally chartered bank and bank holding company headquartered in Salt Lake City, Utah, with roughly $87 billion in total assets. It is a super-regional operating a single national bank charter across seven regional divisional brands - Zions Bank, Amegy Bank, California Bank & Trust, National Bank of Arizona, Nevada State Bank, Vectra Bank Colorado, and The Commerce Bank of Washington - serving consumers, small business, and commercial/treasury clients across the Western United States. On the open-finance front Zions runs NO public first-party developer API portal: developer.zionsbank.com and api.zionsbank.com do not resolve, and its business digital-banking surface (Treasury Internet Banking at treasurygateway.zionsbank.com) is credential-gated with no published API reference or downloadable OpenAPI. As a large depository institution it is subject to the CFPB Section 1033 Personal Financial Data Rights rule, but Zions has not
  published a first-party data-access API or a documented FDX-conformant endpoint; consumer-permissioned data sharing in practice reaches Zions through third-party aggregators (Plaid/MX/Finicity/Akoya) rather than a first-party API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Zions Bancorporation
nav: Providers
network: true
overview: 'Zions Bancorporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Super-Regional Bank, and Treasury Management.


  Zions Bancorporation''s developer surface includes documentation and 3 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Zions Bancorporation Domain Security
  slug: zions-bancorporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zions-bancorporation
tags:
- Financial-Services
- Banking
- United States
- Super-Regional Bank
- Treasury Management
- Open Finance
- Data Aggregation
website: https://www.zionsbancorporation.com/
---
