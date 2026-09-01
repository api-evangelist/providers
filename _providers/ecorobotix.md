---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The authenticated REST API behind the Ecorobotix cloud portal at portal.ecorobotix.cloud, which customers use to manage ARA sprayer fleets, treatment jobs and field data. The service is a Django REST '
  name: Ecorobotix Portal API
  slug: ecorobotix-portal-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecorobotix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecorobotix.com/en-us/
- group: company
  title: ''
  type: Blog
  url: https://press.ecorobotix.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://press.ecorobotix.com/rss
- group: operate
  title: ''
  type: Support
  url: https://ecorobotix.com/en-us/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecorobotix.com/wp-content/uploads/2025/09/2025-09-01-Ecorobotix_General_Privacy_Policy_ENG-2.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecorobotix.com/wp-content/uploads/2025/09/2025-09-01-Ecorobotix_End-User-Agreement_ENG.pdf
- group: start
  title: ''
  type: Login
  url: https://portal.ecorobotix.cloud/auth/login/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ecorobotix-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ecorobotix-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ecorobotix-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ecorobotix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ecorobotix-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Ecorobotix runs a real Django REST Framework API with a live drf-spectacular OpenAPI endpoint at portal.ecorobotix.cloud/api/schema/, but it returns HTTP 401 "Authentication credentials were not provided." to anonymous clients and every other /api/ path 302-redirects to the customer portal login, so the specification exists and is simply never published outside a machine-owner account.
  evidence:
  - status: 401
    url: https://portal.ecorobotix.cloud/api/schema/
  - status: 401
    url: https://portal.ecorobotix.cloud/api/schema/swagger-ui/
  - status: 302
    url: https://portal.ecorobotix.cloud/api/
  - status: 503
    url: https://api.ecorobotix.cloud/openapi.json
  - status: 404
    url: https://ecorobotix.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-12'
description: Ecorobotix SA is a Swiss agricultural technology company founded in 2011 and headquartered in Yverdon-les-Bains, Switzerland, building AI-driven ultra-high-precision (UHP) crop-care equipment. Its flagship ARA smart sprayer combines Plant-by-Plant AI detection with UHP-Spray-Technology to scan a field, classify crops versus weeds in under 250 milliseconds, and place treatment on a roughly six-by-six centimetre target, cutting herbicide and plant-protection input volumes by up to 95 percent compared with broadcast spraying. The product family spans the ARA620 and ARA595 UHP sprayers for row and vegetable crops, the ALBA UHP sprayer for turf, and a library of crop-specific algorithms for broccoli, carrots, onions and chicory. More than 1,000 ARA units have been deployed across Europe, the United Kingdom, North America, South America and Australia/New Zealand. Machine telemetry, treatment maps and fleet data are delivered to customers through the Ecorobotix cloud portal, which
  is backed by an authenticated REST API; that API is not offered as a public developer program.
image: https://ecorobotix.com/wp-content/uploads/2025/03/favicon-96x96-1.png
layout: provider
modified: '2026-08-12'
name: Ecorobotix
nav: Providers
network: true
overview: 'Ecorobotix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Precision Agriculture, and Robotics.


  Ecorobotix''s developer surface includes engineering blog, support, authentication, and 10 more developer resources.'
plans:
- name: Ecorobotix Plans Pricing
  plan_count: 0
  slug: ecorobotix-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Ecorobotix Rate Limits
  slug: ecorobotix-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ecorobotix Authentication
  slug: ecorobotix-authentication
  summary_line: session/unknown · 0 schemes
- kind: domain-security
  name: Ecorobotix Domain Security
  slug: ecorobotix-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ecorobotix
tags:
- Company
- Agriculture
- AgTech
- Precision Agriculture
- Robotics
- Artificial Intelligence
- Computer-Vision
- Machine-Learning
- Sustainability
- Farm Equipment
- Switzerland
- IoT
website: https://ecorobotix.com/en-us/
---
