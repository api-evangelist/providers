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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API providing geolocation, timezone, currency, connection, and security data for IPv4 and IPv6 addresses. Returns location coordinates, city, region, country, ISP, ASN, proxy/VPN/Tor detection, a
  name: ipbase IP Geolocation API
  slug: ipbase-ip-geolocation-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipbase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ipbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://ipbase.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/everapihq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everapi/
- group: commercial
  title: ''
  type: Pricing
  url: https://ipbase.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://ipbase.freshstatus.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/everapi
- group: commercial
  title: ''
  type: Plans
  url: plans/ipbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ipbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ipbase-finops.yml
created: '2026-06-13'
description: ipbase is an IP geolocation REST API providing accurate location, currency, timezone, connection type, proxy/VPN detection, and security threat data for any IPv4 or IPv6 address. Operated by Everapi GmbH, the API serves businesses needing programmatic IP address intelligence for fraud detection, content localization, and data-driven decisions.
finops:
- name: Ipbase Finops
  service_category: ''
  slug: ipbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ipbase.png
layout: provider
modified: '2026-06-13'
name: ipbase
nav: Providers
network: true
overview: 'ipbase publishes 1 API on the [APIs.io](https://apis.io/) network: IP Geolocation API. Tagged areas include IP Geolocation, IP Address, Geolocation, Security, and VPN Detection.


  ipbase''s developer surface includes documentation, pricing, and 9 more developer resources.'
plans:
- name: Ipbase Plans Pricing
  plan_count: 5
  slug: ipbase-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Ipbase Rate Limits
  slug: ipbase-rate-limits
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 32.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipbase/refs/heads/main/screenshots/ipbase-2026-06-20T183549.png
security:
- kind: domain-security
  name: Ipbase Domain Security
  slug: ipbase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ipbase
tags:
- IP Geolocation
- IP Address
- Geolocation
- Security
- VPN Detection
- Proxy Detection
- Timezone
- Currency
- ASN
- Threat Intelligence
website: https://ipbase.com
---
