---
access_model:
  confidence: high
  label: Usage-Based
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.clerk.io/pricing
  - https://www.clerk.io/free-trial
  - plans/clerk-io-plans-pricing.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Clerk.js is the browser-side JavaScript library for embedding Clerk.io recommendation slots, search, and email opens on a storefront, with Liquid templating support and event tracking.
  name: Clerk.js Client Library
  slug: clerkjs
- description: The Accessories API from Clerk.io — 1 operation(s) for accessories.
  name: Clerk.io Accessories API
  slug: clerk-io-accessories-api
- description: The Audiences API from Clerk.io — 3 operation(s) for audiences.
  name: Clerk.io Audiences API
  slug: clerk-io-audiences-api
- description: The Campaigns API from Clerk.io — 2 operation(s) for campaigns.
  name: Clerk.io Campaigns API
  slug: clerk-io-campaigns-api
- description: The Catalog API from Clerk.io — 5 operation(s) for catalog.
  name: Clerk.io Catalog API
  slug: clerk-io-catalog-api
- description: The Logging API from Clerk.io — 9 operation(s) for logging.
  name: Clerk.io Logging API
  slug: clerk-io-logging-api
- description: The Merchandising API from Clerk.io — 4 operation(s) for merchandising.
  name: Clerk.io Merchandising API
  slug: clerk-io-merchandising-api
- description: The Parcels API from Clerk.io — 1 operation(s) for parcels.
  name: Clerk.io Parcels API
  slug: clerk-io-parcels-api
- description: The Privacy API from Clerk.io — 2 operation(s) for privacy.
  name: Clerk.io Privacy API
  slug: clerk-io-privacy-api
- description: The Product Data API from Clerk.io — 4 operation(s) for product data.
  name: Clerk.io Product Data API
  slug: clerk-io-product-data-api
- description: The Recommendations API from Clerk.io — 25 operation(s) for recommendations.
  name: Clerk.io Recommendations API
  slug: clerk-io-recommendations-api
- description: The Search API from Clerk.io — 6 operation(s) for search.
  name: Clerk.io Search API
  slug: clerk-io-search-api
- description: The Subscribers API from Clerk.io — 2 operation(s) for subscribers.
  name: Clerk.io Subscribers API
  slug: clerk-io-subscribers-api
- description: The Tokens API from Clerk.io — 1 operation(s) for tokens.
  name: Clerk.io Tokens API
  slug: clerk-io-tokens-api
artifact_total: 24
collections:
- collection_type: open
  name: Clerk.io API
  slug: open-clerk-io
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/clerk-io-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clerk-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerk-io-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clerkio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clerk-io
- group: company
  title: ''
  type: Website
  url: https://www.clerk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clerk.io/
- group: other
  title: ''
  type: Knowledgebase
  url: https://help.clerk.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clerk.io/
- group: company
  title: ''
  type: Blog
  url: https://www.clerk.io/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clerk.io/pricing
- group: company
  title: ''
  type: Partners
  url: https://www.clerk.io/partners
- group: auth
  title: ''
  type: Trust Center
  url: https://trust.clerk.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clerk.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clerk.io/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clerk-io-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clerk-io-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.clerk.io/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clerk-io-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.clerk.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clerk.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clerk.io/docs/how-the-clerkio-platform-works
- group: operate
  title: ''
  type: Support
  url: https://help.clerk.io/
- group: start
  title: ''
  type: SignUp
  url: https://www.clerk.io/free-trial
- group: start
  title: ''
  type: Login
  url: https://my.clerk.io/
- group: build
  title: ''
  type: Packages
  url: packages/clerk-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clerk-io-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clerk-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clerk-io-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clerk-io-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/clerk-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.clerk.io/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clerk-io-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clerk-io-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clerk-io-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clerk-io-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/clerk-io-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clerk-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clerk-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clerk-io-finops.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2025-02-08'
description: Clerk.io is an e-commerce personalization platform that uses artificial intelligence and machine learning to deliver tailored product recommendations, on-site search results, audience-segmented email campaigns, and merchandising controls for online retailers. The platform exposes a REST API for product, category, order, and customer data ingestion, plus client-side JavaScript and Liquid templating for recommendation slots and search experiences.
finops:
- name: Clerk Io Finops
  service_category: API
  slug: clerk-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clerk-io.png
jsonld:
- class_count: 0
  name: Clerk Io Context
  property_count: 5
  slug: clerk-io-context
layout: provider
mcp_servers:
- description: ''
  name: Clerk.io MCP Server
  slug: clerkio-mcp-server
modified: '2026-08-13'
name: Clerk.io
nav: Providers
network: true
overview: 'Clerk.io publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accessories API, Audiences API, Campaigns API, and 10 more. Tagged areas include Artificial Intelligence, Commerce, E-Commerce, Email Marketing, and Personalization.


  The Clerk.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clerk.io''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Clerk Io Plans Pricing
  plan_count: 5
  slug: clerk-io-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Clerk Io Rate Limits
  slug: clerk-io-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Clerk.io API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clerk-io-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 50.0
    contract_quality: 62.0
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 50.0
    operational_transparency: 2.6
  previous_composite: 58.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clerk-io/refs/heads/main/screenshots/clerk-io-2026-06-20T174507.png
security:
- kind: authentication
  name: Clerk Io Authentication
  slug: clerk-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Clerk Io Domain Security
  slug: clerk-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clerk Io Trust Center
  slug: clerk-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: clerk-io
tags:
- Artificial Intelligence
- Commerce
- E-Commerce
- Email Marketing
- Personalization
- Recommendations
- Search
website: https://www.clerk.io/
---
