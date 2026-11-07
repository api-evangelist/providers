---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 3
asyncapis:
- description: ''
  name: Ampersand Ai Webhooks
  slug: ampersand-ai-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ampersand.ai/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ampersand.ai/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ampersand.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amp-labs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ampersand.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ampersand.ai/reference
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
overview: 'Ampersand publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Enterprise, and Automation.


  The Ampersand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ampersand''s developer surface includes changelog, API reference, CLI, sandbox, authentication, documentation, pricing, and 14 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.1
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 39.3
    discoverability: 46.4
    operational_transparency: 55.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ampersand-ai/ampersand-ai-2026-11-03T120823.png
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
- Automation
website: https://www.ampersand.ai/
---
