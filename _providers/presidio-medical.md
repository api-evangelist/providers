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
  url: security/presidio-medical-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/presidio-medical-llms.txt
- group: company
  title: ''
  type: Website
  url: https://presidiomedical.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/presidio-medical-inc
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/presidio-medical_stock/
coverage:
  checked: '2026-08-05'
  detail: Presidio Medical manufactures an implantable ultra-low-frequency spinal cord stimulator and has never run a developer program; on top of that its corporate WordPress site went offline sometime after the Internet Archive's last 200 capture on 2026-06-07 and now returns a WP Engine "Site Not Configured" HTTP 404 on every path including the root and a control path, while no api/developer/docs/portal subdomain resolves at all.
  evidence:
  - status: 404
    url: https://presidiomedical.com/
  - status: 404
    url: https://presidiomedical.com/openapi.json
  - status: 404
    url: https://presidiomedical.com/.well-known/agent-card.json
  - status: 404
    url: https://presidiomedical.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Presidio Medical is a privately held, clinical-stage medical device company headquartered in South San Francisco, California, founded in 2017 by Kenneth Wu and led by CEO and Chairman Michael Onuscheck. It is developing an implantable Ultra Low Frequency (ULF) neuromodulation platform intended to treat diseases of undesired neural activity, with a first indication in chronic nociceptive low back pain. The therapy delivers ultra low frequency current through an epidural spinal cord stimulation (SCS) lead to reversibly inhibit pain-signaling neurons via sodium channel inactivation, positioned as a non-opioid alternative to conventional SCS. The company raised a $72M Series C in 2023 led by Deerfield Management with Invus Opportunities, Action Potential Venture Capital and ShangBay Capital, and received FDA IDE approval for the global pivotal FULFILL randomized controlled trial in the United States and Australia. Presidio Medical sells an implantable medical device, not software;
  it has never operated a developer program, public API, SDK or machine-readable API contract. As of 2026-08-05 its corporate WordPress site at presidiomedical.com is offline, returning a WP Engine "Site Not Configured" HTTP 404 on every path including the root.
layout: provider
modified: '2026-08-05'
name: Presidio Medical
nav: Providers
network: true
overview: Presidio Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Neuromodulation, Neurotechnology, and Spinal Cord Stimulation.
random_paper: 10
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Presidio Medical Domain Security
  slug: presidio-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: presidio-medical
tags:
- Company
- Medical Devices
- Neuromodulation
- Neurotechnology
- Spinal Cord Stimulation
- Chronic Pain
- Implantable Devices
- Clinical Stage
- Healthcare
- Life Sciences
website: https://presidiomedical.com/
---
