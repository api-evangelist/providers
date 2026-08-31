---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Builtwith Agentic Access
  operation_count: 20
  slug: builtwith-agentic-access
  summary_line: 20 operations · 1 acting
api_count: 10
apis:
- description: Current and historical website technology information for single or multiple domains with support for JSON, XML, and CSV formats.
  name: BuiltWith Domain API
  slug: builtwith-domain-api
- description: Retrieve lists of websites using specific web technologies in XML, JSON, TXT, CSV, and TSV formats.
  name: BuiltWith Lists API
  slug: builtwith-lists-api
- description: Access technology trend data showing adoption and growth of web technologies over time.
  name: BuiltWith Trends API
  slug: builtwith-trends-api
- description: Track technology additions and removals on websites with business context in JSON format.
  name: BuiltWith Change API
  slug: builtwith-change-api
- description: Website interconnection data revealing domain relationships via shared IPs, analytics, and other attributes.
  name: BuiltWith Relationships API
  slug: builtwith-relationships-api
- description: Free tier API providing technology group counts and last-updated timestamps for website domains.
  name: BuiltWith Free API
  slug: builtwith-free-api
- description: Natural language website lookups returning technology profile data in JSON and CSV formats.
  name: BuiltWith Ask API
  slug: builtwith-ask-api
- description: Real-time WebSocket feed of technology detections as they happen across the web.
  name: BuiltWith Live Feed API
  slug: builtwith-live-feed-api
- description: Resolve company names to their associated domain names in JSON and XML formats.
  name: BuiltWith Company to URL API
  slug: builtwith-company-to-url-api
- description: Retrieve related domains associated with IPs and other website attributes.
  name: BuiltWith Tags API
  slug: builtwith-tags-api
- description: Get technology suggestions based on a website's existing technology profile.
  name: BuiltWith Recommendations API
  slug: builtwith-recommendations-api
- description: Find websites that use specific keywords in their content.
  name: BuiltWith Keywords API
  slug: builtwith-keywords-api
- description: Search websites by keyword content returning results in JSON and CSV formats.
  name: BuiltWith Keyword Search API
  slug: builtwith-keyword-search-api
- description: Text-based technology searches using vector embeddings for semantic similarity matching.
  name: BuiltWith Vector Search API
  slug: builtwith-vector-search-api
- description: Access website redirect chain data to understand domain redirect patterns.
  name: BuiltWith Redirects API
  slug: builtwith-redirects-api
- description: eCommerce product lookup for identifying products and merchants across the web.
  name: BuiltWith Product API
  slug: builtwith-product-api
- description: Website trustworthiness assessment providing reliability and safety scores for domains.
  name: BuiltWith Trust API
  slug: builtwith-trust-api
- description: Access financial data from SEC Edgar and UK Companies House filings for domains, including revenue, assets, and equity data.
  name: BuiltWith Financial API
  slug: builtwith-financial-api
- description: Batch domain processing for high-volume technology lookups across large domain lists.
  name: BuiltWith Bulk Domain API
  slug: builtwith-bulk-domain-api
- description: Model Context Protocol server integration enabling AI assistants to query BuiltWith technology detection data natively.
  name: BuiltWith MCP API
  slug: builtwith-mcp-api
- description: Asynchronous batch domain processing
  name: BuiltWith Bulk Processing API
  slug: builtwith-bulk-processing-api
- description: Single or multi-domain technology detection endpoints
  name: BuiltWith Domain Lookup API
  slug: builtwith-domain-lookup-api
- description: Identify domain interconnections via shared identifiers
  name: BuiltWith Domain Relationships API
  slug: builtwith-domain-relationships-api
- description: Technology count lookups for free tier
  name: BuiltWith Free Lookup API
  slug: builtwith-free-lookup-api
- description: Lookup domains by IP or attribute identifier
  name: BuiltWith Tag Lookup API
  slug: builtwith-tag-lookup-api
- description: Track technology additions and removals on websites
  name: BuiltWith Technology Changes API
  slug: builtwith-technology-changes-api
- description: Retrieve websites using specific technologies
  name: BuiltWith Technology Lists API
  slug: builtwith-technology-lists-api
- description: Technology adoption trends and market share data
  name: BuiltWith Technology Trends API
  slug: builtwith-technology-trends-api
- description: The AgentAuth API from BuiltWith — 2 operation(s) for agentauth.
  name: BuiltWith Agent Auth API
  slug: builtwith-agentauth-api
- description: The AgentPayments API from BuiltWith — 3 operation(s) for agentpayments.
  name: BuiltWith Agent Payments API
  slug: builtwith-agentpayments-api
- description: The Ask API from BuiltWith — 1 operation(s) for ask.
  name: BuiltWith Ask API
  slug: builtwith-ask-api
