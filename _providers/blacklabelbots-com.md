---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public agent API for Black Label Bots
  name: Black Label Bots Agent API
  slug: black-label-bots-agent-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/blacklabelbots-com/plans/blacklabelbots-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blacklabelbots-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/blacklabelbots-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://blacklabelbots.com/privacy
- group: auth
  href: https://artifacts.apis.io/blacklabelbots-com/authentication/blacklabelbots-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blacklabelbots-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/blacklabelbots-com/conformance/blacklabelbots-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blacklabelbots-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blacklabelbots-com/llms/blacklabelbots-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blacklabelbots-com-llms.txt
- group: build
  href: https://artifacts.apis.io/blacklabelbots-com/mcp/blacklabelbots-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blacklabelbots-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/blacklabelbots-com/mcp/blacklabelbots-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blacklabelbots-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/blacklabelbots-com/well-known/blacklabelbots-com-tryacee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blacklabelbots-com-tryacee-security.txt
- group: auth
  href: https://artifacts.apis.io/blacklabelbots-com/well-known/blacklabelbots-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blacklabelbots-com-security.txt
- group: agent
  href: https://artifacts.apis.io/blacklabelbots-com/well-known/blacklabelbots-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blacklabelbots-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blacklabelbots-com/hosts/blacklabelbots-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacklabelbots-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blacklabelbots-com/vendors/blacklabelbots-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blacklabelbots-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/black-label-tec
- group: start
  title: ''
  type: GettingStarted
  url: https://blacklabelbots.com/marketing-setup
- group: docs
  title: ''
  type: APIReference
  url: https://blacklabelbots.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/blacklabelbots-com/security/blacklabelbots-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blacklabelbots-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blacklabelbots-com/security/blacklabelbots-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacklabelbots-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blacklabelbots.com/
- group: docs
  title: ''
  type: Documentation
  url: https://blacklabelbots.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://blacklabelbots.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blacklabelbots.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blacklabelbots.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://blacklabelbots.com/support
- group: company
  title: ''
  type: About
  url: https://blacklabelbots.com/about
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://blacklabelbots.com/openapi.json
  - status: null
    url: https://blacklabelbots.com/mcp
  - status: 401
    url: https://operator.blacklabelbots.com/mcp
  - status: 200
    url: https://blacklabelbots.com/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Black Label Bots provides business software tools for Mac and Windows platforms, offering services such as custom website building, music mastering, campaign brief creation, and various automation utilities. Their platform includes pricing plans, integrations, developer resources, and a suite of applications aimed at enhancing productivity for creators and businesses.
image: https://blacklabelbots.com/assets/web/og/brand.webp
layout: provider
mcp_servers:
- description: Remote MCP server at blacklabelbots.com.
  name: blacklabelbots-com MCP Server
  slug: blacklabelbots-com-mcp-yml
modified: '2026-10-29'
name: blacklabelbots-com
nav: Providers
network: true
overview: 'blacklabelbots-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business, Software, Productivity, Automation, and Mac.


  blacklabelbots-com''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, support, and 19 more developer resources.'
plans:
- name: Blacklabelbots Com Plans Pricing
  plan_count: 7
  slug: blacklabelbots-com-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 47.0
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blacklabelbots Com Authentication
  slug: blacklabelbots-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blacklabelbots Com Domain Security
  slug: blacklabelbots-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blacklabelbots Com Vulnerability Disclosure
  slug: blacklabelbots-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: site-info
  slug: blacklabelbots-com-site-info
slug: blacklabelbots-com
tags:
- Business
- Software
- Productivity
- Automation
- Mac
- Windows
website: https://blacklabelbots.com/
---
