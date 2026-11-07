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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Dog Leadership Academy's platform, accessed via MCP endpoints.
  name: Dog Leadership Academy API
  slug: dog-leadership-academy-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dogleadershipacademy-com/llms/dogleadershipacademy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dogleadershipacademy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dogleadershipacademy-com/mcp/dogleadershipacademy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dogleadershipacademy-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dogleadershipacademy-com/hosts/dogleadershipacademy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dogleadershipacademy-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://dogleadershipacademy.com/login/
- group: auth
  href: https://artifacts.apis.io/dogleadershipacademy-com/security/dogleadershipacademy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dogleadershipacademy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dogleadershipacademy.com/
coverage:
  checked: '2026-11-05'
  detail: Provider only offers MCP endpoints without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://dogleadershipacademy.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dog Leadership Academy offers online dog training led by Sydney behaviourist George Tran. Their personalised, opinionated, progress‑tracked programs help owners improve canine behaviour. Visitors can start with a free 2‑minute behaviour assessment and access courses covering obedience, confidence building, and problem solving, all delivered through an interactive web platform.
image: https://www.dogleadershipacademy.com/assets/og-home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at dogleadershipacademy.com.
  name: Dog Leadership Academy MCP Server
  slug: dogleadershipacademy-com-mcp-yml
modified: '2026-11-05'
name: Dog Leadership Academy
nav: Providers
network: true
overview: Dog Leadership Academy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Dog Training, Online Education, Behavioural Science, Pets, and Australia.
random_paper: 11
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dogleadershipacademy Com Domain Security
  slug: dogleadershipacademy-com-domain-security
  summary_line: TLSv1.3
slug: dogleadershipacademy-com
tags:
- Dog Training
- Online Education
- Behavioural Science
- Pets
- Australia
website: https://dogleadershipacademy.com/
---
