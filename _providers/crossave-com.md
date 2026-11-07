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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Crossave provides e‑commerce aggregation APIs for price, shipping, duty and VAT calculations.
  name: Crossave API
  slug: crossave-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/crossave-com/llms/crossave-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crossave-com-llms.txt
- group: other
  href: https://artifacts.apis.io/crossave-com/hosts/crossave-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crossave-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crossave-com/vendors/crossave-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crossave-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crossave-com/security/crossave-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossave-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crossave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crossave.com/en/guide
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crossave.com/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crossave.com/en/termini
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: unreachable
    url: https://api.crossave.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Crossave is an e‑commerce platform that aggregates product listings from multiple online marketplaces, providing price, shipping, duty and VAT calculations for collectors and shoppers. It offers detailed guides on collectibles, import duties, and currency conversion, helping users compare costs across borders and make informed purchasing decisions.
image: https://crossave.com/static/og-card.png
layout: provider
modified: '2026-11-04'
name: Crossave
nav: Providers
network: true
overview: 'Crossave is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Collectibles, Price Comparison, import-duty, and International Shipping.


  Crossave''s developer surface includes documentation and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crossave Com Domain Security
  slug: crossave-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: crossave-com
tags:
- E-Commerce
- Collectibles
- Price Comparison
- import-duty
- International Shipping
website: https://crossave.com/
---
