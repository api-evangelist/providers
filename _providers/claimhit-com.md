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
    agent_skills: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Commercial-relevance signals for a patent: who in the market appears to practise it, with element-level evidence.'
  name: ClaimHit Partner API
  slug: claimhit-partner-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/claimhit-com/plans/claimhit-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claimhit-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/claimhit-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/claimhit-com/conventions/claimhit-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/claimhit-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.claimhit.com/security
- group: auth
  href: https://artifacts.apis.io/claimhit-com/authentication/claimhit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/claimhit-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/claimhit-com/conformance/claimhit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claimhit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claimhit-com/llms/claimhit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claimhit-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/claimhit-com/mcp/claimhit-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/claimhit-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/claimhit-com/well-known/claimhit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claimhit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/claimhit-com/hosts/claimhit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claimhit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claimhit-com/vendors/claimhit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claimhit-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.claimhit.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.claimhit.com/press
- group: start
  title: ''
  type: Login
  url: https://app.claimhit.com/signin
- group: auth
  href: https://artifacts.apis.io/claimhit-com/security/claimhit-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/claimhit-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/claimhit-com/security/claimhit-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/claimhit-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/claimhit-com/security/claimhit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claimhit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claimhit.com/
- group: company
  title: ''
  type: Blog
  url: https://claimhit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://claimhit.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claimhit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claimhit.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://claimhit.com/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://claimhit.com/fit
created: '2026-10-29'
description: ClaimHit provides patent‑to‑market intelligence, helping users discover which companies are using or potentially infringing on a given patent. The platform aggregates public evidence, generates hit charts, and offers a workflow that includes expert legal review. Features include searchable claim databases, automated evidence collection, and customizable reporting, aimed at IP professionals, litigators, and businesses seeking competitive insight.
image: https://claimhit.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.claimhit.com.
  name: claimhit-com MCP Server
  slug: claimhit-com-mcp-yml
modified: '2026-10-29'
name: claimhit-com
nav: Providers
network: true
overview: 'claimhit-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Patents, Intelligence, Legal Tech, and IP.


  claimhit-com''s developer surface includes authentication, engineering blog, pricing, support, getting-started guide, and 19 more developer resources.'
plans:
- name: Claimhit Com Plans Pricing
  plan_count: 3
  slug: claimhit-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Claimhit Com Rate Limits
  slug: claimhit-com-rate-limits
scopes:
- name: Claimhit Com Scopes
  scope_count: 0
  slug: claimhit-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 75.8
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/claimhit-com/claimhit-com-2026-11-03T124259.png
security:
- kind: authentication
  name: Claimhit Com Authentication
  slug: claimhit-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Claimhit Com Domain Security
  slug: claimhit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Claimhit Com Vulnerability Disclosure
  slug: claimhit-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Claimhit Com Trust Center
  slug: claimhit-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: claimhit-com
tags:
- Company
- Patents
- Intelligence
- Legal Tech
- IP
website: https://claimhit.com/
---
