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
artifact_total: 0
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aspace-international-holdings-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aspace-international-holdings
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/aspace-international-holdings
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/aspace-international-holdings-stock
coverage:
  checked: '2026-08-06'
  detail: ASPACE International Holdings is an aerospace manufacturing and investment holding company with no corporate website at all — aspace.com, aspaceholdings.com, aspaceint.com, aspace.global and aspace.com.hk return NXDOMAIN, aspace.ae is a parked OnlyDomains holding page and aspace.io/.co/.space are registrar landers, leaving a LinkedIn page that lists no website and a Hiive secondary-market listing as the only first-party surfaces, while the related USPACE Technology Group group site 404s on /developers, /api, /docs, /openapi.json, /llms.txt and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://www.linkedin.com/company/aspace-international-holdings
  - status: 200
    url: https://www.hiive.com/securities/aspace-international-holdings-stock
  - status: 200
    url: http://aspace.ae/
  - status: 404
    url: https://www.uspace.com/developers
  - status: 404
    url: https://www.uspace.com/openapi.json
  - status: 404
    url: https://www.uspace.com/llms.txt
  - status: 404
    url: https://www.uspace.com/.well-known/agent-card.json
  - status: 404
    url: https://www.uspace.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'ASPACE International Holdings is a commercial space company founded in 2015 with offices listed in Dubai, United Arab Emirates and Hong Kong, China. It positions itself as an aerospace manufacturing conglomerate centred on the Abu Dhabi Space Eco City — a three-million-square-metre industrial cluster it says will bring together more than 3,000 partner companies across satellite manufacturing, space trade and aerospace technology innovation. The ASPACE brand is shared with Hong Kong-listed USPACE Technology Group, whose satellite-manufacturing subsidiary was renamed Aspace Satellite Technology Limited in 2023. ASPACE International Holdings has taken investment from Alpha MBM Investments and makes minority investments of its own, including a stake in the private-equity trading platform Cubin LLC announced in 2023. It is a hardware, industrial-development and investment holding business rather than a software vendor: no first-party corporate domain for the company resolves, its
  only verified public surfaces are a LinkedIn company page, a Hiive secondary-market listing and third-party investor databases, and it publishes no developer program, API, SDK or machine-readable specification of any kind.'
layout: provider
modified: '2026-08-06'
name: ASPACE International Holdings
nav: Providers
network: true
overview: ASPACE International Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Space, Commercial Space, and Satellite Manufacturing.
random_paper: 6
score:
  band: minimal
  composite: 5.4
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
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aspace-international-holdings/refs/heads/main/screenshots/aspace-international-holdings-2026-08-07T161800.png
slug: aspace-international-holdings
tags:
- Company
- Aerospace
- Space
- Commercial Space
- Satellite Manufacturing
- Holding Company
- Investment
- United Arab Emirates
- Hong Kong
---
