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
    agent_card: conformant
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Applayer.io provides an AI application layer with endpoints for workflow automation, model routing, and integrations.
  name: Applayer API
  slug: applayer-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://applayer.io/trust
- group: agent
  href: https://artifacts.apis.io/applayer-io/llms/applayer-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applayer-io-llms.txt
- group: other
  href: https://artifacts.apis.io/applayer-io/a2a/applayer-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/applayer-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/applayer-io/mcp/applayer-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/applayer-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/applayer-io/well-known/applayer-io-tango-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/applayer-io-tango-security.txt
- group: auth
  href: https://artifacts.apis.io/applayer-io/well-known/applayer-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/applayer-io-security.txt
- group: agent
  href: https://artifacts.apis.io/applayer-io/well-known/applayer-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applayer-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/applayer-io/hosts/applayer-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applayer-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/applayer-io/vendors/applayer-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applayer-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/applayer-io/security/applayer-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/applayer-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/applayer-io/security/applayer-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applayer-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applayer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://applayer.io/platform
- group: auth
  title: ''
  type: Trust
  url: https://applayer.io/trust
- group: operate
  title: ''
  type: Contact
  url: https://applayer.io/contact
coverage:
  checked: '2026-11-01'
  detail: Homepage and platform pages provide no OpenAPI, GraphQL, or other machine‑readable contract despite public documentation.
  evidence:
  - status: 404
    url: https://applayer.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Applayer.io provides an AI application layer that enables businesses to deploy AI‑driven apps across support, sales, operations, and knowledge work. The platform offers model‑agnostic routing, native connectors to over 200 services like Salesforce and Zendesk, and enterprise‑grade guardrails, audit trails, and PII redaction. It targets both SMBs and large enterprises, delivering workflow automation, AI agents, and customizable AI marketing funnels to improve efficiency and reduce labor costs.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/attachments/og-images/aad41443-cbfa-47f4-a87b-23a9671cbe99
layout: provider
mcp_servers:
- description: Remote MCP server at tango.applayer.io requiring OAuth.
  name: Applayer.io MCP Server
  slug: applayer-io-mcp-yml
modified: '2026-11-01'
name: Applayer.io
nav: Providers
network: true
overview: 'Applayer.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Enterprise, and Software-as-a-Service.


  Applayer.io''s developer surface includes documentation and 14 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 3.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 10.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applayer Io Domain Security
  slug: applayer-io-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Applayer Io Vulnerability Disclosure
  slug: applayer-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: applayer-io
tags:
- Company
- Artificial Intelligence
- Automation
- Enterprise
- Software-as-a-Service
- Integration
website: https://applayer.io/
---
