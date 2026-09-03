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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vantis-vascular-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vantisvascular.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vantisvascular.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vantis-vascular
coverage:
  checked: '2026-09-02'
  detail: Vantis Vascular manufactures single-use interventional catheters — the FDA 510(k)-cleared CrossFAST guide extension system and the in-development CrossSHOCK IVL system — and its only web property is a stock WordPress marketing site (the default "Hello world!" post is still published) whose every path, including a negative-control path that cannot exist, answers HTTP 202 behind a SiteGround captcha challenge; no api/developer/docs/portal/app/mcp subdomain resolves and no GitHub organization exists.
  evidence:
  - status: 202
    url: https://vantisvascular.com/
  - status: 202
    url: https://vantisvascular.com/.well-known/api-catalog
  - status: 202
    url: https://vantisvascular.com/.well-known/vantis-vascular-negative-control-7f3ab91c.json
  - status: 202
    url: https://vantisvascular.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/vantisvascular
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: Vantis Vascular, Inc. is a San Jose, California medical device company founded by interventional cardiologists to build performance-driven tools for complex vascular interventions. Its flagship CrossFAST Integrated Microcatheter Guide Extension System — a dual-monorail advanced delivery system cleared by the FDA under 510(k) and in commercial use since 2025 — is designed to improve deliverability and control in complex, calcified coronary and peripheral anatomy, and a CrossSHOCK intravascular lithotripsy (IVL) system is in development. The company has raised roughly $30M across seed and Series B rounds. It builds and sells physical single-use interventional devices to hospitals and interventionalists; it is not a software vendor and publishes no public API, SDK, developer portal or machine-readable contract of any kind.
layout: provider
modified: '2026-09-02'
name: Vantis Vascular
nav: Providers
network: true
overview: Vantis Vascular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health Care, Cardiovascular, and Interventional Cardiology.
random_paper: 17
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Vantis Vascular Domain Security
  slug: vantis-vascular-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vantis-vascular
tags:
- Company
- Medical Devices
- Health Care
- Cardiovascular
- Interventional Cardiology
- Vascular
- Catheters
- Medical Technology
website: https://vantisvascular.com/
---
