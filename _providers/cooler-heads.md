---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Anonymous Model Context Protocol endpoint served from the Cooler Heads web host. It is the Wix Site MCP surface (platform-provided, not a first-party Cooler Heads API): nine tools that let an agent re'
  name: Cooler Heads Site MCP
  slug: cooler-heads-site-mcp
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cooler-heads-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coolerheads.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cooler-heads-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cooler-heads-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cooler-heads-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cooler-heads-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cooler-heads-conformance.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coolerheads.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.coolerheads.com/blog-feed.xml
- group: operate
  title: ''
  type: Support
  url: https://www.coolerheads.com/contact
- group: company
  title: ''
  type: Press
  url: https://www.coolerheads.com/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cooler-heads-technology/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/cooler-heads_stock/
created: '2026-08-09'
description: Cooler Heads Care, Inc. is a San Diego medical device company founded in 2018 by Kate Dilligan that makes Amma, an FDA-cleared Portable Scalp Cooling System (PSCS) used to reduce chemotherapy-induced hair loss. Amma circulates chilled fluid through a fitted cap to constrict scalp blood vessels and limit chemotherapy delivery to hair follicles, and is designed to be portable enough that patients can keep cooling outside the infusion chair. The company sells to infusion centers and oncology practices and publishes patient, provider, reimbursement and training material on its own site. It ships no developer API, SDK or public API documentation; its only machine-readable public surface is the Wix-platform site MCP endpoint and llms.txt served from its own host.
image: https://static.wixstatic.com/media/6583f1_f14833176fd248229e8238fdeb4af315~mv2.jpg/v1/fill/w_1600,h_840,al_c/6583f1_f14833176fd248229e8238fdeb4af315~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Site Visitor Assistant for site "Cooler Heads Care, Inc."
  slug: site-visitor-assistant-for-site-cooler-heads-care-inc
modified: '2026-08-09'
name: Cooler Heads
nav: Providers
network: true
overview: 'Cooler Heads publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Oncology, and Scalp Cooling.


  Cooler Heads'' developer surface includes authentication, engineering blog, support, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cooler-heads/refs/heads/main/screenshots/cooler-heads-2026-09-02T145137.png
security:
- kind: authentication
  name: Cooler Heads Authentication
  slug: cooler-heads-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cooler Heads Domain Security
  slug: cooler-heads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cooler-heads
tags:
- Company
- Medical Devices
- Healthcare
- Oncology
- Scalp Cooling
- Patient Care
- MCP
website: https://www.coolerheads.com/
---
