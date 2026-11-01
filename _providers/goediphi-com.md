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
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/goediphi-com/llms/goediphi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goediphi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/goediphi-com/mcp/goediphi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/goediphi-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/goediphi-com/hosts/goediphi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goediphi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/goediphi-com/vendors/goediphi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goediphi-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.goediphi.com/blog
- group: auth
  href: https://artifacts.apis.io/goediphi-com/security/goediphi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goediphi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goediphi.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://goediphi.com/mcp
  - status: 403
    url: https://www.goediphi.com/mcp
  - status: 200
    url: https://goediphi.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Ediphi is an innovative training platform focused on hospitality education, offering immersive VR-based learning experiences, international internship opportunities, and AI-powered training solutions for universities, companies, and individual learners. The company leverages cutting‑edge technology to provide customizable curricula, track student progress, and connect learners with global career pathways in the hospitality industry, aiming to modernize skill development and bridge the gap between academic training and real‑world industry demands.
image: https://static.wixstatic.com/media/ee3a5b_b8501580750e4eb2994cdbe3a90c26d1%7Emv2.png/v1/fit/w_2500,h_1330,al_c/ee3a5b_b8501580750e4eb2994cdbe3a90c26d1%7Emv2.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.goediphi.com.
  name: Ediphi MCP Server
  slug: goediphi-com-mcp-yml
modified: '2026-10-24'
name: Ediphi
nav: Providers
network: true
overview: 'Ediphi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Education, VR, and AI.


  Ediphi''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Goediphi Com Domain Security
  slug: goediphi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goediphi-com
tags:
- Company
- Hospitality
- Education
- VR
- AI
website: https://goediphi.com/
---
