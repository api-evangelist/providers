---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Deterministic court rules compliance checking for federal filings
  name: Court Rules API
  slug: court-rules-api
artifact_total: 5
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/rate-limits/courtrules-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/courtrules-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/authentication/courtrules-authentication.yml
  title: ''
  type: Authentication
  url: authentication/courtrules-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/conformance/courtrules-conformance.yml
  title: ''
  type: Conformance
  url: conformance/courtrules-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/llms/courtrules-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/courtrules-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/a2a/courtrules-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/courtrules-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/mcp/courtrules-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/courtrules-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/well-known/courtrules-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/courtrules-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/hosts/courtrules-hosts.yml
  title: ''
  type: Hosts
  url: hosts/courtrules-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/vendors/courtrules-vendors.yml
  title: ''
  type: Vendors
  url: vendors/courtrules-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.courtrules.app/team
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.courtrules.app/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.courtrules.app/api-reference/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/courtrules/refs/heads/main/security/courtrules-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/courtrules-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.courtrules.app/
- group: docs
  title: ''
  type: Documentation
  url: https://www.courtrules.app/api
- group: start
  title: ''
  type: SignUp
  url: https://www.courtrules.app/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.courtrules.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.courtrules.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.courtrules.app/support
- group: company
  title: ''
  type: Blog
  url: https://www.courtrules.app/blog
created: '2026-10-02'
description: Court Rules provides structured legal and enforcement data from U.S. federal and state courts, including judge rules, filing deadlines, court holidays, and enforcement actions. The platform offers an API that enables developers to integrate court rule searches, compliance checks, and legal intelligence into products, supporting both free tier access and paid plans for higher volume and advanced features.
image: https://www.courtrules.app/opengraph-image?a428ae78c988eff6
layout: provider
mcp_servers:
- description: ''
  name: Court Rules MCP Server
  slug: court-rules-mcp-server
modified: '2026-10-02'
name: Court Rules
nav: Providers
network: true
overview: 'Court Rules publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Data, CourtRules, Compliance, and US Law.


  Court Rules'' developer surface includes authentication, getting-started guide, API reference, documentation, signup flow, support, engineering blog, and 13 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 3
  name: Courtrules Rate Limits
  slug: courtrules-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 68.3
    operational_transparency: 31.6
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Courtrules Authentication
  slug: courtrules-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Courtrules Domain Security
  slug: courtrules-domain-security
  summary_line: TLSv1.3 · HSTS
slug: courtrules
tags:
- Legal Data
- CourtRules
- Compliance
- US Law
website: https://www.courtrules.app/
---
