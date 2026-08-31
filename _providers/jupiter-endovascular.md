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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupiter-endovascular-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jupiterendo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jupiterendo.com/privacy-policy/
coverage:
  checked: '2026-08-23'
  detail: Jupiter Endovascular is a pre-commercial clinical-stage manufacturer of a physical Class III catheter device (the Vertex Pulmonary Embolectomy System, in the SPIRARE I and II trials) — software is not the product, and the only web property is a SiteGround-hosted WordPress marketing site at jupiterendo.com that answers every path, including a deliberately bogus control path, with an identical 202 sg-captcha interstitial; there is no GitHub organization, no package on npm or PyPI, and the api/developer/docs subdomains all wildcard to a NameBright parking host rather than to any developer surface.
  evidence:
  - status: 202
    url: https://jupiterendo.com/openapi.json
  - status: 202
    url: https://jupiterendo.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/jupiter-endovascular
  - status: 404
    url: https://registry.npmjs.org/jupiter-endovascular
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: Jupiter Endovascular, Inc. is a privately held medical technology company headquartered in Menlo Park, California, developing Endoportal Control, a platform technology that fixes a flexibly navigated endoportal device into a stable state inside the vasculature so a catheter-based intervention can be delivered with the precision and control of direct surgical access. Its lead product is the Vertex Pulmonary Embolectomy System for acute pulmonary embolism, evaluated in the SPIRARE I first-in-human study (NCT06571760) and the FDA-approved SPIRARE II U.S. pivotal study. The company exited stealth with $21M and later closed an oversubscribed Series B surpassing its $40M target, led by Sonder Capital. Jupiter Endovascular is a pre-commercial clinical-stage device manufacturer and publishes no developer program, no API, and no machine-readable interface of any kind.
layout: provider
modified: '2026-08-23'
name: Jupiter Endovascular
nav: Providers
network: true
overview: Jupiter Endovascular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Healthcare, and Interventional Cardiology.
random_paper: 3
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
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Jupiter Endovascular Domain Security
  slug: jupiter-endovascular-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jupiter-endovascular
tags:
- Company
- Medical Devices
- Medical Technology
- Healthcare
- Interventional Cardiology
- Pulmonary Embolism
- Clinical Trials
website: https://jupiterendo.com/
---
