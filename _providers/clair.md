---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://getclair.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getclair
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getclair.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/66cded96fc6449eec10d942a/68c9b8fc52b7e5dcd7093db6_Privacy%20Policy.All%20(9.9.25).pdf
- group: operate
  title: ''
  type: Support
  url: https://getclair.com/knowledge
- group: build
  title: ''
  type: Packages
  url: packages/clair-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clair-packages.yml
- group: design
  title: ''
  type: Components
  url: components/clair-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clair-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clair-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clair-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clair-llms.txt
coverage:
  checked: '2026-08-09'
  detail: Clair runs a partner REST API for earned wage access but ships its API documentation only to contracted partners via getclair.com/partner ("contact sales@getclair.com / schedule a demo") — there is no developer subdomain at all (developer., developers., docs. and api-docs..getclair.com are all NXDOMAIN) and api.getclair.com answers every path, including a control path that cannot exist, with the same 403 Cloudflare page.
  evidence:
  - status: 403
    url: https://api.getclair.com/openapi.json
  - status: 403
    url: https://api.getclair.com/zzz-control-path-does-not-exist-9987
  - status: 404
    url: https://getclair.com/.well-known/agent-card.json
  - status: 404
    url: https://getclair.com/llms.txt
  - status: 200
    url: https://status.getclair.com/
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: Clair Inc is a New York-based financial technology company that provides free, compliant On-Demand Pay (earned wage access) as an embedded service inside the payroll, time-and-attendance and workforce-management platforms employees already use. Rather than selling a consumer app, Clair partners with platforms — Gusto Embedded Payroll, Check, 7shifts and others — and connects to them over a partner REST API that transmits employee, employment and attendance data, which Clair's underwriting engine uses to originate 0% APR earned wage advances through its FDIC-insured partner bank, Pathward N.A. Partners embed a Clair-hosted user experience (a WebView component, distributed for iOS as Swift packages) so employees can take an advance, review history and handle loan servicing without a separate login. Clair has raised roughly $218M in total capital, including a $23.2M Series B in May 2025.
image: https://avatars.githubusercontent.com/getclair
layout: provider
modified: '2026-08-09'
name: Clair
nav: Providers
network: true
overview: 'Clair is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, FinTech, Earned Wage Access, and On-Demand Pay.


  Clair''s developer surface includes support, changelog, and 10 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 15.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: domain-security
  name: Clair Domain Security
  slug: clair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clair
tags:
- Company
- Financial Services
- FinTech
- Earned Wage Access
- On-Demand Pay
- Payroll
- Embedded Finance
- Banking
- Human Resources
website: https://getclair.com/
---
