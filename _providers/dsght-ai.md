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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dsght-ai/llms/dsght-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dsght-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dsght-ai/mcp/dsght-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dsght-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/dsght-ai/hosts/dsght-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dsght-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dsght-ai/vendors/dsght-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dsght-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dsght.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dsght.ai/privacy
- group: auth
  href: https://artifacts.apis.io/dsght-ai/security/dsght-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dsght-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dsght.ai/
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discoverable on the API host or docs host.
  evidence:
  - status: 0
    url: https://api.dsght.ai/openapi.json
  - status: 0
    url: https://api.dsght.ai/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: DSGHT.ai provides an AI strategic foresight platform for regulated industries in Central and Eastern Europe (CEE). It monitors over 350,000 sources, generates multiple plausible futures, and stress‑tests each tension to help boards make decision‑ready choices. The service offers continuous, auditable insights and a free tier for early adopters.
image: https://www.dsght.ai/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.dsght.ai.
  name: DSGHT.ai MCP Server
  slug: dsght-ai-mcp-yml
modified: '2026-11-06'
name: DSGHT.ai
nav: Providers
network: true
overview: DSGHT.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Foresight, Analytics, and Platform.
random_paper: 17
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dsght Ai Domain Security
  slug: dsght-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dsght-ai
tags:
- Company
- Artificial Intelligence
- Foresight
- Analytics
- Platform
- CEE
website: https://dsght.ai/
---
