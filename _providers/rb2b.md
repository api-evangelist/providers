---
access_model:
  confidence: high
  label: Free plan plus paid tiers; API credits sold separately
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.rb2b.com/pricing
  - https://ui.api.rb2b.com/signup
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: Credit-metered Identification endpoints that convert anonymous web signals (IP addresses) into business identifiers — POST /ip_to_company, POST /ip_to_hem (hashed email, ranked by confidence) and POST
  name: RB2B Identification API
  slug: rb2b-identification-api
- description: 'Credit-metered Enrichment endpoints that take a known identifier — hashed email (MD5), plaintext email, or LinkedIn slug — and return additional B2B attributes: POST /hem_to_linkedin, /hem_to_best_lin'
  name: RB2B Enrichment API
  slug: rb2b-enrichment-api
- description: The domain-management and usage API for RB2B OEM partners embedding RB2B identification inside their own platforms — POST /add_domain, POST /delete_domain, GET /domains and GET /credit_usage, authenti
  name: RB2B OEM Partner API
  slug: rb2b-oem-partner-api
- description: 'The RB2B JavaScript pixel installed in a site header (or via Google Tag Manager / Segment / RudderStack / Shopify / Webflow / WordPress / HubSpot CMS / Wix / Next.js / React / Angular) is the primary '
  name: RB2B Pixel and Destination Webhooks
  slug: rb2b-pixel-webhooks
artifact_total: 12
asyncapis:
- description: ''
  name: Rb2B Webhooks
  slug: rb2b-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.rb2b.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.rb2b.com/en/
- group: operate
  title: ''
  type: Support
  url: https://support.rb2b.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.rb2b.com/en/collections/7815667-script-installation
- group: company
  title: ''
  type: Blog
  url: https://www.rb2b.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rb2b.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ui.api.rb2b.com/signup
- group: start
  title: ''
  type: Login
  url: https://ui.api.rb2b.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rb2b.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rb2b.com/privacy-policy
- group: company
  title: ''
  type: Partner
  url: https://www.rb2b.com/partner
- group: other
  title: ''
  type: APIs
  url: https://retention.com/apis
- group: start
  title: ''
  type: APIPortal
  url: https://ui.api.rb2b.com
- group: company
  title: ''
  type: APIPartnerProgram
  url: https://support.rb2b.com/en/articles/12579426-rb2b-s-oem-partner-program
- group: build
  title: ''
  type: Library
  url: https://library.rb2b.com
- group: operate
  title: ''
  type: Contact
  url: mailto:support@rb2b.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RetentionAdam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rb2b
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/retentiondotcom/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rb2b-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rb2b-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rb2b-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/rb2b-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rb2b-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rb2b-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rb2b-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rb2b-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rb2b-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rb2b-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rb2b-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rb2b-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rb2b-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.rb2b.com/en/articles/10442291-changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/rb2b-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rb2b-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rb2b-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/rb2b-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rb2b-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rb2b-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rb2b-domain-security.yml
created: '2026-05-25'
description: RB2B is a US-focused B2B website visitor identification platform that resolves anonymous web traffic into person-level leads — names, LinkedIn profiles, hashed and plaintext business emails, mobile ad IDs, and full business profiles — and pushes them to sales, marketing, and ad-tech systems. The product is delivered as a JavaScript pixel plus a knowledge- base and pipeline of 50+ destination integrations (Slack, Microsoft Teams, Salesforce, HubSpot, Clay, Zapier, Apollo, Customer.io, Demandbase, and others), with global company-level identification and US-only person- level resolution. RB2B operates a separate API Partner Program at api.rb2b.com/api/v1 that exposes credit-metered Identification endpoints (IP → Company, IP → HEM, IP → MAID) and Enrichment endpoints (HEM/Email → LinkedIn, HEM/Email → Business Profile, HEM/Email → MAID, LinkedIn → Hashed Emails, LinkedIn → Personal Email, LinkedIn → Mobile Phone, LinkedIn → Business Profile) for SaaS developers, GTM engineers,
  retailers, and ad-tech platforms that want to embed identity resolution into their own apps and identity graphs. A separate OEM Partner API at app.rb2b.com/api/v1 manages authorized domains and credit usage for partners embedding RB2B in their own products. RB2B publishes no OpenAPI; the only machine-readable description of its API is its own first-party MCP server, @rb2b/rb2b-apis-mcp, which exposes 19 tools over the same endpoints. The platform is SOC 2 Type 2 certified and CCPA compliant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rb2b.png
layout: provider
mcp_servers:
- description: ''
  name: rb2b-apis-mcp
  slug: rb2b-apis-mcp
- description: ''
  name: rb2b-mcp.yml
  slug: rb2b-mcpyml
modified: '2026-08-12'
name: RB2B
nav: Providers
network: true
overview: 'RB2B publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Identity Resolution, Visitor Identification, B2B Data, Lead Generation, and Sales Intelligence.


  The RB2B catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RB2B''s developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, CLI, and 34 more developer resources.'
plans:
- name: Rb2B Plans Pricing
  plan_count: 5
  slug: rb2b-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Rb2B Rate Limits
  slug: rb2b-rate-limits
score:
  band: strong
  composite: 60.9
  delta: 48.6
  facets:
    commercial_clarity: 92.1
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 12.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/rb2b/refs/heads/main/screenshots/rb2b-2026-06-20T192625.png
security:
- kind: authentication
  name: Rb2B Authentication
  slug: rb2b-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rb2B Domain Security
  slug: rb2b-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rb2B Trust Center
  slug: rb2b-trust-center
  summary_line: SOC 2 Type 2, CCPA, GDPR
slug: rb2b
tags:
- Identity Resolution
- Visitor Identification
- B2B Data
- Lead Generation
- Sales Intelligence
- Marketing
- Data Enrichment
- LinkedIn Enrichment
- Hashed Email
- Mobile Ad ID
- Firmographics
- Webhooks
- Pixel
- Adtech
- Identity Graph
- MCP
website: https://www.rb2b.com
---
