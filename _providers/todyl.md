---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Todyl's External API is a path-versioned REST API served from https://api.todyl.com. Probing it unauthenticated returns Todyl's own JSON error envelope ({"error":{"code":"auth_missing_token","message"
  name: Todyl External API
  slug: todyl-external-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/todyl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.todyl.com/
- group: company
  title: ''
  type: Blog
  url: https://www.todyl.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.todyl.com/blog/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://www.todyl.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.todyl.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.todyl.com/request-pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.todyl.com/session/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.todyl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.todyl.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.todyl.com/system-description
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/todylcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/todyl
- group: design
  title: ''
  type: Conformance
  url: conformance/todyl-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/todyl-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/todyl-plans-pricing.yml
coverage:
  checked: '2026-08-30'
  detail: Todyl runs a live production REST API at api.todyl.com, but the host authenticates EVERY path — /openapi.json, /v1/openapi.json and /.well-known/* all return 401 auth_missing_token — and the API reference itself is published only inside the customer knowledge base at support.todyl.com, whose root serves a Next.js sign-in page marked noindex/nofollow, so an integrator cannot read the contract before buying.
  evidence:
  - status: 401
    url: https://api.todyl.com/openapi.json
  - status: 401
    url: https://api.todyl.com/v1/devices
  - status: 200
    url: https://support.todyl.com/
  - status: 404
    url: https://www.todyl.com/developers
  reason: customer-only-docs
  state: gated
created: '2026-08-30'
description: Todyl is a Denver, Colorado cybersecurity company that sells a single-agent, cloud-native security platform to managed service providers, solution providers and internal IT teams. The Todyl Security Platform consolidates modules that are usually bought separately — SASE (Secure Access Service Edge, delivered over Todyl's Secure Global Network), Endpoint Security (EDR/NGAV), a cloud-native SIEM, MXDR (24x7 managed extended detection and response with a human SOC), GRC (governance, risk and compliance), and Security Automation playbooks — behind one agent and one multi-tenant portal. Todyl operates a live production REST API at https://api.todyl.com (path-versioned at /v1) that partners use to enumerate devices, deployment groups and billing data across their tenants, and it integrates with PSA/RMM tooling such as Autotask and ConnectWise. Access is authenticated with an External API token pair issued inside the Todyl portal; the API reference itself is published only in the customer-authenticated
  knowledge base, so no public OpenAPI, reference page or developer portal exists at the time of this profile.
image: https://cdn.prod.website-files.com/6961173a0b3c0ce2c689dccc/696157d64c5080ff6aff85a5_todyl-logo.svg
layout: provider
modified: '2026-08-30'
name: Todyl
nav: Providers
network: true
overview: 'Todyl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Managed Service Providers, and SASE.


  Todyl''s developer surface includes engineering blog, support, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Todyl Plans Pricing
  plan_count: 0
  slug: todyl-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Todyl Rate Limits
  slug: todyl-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 23.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/todyl/refs/heads/main/screenshots/todyl-2026-09-02T163839.png
security:
- kind: authentication
  name: Todyl Authentication
  slug: todyl-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Todyl Domain Security
  slug: todyl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: todyl
tags:
- Company
- Cybersecurity
- Security
- Managed Service Providers
- SASE
- SIEM
- Endpoint Security
- Managed Detection and Response
- Governance Risk and Compliance
- Zero Trust
- Networking
website: https://www.todyl.com/
---
