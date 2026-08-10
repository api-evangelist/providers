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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: A REST API that resolves IPv4/IPv6 addresses and Autonomous System Numbers to rich intelligence including geolocation, ISP/carrier details, company data, currency and time zone, and threat classificat
  name: IPregistry IP Geolocation and Threat Intelligence API
  slug: ipregistry-ip-geolocation-and-threat-intelligence-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ipregistry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipregistry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ipregistry.co
- group: docs
  title: ''
  type: Documentation
  url: https://ipregistry.co/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ipregistry
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ipregistry
- group: company
  title: ''
  type: Blog
  url: https://ipregistry.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ipregistry.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://ipregistry.co/status
- group: other
  title: ''
  type: X
  url: https://twitter.com/ipregistryco
- group: operate
  title: ''
  type: ChangeLog
  url: https://ipregistry.co/changelog
- group: commercial
  title: ''
  type: Plans
  url: plans/ipregistry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ipregistry-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ipregistry-finops.yml
- group: start
  title: ''
  type: BlogIndex
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ipregistry-context.jsonld
created: '2026-06-12'
description: IPregistry provides a fast, reliable IP geolocation and threat intelligence REST API for looking up information associated with IPv4 or IPv6 addresses and Autonomous Systems (AS). The API returns location data, connection details, company and carrier information, time zone, currency, and comprehensive security threat assessments from over 220 OSINT threat feeds. It supports single and batch IP lookups, user-agent parsing, ASN queries, and optional EU-region routing for data residency compliance. All lookups are authenticated via API key and billed against prepaid credits that never expire.
finops:
- name: Ipregistry Finops
  service_category: ''
  slug: ipregistry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ipregistry.png
jsonld:
- class_count: 4
  name: Ipregistry Context
  property_count: 76
  slug: ipregistry-context
layout: provider
modified: '2026-06-12'
name: IPregistry
nav: Providers
network: true
overview: 'IPregistry publishes 1 API on the [APIs.io](https://apis.io/) network: IP Geolocation and Threat Intelligence API. Tagged areas include IP Geolocation, Threat Intelligence, IP Address, ASN, and Carrier.


  The IPregistry catalog on APIs.io includes 1 JSON-LD context.


  IPregistry''s developer surface includes documentation, engineering blog, pricing, changelog, and 12 more developer resources.'
plans:
- name: Ipregistry Plans Pricing
  plan_count: 6
  slug: ipregistry-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Ipregistry Rate Limits
  slug: ipregistry-rate-limits
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 36.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipregistry/refs/heads/main/screenshots/ipregistry-2026-06-20T183556.png
security:
- kind: domain-security
  name: Ipregistry Domain Security
  slug: ipregistry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ipregistry Vulnerability Disclosure
  slug: ipregistry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ipregistry
tags:
- IP Geolocation
- Threat Intelligence
- IP Address
- ASN
- Carrier
- Security
- Location Data
- User-Agent Parsing
- VPN Detection
- Proxy Detection
website: https://ipregistry.co
---
