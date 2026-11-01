---
access_model:
  confidence: high
  label: Paid plans from $79/mo, demo-led signup
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.demandsphere.com/pricing/
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Demandsphere Agentic Access
  operation_count: 10
  slug: demandsphere-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://api.demandsphere.com
  baseurl_source: declared
  description: The Keywords API from DemandSphere — 6 operation(s) for keywords.
  name: DemandSphere Keywords API
  slug: demandsphere-keywords-api
- baseURL: https://api.demandsphere.com
  baseurl_source: declared
  description: The Pages API from DemandSphere — 1 operation(s) for pages.
  name: DemandSphere Pages API
  slug: demandsphere-pages-api
- baseURL: https://api.demandsphere.com
  baseurl_source: declared
  description: The SearchEngines API from DemandSphere — 1 operation(s) for searchengines.
  name: DemandSphere SearchEngines API
  slug: demandsphere-searchengines-api
- baseURL: https://api.demandsphere.com
  baseurl_source: declared
  description: The Sites API from DemandSphere — 2 operation(s) for sites.
  name: DemandSphere Sites API
  slug: demandsphere-sites-api
artifact_total: 21
collections:
- collection_type: open
  name: DemandSphere API v5.0 Documentation Keywords API
  slug: open-demandsphere-keywords-api
- collection_type: open
  name: DemandSphere API v5.0 Documentation Keywords Pages API
  slug: open-demandsphere-pages-api
- collection_type: open
  name: DemandSphere API v5.0 Documentation Keywords SearchEngines API
  slug: open-demandsphere-searchengines-api
- collection_type: open
  name: DemandSphere API v5.0 Documentation Keywords Sites API
  slug: open-demandsphere-sites-api
common:
- group: other
  href: https://artifacts.apis.io/demandsphere/capabilities/demandsphere-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/demandsphere-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/demandsphere/overlays/demandsphere-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/demandsphere-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/demandsphere/security/demandsphere-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/demandsphere-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/demandsphere/security/demandsphere-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/demandsphere-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/demandsphere/security/demandsphere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demandsphere-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/demandsphere/authentication/demandsphere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demandsphere-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://demandsphere.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.demandsphere.com/solutions/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://help.demandsphere.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.demandsphere.com/platform/apis/rest-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.demandsphere.com/platform/apis/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demandsphere.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.demandsphere.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.demandsphere.com/resources/help-center/
- group: start
  title: ''
  type: SignUp
  url: https://www.demandsphere.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demandsphere.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.demandsphere.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DemandSphereDev
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demandsphere.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.demandsphere.com/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.demandsphere.com/security/
- group: auth
  title: ''
  type: Security
  url: https://www.demandsphere.com/security/
- group: agent
  href: https://artifacts.apis.io/demandsphere/mcp/demandsphere-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/demandsphere-mcp.yml
- group: agent
  href: https://artifacts.apis.io/demandsphere/llms/demandsphere-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demandsphere-llms.txt
- group: agent
  href: https://artifacts.apis.io/demandsphere/well-known/demandsphere-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/demandsphere-well-known.yml
- group: design
  href: https://artifacts.apis.io/demandsphere/lifecycle/demandsphere-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demandsphere-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/demandsphere/conformance/demandsphere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/demandsphere-conformance.yml
- group: build
  href: https://artifacts.apis.io/demandsphere/packages/demandsphere-packages.yml
  title: ''
  type: Packages
  url: packages/demandsphere-packages.yml
- group: agent
  href: https://artifacts.apis.io/demandsphere/agentic-access/demandsphere-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/demandsphere-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/demandsphere/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/demandsphere/mcp/demandsphere-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/demandsphere-tool-crosswalk.yml
- group: commercial
  href: https://artifacts.apis.io/demandsphere/plans/demandsphere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demandsphere-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/demandsphere/rate-limits/demandsphere-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/demandsphere-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/demandsphere/changelog/demandsphere-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/demandsphere-changelog.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.demandsphere.com/resources/help-center/
created: '2026-07-17'
description: DemandSphere is a unified AI search visibility platform (founded 2010, Y Combinator S10) that tracks brand presence across traditional search engine results pages, AI search engines (ChatGPT, Gemini, Perplexity, AI Overviews, AI Mode), and agentic surfaces. Its modular products cover DemandMetrics SERP analytics, DemandMetrics for Gen AI (LLM visibility and citation tracking), DemandSphere Agents workflow automation, Analytics AX log-file analytics, and Search Intelligence, a BigQuery data warehouse. The DemandSphere REST API (v5.0) exposes rank tracking, ranking trends, keyword groups, local rankings, landing matches, search-engine summaries, and site hierarchy data as JSON over api-key authentication, across 200+ markets and 10+ search engines, and is complemented by a first-party Model Context Protocol (MCP) server for agent access.
finops:
- has_sources: true
  method: derived
  name: Demandsphere Finops
  primary_unit: gb
  service_category: ''
  slug: demandsphere-finops
  template: false
image: https://www.demandsphere.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at www.demandsphere.com; 8 tools listed.
  name: DemandSphere MCP Server
  slug: demandsphere-mcp-yml
modified: '2026-08-13'
name: DemandSphere
nav: Providers
network: true
overview: 'DemandSphere publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Keywords API, Pages API, SearchEngines API, and 1 more. Tagged areas include Company, SEO, Search Intelligence, SERP Analytics, and AI Search.


  DemandSphere''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 28 more developer resources.'
plans:
- name: Demandsphere Plans Pricing
  plan_count: 7
  slug: demandsphere-plans-pricing
- name: Demandsphere Price Estimates
  plan_count: 0
  slug: demandsphere-price-estimates
random_paper: 16
rate_limits:
- limit_count: 0
  name: Demandsphere Rate Limits
  slug: demandsphere-rate-limits
score:
  band: strong
  composite: 60.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 58.9
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/demandsphere/demandsphere-2026-07-25T211708.png
security:
- kind: authentication
  name: Demandsphere Authentication
  slug: demandsphere-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Demandsphere Domain Security
  slug: demandsphere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Demandsphere Vulnerability Disclosure
  slug: demandsphere-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Demandsphere Trust Center
  slug: demandsphere-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: Audit landing pages against ranking keywords
  slug: demandsphere-audit-landing-pages
- name: Compare search engine performance
  slug: demandsphere-compare-search-engine-performance
- name: Track keyword ranking trends
  slug: demandsphere-track-ranking-trends
slug: demandsphere
tags:
- Company
- SEO
- Search Intelligence
- SERP Analytics
- AI Search
- LLM Visibility
- Rank Tracking
- Analytics
- MCP
website: https://demandsphere.com
---
