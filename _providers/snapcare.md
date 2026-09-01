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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://snapcare.com/
- group: company
  title: ''
  type: Blog
  url: https://snapcare.com/articles
- group: operate
  title: ''
  type: Support
  url: https://snapcare.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snapcare.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snapcare.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.snapcare.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snapcare-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snapcare-domain-security.yml
coverage:
  checked: '2026-08-28'
  detail: SnapCare sells Booker as a managed SaaS to healthcare organizations and publishes nothing for developers — no /developers or /api route, api.snapcare.com and docs.snapcare.com are NXDOMAIN, the GitHub org `snapcare` has zero public repositories, and app.snapcare.com (the Booker SPA) returns clean JSON 404s on every /.well-known path rather than any discovery document; a Fastly JavaScript bot challenge on the marketing origin additionally blocked reading the llms.txt SnapCare does serve.
  evidence:
  - status: 0
    url: https://api.snapcare.com/openapi.json
  - status: 404
    url: https://snapcare.com/.well-known/api-catalog
  - status: 404
    url: https://app.snapcare.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/snapcare/repos
  - status: 200
    url: https://snapcare.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: SnapCare is an Atlanta-based healthcare workforce company, founded in 2017 as SnapNurse and relaunched under the SnapCare name in 2023, that pairs a national clinician marketplace with Booker, its SaaS workforce platform for hospitals, post-acute facilities, agency suppliers and clinicians. Booker combines predictive scheduling against census and historical demand trends, real-time per-diem shift fulfillment, internal float-pool management, same-day pay, and escalation of unfilled shifts to approved contingent suppliers. SnapCare acquired predictive staffing analytics vendor Medecipher in 2024 and merged with the nurse community connectRN in April 2026, raising a Series A led by Suvretta Capital. SnapCare sells the platform to healthcare organizations rather than to developers; no public developer program, API reference, or machine-readable API contract was found on its public surface.
layout: provider
modified: '2026-08-28'
name: SnapCare
nav: Providers
network: true
overview: 'SnapCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Staffing, Workforce Management, and Scheduling.


  SnapCare''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Snapcare Plans Pricing
  plan_count: 0
  slug: snapcare-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Snapcare Rate Limits
  slug: snapcare-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Snapcare Domain Security
  slug: snapcare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: snapcare
tags:
- Company
- Healthcare
- Staffing
- Workforce Management
- Scheduling
- Marketplace
- Human Resources
- Nursing
website: https://snapcare.com/
---
