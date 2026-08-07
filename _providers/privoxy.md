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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Privoxy is a non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page content, and managing cookies.
  name: Privoxy
  slug: privoxy
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/privoxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.privoxy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.privoxy.org/user-manual/
- group: operate
  title: ''
  type: FAQ
  url: https://www.privoxy.org/faq/index.html
- group: docs
  title: ''
  type: Developer Manual
  url: https://www.privoxy.org/developer-manual/index.html
- group: build
  title: ''
  type: Source Code
  url: https://www.privoxy.org/gitweb/
- group: other
  title: ''
  type: Downloads
  url: https://sourceforge.net/projects/ijbswa/files/
- group: operate
  title: ''
  type: Support
  url: https://www.privoxy.org/user-manual/contact.html
created: '2026-03-27'
description: Privoxy is a non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page content, and managing cookies.
finops:
- name: Privoxy Finops
  service_category: API
  slug: privoxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/privoxy.png
layout: provider
modified: '2026-03-27'
name: Privoxy
nav: Providers
network: true
overview: 'Privoxy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Privacy Proxy and Proxy.


  Privoxy''s developer surface includes documentation, FAQ, support, and 5 more developer resources.'
plans:
- name: Privoxy Plans Pricing
  plan_count: 3
  slug: privoxy-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Privoxy Rate Limits
  slug: privoxy-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 18.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/privoxy/refs/heads/main/screenshots/privoxy-2026-06-20T192117.png
security:
- kind: domain-security
  name: Privoxy Domain Security
  slug: privoxy-domain-security
  summary_line: TLSv1.3
slug: privoxy
tags:
- Privacy Proxy
- Proxy
website: https://www.privoxy.org/
---
