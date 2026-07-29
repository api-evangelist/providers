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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Networkcalc Agentic Access
  operation_count: 6
  slug: networkcalc-agentic-access
  summary_line: 6 operations
api_count: 5
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
artifact_total: 10
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
random_paper: 75
rate_limits:
- limit_count: 5
  name: Networkcalc Rate Limits
  slug: networkcalc-rate-limits
score:
  band: thin
  composite: 33.0
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
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