- description: The Change API from BuiltWith — 1 operation(s) for change.
  name: BuiltWith Change API
  slug: builtwith-change-api
- description: The Company Research API from BuiltWith — 4 operation(s) for company research.
  name: BuiltWith Company Research API
  slug: builtwith-company-research-api
- description: The CompanyToUrl API from BuiltWith — 1 operation(s) for companytourl.
  name: BuiltWith Company To URL API
  slug: builtwith-companytourl-api
- description: The Domain API from BuiltWith — 4 operation(s) for domain.
  name: BuiltWith Domain API
  slug: builtwith-domain-api
- description: The Domain Intelligence API from BuiltWith — 2 operation(s) for domain intelligence.
  name: BuiltWith Domain Intelligence API
  slug: builtwith-domain-intelligence-api
- description: The Financial API from BuiltWith — 1 operation(s) for financial.
  name: BuiltWith Financial API
  slug: builtwith-financial-api
- description: The Free API from BuiltWith — 1 operation(s) for free.
  name: BuiltWith Free API
  slug: builtwith-free-api
- description: The Keywords API from BuiltWith — 1 operation(s) for keywords.
  name: BuiltWith Keywords API
  slug: builtwith-keywords-api
- description: The KeywordSearch API from BuiltWith — 1 operation(s) for keywordsearch.
  name: BuiltWith Keyword Search API
  slug: builtwith-keywordsearch-api
- description: The List Passes API from BuiltWith — 2 operation(s) for list passes.
  name: BuiltWith List Passes API
  slug: builtwith-list-passes-api
- description: The Lists API from BuiltWith — 1 operation(s) for lists.
  name: BuiltWith Lists API
  slug: builtwith-lists-api
- description: The Meta API from BuiltWith — 2 operation(s) for meta.
  name: BuiltWith Meta API
  slug: builtwith-meta-api
- description: The Mppx API from BuiltWith — 3 operation(s) for mppx.
  name: BuiltWith Mppx API
  slug: builtwith-mppx-api
- description: The Product API from BuiltWith — 1 operation(s) for product.
  name: BuiltWith Product API
  slug: builtwith-product-api
- description: The Recommendations API from BuiltWith — 1 operation(s) for recommendations.
  name: BuiltWith Recommendations API
  slug: builtwith-recommendations-api
- description: The Redirects API from BuiltWith — 1 operation(s) for redirects.
  name: BuiltWith Redirects API
  slug: builtwith-redirects-api
- description: The Relationships API from BuiltWith — 1 operation(s) for relationships.
  name: BuiltWith Relationships API
  slug: builtwith-relationships-api
- description: The Social API from BuiltWith — 1 operation(s) for social.
  name: BuiltWith Social API
  slug: builtwith-social-api
- description: The Tags API from BuiltWith — 1 operation(s) for tags.
  name: BuiltWith Tags API
  slug: builtwith-tags-api
- description: The Technology Discovery API from BuiltWith — 1 operation(s) for technology discovery.
  name: BuiltWith Technology Discovery API
  slug: builtwith-technology-discovery-api
- description: The Technology Intelligence API from BuiltWith — 3 operation(s) for technology intelligence.
  name: BuiltWith Technology Intelligence API
  slug: builtwith-technology-intelligence-api
- description: The Trends API from BuiltWith — 1 operation(s) for trends.
  name: BuiltWith Trends API
  slug: builtwith-trends-api
- description: The Trust and Risk API from BuiltWith — 1 operation(s) for trust and risk.
  name: BuiltWith Trust and Risk API
  slug: builtwith-trust-and-risk-api
- description: The Trust API from BuiltWith — 1 operation(s) for trust.
  name: BuiltWith Trust API
  slug: builtwith-trust-api
- description: The Vector API from BuiltWith — 1 operation(s) for vector.
  name: BuiltWith Vector API
  slug: builtwith-vector-api
- description: The Website Search API from BuiltWith — 1 operation(s) for website search.
  name: BuiltWith Website Search API
  slug: builtwith-website-search-api
artifact_total: 85
asyncapis:
- description: Real-time technology detection notifications over WebSocket. Subscribe to technology channels or rule channels and receive an event each time BuiltWith detects a technology on a website. Requires an a
  name: BuiltWith Live Feed API
  slug: builtwith-live-feed-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BuiltWith Change Bulk Processing API
  slug: open-builtwith-bulk-processing-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Domain Lookup API
  slug: open-builtwith-domain-lookup-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Domain Relationships API
  slug: open-builtwith-domain-relationships-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Free Lookup API
  slug: open-builtwith-free-lookup-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Tag Lookup API
  slug: open-builtwith-tag-lookup-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Technology Changes API
  slug: open-builtwith-technology-changes-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Technology Lists API
  slug: open-builtwith-technology-lists-api
