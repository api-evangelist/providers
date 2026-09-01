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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supira-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://supiramedical.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supiramedical.com/privacy-statement-us/
- group: company
  title: ''
  type: Press
  url: https://supiramedical.com/category/press-releases/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/supira-medical
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/supira-medical_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supira-medical-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Supira Medical manufactures a catheter-based percutaneous heart pump, not software — no api/developer/docs/portal/status subdomain of supiramedical.com resolves in DNS at all, and the marketing site (a WordPress instance behind a SiteGround sg-captcha that answers HTTP 202 on every path) advertises no developer program, SDK, or integration.
  evidence:
  - status: 0
    url: https://api.supiramedical.com/
  - status: 202
    url: https://supiramedical.com/.well-known/api-catalog
  - status: 202
    url: https://supiramedical.com/
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: Supira Medical, Inc. is a clinical-stage medical device company in Los Gatos, California, and a portfolio company of the Shifamed medtech innovation hub. It is developing a next-generation percutaneous ventricular assist device (pVAD) — a catheter-based blood pump delivered through a 10 French (approximately 3.3 mm) sheath — intended to provide temporary cardiovascular hemodynamic support for patients undergoing high-risk percutaneous coronary intervention (HRPCI) and for patients in cardiogenic shock. The system has received FDA Breakthrough Device Designation and is in U.S. clinical study. The company is privately held and has raised capital through Series A–E financings led by investors including Cormorant Asset Management and The Capital Partnership. Supira Medical builds implantable and catheter-based hardware; it does not operate a public developer program, publish machine-readable API descriptions, or ship client libraries, and no public API surface was found for it.
layout: provider
modified: '2026-08-29'
name: Supira Medical
nav: Providers
network: true
overview: Supira Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiovascular, and Heart Pump.
random_paper: 17
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
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
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Supira Medical Domain Security
  slug: supira-medical-domain-security
  summary_line: TLSv1.3
slug: supira-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiovascular
- Heart Pump
- Clinical Stage
- Medical Technology
- Private Company
website: https://supiramedical.com/
---
