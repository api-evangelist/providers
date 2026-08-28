---
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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profility.com/
- group: company
  title: ''
  type: About
  url: https://profility.com/about/
- group: other
  title: ''
  type: Products
  url: https://profility.com/products/
- group: company
  title: ''
  type: Blog
  url: https://profility.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://profility.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://profility.com/profility-privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://dashboard.profility.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/profility-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/profility-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profility-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Profility ships its post-acute care platform only as two ASP.NET customer login applications (dashboard.profility.com, ranking.profility.com) which return clean 404s on every OpenAPI, GraphQL, MCP and agent-card path, and the company publishes no developer portal, API reference, SDK or pricing page anywhere on profility.com.
  evidence:
  - status: 404
    url: https://dashboard.profility.com/openapi.json
  - status: 404
    url: https://dashboard.profility.com/swagger/v1/swagger.json
  - status: 404
    url: https://dashboard.profility.com/.well-known/agent-card.json
  - status: 404
    url: https://ranking.profility.com/openapi.json
  - status: 404
    url: https://ranking.profility.com/graphql
  - status: 202
    url: https://profility.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Profility, Inc. is a Boston-based healthcare technology company whose AI-powered platform supports collaboration and decision-making across the post-acute care continuum. Its cloud platform combines large historical patient datasets with predictive analytics to build personalized care-planning profiles, predict rehabilitation success and readmission risk across post-acute settings, and guide placement and referral decisions between hospitals, skilled nursing facilities, home health, behavioral health and dialysis providers. Its PReP Authorize product automates prior authorization and concurrent review for managed-care patients, covering managed-care contract intelligence, denial reduction and audit preparedness. Profility markets analytical reporting that scores post-acute providers and maps local market position for referral-pattern optimization. The company reports deployment across 500+ facilities. Profility ships its platform as an end-user web application; it publishes
  no public developer program, API reference or machine-readable specification.
layout: provider
modified: '2026-08-26'
name: Profility
nav: Providers
network: true
overview: 'Profility is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health IT, Post-Acute Care, Artificial Intelligence, and Predictive Analytics.


  Profility''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Profility Plans Pricing
  plan_count: 0
  slug: profility-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Profility Rate Limits
  slug: profility-rate-limits
score:
  band: minimal
  composite: 5.4
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Profility Domain Security
  slug: profility-domain-security
  summary_line: TLSv1.3 · DMARC
slug: profility
tags:
- Healthcare
- Health IT
- Post-Acute Care
- Artificial Intelligence
- Predictive Analytics
- Care Coordination
- Prior Authorization
- Revenue Cycle Management
website: https://profility.com/
---
