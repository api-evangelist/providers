---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Networkcalc Agentic Access
  operation_count: 6
  slug: networkcalc-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://networkcalc.com/api
  baseurl_source: declared
  description: Binary, decimal, and hexadecimal conversions.
  name: NetworkCalc Binary Converter API
  slug: networkcalc-binary-converter-api
- baseURL: https://networkcalc.com/api
  baseurl_source: declared
  description: DNS lookups and record queries.
  name: NetworkCalc DNS API
  slug: networkcalc-dns-api
- baseURL: https://networkcalc.com/api
  baseurl_source: declared
  description: Encoding and decoding helpers.
  name: NetworkCalc Encoder API
  slug: networkcalc-encoder-api
- baseURL: https://networkcalc.com/api
  baseurl_source: declared
  description: TLS/SSL certificate and security utilities.
  name: NetworkCalc Security API
  slug: networkcalc-security-api
- baseURL: https://networkcalc.com/api
  baseurl_source: declared
  description: IPv4 and IPv6 subnet calculations.
  name: NetworkCalc Subnet Calculator API
  slug: networkcalc-subnet-calculator-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NetworkCalc Binary Converter API
  slug: open-networkcalc-binary-converter-api
- collection_type: open
  name: NetworkCalc Binary Converter DNS API
  slug: open-networkcalc-dns-api
- collection_type: open
  name: NetworkCalc Binary Converter Encoder API
  slug: open-networkcalc-encoder-api
- collection_type: open
  name: NetworkCalc Binary Converter Security API
  slug: open-networkcalc-security-api
- collection_type: open
  name: NetworkCalc Binary Converter Subnet Calculator API
  slug: open-networkcalc-subnet-calculator-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/plans/networkcalc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/networkcalc-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/rate-limits/networkcalc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/networkcalc-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/finops/networkcalc-finops.yml
  title: ''
  type: FinOps
  url: finops/networkcalc-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://networkcalc.com/articles/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/agentic-access/networkcalc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/networkcalc-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/security/networkcalc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/networkcalc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://networkcalc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://networkcalc.com/api/docs
created: '2025-02-09'
description: NetworkCalc provides a free RESTful API platform for monitoring and managing business networks and domains. Public APIs include a subnet calculator, DNS tools, security tools, encoder, and binary converter, with additional authenticated APIs for alerts, authorization, domains, reports, and subnets.
finops:
- has_sources: false
  method: generated
  name: Networkcalc Finops
  primary_unit: ''
  service_category: API
  slug: networkcalc-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/networkcalc.png
layout: provider
modified: '2026-10-06'
name: NetworkCalc
nav: Providers
network: true
overview: 'NetworkCalc publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Binary Converter API, DNS API, Encoder API, and 2 more. Tagged areas include Networking, DNS, Security, Subnetting, and Domains.


  NetworkCalc''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Networkcalc Plans Pricing
  plan_count: 3
  slug: networkcalc-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Networkcalc Rate Limits
  slug: networkcalc-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 43.5
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 19.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/screenshots/networkcalc-2026-06-20T190215.png
security:
- kind: domain-security
  name: Networkcalc Domain Security
  slug: networkcalc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: networkcalc
tags:
- Networking
- DNS
- Security
- Subnetting
- Domains
- Calculator
website: https://networkcalc.com/
---
