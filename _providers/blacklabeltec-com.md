---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Blacklabeltec Com Agentic Access
  operation_count: 4
  slug: blacklabeltec-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Read-only access to canonical company facts, the public product catalog, and released research datasets.
  name: BlackLabel Public Evidence API
  slug: blacklabel-public-evidence-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/blacklabeltec-com/agentic-access/blacklabeltec-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blacklabeltec-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/blacklabeltec-com/plans/blacklabeltec-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blacklabeltec-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blacklabeltec-com/rules/blacklabeltec-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blacklabeltec-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/blacklabeltec-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blacklabeltec-com/errors/blacklabeltec-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blacklabeltec-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blacklabeltec-com/conformance/blacklabeltec-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blacklabeltec-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blacklabeltec-com/llms/blacklabeltec-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blacklabeltec-com-llms.txt
- group: build
  href: https://artifacts.apis.io/blacklabeltec-com/mcp/blacklabeltec-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blacklabeltec-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/blacklabeltec-com/mcp/blacklabeltec-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blacklabeltec-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/blacklabeltec-com/well-known/blacklabeltec-com-tryacee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blacklabeltec-com-tryacee-security.txt
- group: auth
  href: https://artifacts.apis.io/blacklabeltec-com/well-known/blacklabeltec-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blacklabeltec-com-security.txt
- group: agent
  href: https://artifacts.apis.io/blacklabeltec-com/well-known/blacklabeltec-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blacklabeltec-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blacklabeltec-com/hosts/blacklabeltec-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacklabeltec-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blacklabeltec-com/vendors/blacklabeltec-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blacklabeltec-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/blacklabeltec-com/packages/blacklabeltec-com-packages.yml
  title: ''
  type: SDKs
  url: packages/blacklabeltec-com-packages.yml
- group: build
  href: https://artifacts.apis.io/blacklabeltec-com/packages/blacklabeltec-com-packages.yml
  title: ''
  type: Packages
  url: packages/blacklabeltec-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://blacklabeltec.com/trust
- group: auth
  title: ''
  type: Security
  url: https://blacklabeltec.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://blacklabeltec.com/company/press
- group: start
  title: ''
  type: GettingStarted
  url: https://blacklabeltec.com/products/permission-onboarding
- group: auth
  href: https://artifacts.apis.io/blacklabeltec-com/security/blacklabeltec-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blacklabeltec-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blacklabeltec-com/security/blacklabeltec-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacklabeltec-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blacklabeltec.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://blacklabeltec.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://blacklabeltec.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://blacklabeltec.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://blacklabeltec.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://blacklabeltec.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blacklabeltec.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blacklabeltec.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/black-label-tec
created: '2026-10-29'
description: BlackLabel Tech is a Gulf Shores, Alabama-based software, cybersecurity and AI automation company that builds custom desktop, mobile and web applications, AI assistants, workflow automation tools, and business platforms. It offers products such as AI Front Desk, Sales Operator, and provides custom software development services. The company operates under the trade name of Black Label Trading L.L.C., Newnan, Georgia.
image: https://blacklabeltec.com/brand/bl-mark.png?v=3
layout: provider
mcp_servers:
- description: Remote MCP server at blacklabeltec.com.
  name: blacklabeltec-com MCP Server
  slug: blacklabeltec-com-mcp-yml
modified: '2026-10-29'
name: blacklabeltec-com
nav: Providers
network: true
overview: 'blacklabeltec-com is listed with 1 API on the [APIs.io](https://apis.io/) network: BlackLabel Public Evidence API. Tagged areas include Software, Artificial Intelligence, Automation, Cybersecurity, and Custom Software.


  The blacklabeltec-com catalog on APIs.io includes 1 Spectral governance ruleset.


  blacklabeltec-com''s developer surface includes getting-started guide, documentation, API reference, pricing, support, and 26 more developer resources.'
plans:
- name: Blacklabeltec Com Plans Pricing
  plan_count: 3
  slug: blacklabeltec-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Blacklabeltec Com Rate Limits
  slug: blacklabeltec-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: blacklabeltec-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: blacklabeltec-com-rules
scopes:
- name: Blacklabeltec Com Scopes
  scope_count: 0
  slug: blacklabeltec-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 35.0
    discoverability: 75.8
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blacklabeltec Com Authentication
  slug: blacklabeltec-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Blacklabeltec Com Domain Security
  slug: blacklabeltec-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blacklabeltec Com Vulnerability Disclosure
  slug: blacklabeltec-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: get-build-evidence
  slug: blacklabeltec-com-get-build-evidence
- name: get-company-facts
  slug: blacklabeltec-com-get-company-facts
- name: get-product
  slug: blacklabeltec-com-get-product
- name: list-products
  slug: blacklabeltec-com-list-products
slug: blacklabeltec-com
tags:
- Software
- Artificial Intelligence
- Automation
- Cybersecurity
- Custom Software
website: https://blacklabeltec.com/
---
