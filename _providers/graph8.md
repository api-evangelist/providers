---
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: One REST API across the revenue surface — contacts, companies, campaigns and events — plus SDKs, a CLI and an MCP server. Preview access; a workspace endpoint is issued on request.
  name: graph8 build API
  slug: graph8-build-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://graph8.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://graph8.com/build/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.graph8.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://graph8.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://graph8.com/llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.graph8.com/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/graph8-plans.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://graph8.com/build/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://graph8.com/build/changelog
created: '2026-08-03'
description: 'graph8 is an autonomous revenue system — an AI-native B2B sales platform that finds buyers, launches campaigns, runs conversations and builds pipeline against a single buyer graph. It spans buyer and intent data (a claimed 700M contacts and 100M companies), signals, a campaign studio, named agents, CRM and pipeline reporting, a built-in CDP with 500+ connectors, and a desktop companion. It is one of four brands under one company: graph8 the platform, graph8 build the developer platform, CIENCE the SDR and GTM services arm, and Tenbound the research magazine and community. The developer surface at graph8.com/build is documented across six areas — REST API, SDKs, CLI, MCP, React components and infrastructure — but is in preview: at the time of profiling no OpenAPI and no MCP endpoint were publicly fetchable, and a workspace endpoint is issued on request rather than self-serve.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graph8.png
layout: provider
mcp_servers:
- description: ''
  name: graph8 MCP Server
  slug: graph8-mcp-server
modified: '2026-08-03'
name: graph8
nav: Providers
network: true
overview: 'graph8 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales, Revenue, Business Intelligence, Contacts, and Companies.


  graph8''s developer surface includes documentation, pricing, changelog, and 6 more developer resources.'
plans:
- name: Graph8 Plans
  plan_count: 0
  slug: graph8-plans
random_paper: 19
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 39.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 27.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graph8/refs/heads/main/screenshots/graph8-2026-08-07T165820.png
slug: graph8
tags:
- Sales
- Revenue
- Business Intelligence
- Contacts
- Companies
- Signals
- Intent
- Agents
- Artificial Intelligence
- Campaigns
- CRM
- Data Pipeline
- MCP
website: https://graph8.com
---
