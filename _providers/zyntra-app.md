---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
  score: 5.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zyntra App Agentic Access
  operation_count: 5
  slug: zyntra-app-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: Read‑only email testing API allowing automation of sign‑up, password‑reset, magic‑link and OTP flows.
  name: Zyntra API
  slug: zyntra-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/zyntra-app/plans/zyntra-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zyntra-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/zyntra-app/llms/zyntra-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zyntra-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/zyntra-app/mcp/zyntra-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zyntra-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/zyntra-app/hosts/zyntra-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zyntra-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/zyntra-app/vendors/zyntra-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zyntra-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/zyntra-app/packages/zyntra-app-packages.yml
  title: ''
  type: SDKs
  url: packages/zyntra-app-packages.yml
- group: build
  href: https://artifacts.apis.io/zyntra-app/packages/zyntra-app-packages.yml
  title: ''
  type: Packages
  url: packages/zyntra-app-packages.yml
- group: auth
  href: https://artifacts.apis.io/zyntra-app/security/zyntra-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zyntra-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zyntra.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zyntra.app
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zyntra.app/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zyntra.app/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://zyntra.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://zyntra.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zyntra.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zyntra.app/privacy-policy
coverage:
  checked: '2026-10-31'
  detail: Docs are served as a JavaScript SPA, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.zyntra.app
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Zyntra provides a read‑only email testing API that lets developers automate sign‑up, password‑reset, magic‑link and OTP flows. By sending test emails to team‑specific addresses, teams can retrieve email content, links and attachments over a simple REST endpoint. The service includes free tools like SPF/DKIM/DMARC checking, an email header analyzer, and SDKs for popular test frameworks. Plans range from a free tier with 150 emails/month to paid tiers with higher limits and longer retention.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.zyntra.app requiring an API key.
  name: Zyntra MCP Server
  slug: zyntra-app-mcp-yml
modified: '2026-10-31'
name: Zyntra
nav: Providers
network: true
overview: 'Zyntra publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Email Testing, Automated Tests, QA, Password Reset, and Magic Link.


  The Zyntra catalog on APIs.io includes 1 Spectral governance ruleset.


  Zyntra''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Zyntra App Plans Pricing
  plan_count: 3
  slug: zyntra-app-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Zyntra API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: zyntra-app-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 6.0
    developer_ergonomics: 22.6
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zyntra App Authentication
  slug: zyntra-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zyntra App Domain Security
  slug: zyntra-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: email-management
  slug: zyntra-app-email-management
slug: zyntra-app
tags:
- Email Testing
- Automated Tests
- QA
- Password Reset
- Magic Link
website: https://zyntra.app/
---
