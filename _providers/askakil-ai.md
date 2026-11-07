---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/askakil-ai/llms/askakil-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askakil-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/askakil-ai/mcp/askakil-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/askakil-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/askakil-ai/well-known/askakil-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askakil-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/askakil-ai/hosts/askakil-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askakil-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/askakil-ai/vendors/askakil-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askakil-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/askakil-ai/security/askakil-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askakil-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askakil.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://askakil.ai/mcp
- group: company
  title: ''
  type: About
  url: https://askakil.ai/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askakil.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askakil.ai/terms
coverage:
  checked: '2026-11-01'
  detail: Documentation is HTML without a discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://askakil.ai/mcp/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Akil provides AI‑ready access to New York City public records, offering a curated toolkit of over 200 data sources such as building permits, school information, and city council actions. By connecting these datasets to AI assistants, Akil enables developers to build intelligent applications that query, explain, and visualize municipal data with source attribution and coverage limits.
image: https://askakil.ai/brand/v3/akil-a-dot.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.askakil.ai requiring an API key.
  name: Akil MCP Server
  slug: askakil-ai-mcp-yml
modified: '2026-11-01'
name: Akil
nav: Providers
network: true
overview: 'Akil is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, NYC, Public Records, Artificial Intelligence, and Government.


  Akil''s developer surface includes documentation and 10 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 11.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askakil Ai Domain Security
  slug: askakil-ai-domain-security
  summary_line: TLSv1.3
slug: askakil-ai
tags:
- Data
- NYC
- Public Records
- Artificial Intelligence
- Government
website: https://askakil.ai/
---
