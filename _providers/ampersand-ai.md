---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 3
asyncapis:
- description: ''
  name: Ampersand Ai Webhooks
  slug: ampersand-ai-webhooks
common:
- group: design
  href: https://artifacts.apis.io/ampersand-ai/asyncapi/ampersand-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ampersand-ai-webhooks.yml
- group: build
  href: https://artifacts.apis.io/ampersand-ai/cli/ampersand-ai-cli.yml
  title: ''
  type: CLI
  url: cli/ampersand-ai-cli.yml
- group: start
  href: https://artifacts.apis.io/ampersand-ai/sandbox/ampersand-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ampersand-ai-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/ampersand-ai/authentication/ampersand-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ampersand-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/ampersand-ai/llms/ampersand-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ampersand-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/ampersand-ai/a2a/ampersand-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ampersand-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/ampersand-ai/well-known/ampersand-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ampersand-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/ampersand-ai/well-known/ampersand-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ampersand-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/ampersand-ai/hosts/ampersand-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ampersand-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ampersand-ai/vendors/ampersand-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ampersand-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ampersand-ai/security/ampersand-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ampersand-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ampersand.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ampersand.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ampersand.ai/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ampersand.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ampersand.ai/blog
- group: company
  title: ''
  type: About
  url: https://www.ampersand.ai/about
created: '2026-10-24'
description: Ampersand provides integration infrastructure for enterprise products, enabling engineering, solution, and revenue teams to connect and synchronize data across platforms such as Salesforce, NetSuite, HubSpot, Marketo, Zendesk, and Intercom. Their platform offers pre‑built integrations, a developer portal, comprehensive documentation, pricing details, and resources like case studies and a changelog. Ampersand aims to simplify complex integrations, accelerate time‑to‑value, and support scalable enterprise workflows.
image: https://www.ampersand.ai/og/home.png
layout: provider
modified: '2026-10-24'
name: Ampersand
nav: Providers
network: true
overview: 'Ampersand publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Enterprise, API, and Automation.


  The Ampersand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ampersand''s developer surface includes CLI, sandbox, authentication, documentation, pricing, engineering blog, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 44.8
    developer_ergonomics: 47.6
    discoverability: 48.2
    operational_transparency: 18.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ampersand Ai Authentication
  slug: ampersand-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ampersand Ai Domain Security
  slug: ampersand-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ampersand-ai
tags:
- Company
- Integration
- Enterprise
- API
- Automation
website: https://www.ampersand.ai/
---
