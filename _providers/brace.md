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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brace.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brace-ai
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/brace_stock/
- group: operate
  title: ''
  type: PressRelease
  url: https://press.stavvy.com/stavvy-acquires-brace
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brace-lifecycle.yml
coverage:
  checked: '2026-08-08'
  detail: Brace was acquired by Stavvy (announced 1 August 2023) and fully absorbed — brace.ai now 301-redirects every path, including /robots.txt, to stavvy.com/mortgage-servicing-solution, and docs., developer., api. and app.brace.ai have all been removed from DNS, so there is no Brace-branded surface left to read.
  evidence:
  - status: 301
    url: https://brace.ai/
  - status: 404
    url: https://brace.ai/openapi.json
  - status: 404
    url: https://brace.ai/llms.txt
  - status: 0
    url: https://docs.brace.ai/
  - status: 0
    url: https://api.brace.ai/
  - status: 200
    url: https://press.stavvy.com/stavvy-acquires-brace
  reason: defunct
  state: none
created: '2026-08-08'
description: 'Brace (Brace Software, Inc., brace.ai) was a Culver City, California fintech founded in 2017 by Eric Rachmel and Amr Mohamed that rebuilt mortgage default servicing as software. Its Default Management Platform covered the end-to-end loss-mitigation lifecycle for servicers, lenders and investors — a homeowner engagement portal, a centralized responsive application, a rules and underwriting engine, document classification and data extraction, and event-driven communications and reporting — replacing the paper-based, inconsistent default workflows used by top U.S. mortgage servicers. The company raised a reported ~$30M and was acquired by Boston-based mortgage technology firm Stavvy, announced 1 August 2023, folding Brace''s loss-mitigation platform into Stavvy''s eClosing, digital notarization and foreclosure suite. Brace does not survive as an independent surface: brace.ai now 301-redirects every path to stavvy.com/mortgage-servicing-solution, and no docs., developer., api.
  or app. subdomain resolves in DNS. No public API, developer portal, machine-readable specification or SDK was ever published under the Brace brand — the Wayback CDX index for brace.ai carries no developer or API path — so this profile records identity and exit rather than an API surface.'
layout: provider
modified: '2026-08-08'
name: Brace
nav: Providers
network: true
overview: Brace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Mortgage Servicing, Loss Mitigation, and Default Servicing.
random_paper: 5
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Brace Domain Security
  slug: brace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brace
tags:
- Company
- Mortgage
- Mortgage Servicing
- Loss Mitigation
- Default Servicing
- Financial-Services
- Fintech
- Real-Estate
- Workflow-Automation
- Acquired
website: https://brace.ai/
---
