---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automotus-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/automotus-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/automotus-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.automotus.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.automotus.co/company-news-insights/
- group: operate
  title: ''
  type: Support
  url: https://curbpasshelp.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://www.curbpass.io/login
- group: start
  title: ''
  type: Login
  url: https://www.curbsuite.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.automotus.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.automotus.ai/privacypolicy
- group: operate
  title: ''
  type: Contact
  url: https://www.automotus.ai/contact
created: '2026-07-17'
description: Automotus is a smart-city and urban-mobility technology company that provides automated curb management using computer vision. Its CurbSight AI cameras use automatic license plate recognition (ALPR), 5G connectivity, edge processing, and privacy-by-design to monitor curb activity, while CurbPass handles curb access payment and invoicing and CurbSuite delivers an enforcement and analytics dashboard. Automotus works with cities, airports, and commercial fleets to reduce congestion, improve safety and compliance, cut emissions, and generate new curb revenue. It was surfaced as a Techstars portfolio company and added to the API Evangelist network for enrichment; no public developer/API surface has been found yet.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automotus.png
layout: provider
mcp_servers:
- description: ''
  name: Automotus MCP Server
  slug: automotus-mcp-server
modified: '2026-07-18'
name: Automotus
nav: Providers
network: true
overview: 'Automotus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Cities, Urban Mobility, Curb Management, and Computer-Vision.


  Automotus'' developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automotus/refs/heads/main/screenshots/automotus-2026-07-25T201835.png
security:
- kind: domain-security
  name: Automotus Domain Security
  slug: automotus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: automotus
tags:
- Company
- Smart Cities
- Urban Mobility
- Curb Management
- Computer-Vision
- Transportation
- Parking
- Enforcement
website: https://www.automotus.ai/
---
