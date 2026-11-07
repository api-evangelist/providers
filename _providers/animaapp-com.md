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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Anima’s API lets you expand your product offering by turning Figma designs or live websites into clean, production-ready code.
  name: Anima API
  slug: anima-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/animaapp-com/well-known/animaapp-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animaapp-com-status-security.txt
- group: auth
  title: ''
  type: Security
  url: https://support.animaapp.com/en/articles/2726094-security-at-anima
- group: design
  href: https://artifacts.apis.io/animaapp-com/lifecycle/animaapp-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/animaapp-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/animaapp-com/llms/animaapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animaapp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/animaapp-com/mcp/animaapp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animaapp-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/animaapp-com/well-known/animaapp-com-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animaapp-com-support-security.txt
- group: auth
  href: https://artifacts.apis.io/animaapp-com/well-known/animaapp-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animaapp-com-security.txt
- group: auth
  href: https://artifacts.apis.io/animaapp-com/well-known/animaapp-com-animaapp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animaapp-com-animaapp-security.txt
- group: agent
  href: https://artifacts.apis.io/animaapp-com/well-known/animaapp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animaapp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/animaapp-com/hosts/animaapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animaapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/animaapp-com/vendors/animaapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animaapp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/animaapp-com/packages/animaapp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/animaapp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/animaapp-com/packages/animaapp-com-packages.yml
  title: ''
  type: Packages
  url: packages/animaapp-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.animaapp.com/
- group: start
  title: ''
  type: Sandbox
  url: https://www.animaapp.com/lp/playground
- group: start
  title: ''
  type: Login
  url: https://projects.animaapp.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.animaapp.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.animaapp.com/changelog
- group: auth
  href: https://artifacts.apis.io/animaapp-com/security/animaapp-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/animaapp-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/animaapp-com/security/animaapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animaapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.animaapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.animaapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.animaapp.com/docs/anima-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.animaapp.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.animaapp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.animaapp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AnimaApp/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.animaapp.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://animaapp.s3.amazonaws.com/home/TOS.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://animaapp.s3.amazonaws.com/home/TOS.pdf
coverage:
  checked: '2026-11-01'
  detail: The API reference requires contacting sales and provides no public machine‑readable specification.
  evidence:
  - status: 200
    url: https://docs.animaapp.com/docs/anima-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Anima (Anima App, Inc.) is an AI‑powered design agent that transforms Figma designs, URLs, and text prompts into production‑ready web applications. It offers a platform for product teams to build directly and an API for coding agents and AI development platforms, powering services like Bolt.new, Replit, and ChatAndBuild. Founded in 2017, Anima provides features such as design‑to‑code conversion, custom domains, databases, and real‑time collaboration.
image: https://a.storyblok.com/f/89137/1840x1142/548f935261/anima-the-ux-design-agent.png
layout: provider
mcp_servers:
- description: Remote MCP server at public-api.animaapp.com requiring OAuth.
  name: Anima MCP Server
  slug: animaapp-com-mcp-yml
modified: '2026-11-01'
name: Anima
nav: Providers
network: true
overview: 'Anima is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Design, Code Generation, and Platform.


  Anima''s developer surface includes sandbox, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
plans:
- name: Animaapp Com Plans Pricing
  plan_count: 0
  slug: animaapp-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Animaapp Com Rate Limits
  slug: animaapp-com-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.3
    operational_transparency: 23.7
  previous_composite: 33.9
  provenance:
    conformance: unknown
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
  name: Animaapp Com Domain Security
  slug: animaapp-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Animaapp Com Vulnerability Disclosure
  slug: animaapp-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: animaapp-com
tags:
- Artificial Intelligence
- Design
- Code Generation
- Platform
website: https://www.animaapp.com/
---
