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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sevaro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sevaro.com/
- group: company
  title: ''
  type: Blog
  url: https://sevaro.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://sevaro.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://sevaro.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SevaroHealth
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sevaro.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sevaro-lifecycle.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sevaro.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sevaro.com/terms-and-conditions/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sevaro-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sevaro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sevaro-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sevaro-conformance.yml
coverage:
  checked: '2026-08-27'
  detail: 'Sevaro ships real software — the Synapse AI platform, Sevaro Video, Synapse for Providers, OneCall and a Triage mobile app, all listed as components on its own Atlassian Statuspage — but exclusively as an end-user clinical product sold to hospitals: api., developer. and docs.sevaro.com do not resolve in DNS, the Synapse AI product page markets "Integrations" and EMR connectivity without naming a single interface, and the only public host is a WordPress marketing site whose every /.well-known/ path 404s.'
  evidence:
  - status: 200
    url: https://sevaro.com/synapse-ai/
  - status: 404
    url: https://sevaro.com/.well-known/api-catalog
  - status: 404
    url: https://sevaro.com/openapi.json
  - status: 200
    url: https://sevaro.com/llms.txt
  - status: 200
    url: https://status.sevaro.com/api/v2/components.json
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: Sevaro (Sevaro Health) is a physician-led virtual neurology company that delivers telestroke, teleneurohospitalist rounding, remote EEG, neuro-intensive care, neuro-rehab and ambulatory neurology clinic services to hospitals across the United States. Its clinical delivery runs on Synapse AI, an integrated telemedicine platform that unifies EMR access, imaging, video, automated urgent call routing (Sevaro OneCall), AI stroke triage, ambient documentation and analytics, with companion Sevaro Video, Synapse for Providers, Synapse Analytics and Triage by Sevaro mobile surfaces. Sevaro sells to hospital systems through a demo-and-contract motion; it publishes no public developer portal, API reference, or machine-readable API contract of any kind.
image: https://sevaro.com/wp-content/uploads/2024/10/logo-hor-black.svg
layout: provider
modified: '2026-08-27'
name: Sevaro
nav: Providers
network: true
overview: 'Sevaro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telemedicine, and Teleneurology.


  Sevaro''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Sevaro Plans Pricing
  plan_count: 0
  slug: sevaro-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Sevaro Rate Limits
  slug: sevaro-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Sevaro Domain Security
  slug: sevaro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sevaro
tags:
- Company
- Health
- Healthcare
- Telemedicine
- Teleneurology
- Telestroke
- Neurology
- Artificial Intelligence
- Clinical Services
website: https://sevaro.com/
---
