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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.sightdx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sightdiagnostics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sight-diagnostics
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sight-diagnostics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sight-diagnostics-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sight-diagnostics-domain-security.yml
coverage:
  checked: '2026-08-27'
  detail: Sight Diagnostics sells the OLO point-of-care hematology analyzer as an instrument plus a clinical-workflow service and runs a single-page Wix marketing site — sightdx.com has no developer, docs, API or integration section, no api./developer./docs. subdomain resolves, its GitHub org github.com/sightdiagnostics has zero public repositories, and the only machine surface on the domain is the /llms.txt and /_api/mcp pair that the Wix platform auto-provisions for every tenant.
  evidence:
  - status: 200
    url: https://www.sightdx.com/
  - status: 400
    url: https://www.sightdx.com/openapi.json
  - status: 404
    url: https://www.sightdx.com/api-docs
  - status: 0
    url: https://api.sightdx.com/
  - status: 0
    url: https://developer.sightdx.com/
  - status: 0
    url: https://docs.sightdx.com/
  - status: 400
    url: https://www.sightdx.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/sightdiagnostics
  - status: 200
    url: https://www.sightdx.com/llms.txt
  - status: 200
    url: https://www.sightdx.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: 'Sight Diagnostics is an Israeli medical-device and diagnostics company, founded in 2011 and headquartered in Tel Aviv, that built Sight OLO — an FDA 510(k)-cleared, CE-marked point-of-care hematology analyzer producing a 19-parameter, five-part-differential Complete Blood Count from two drops of capillary or venous blood in about ten minutes. OLO replaces reagent-based flow cytometry with digital microscopy and machine vision: it images the sample across five illumination channels (405nm, 517nm and 633nm brightfield plus 365nm and 460nm fluorescence) and classifies cells with computer-vision models rather than impedance or optical scatter. The company raised roughly $124M across six rounds and has more recently repositioned around live immune-cell analysis and "immune signatures". Sight Diagnostics is an instrument and clinical-workflow business, not a software platform: it publishes no public API, no developer portal, no SDKs and no machine-readable contract. Device connectivity
  to LIS/EMR systems is delivered as a customer integration engagement rather than as a documented public interface, so there is no developer surface to profile.'
image: https://static.wixstatic.com/media/a6dc54_dcc7d9f74ab6416186ef600457ae343b~mv2.jpg/v1/fill/w_1400,h_550,al_c/a6dc54_dcc7d9f74ab6416186ef600457ae343b~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Sight Diagnostics Site MCP (Wix "Site Visitor Assistant")
  slug: sight-diagnostics-site-mcp-wix-site-visitor-assistant
modified: '2026-08-27'
name: Sight Diagnostics
nav: Providers
network: true
overview: Sight Diagnostics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Diagnostics, and Hematology.
random_paper: 0
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.4
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
  name: Sight Diagnostics Domain Security
  slug: sight-diagnostics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sight-diagnostics
tags:
- Company
- Healthcare
- Medical Devices
- Diagnostics
- Hematology
- Point of Care
- Laboratory
- Artificial Intelligence
- Computer-Vision
- Israel
website: https://www.sightdx.com/
---
