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
- description: Asksteps provides an API for forms, funnels and PDF handling as described in the developer portal.
  name: Asksteps API
  slug: asksteps-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/asksteps-co/llms/asksteps-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asksteps-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/asksteps-co/mcp/asksteps-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asksteps-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asksteps-co/well-known/asksteps-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asksteps-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/asksteps-co/hosts/asksteps-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asksteps-co-hosts.yml
- group: auth
  href: https://artifacts.apis.io/asksteps-co/security/asksteps-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asksteps-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asksteps.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://asksteps.co/entwickler
- group: docs
  title: ''
  type: Documentation
  url: https://asksteps.co/entwickler/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://asksteps.co/entwickler/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://asksteps.co/online-funnels
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asksteps.co/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asksteps.co/datenschutz
created: '2026-11-01'
description: Asksteps provides online form, funnel, and PDF solutions for developers and agencies. Their platform enables creation of custom web forms, PDF conversion, and automated lead funnels, supporting multilingual interfaces and integration with MCP servers. The service offers design customization, pricing plans, and compliance documentation, targeting businesses seeking digital form automation and workflow optimization.
layout: provider
mcp_servers:
- description: Remote MCP server at api.asksteps.co.
  name: asksteps MCP Server
  slug: asksteps-co-mcp-yml
modified: '2026-11-01'
name: asksteps
nav: Providers
network: true
overview: 'asksteps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Forms, PDFs, Funnels, and Automation.


  asksteps'' developer surface includes documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asksteps Co Domain Security
  slug: asksteps-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asksteps-co
tags:
- Company
- Forms
- PDFs
- Funnels
- Automation
- Developer Tools
website: https://asksteps.co/
---
