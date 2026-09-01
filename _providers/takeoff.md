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
artifact_total: 2
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TakeoffTech
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/takeoff-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/takeoff-domain-security.yml
coverage:
  checked: '2026-08-29'
  detail: 'Takeoff''s API is real and live but has no public face at all: api.takeoff.com holds a Google Trust Services certificate reissued 2026-07-16 and answers {"code":"401", "message":"Missing authentication header."} on /auth and /sites and {"message":"Forbidden"} on /webhooks and /identity, yet it names no header, serves no OAuth metadata and 404s every spec path, while the company''s own marketing site www.takeoff.com has had no TLS certificate provisioned at its Webflow origin since the 2024 Chapter 11 and Woolworths asset sale — so integration docs exist only for deployed grocer tenants.'
  evidence:
  - status: 401
    url: https://api.takeoff.com/auth
  - status: 403
    url: https://api.takeoff.com/webhooks
  - status: 404
    url: https://api.takeoff.com/openapi.json
  - status: 404
    url: https://api.takeoff.com/.well-known/agent-card.json
  - status: 404
    url: https://api.takeoff.com/llms.txt
  - status: 0
    url: https://www.takeoff.com/
  - status: 0
    url: https://status.takeoff.com/
  - status: 200
    url: https://github.com/TakeoffTech
  - status: 403
    url: https://forgeglobal.com/takeoff_stock/
  reason: customer-only-docs
  state: gated
created: '2026-08-29'
description: 'Takeoff Technologies, Inc. is an eGrocery micro-fulfillment company founded in 2016 and headquartered in Waltham, Massachusetts. It paired KNAPP-built robotic storage-and-retrieval hardware with its own cloud software stack — order management, inventory, pick routing, labor management, and delivery orchestration — into micro-fulfillment centers (MFCs) installed inside or beside existing supermarkets, so grocers could assemble online orders in minutes instead of sending shoppers down the aisles. Customers and partners included Albertsons, Wakefern Food Corp., Woolworths Group and Chilean grocer SMU. The company filed for Chapter 11 in May 2024 and Woolworths Group acquired its micro-fulfillment assets in August 2024. Takeoff never published a public developer program: there is no developer portal, API reference, SDK or machine-readable specification anywhere on its public surface, and the marketing site at www.takeoff.com no longer serves TLS. A closed API gateway at api.takeoff.com
  remains live and actively certificate-maintained, serving customer integrations behind authentication.'
image: https://avatars.githubusercontent.com/u/32682326?s=200&v=4
layout: provider
modified: '2026-08-29'
name: TakeOff
nav: Providers
network: true
overview: TakeOff is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, Retail, E-Commerce, and Fulfillment.
random_paper: 1
score:
  band: minimal
  composite: 6.1
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
  previous_composite: 6.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Takeoff Authentication
  slug: takeoff-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Takeoff Domain Security
  slug: takeoff-domain-security
  summary_line: DNSSEC · DMARC
slug: takeoff
tags:
- Company
- Grocery
- Retail
- E-Commerce
- Fulfillment
- Micro-Fulfillment
- Warehouse Automation
- Robotics
- Supply Chain
- Logistics
---
