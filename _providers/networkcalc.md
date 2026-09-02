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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Networkcalc Agentic Access
  operation_count: 6
  slug: networkcalc-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Binary, decimal, and hexadecimal conversions.
  name: NetworkCalc Binary Converter API
  slug: networkcalc-binary-converter-api
- description: DNS lookups and record queries.
  name: NetworkCalc DNS API
  slug: networkcalc-dns-api
- description: Encoding and decoding helpers.
  name: NetworkCalc Encoder API
  slug: networkcalc-encoder-api
- description: TLS/SSL certificate and security utilities.
  name: NetworkCalc Security API
  slug: networkcalc-security-api
- description: IPv4 and IPv6 subnet calculations.
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/networkcalc-agentic-access.yml
- group: auth
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
- name: Networkcalc Finops
  service_category: API
  slug: networkcalc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/networkcalc.png
layout: provider
modified: '2026-05-19'
name: NetworkCalc
nav: Providers
network: true
overview: 'NetworkCalc publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Binary Converter API, DNS API, Encoder API, and 2 more. Tagged areas include Networking, DNS, Security, Subnetting, and Domains.


  NetworkCalc''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Networkcalc Plans Pricing
  plan_count: 3
  slug: networkcalc-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Networkcalc Rate Limits
  slug: networkcalc-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
