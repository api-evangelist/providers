---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: A live remote Model Context Protocol endpoint that exposes DoubleVerify's media quality, verification and performance data to an AI assistant as the DV Neura Insight Agent. DoubleVerify states that cl
  name: DV Neura MCP Server
  slug: dv-neura-mcp-server
- description: DoubleVerify's asynchronous reporting API. A caller submits a data request, receives an ID, and retrieves the result as a CSV stream once the data is available; the request ID stays valid for 30 days.
  name: DV Report Data API
  slug: dv-report-data-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/doubleverify-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doubleverify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doubleverify.com
- group: company
  title: ''
  type: About
  url: https://doubleverify.com/company/about
- group: other
  title: ''
  type: Platform
  url: https://doubleverify.com
- group: other
  title: ''
  type: Pinnacle
  url: https://pinnacle.doubleverify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.doubleverify.com
- group: other
  title: ''
  type: KnowledgeHub
  url: https://doubleverify.com/knowledge-hub
- group: company
  title: ''
  type: Newsroom
  url: https://doubleverify.com/company/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.doubleverify.com
- group: company
  title: ''
  type: Careers
  url: https://doubleverify.com/company/careers
- group: operate
  title: ''
  type: Contact
  url: https://doubleverify.com/lp/contact
- group: operate
  title: ''
  type: Support
  url: https://doubleverify.com/lp/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doubleverify.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doubleverify.com/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DoubleVerify
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DoubleVerify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doubleverify
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/doubleverify
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DoubleVerifyInc
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/doubleverify
- group: company
  title: ''
  type: Blog
  url: https://doubleverify.com/blog/rss.xml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doubleverify-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doubleverify-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/doubleverify-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doubleverify-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doubleverify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.doubleverify.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doubleverify-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doubleverify.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doubleverify-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/doubleverify-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doubleverify-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doubleverify-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/doubleverify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doubleverify-rate-limits.yml
created: '2026-05-25'
description: 'DoubleVerify (NYSE: DV) is a New York-based software platform for digital media measurement, data, and analytics. The company''s Media Effectiveness Platform — branded DV MAP (Media AdVantage Platform) — verifies ad impressions across the open web, social, connected TV, and commerce networks, detecting fraud and invalid traffic (IVT), measuring viewability and attention, scoring brand suitability and contextual relevance, and attributing outcomes. The platform analyzes trillions of media transactions per year for advertisers, publishers, supply-side platforms, and ad marketplaces. Core products include DV Authentic Attention, DV Custom Contextual (a semantic-science contextual targeting engine across 200k+ concepts), DV Authentic Brand Suitability, the DV Publisher Suite, DV Marketplace Suite, and Scibids AI for AI-powered programmatic bidding. DoubleVerify is MRC-accredited and integrates with the leading DSPs, SSPs, social platforms (Meta, TikTok, YouTube, X, Snap, Pinterest,
  Reddit, LinkedIn), CTV platforms, retail-media networks, and ad servers. Customers and partners access measurement, contextual, and optimization data primarily through DV Pinnacle — DoubleVerify''s customer-facing reporting and configuration platform — which exposes a Bearer-token protected Data API for pulling reports, and through SDK and tag-based integrations on supply and publisher endpoints. DoubleVerify does not publish an open developer portal or an OpenAPI specification; developer documentation at developer.doubleverify.com is gated, and API tokens are provisioned per partner/program through Pinnacle. As of the DV Neura launch DoubleVerify also runs a live remote Model Context Protocol server at https://mcp.doubleverify.com/mcp — the DV Neura Insight Agent — authenticated with OAuth 2.1 against its Keycloak CIAM realm and connectable today from Anthropic Claude, which makes DoubleVerify one of the few ad-verification vendors running a real agent surface even though it still ships
  no public machine-readable contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doubleverify.png
layout: provider
mcp_servers:
- description: ''
  name: DV Neura MCP Server
  slug: dv-neura-mcp-server
modified: '2026-08-13'
name: DoubleVerify
nav: Providers
network: true
overview: 'DoubleVerify publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ad Verification, Ad Measurement, Media Quality, Brand Suitability, and Viewability.


  DoubleVerify''s developer surface includes support, GitHub presence, YouTube channel, engineering blog, authentication, and 31 more developer resources.'
plans:
- name: Doubleverify Plans Pricing
  plan_count: 0
  slug: doubleverify-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Doubleverify Rate Limits
  slug: doubleverify-rate-limits
scopes:
- name: Doubleverify Scopes
  scope_count: 21
  slug: doubleverify-scopes
  summary_line: 21 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doubleverify/refs/heads/main/screenshots/doubleverify-2026-06-20T180204.png
security:
- kind: authentication
  name: Doubleverify Authentication
  slug: doubleverify-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Doubleverify Domain Security
  slug: doubleverify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doubleverify Vulnerability Disclosure
  slug: doubleverify-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Doubleverify Trust Center
  slug: doubleverify-trust-center
  summary_line: SOC 2, ISO/IEC 27001, ISO/IEC 27001 Statement of Applicability, ISO/IEC 27701, GDPR, CCPA, CPRA, LGPD, PIPEDA, VCDPA, EU-US Data Privacy Framework, Swiss-US Data Privacy Framework, UK Extension to the EU-US Data Privacy Framework, APEC CBPR, APEC PRP, TRUSTe
slug: doubleverify
tags:
- Ad Verification
- Ad Measurement
- Media Quality
- Brand Suitability
- Viewability
- Attention Measurement
- Invalid Traffic
- Fraud Detection
- Contextual Targeting
- Programmatic Advertising
- Connected TV
- Social Media Measurement
- Commerce Media
- Publisher Analytics
- MRC Accredited
- AdTech
website: https://doubleverify.com
---
