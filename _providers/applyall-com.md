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
api_count: 1
apis:
- description: ApplyAll MCP provides job search automation via a Machine-Callable Protocol (MCP) documented at the MCP endpoint.
  name: ApplyAll MCP
  slug: applyall-mcp
artifact_total: 4
common:
- group: operate
  title: ''
  type: Support
  url: https://help.applyall.com/
- group: agent
  href: https://artifacts.apis.io/applyall-com/llms/applyall-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applyall-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/applyall-com/mcp/applyall-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/applyall-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/applyall-com/well-known/applyall-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applyall-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/applyall-com/hosts/applyall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applyall-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/applyall-com/vendors/applyall-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applyall-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://applyall.com/security
- group: start
  title: ''
  type: Login
  url: https://applyall.com/login
- group: auth
  href: https://artifacts.apis.io/applyall-com/security/applyall-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/applyall-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/applyall-com/security/applyall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applyall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applyall.com/
- group: company
  title: ''
  type: Blog
  url: https://applyall.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://applyall.com/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://applyall.com/mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://applyall.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://applyall.com/privacy
coverage:
  checked: '2026-11-01'
  detail: ApplyAll only publishes an MCP endpoint and no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 0
    url: https://api.applyall.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ApplyAll provides AI‑powered job search support, guaranteeing real interviews or a money‑back refund. The service combines automated application submission with human review, having delivered over 50,000 interviews and offers from 2 million+ applications. Founded by Tal Flanchraych after a layoff, it serves individual jobseekers and partners such as career coaches, universities, and employers, offering white‑label solutions and outplacement services. ApplyAll emphasizes outcomes over activity, ensuring applications appear authentic and remain invisible to recruiters.
image: https://applyall.com/preview.png
layout: provider
mcp_servers:
- description: Remote MCP server at applyall.com.
  name: ApplyAll MCP Server
  slug: applyall-com-mcp-yml
modified: '2026-11-01'
name: ApplyAll
nav: Providers
network: true
overview: 'ApplyAll is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job Search, Artificial Intelligence, InterviewGuarantee, Career Coaching, and White Label.


  ApplyAll''s developer surface includes support, engineering blog, documentation, API reference, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 19.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applyall Com Domain Security
  slug: applyall-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Applyall Com Vulnerability Disclosure
  slug: applyall-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: applyall-com
tags:
- Job Search
- Artificial Intelligence
- InterviewGuarantee
- Career Coaching
- White Label
website: https://applyall.com/
---