- collection_type: open
  name: BuiltWith Change Bulk Processing Technology Trends API
  slug: open-builtwith-technology-trends-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/builtwith-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/builtwith-pay-per-call-with-x402.md
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/builtwith/builtwith-mcp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/builtwith/builtwith-mcp/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/builtwith/builtwith-mcp/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/builtwith-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/builtwith-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/builtwith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/builtwith-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://builtwith.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.builtwith.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/builtwith
- group: company
  title: ''
  type: Blog
  url: https://blog.builtwith.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://builtwith.com/plans
- group: other
  title: ''
  type: X
  url: https://x.com/builtwith
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.builtwith.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/builtwithcom/builtwith/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/builtwith-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/builtwith-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/builtwith-finops.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/builtwith-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/builtwith-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/builtwith-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/builtwith-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/builtwith-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/builtwith-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/builtwith-security.txt
- group: auth
  title: ''
  type: Security
  url: https://builtwith.com/.well-known/security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/builtwith-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/builtwith-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/builtwith-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/builtwith-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/builtwith-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/builtwith-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/builtwith-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/builtwith-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/builtwith-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/builtwith-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/builtwith-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/builtwith-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/builtwith-live-feed-asyncapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/builtwith-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/builtwith-domain-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/builtwith-change-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/builtwith-lists-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/builtwith-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/builtwith-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: Examples
  url: examples/builtwith-domain-example.json
- group: build
  title: ''
  type: Examples
  url: examples/builtwith-lists-example.json
- group: build
  title: ''
  type: Examples
  url: examples/builtwith-trends-example.json
- group: build
  title: ''
  type: Examples
  url: examples/builtwith-change-example.json
- group: other
  title: ''
  type: Overlay
  url: overlays/builtwith-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/builtwith-x402-pay-per-call-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.builtwith.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.builtwith.com/domain-api
- group: operate
  title: ''
  type: Support
  url: https://builtwith.com/contact
- group: operate
  title: ''
  type: SupportFAQs
  url: https://builtwith.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://builtwith.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://builtwith.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://builtwith.com/signup
- group: start
  title: ''
  type: Login
  url: https://builtwith.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/builtwith
created: 2026-06-13
description: Technology profiling and lead generation platform with a REST API for detecting technologies used by websites, tracking technology trends, and identifying technology adoption across 491.9 million domains and 115,907 tracked web technologies.
examples:
- key_count: 1
  name: Builtwith Change Example
  slug: builtwith-change-example
- key_count: 1
  name: Builtwith Domain Example
  slug: builtwith-domain-example
- key_count: 2
  name: Builtwith Lists Example
  slug: builtwith-lists-example
- key_count: 1
  name: Builtwith Trends Example
  slug: builtwith-trends-example
finops:
- name: Builtwith Finops
  service_category: ''
  slug: builtwith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/builtwith.png
json_schemas:
- name: BuiltWith Change API Result
  property_count: 1
  slug: builtwith-change
- name: BuiltWith Domain API Result
  property_count: 1
  slug: builtwith-domain
- name: BuiltWith Lists API Result
  property_count: 2
  slug: builtwith-lists
jsonld:
- class_count: 10
  name: Builtwith Context
  property_count: 52
  slug: builtwith-context
layout: provider
mcp_servers:
- description: ''
  name: BuiltWith MCP Server
  slug: builtwith-mcp-server
modified: 2026-08-14
name: BuiltWith
nav: Providers
network: true
overview: 'BuiltWith publishes 52 APIs on the [APIs.io](https://apis.io/) network, including Domain API, Lists API, Trends API, and 49 more. Tagged areas include Technology Profiling, Lead Generation, Web Intelligence, Technology Detection, and Website Analysis.


  The BuiltWith catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BuiltWith''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, code examples, API reference, and 56 more developer resources.'
plans:
- name: Builtwith Plans Pricing
  plan_count: 6
  slug: builtwith-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Builtwith Rate Limits
  slug: builtwith-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: BuiltWith API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: builtwith-jsonschema-spectral-rules
scopes:
- name: Builtwith Scopes
  scope_count: 2
  slug: builtwith-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 32
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -3.3
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 43.2
    contract_quality: 70.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 43.2
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/builtwith/refs/heads/main/screenshots/builtwith-2026-06-20T173756.png
security:
- kind: authentication
  name: Builtwith Authentication
  slug: builtwith-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Builtwith Domain Security
  slug: builtwith-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Builtwith Vulnerability Disclosure
  slug: builtwith-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: builtwith
tags:
- Technology Profiling
- Lead Generation
- Web Intelligence
- Technology Detection
- Website Analysis
- Market Research
- Technographics
- Sales Intelligence
- AI Agents
- MCP
- Agentic Commerce
- Real-time Data
website: https://builtwith.com/
---
