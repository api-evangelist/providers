---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 39
  human_in_the_loop: 8
  name: Stacklok Agentic Access
  operation_count: 84
  slug: stacklok-agentic-access
  summary_line: 84 operations · 39 acting · 8 human-in-the-loop
api_count: 1
apis:
- description: The clients API from Stacklok — 5 operation(s) for clients.
  name: Stacklok clients API
  slug: stacklok-clients-api
- description: The discovery API from Stacklok — 1 operation(s) for discovery.
  name: Stacklok discovery API
  slug: stacklok-discovery-api
- description: The groups API from Stacklok — 2 operation(s) for groups.
  name: Stacklok groups API
  slug: stacklok-groups-api
- description: The logs API from Stacklok — 2 operation(s) for logs.
  name: Stacklok logs API
  slug: stacklok-logs-api
- description: The registry API from Stacklok — 10 operation(s) for registry.
  name: Stacklok registry API
  slug: stacklok-registry-api
- description: The registry-servers API from Stacklok — 2 operation(s) for registry-servers.
  name: Stacklok registry-servers API
  slug: stacklok-registry-servers-api
- description: The registry-skills API from Stacklok — 2 operation(s) for registry-skills.
  name: Stacklok registry-skills API
  slug: stacklok-registry-skills-api
- description: The secrets API from Stacklok — 4 operation(s) for secrets.
  name: Stacklok secrets API
  slug: stacklok-secrets-api
- description: The skills API from Stacklok — 12 operation(s) for skills.
  name: Stacklok skills API
  slug: stacklok-skills-api
- description: The system API from Stacklok — 3 operation(s) for system.
  name: Stacklok system API
  slug: stacklok-system-api
- description: The v1 API from Stacklok — 10 operation(s) for v1.
  name: Stacklok v1 API
  slug: stacklok-v1-api
- description: The version API from Stacklok — 1 operation(s) for version.
  name: Stacklok version API
  slug: stacklok-version-api
- description: The workloads API from Stacklok — 13 operation(s) for workloads.
  name: Stacklok workloads API
  slug: stacklok-workloads-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ToolHive Registry clients API
  slug: open-stacklok-clients-api
- collection_type: open
  name: ToolHive Registry clients discovery API
  slug: open-stacklok-discovery-api
- collection_type: open
  name: ToolHive Registry clients groups API
  slug: open-stacklok-groups-api
- collection_type: open
  name: ToolHive Registry clients logs API
  slug: open-stacklok-logs-api
- collection_type: open
  name: ToolHive clients registry API
  slug: open-stacklok-registry-api
- collection_type: open
  name: ToolHive Registry clients registry-servers API
  slug: open-stacklok-registry-servers-api
- collection_type: open
  name: ToolHive Registry clients registry-skills API
  slug: open-stacklok-registry-skills-api
- collection_type: open
  name: ToolHive Registry clients secrets API
  slug: open-stacklok-secrets-api
- collection_type: open
  name: ToolHive Registry clients skills API
  slug: open-stacklok-skills-api
- collection_type: open
  name: ToolHive Registry clients system API
  slug: open-stacklok-system-api
- collection_type: open
  name: ToolHive Registry clients v1 API
  slug: open-stacklok-v1-api
- collection_type: open
  name: ToolHive Registry clients version API
  slug: open-stacklok-version-api
- collection_type: open
  name: ToolHive Registry clients workloads API
  slug: open-stacklok-workloads-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stacklok-discover-and-run-mcp-server.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stacklok-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stacklok-registry-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/stacklok-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://www.stacklok.com/
created: '2026-07-17'
description: 'Stacklok is a company surfaced as a portfolio company of accel, bain-capital-ventures and added to the API Evangelist network as a stub for enrichment. Sector: open-source. This profile is a lead awaiting the enrichment pipeline.'
layout: provider
mcp_servers:
- description: ''
  name: Stacklok MCP Server
  slug: stacklok-mcp-server
modified: '2026-07-17'
name: Stacklok
nav: Providers
network: true
overview: Stacklok publishes 13 APIs on the [APIs.io](https://apis.io/) network, including clients API, discovery API, groups API, and 10 more. Tagged areas include Company and Open-Source.
random_paper: 20
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 95.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 48.8
    developer_ergonomics: 1.8
    discoverability: 44.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Stacklok Authentication
  slug: stacklok-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Stacklok Domain Security
  slug: stacklok-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stacklok
tags:
- Company
- Open-Source
website: https://www.stacklok.com/
---
