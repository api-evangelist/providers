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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: DNS Coffee collects, analyzes, and archives changes to root zone files provided by various top-level domains (TLDs), offering one of the most comprehensive views of the current state of the Domain Nam
  name: DNS Coffee API
  slug: dns-coffee
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dns-coffee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dns-coffee-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.dns.coffee/doc/
- group: company
  title: ''
  type: Website
  url: https://dns.coffee/
- group: company
  title: ''
  type: About
  url: https://dns.coffee/about
created: '2025-02-09'
description: DNS Coffee collects, analyzes, and archives changes to root zone files provided by various top-level domains (TLDs), offering one of the most comprehensive views of the current state of the Domain Name System (DNS). By continuously tracking these changes, DNS Coffee uncovers valuable trends over time, making it a powerful resource for analysis and research. What began in 2011 with just 4 zones has grown into a robust platform that now processes data from over 1,200 zones daily.
finops:
- name: Dns Coffee Finops
  service_category: API
  slug: dns-coffee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dns-coffee.png
layout: provider
modified: '2026-04-28'
name: DNS Coffee
nav: Providers
network: true
overview: 'DNS Coffee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DNS, Domain Names, and Domains.


  DNS Coffee''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Dns Coffee Plans Pricing
  plan_count: 3
  slug: dns-coffee-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Dns Coffee Rate Limits
  slug: dns-coffee-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 20.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dns-coffee/refs/heads/main/screenshots/dns-coffee-2026-06-20T180101.png
security:
- kind: domain-security
  name: Dns Coffee Domain Security
  slug: dns-coffee-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dns Coffee Vulnerability Disclosure
  slug: dns-coffee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dns-coffee
tags:
- DNS
- Domain Names
- Domains
website: https://dns.coffee/
---
