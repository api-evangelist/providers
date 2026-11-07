---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Beevr Ai Agentic Access
  operation_count: 9
  slug: beevr-ai-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The About API from BeevR — 1 operation(s) for about.
  name: BeevR About API
  slug: beevr-ai-about-api
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The Articles API from BeevR — 2 operation(s) for articles.
  name: BeevR Articles API
  slug: beevr-ai-articles-api
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The Case Studies API from BeevR — 2 operation(s) for case studies.
  name: BeevR Case Studies API
  slug: beevr-ai-case-studies-api
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The Health API from BeevR — 1 operation(s) for health.
  name: BeevR Health API
  slug: beevr-ai-health-api
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The Pricing API from BeevR — 1 operation(s) for pricing.
  name: BeevR Pricing API
  slug: beevr-ai-pricing-api
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The Search API from BeevR — 1 operation(s) for search.
  name: BeevR Search API
  slug: beevr-ai-search-api
- baseURL: https://beevr.ai/agent-api
  baseurl_source: declared
  description: The Services API from BeevR — 1 operation(s) for services.
  name: BeevR Services API
  slug: beevr-ai-services-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/beevr-ai/agentic-access/beevr-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beevr-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/beevr-ai/rules/beevr-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/beevr-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/beevr-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://beevr.ai/security
- group: design
  href: https://artifacts.apis.io/beevr-ai/errors/beevr-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beevr-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beevr-ai/conformance/beevr-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beevr-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beevr-ai/llms/beevr-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beevr-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/beevr-ai/a2a/beevr-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beevr-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/beevr-ai/mcp/beevr-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/beevr-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/beevr-ai/mcp/beevr-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beevr-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/beevr-ai/well-known/beevr-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beevr-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/beevr-ai/well-known/beevr-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beevr-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/beevr-ai/hosts/beevr-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beevr-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/beevr-ai/vendors/beevr-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beevr-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://beevr.ai/security
- group: auth
  href: https://artifacts.apis.io/beevr-ai/security/beevr-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/beevr-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/beevr-ai/security/beevr-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beevr-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beevr-ai/security/beevr-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beevr-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beevr.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://beevr.ai/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://beevr.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://beevr.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beevr-labs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beevr.ai/privacy
created: '2026-11-02'
description: BeevR is a founder-led software and frontier‑AI development studio based in Hanoi, Vietnam, serving clients worldwide. We ship production‑grade software and AI for regulated industries — fixed price, fixed timeline, and you own 100% of the code. Our services include custom software development, frontier AI solutions, HIPAA‑compliant healthcare software, PCI DSS fintech software, manufacturing & industrial software, compliance engineering, and MVP development for startups.
image: https://beevr.ai/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at beevr.ai.
  name: BeevR MCP Server
  slug: beevr-ai-mcp-yml
modified: '2026-11-02'
name: BeevR
nav: Providers
network: true
overview: 'BeevR publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including About API, Articles API, Case Studies API, and 4 more. Tagged areas include Software, Artificial Intelligence, Development, Vietnam, and Regulated Industries.


  The BeevR catalog on APIs.io includes 1 Spectral governance ruleset.


  BeevR''s developer surface includes API reference, support, engineering blog, and 21 more developer resources.'
plans:
- name: Beevr Ai Plans Pricing
  plan_count: 0
  slug: beevr-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Beevr Ai Rate Limits
  slug: beevr-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: BeevR API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: beevr-ai-rules
scopes:
- name: Beevr Ai Scopes
  scope_count: 0
  slug: beevr-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 41.7
    developer_ergonomics: 13.6
    discoverability: 65.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - vietnam
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beevr Ai Authentication
  slug: beevr-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Beevr Ai Domain Security
  slug: beevr-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Beevr Ai Vulnerability Disclosure
  slug: beevr-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Beevr Ai Trust Center
  slug: beevr-ai-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
skill_count: 7
skills:
- name: about-beevr
  slug: beevr-ai-about-beevr
- name: get-case-study
  slug: beevr-ai-get-case-study
- name: get-pricing
  slug: beevr-ai-get-pricing
- name: list-articles
  slug: beevr-ai-list-articles
- name: list-case-studies
  slug: beevr-ai-list-case-studies
- name: list-services
  slug: beevr-ai-list-services
- name: search-beevr
  slug: beevr-ai-search-beevr
slug: beevr-ai
tags:
- Software
- Artificial Intelligence
- Development
- Vietnam
- Regulated Industries
website: https://beevr.ai/
---
