---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: API for Scout APM platform, providing monitoring data and MCP server access.
  name: Scout APM API
  slug: scout-apm-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scoutapm.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scoutapm.com/pricing
- group: commercial
  href: https://artifacts.apis.io/scout-apm/plans/scout-apm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scout-apm-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/scout-apm/cli/scout-apm-cli.yml
  title: ''
  type: CLI
  url: cli/scout-apm-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.scoutapm.com/security
- group: design
  href: https://artifacts.apis.io/scout-apm/conformance/scout-apm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scout-apm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scout-apm/llms/scout-apm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scout-apm-llms.txt
- group: agent
  href: https://artifacts.apis.io/scout-apm/mcp/scout-apm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scout-apm-mcp.yml
- group: agent
  href: https://artifacts.apis.io/scout-apm/well-known/scout-apm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scout-apm-well-known.yml
- group: other
  href: https://artifacts.apis.io/scout-apm/hosts/scout-apm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scout-apm-hosts.yml
- group: other
  href: https://artifacts.apis.io/scout-apm/vendors/scout-apm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scout-apm-vendors.yml
- group: build
  href: https://artifacts.apis.io/scout-apm/packages/scout-apm-packages.yml
  title: ''
  type: SDKs
  url: packages/scout-apm-packages.yml
- group: build
  href: https://artifacts.apis.io/scout-apm/packages/scout-apm-packages.yml
  title: ''
  type: Packages
  url: packages/scout-apm-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.scoutapm.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scoutapp
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.scoutapm.com/blog/category/changelog
- group: auth
  href: https://artifacts.apis.io/scout-apm/security/scout-apm-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scout-apm-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/scout-apm/security/scout-apm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scout-apm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scoutapm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://scoutapm.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scoutapm.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://scoutapm.com/docs
- group: company
  title: ''
  type: Blog
  url: https://scoutapm.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scoutapm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scoutapm.com/privacy
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://scoutapm.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Scout APM provides AI‑assisted application performance monitoring, offering real‑time error tracking, log management, metrics, query analysis, and alerting. Its platform integrates with popular languages and frameworks, delivering code‑level visibility, automated anomaly detection, and a MCP server for AI agents. Users can explore dashboards, configure alerts, and access a CLI, all aimed at faster issue resolution and improved developer productivity.
image: https://www.scoutapm.com/assets/images/og/og-home.png
layout: provider
mcp_servers:
- description: Remote MCP server at scoutapm.com requiring OAuth.
  name: Scout APM MCP Server
  slug: scout-apm-mcp-yml
modified: '2026-10-26'
name: Scout APM
nav: Providers
network: true
overview: 'Scout APM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, APM, AI-assisted, and Performance.


  Scout APM''s developer surface includes pricing, CLI, changelog, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Scout Apm Plans Pricing
  plan_count: 7
  slug: scout-apm-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 66.7
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scout-apm/scout-apm-2026-11-03T142823.png
security:
- kind: domain-security
  name: Scout Apm Domain Security
  slug: scout-apm-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Scout Apm Trust Center
  slug: scout-apm-trust-center
  summary_line: SOC 2, HIPAA
slug: scout-apm
tags:
- Company
- Monitoring
- APM
- AI-assisted
- Performance
website: https://www.scoutapm.com/
---
