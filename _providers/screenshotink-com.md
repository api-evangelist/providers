---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'screenshotink-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: screenshotink-com API
  slug: screenshotink-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/screenshotink-com/plans/screenshotink-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/screenshotink-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/screenshotink-com/rules/screenshotink-com-rules.yml
  title: ''
  type: Spectral
  url: rules/screenshotink-com-rules.yml
- group: design
  href: https://artifacts.apis.io/screenshotink-com/vocabulary/screenshotink-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/screenshotink-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/screenshotink-com/conventions/screenshotink-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/screenshotink-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/screenshotink-com/authentication/screenshotink-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/screenshotink-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/screenshotink-com/errors/screenshotink-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/screenshotink-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/screenshotink-com/conformance/screenshotink-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/screenshotink-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/screenshotink-com/llms/screenshotink-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/screenshotink-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/screenshotink-com/mcp/screenshotink-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/screenshotink-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/screenshotink-com/well-known/screenshotink-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/screenshotink-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/screenshotink-com/hosts/screenshotink-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/screenshotink-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/screenshotink-com/vendors/screenshotink-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/screenshotink-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/screenshotink-com/packages/screenshotink-com-packages.yml
  title: ''
  type: SDKs
  url: packages/screenshotink-com-packages.yml
- group: build
  href: https://artifacts.apis.io/screenshotink-com/packages/screenshotink-com-packages.yml
  title: ''
  type: Packages
  url: packages/screenshotink-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://screenshotink.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://screenshotink.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/screenshotink-com/security/screenshotink-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/screenshotink-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://screenshotink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://screenshotink.com/docs
- group: company
  title: ''
  type: Blog
  url: https://screenshotink.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://screenshotink.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://screenshotink.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://screenshotink.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bikker/screenshotink-mcp
created: '2026-10-31'
description: ScreenshotInk offers a fast, EU‑hosted Screenshot API that captures full‑page screenshots of any URL, supports bulk capture, visual diff, Lighthouse audits, and includes an MCP server for AI agents. It provides a developer portal with documentation, quick‑start guides, pricing plans, a blog, and open‑source tools, with a free tier of 100 captures per month.
image: https://screenshotink.com/assets/og/og-home.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.screenshotink.com requiring OAuth.
  name: screenshotink-com MCP Server
  slug: screenshotink-com-mcp-yml
modified: '2026-10-31'
name: screenshotink-com
nav: Providers
network: true
overview: 'screenshotink-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Screenshot, API, Automation, Monitoring, and MCP.


  The screenshotink-com catalog on APIs.io includes 1 Spectral governance ruleset.


  screenshotink-com''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Screenshotink Com Plans Pricing
  plan_count: 4
  slug: screenshotink-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Screenshotink Com Rate Limits
  slug: screenshotink-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: screenshotink-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: screenshotink-com-rules
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 38.0
    developer_ergonomics: 42.9
    discoverability: 56.7
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Screenshotink Com Authentication
  slug: screenshotink-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Screenshotink Com Domain Security
  slug: screenshotink-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: screenshotink-com
tags:
- Screenshot
- API
- Automation
- Monitoring
- MCP
website: https://screenshotink.com/
---
