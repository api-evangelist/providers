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
  href: https://artifacts.apis.io/airiskmanagement-ca/llms/airiskmanagement-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airiskmanagement-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/airiskmanagement-ca/mcp/airiskmanagement-ca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/airiskmanagement-ca-mcp.yml
- group: other
  href: https://artifacts.apis.io/airiskmanagement-ca/hosts/airiskmanagement-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airiskmanagement-ca-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airiskmanagement.ca/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airiskmanagement.ca/privacy
- group: company
  title: ''
  type: Blog
  url: https://airiskmanagement.ca/blog
- group: auth
  href: https://artifacts.apis.io/airiskmanagement-ca/security/airiskmanagement-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airiskmanagement-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airiskmanagement.ca/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://ailist.airiskmanagement.ca/mcp
  - status: 200
    url: https://airiskmanagement.ca/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Aeon AI Risk Management provides AI consulting, private AI deployment, and cybersecurity services. They help organizations implement AI workflows, set up private AI environments, strengthen cybersecurity, and establish practical AI governance. Their offerings include AI implementation, private AI setup, AI governance, security assessments, and research, targeting enterprises seeking controlled, secure AI solutions.
image: https://d2xsxph8kpxj0f.cloudfront.net/310519663219538527/4PTvb7yNNDzGtkchndPoyy/AeonLogo_black_a7962169.png
layout: provider
mcp_servers:
- description: Remote MCP server at ailist.airiskmanagement.ca.
  name: Aeon AI Risk Management MCP Server
  slug: airiskmanagement-ca-mcp-yml
modified: '2026-11-01'
name: Aeon AI Risk Management
nav: Providers
network: true
overview: 'Aeon AI Risk Management is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Consulting, Cybersecurity, Private AI, and Risk Management.


  Aeon AI Risk Management''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 9.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airiskmanagement Ca Domain Security
  slug: airiskmanagement-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airiskmanagement-ca
tags:
- Artificial Intelligence
- Consulting
- Cybersecurity
- Private AI
- Risk Management
website: https://airiskmanagement.ca/
---
