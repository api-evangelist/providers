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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Demandsphere Agentic Access
  operation_count: 10
  slug: demandsphere-agentic-access
  summary_line: 10 operations · 10 acting
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: Overlay
  url: overlays/demandsphere-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/demandsphere-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/demandsphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demandsphere-domain-security.yml
- group: auth
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
  title: ''
  type: MCPServer
  url: mcp/demandsphere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demandsphere-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/demandsphere-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demandsphere-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/demandsphere-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/demandsphere-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demandsphere-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/demandsphere-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/demandsphere-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demandsphere-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/demandsphere-changelog.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.demandsphere.com/resources/help-center/
created: '2026-07-17'
description: DemandSphere is a unified AI search visibility platform (founded 2010, Y Combinator S10) that tracks brand presence across traditional search engine results pages, AI search engines (ChatGPT, Gemini, Perplexity, AI Overviews, AI Mode), and agentic surfaces. Its modular products cover DemandMetrics SERP analytics, DemandMetrics for Gen AI (LLM visibility and citation tracking), DemandSphere Agents workflow automation, Analytics AX log-file analytics, and Search Intelligence, a BigQuery data warehouse. The DemandSphere REST API (v5.0) exposes rank tracking, ranking trends, keyword groups, local rankings, landing matches, search-engine summaries, and site hierarchy data as JSON over api-key authentication, across 200+ markets and 10+ search engines, and is complemented by a first-party Model Context Protocol (MCP) server for agent access.
image: https://www.demandsphere.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: DemandSphere MCP Server
  slug: demandsphere-mcp-server
modified: '2026-08-13'
name: DemandSphere
nav: Providers
network: true
overview: 'DemandSphere publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Keywords API, Pages API, SearchEngines API, and 1 more. Tagged areas include Company, SEO, Search Intelligence, SERP Analytics, and AI Search.


  DemandSphere''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 27 more developer resources.'
plans:
- name: Demandsphere Plans Pricing
  plan_count: 3
  slug: demandsphere-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Demandsphere Rate Limits
  slug: demandsphere-rate-limits
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 53.6
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demandsphere/refs/heads/main/screenshots/demandsphere-2026-07-25T211708.png
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
  summary_line: disclosure policy published
- kind: trust-center
  name: Demandsphere Trust Center
  slug: demandsphere-trust-center
  summary_line: SOC 2, GDPR
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
