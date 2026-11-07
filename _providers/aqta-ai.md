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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Aqta's Seal product providing AI verification and receipt generation.
  name: Seal API
  slug: seal-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: Compliance
  url: https://aqta.ai/trust
- group: agent
  href: https://artifacts.apis.io/aqta-ai/llms/aqta-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aqta-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/aqta-ai/mcp/aqta-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aqta-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aqta-ai/well-known/aqta-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aqta-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/aqta-ai/well-known/aqta-ai-doc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aqta-ai-doc-security.txt
- group: auth
  href: https://artifacts.apis.io/aqta-ai/well-known/aqta-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aqta-ai-app-security.txt
- group: auth
  href: https://artifacts.apis.io/aqta-ai/well-known/aqta-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aqta-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/aqta-ai/well-known/aqta-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aqta-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aqta-ai/hosts/aqta-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aqta-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aqta-ai/vendors/aqta-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aqta-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aqta.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://app.aqta.ai/support
- group: operate
  title: ''
  type: StatusPage
  url: https://app.aqta.ai/status
- group: auth
  title: ''
  type: Security
  url: https://app.aqta.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aqta.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://aqta.ai/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aqta-ai
- group: company
  title: ''
  type: Blog
  url: https://aqta.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://doc.aqta.ai/
- group: auth
  href: https://artifacts.apis.io/aqta-ai/security/aqta-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aqta-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aqta-ai/security/aqta-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aqta-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aqta-ai/security/aqta-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aqta-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aqta.ai/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are client‑side rendered JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://doc.aqta.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Aqta builds AI verification products that ensure autonomous agents act within approved parameters. Their flagship Seal product checks and signs AI decisions before they are executed, providing an auditable receipt. Testera offers free language‑learning AI tutors in over 20 languages. Based in Dublin, the team combines AI safety expertise with cloud security and risk consulting to create transparent, verifiable AI workflows for enterprises and developers.
image: https://aqta.ai/og-aqta-2026-10-25.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at app.aqta.ai.
  name: Aqta MCP Server
  slug: aqta-ai-mcp-yml
modified: '2026-11-01'
name: Aqta
nav: Providers
network: true
overview: 'Aqta is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Verification, Transparency, Dublin, and Startups.


  Aqta''s developer surface includes support, engineering blog, documentation, and 20 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.5
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 21.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aqta Ai Domain Security
  slug: aqta-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aqta Ai Vulnerability Disclosure
  slug: aqta-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aqta Ai Trust Center
  slug: aqta-ai-trust-center
  summary_line: HIPAA, GDPR
slug: aqta-ai
tags:
- Artificial Intelligence
- Verification
- Transparency
- Dublin
- Startups
website: https://aqta.ai/
---
