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
  url: security/adona-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adonamed.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adona-medical
- group: other
  title: ''
  type: X
  url: https://x.com/adonamedical
created: '2026-08-06'
description: 'Adona Medical is a clinical-stage medical device company headquartered in Los Gatos, California, and a Shifamed portfolio company, developing an adjustable interatrial shunt with integrated bi-atrial pressure monitoring for patients with advanced heart failure. The implant uses nitinol shape-memory geometry so the shunt flow channel can be enlarged or reduced after implantation, allowing hemodynamic therapy to be re-titrated as a patient''s condition evolves. The company completed enrollment in its ATHENS-HF first-in-human study of the device. Adona Medical is a device and clinical company rather than a software vendor: it publishes no public developer program, API, SDK, or machine-readable specifications, and its device is investigational and not approved for sale.'
layout: provider
modified: '2026-08-06'
name: Adona Medical
nav: Providers
network: true
overview: Adona Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Healthcare, and Cardiovascular.
random_paper: 19
score:
  band: minimal
  composite: 2.9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/adona-medical/refs/heads/main/screenshots/adona-medical-2026-08-07T160923.png
security:
- kind: domain-security
  name: Adona Medical Domain Security
  slug: adona-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adona-medical
tags:
- Company
- Medical Devices
- Medical Technology
- Healthcare
- Cardiovascular
- Heart Failure
- Remote Patient Monitoring
- Clinical Stage
website: https://adonamed.com/
---
