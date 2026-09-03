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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Charles Proxy is a cross-platform desktop HTTP proxy and monitor that sits between client applications and the Internet to capture, inspect, and modify traffic. It supports SSL proxying with certifica
  name: Charles Proxy
  slug: charles-proxy
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charles-proxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.charlesproxy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.charlesproxy.com/documentation/
- group: other
  title: ''
  type: Download
  url: https://www.charlesproxy.com/download/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.charlesproxy.com/buy/
- group: operate
  title: ''
  type: Support
  url: https://www.charlesproxy.com/documentation/faqs/
- group: design
  title: ''
  type: LatestVersion
  url: https://www.charlesproxy.com/latest-release/download.do
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.charlesproxy.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.charlesproxy.com/news/
created: '2026-03-26'
description: Charles Proxy is an HTTP proxy and HTTP monitor that enables developers to view all HTTP and SSL/HTTPS traffic between their machine and the Internet, including requests, responses, and HTTP headers. It supports SSL proxying, bandwidth throttling, AJAX debugging, AMF inspection, breakpoints, content rewriting, and traffic recording for API debugging, testing, and development workflows on Windows, macOS, and Linux.
finops:
- name: Charles Proxy Finops
  service_category: API
  slug: charles-proxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charles-proxy.png
layout: provider
modified: '2026-04-23'
name: Charles Proxy
nav: Providers
network: true
overview: 'Charles Proxy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Debugging, API Testing, HTTP Debugging, HTTP Proxy, and SSL Proxying.


  Charles Proxy''s developer surface includes documentation, pricing, support, engineering blog, and 5 more developer resources.'
plans:
- name: Charles Proxy Plans Pricing
  plan_count: 3
  slug: charles-proxy-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Charles Proxy Rate Limits
  slug: charles-proxy-rate-limits
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charles-proxy/refs/heads/main/screenshots/charles-proxy-2026-06-20T174225.png
security:
- kind: domain-security
  name: Charles Proxy Domain Security
  slug: charles-proxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: charles-proxy
tags:
- API Debugging
- API Testing
- HTTP Debugging
- HTTP Proxy
- SSL Proxying
- Traffic Monitoring
- Web Development
website: https://www.charlesproxy.com
---
