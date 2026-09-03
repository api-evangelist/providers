---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Wix-platform Site MCP server Photys serves from its own production host. Nine tools over public site content — business details, in-site search, site API docs discovery, an anonymous visitor-token
  name: Photys Site MCP
  slug: photys-site-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photys-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.photys.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/photys
- group: agent
  title: ''
  type: MCPServer
  url: mcp/photys-therapeutics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/photys-therapeutics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/photys-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/photys-therapeutics-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/photys-therapeutics-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/photys-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/photys-therapeutics-rate-limits.yml
created: '2026-08-26'
description: 'Photys Therapeutics is a clinical-stage biopharmaceutical company in Waltham, Massachusetts advancing proximity-based, targeted protein modulation medicines across three heterobifunctional modalities: PROTAC-based protein degradation (lead program PHT-776/HPB-143, an oral IRAK4 degrader that entered Phase I in August 2026 for autoimmune and inflammatory disease), PHICS (Phosphorylation-Inducing Chimeric Small molecules, partnered with Novo Nordisk since December 2024 for cardiometabolic disease), and tPRIME for restoring protective proteins such as p53 Y220C in oncology. Founded in 2022 out of Amit Choudhary''s lab at the Broad Institute and Brigham and Women''s Hospital with a $75M Series A led by MPM Capital and Longwood Fund. Photys operates no developer program and publishes no OpenAPI, GraphQL, AsyncAPI, WSDL or gRPC contract; its only machine-readable, agent-facing surface is the platform-provided Wix Site MCP endpoint served from its own host at www.photys.com/_api/mcp,
  which answers anonymously with nine tools over site content and business details.'
image: https://static.wixstatic.com/ficons/2079da_8b1665acced14f96aa889139336df6ad%7Emv2.ico
layout: provider
mcp_servers:
- description: ''
  name: Site Visitor Assistant for site "Photys"
  slug: site-visitor-assistant-for-site-photys
modified: '2026-08-26'
name: Photys Therapeutics
nav: Providers
network: true
overview: 'Photys Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  Photys Therapeutics'' developer surface includes authentication and 9 more developer resources.'
plans:
- name: Photys Therapeutics Plans Pricing
  plan_count: 0
  slug: photys-therapeutics-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Photys Therapeutics Rate Limits
  slug: photys-therapeutics-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 12.9
  provenance:
    conformance: first-party
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
screenshot: https://raw.githubusercontent.com/api-evangelist/photys-therapeutics/refs/heads/main/screenshots/photys-therapeutics-2026-09-02T151200.png
security:
- kind: authentication
  name: Photys Therapeutics Authentication
  slug: photys-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Photys Therapeutics Domain Security
  slug: photys-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: photys-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Clinical Trials
- Oncology
- Protein Degradation
- MCP
website: https://www.photys.com/
---
