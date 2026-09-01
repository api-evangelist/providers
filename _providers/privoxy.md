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
  scored_at: '2026-09-01'
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
random_paper: 3
rate_limits:
- limit_count: 5
  name: Privoxy Rate Limits
  slug: privoxy-rate-limits
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
