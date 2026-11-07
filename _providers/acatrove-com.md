---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AcaTrove offers a REST API for accessing platform features and health monitoring endpoints.
  name: AcaTrove API
  slug: acatrove-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/acatrove-com/plans/acatrove-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acatrove-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/acatrove-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/acatrove-com/changelog/acatrove-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/acatrove-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.acatrove.com/security
- group: agent
  href: https://artifacts.apis.io/acatrove-com/llms/acatrove-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acatrove-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/acatrove-com/mcp/acatrove-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acatrove-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/acatrove-com/well-known/acatrove-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acatrove-com-security.txt
- group: auth
  href: https://artifacts.apis.io/acatrove-com/well-known/acatrove-com-acatrove-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acatrove-com-acatrove-security.txt
- group: agent
  href: https://artifacts.apis.io/acatrove-com/well-known/acatrove-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acatrove-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/acatrove-com/hosts/acatrove-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acatrove-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/acatrove-com/vendors/acatrove-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acatrove-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.acatrove.com/security
- group: start
  title: ''
  type: Login
  url: https://www.acatrove.com/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.acatrove.com/changelog
- group: auth
  href: https://artifacts.apis.io/acatrove-com/security/acatrove-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/acatrove-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/acatrove-com/security/acatrove-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acatrove-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/acatrove-com/security/acatrove-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acatrove-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acatrove.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.acatrove.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.acatrove.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.acatrove.com/help/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.acatrove.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.acatrove.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acatrove.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acatrove.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acatrove.com/privacy
coverage:
  checked: '2026-10-31'
  detail: Public documentation exists but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://api.acatrove.com/api/v1/health
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AcaTrove is a research‑focused platform that lets users ask questions of their own papers and receive cited answers. It also helps draft research statements, grant narratives, and biosketches, integrating with Zotero and ORCID to match citations and streamline scholarly writing. The service provides practical guides for researchers, labs, developers, and institutional teams, aiming to accelerate knowledge discovery and documentation.
image: https://www.acatrove.com/brand/acatrove-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.acatrove.com requiring OAuth.
  name: AcaTrove MCP Server
  slug: acatrove-com-mcp-yml
modified: '2026-10-31'
name: AcaTrove
nav: Providers
network: true
overview: 'AcaTrove is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Research, Citations, Knowledge Management, and Productivity.


  AcaTrove''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Acatrove Com Plans Pricing
  plan_count: 5
  slug: acatrove-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Acatrove Com Rate Limits
  slug: acatrove-com-rate-limits
scopes:
- name: Acatrove Com Scopes
  scope_count: 0
  slug: acatrove-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 24.3
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 40.1
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acatrove Com Authentication
  slug: acatrove-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Acatrove Com Domain Security
  slug: acatrove-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acatrove Com Vulnerability Disclosure
  slug: acatrove-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Acatrove Com Trust Center
  slug: acatrove-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: acatrove-com
tags:
- Artificial Intelligence
- Research
- Citations
- Knowledge Management
- Productivity
website: https://acatrove.com/
---
