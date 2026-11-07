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
  href: https://artifacts.apis.io/defaultrank-com/llms/defaultrank-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defaultrank-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/defaultrank-com/mcp/defaultrank-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/defaultrank-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/defaultrank-com/hosts/defaultrank-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defaultrank-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/defaultrank-com/vendors/defaultrank-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defaultrank-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/defaultrank-com/security/defaultrank-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defaultrank-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defaultrank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://defaultrank.com/methodology
- group: other
  title: ''
  type: Report
  url: https://defaultrank.com/reports/2026-10/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defaultrank.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defaultrank.com/terms
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite accessible documentation.
  evidence:
  - status: 200
    url: https://defaultrank.com/methodology
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DefaultRank measures which developer tools AI models recommend and which actually appear in generated code. By aggregating data from model outputs, it provides transparent rankings of IDEs, libraries, and frameworks, helping developers understand AI-driven tool adoption trends.
image: https://defaultrank.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at defaultrank.com.
  name: DefaultRank MCP Server
  slug: defaultrank-com-mcp-yml
modified: '2026-11-05'
name: DefaultRank
nav: Providers
network: true
overview: 'DefaultRank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Developer Tools, Rankings, and Analytics.


  DefaultRank''s developer surface includes documentation and 9 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 10.6
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
    developer_ergonomics: 9.5
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
  name: Defaultrank Com Domain Security
  slug: defaultrank-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: defaultrank-com
tags:
- Company
- Artificial Intelligence
- Developer Tools
- Rankings
- Analytics
website: https://defaultrank.com/
---
