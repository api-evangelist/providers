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
    agent_skills: true
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
  score: 12.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: REST API for Keploy Cloud providing test generation and execution capabilities, app/test-suite management, recordings/mocks, test reports, schema coverage, API keys, clusters, and account/subscription
  name: Keploy Cloud API
  slug: keploy-cloud-api
- description: Hosted, remote Model Context Protocol server (streamable HTTP transport, bearer-token auth, ~80 tools) that proxies Keploy's Cloud REST API, giving agents like Cursor, GitHub Copilot, Claude Code, and
  name: Keploy MCP Server
  slug: keploy-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keploy-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://keploy.io/blog/sitemap.xml
- group: build
  title: ''
  type: Packages
  url: packages/keploy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keploy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keploy-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keploy-llms-full.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/keploy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keploy-lifecycle.yml
created: '2026-07-03'
description: Open-source, AI-native testing platform that captures real production API traffic with eBPF and replays it in CI as deterministic tests, auto-generated mocks, and production-like sandboxes with zero code changes. Offers a Cloud REST API, a hosted MCP server, llms.txt, and generated agent skills.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keploy.png
layout: provider
mcp_servers:
- description: ''
  name: Keploy MCP Server
  slug: keploy-mcp-server
- description: ''
  name: Keploy MCP Server
  slug: keploy-mcp-server-2
modified: '2026-06-20'
name: Keploy
nav: Providers
network: true
overview: 'Keploy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Testing & QA, API Testing, Integration/Regression Testing, Unit Test Generation, and Contract Testing.


  Keploy''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 11.4
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/screenshots/keploy-2026-07-25T223630.png
security:
- kind: domain-security
  name: Keploy Domain Security
  slug: keploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keploy
tags:
- Testing & QA
- API Testing
- Integration/Regression Testing
- Unit Test Generation
- Contract Testing
- CI/CD
- Developer Tools
- AI / Agent Tooling
- eBPF / Observability
- Test Data & Mocking
---
