---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
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
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/applistingagent-com/plans/applistingagent-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/applistingagent-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/applistingagent-com/conventions/applistingagent-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/applistingagent-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/applistingagent-com/conventions/applistingagent-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/applistingagent-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://applistingagent.com/privacy
- group: auth
  href: https://artifacts.apis.io/applistingagent-com/authentication/applistingagent-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/applistingagent-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/applistingagent-com/llms/applistingagent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applistingagent-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/applistingagent-com/mcp/applistingagent-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/applistingagent-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/applistingagent-com/well-known/applistingagent-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/applistingagent-com-security.txt
- group: agent
  href: https://artifacts.apis.io/applistingagent-com/well-known/applistingagent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applistingagent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/applistingagent-com/hosts/applistingagent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applistingagent-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://applistingagent.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://applistingagent.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://applistingagent.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/applistingagent-com/security/applistingagent-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/applistingagent-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/applistingagent-com/security/applistingagent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applistingagent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applistingagent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://applistingagent.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://applistingagent.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://applistingagent.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://applistingagent.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://applistingagent.com/contact
coverage:
  checked: '2026-11-01'
  detail: No machine‑readable OpenAPI/AsyncAPI/GraphQL spec found; attempts at common spec URLs returned 404 HTML pages.
  evidence:
  - status: 404
    url: https://applistingagent.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: App Listing Agent provides AI‑powered automation for app‑store listings, generating screenshots, localized copy, icons and store pages for Apple App Store Connect and Google Play. Users can create workspaces, connect their AI agents, and let the platform handle store credentials, audits and updates, offering plans for indie to enterprise developers.
image: https://applistingagent.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at applistingagent.com requiring OAuth.
  name: App Listing Agent MCP Server
  slug: applistingagent-com-mcp-yml
modified: '2026-11-01'
name: App Listing Agent
nav: Providers
network: true
overview: 'App Listing Agent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, App Store, Automation, Software-as-a-Service, and Marketing.


  App Listing Agent''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Applistingagent Com Plans Pricing
  plan_count: 5
  slug: applistingagent-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 48.3
    operational_transparency: 13.2
  previous_composite: 32.4
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
- kind: authentication
  name: Applistingagent Com Authentication
  slug: applistingagent-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Applistingagent Com Domain Security
  slug: applistingagent-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Applistingagent Com Vulnerability Disclosure
  slug: applistingagent-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: applistingagent-com
tags:
- Artificial Intelligence
- App Store
- Automation
- Software-as-a-Service
- Marketing
website: https://applistingagent.com/
---
