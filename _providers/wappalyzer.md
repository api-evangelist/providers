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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Wappalyzer Agentic Access
  operation_count: 9
  slug: wappalyzer-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 2
apis:
- description: Analyze a single website URL for technology stack detection, returning a detailed breakdown of all identified technologies, frameworks, and platforms.
  name: Wappalyzer Analyze API
  slug: wappalyzer-analyze-api
- description: Deep crawl API that indexes multiple pages of a website to build a comprehensive technology profile, supporting asynchronous callbacks for results delivery.
  name: Wappalyzer Crawl API
  slug: wappalyzer-crawl-api
- description: Bulk access to pre-built technographic datasets covering technology installations across millions of websites, suitable for market research and lead list generation.
  name: Wappalyzer Dataset API
  slug: wappalyzer-dataset-api
- description: The four anonymous, unauthenticated technology and category reference endpoints on the v2 host — the technology directory (7,281 entries), a single technology profile, the category directory (106 entr
  name: Wappalyzer Metadata API
  slug: wappalyzer-metadata-api
- description: First-party hosted Model Context Protocol server at https://mcp.wappalyzer.com/mcp — remote Streamable HTTP, OAuth 2.1 with PKCE and dynamic client registration, exposing three read-only tools and fou
  name: Wappalyzer MCP Server
  slug: wappalyzer-mcp
- description: Shared authentication, billing, and response conventions.
  name: Wappalyzer Basics API
  slug: wappalyzer-basics-api
- description: Lead list creation, pricing, and download lifecycle.
  name: Wappalyzer Lists API
  slug: wappalyzer-lists-api
- description: Website technology lookup and asynchronous crawl callbacks.
  name: Wappalyzer Lookup API
  slug: wappalyzer-lookup-api
- description: Dataset-backed website-serving subdomain discovery.
  name: Wappalyzer Subdomains API
  slug: wappalyzer-subdomains-api
- description: Email verification and deliverability checks.
  name: Wappalyzer Verify API
  slug: wappalyzer-verify-api
artifact_total: 32
asyncapis:
- description: ''
  name: Wappalyzer Webhooks
  slug: wappalyzer-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wappalyzer Public Basics API
  slug: open-wappalyzer-basics-api
- collection_type: open
  name: Wappalyzer Public Basics Lists API
  slug: open-wappalyzer-lists-api
- collection_type: open
  name: Wappalyzer Public Basics Lookup API
  slug: open-wappalyzer-lookup-api
- collection_type: open
  name: Wappalyzer Public Basics Subdomains API
  slug: open-wappalyzer-subdomains-api
- collection_type: open
  name: Wappalyzer Public Basics Verify API
  slug: open-wappalyzer-verify-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/wappalyzer/mcp/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wappalyzer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wappalyzer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wappalyzer-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wappalyzer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://api.wappalyzer.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/wappalyzer-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wappalyzer-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.wappalyzer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wappalyzer.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wappalyzer.com/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.wappalyzer.com/docs/api/v2/basics/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wappalyzer.com/docs/api/v2/basics/
- group: docs
  title: ''
  type: OpenAPI
  url: https://www.wappalyzer.com/openapi/v2-public.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wappalyzer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/wappalyzer-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wappalyzer-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wappalyzer-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wappalyzer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wappalyzer-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wappalyzer-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wappalyzer-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wappalyzer-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/wappalyzer-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wappalyzer-v2-public-overlay.yaml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wappalyzer-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/wappalyzer-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/wappalyzer-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wappalyzer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/wappalyzer/mcp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wappalyzer
- group: other
  title: ''
  type: X
  url: https://twitter.com/Wappalyzer
- group: company
  title: ''
  type: Blog
  url: https://www.wappalyzer.com/articles/
- group: operate
  title: ''
  type: Support
  url: https://www.wappalyzer.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.wappalyzer.com/faq/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wappalyzer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.wappalyzer.com/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wappalyzer.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wappalyzer.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wappalyzer.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/wappalyzer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wappalyzer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wappalyzer-finops.yml
created: '2026-06-13'
description: Technology detection REST API for identifying software, frameworks, CMS platforms, analytics tools, and other technologies used on any website. Provides programmatic access to technographic data via lookup, analyze, crawl, and dataset endpoints using a credit-based model.
examples:
- key_count: 3
  name: Wappalyzer Create List Example
  slug: wappalyzer-create-list-example
- key_count: 12
  name: Wappalyzer Verify Example
  slug: wappalyzer-verify-example
finops:
- name: Wappalyzer Finops
  service_category: ''
  slug: wappalyzer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wappalyzer.png
json_schemas:
- name: LookupResponse
  property_count: 0
  slug: wappalyzer-lookup-response
- name: Technology
  property_count: 7
  slug: wappalyzer-technology
- name: VerifyResult
  property_count: 12
  slug: wappalyzer-verify-result
jsonld:
- class_count: 7
  name: Wappalyzer Context
  property_count: 44
  slug: wappalyzer-context
layout: provider
mcp_servers:
- description: 'Wappalyzer ships two first-party MCP servers: a hosted remote Streamable-HTTP server at https://mcp.wappalyzer.com/mcp secured with OAuth 2.1 (the API key is resolved server-side from the signed-in Wa'
  name: Wappalyzer MCP Server
  slug: wappalyzer-mcp-server
modified: '2026-08-14'
name: Wappalyzer
nav: Providers
network: true
overview: 'Wappalyzer publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Basics API, Lists API, and 3 more. Tagged areas include Technology Detection, Technographics, Website Analysis, CMS Detection, and Framework Detection.


  The Wappalyzer catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Wappalyzer''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 37 more developer resources.'
plans:
- name: Wappalyzer Plans Pricing
  plan_count: 4
  slug: wappalyzer-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Wappalyzer Rate Limits
  slug: wappalyzer-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Wappalyzer API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: wappalyzer-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 27
    catalog_gap: 25.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 29.5
    contract_quality: 81.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 63.2
  previous_composite: 68.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 16.7
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wappalyzer/refs/heads/main/screenshots/wappalyzer-2026-06-20T201222.png
security:
- kind: authentication
  name: Wappalyzer Authentication
  slug: wappalyzer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wappalyzer Domain Security
  slug: wappalyzer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wappalyzer Vulnerability Disclosure
  slug: wappalyzer-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: wappalyzer
tags:
- Technology Detection
- Technographics
- Website Analysis
- CMS Detection
- Framework Detection
- Lead Enrichment
- Sales Intelligence
- Subdomain Discovery
- Email Verification
- Market Research
website: https://www.wappalyzer.com/
---
