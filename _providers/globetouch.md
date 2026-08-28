---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/globetouch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airlinq.com/
- group: company
  title: ''
  type: About
  url: https://www.airlinq.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.airlinq.com/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.airlinq.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.airlinq.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airlinq.com/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://www.airlinq.com/faqs/
- group: other
  title: ''
  type: Glossary
  url: https://www.airlinq.com/glossary/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airlinq
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/airlinq
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/globetouch-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/globetouch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/globetouch-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: Globetouch rebranded to Airlinq in 2020 and its 17-page WordPress site markets Mobilinq as integrating with operator BSS/OSS "through a comprehensive API library", but there is no developer path off that claim — no docs, developer or api subdomain resolves in DNS, /developers, /docs, /api and /pricing all 404, and the only route to the API is the contact-sales form.
  evidence:
  - status: 200
    url: https://www.airlinq.com/mobilinq/
  - status: 404
    url: https://www.airlinq.com/developers/
  - status: 404
    url: https://www.airlinq.com/openapi.json
  - status: 404
    url: https://www.airlinq.com/.well-known/agent-card.json
  - status: 200
    url: https://www.airlinq.com/contact-us/
  reason: sales-gate
  state: gated
created: '2026-08-22'
description: Globetouch is a global mobile and IoT connectivity provider founded in 2010 and headquartered in San Ramon, California, which rebranded to Airlinq in February 2020 — globetouch.com now 301-redirects to www.airlinq.com. Its GConnect / CloudSIM heritage (physical SIM, soft SIM and eSIM provisioning with rule-engine-driven subscription-profile management for mobile operators and IoT enterprises) is carried forward in Mobilinq, the company's IoT connectivity and application management platform, alongside Autolinq for the connected-vehicle ecosystem, Utilinq for electric, gas and water utilities, and Marketlinq, an operator-branded private-5G and IoT marketplace and dashboard. Airlinq markets a "comprehensive API library" for BSS/OSS integration and data and voice plans "enabled via API", but as of August 2026 it publishes no public developer portal, API reference, or machine-readable specification of any kind; the only entry point is a contact-sales form.
image: https://www.airlinq.com/wp-content/uploads/2020/09/cropped-Untitled-design-1-192x192.png
layout: provider
modified: '2026-08-22'
name: Globetouch
nav: Providers
network: true
overview: 'Globetouch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Connectivity, eSIM, and SIM Management.


  Globetouch''s developer surface includes engineering blog, support, FAQ, and 11 more developer resources.'
plans:
- name: Globetouch Plans Pricing
  plan_count: 0
  slug: globetouch-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Globetouch Rate Limits
  slug: globetouch-rate-limits
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Globetouch Domain Security
  slug: globetouch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: globetouch
tags:
- Company
- IoT
- Connectivity
- eSIM
- SIM Management
- Telecommunications
- Mobile
- Connected Vehicles
- Utilities
- Roaming
website: https://www.airlinq.com/
---
