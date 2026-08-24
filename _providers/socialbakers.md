---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Socialbakers Agentic Access
  operation_count: 41
  slug: socialbakers-agentic-access
  summary_line: 41 operations · 29 acting
api_count: 8
apis:
- description: Facebook Ads content and metrics
  name: Socialbakers Ads API
  slug: socialbakers-ads-api
- description: Digital asset management — collections and assets
  name: Socialbakers Assets API
  slug: socialbakers-assets-api
- description: Customer care cases and messages
  name: Socialbakers Care API
  slug: socialbakers-care-api
- description: Community content, labeling and engagement metrics
  name: Socialbakers Community API
  slug: socialbakers-community-api
- description: Social listening content and metrics
  name: Socialbakers Listening API
  slug: socialbakers-listening-api
- description: Published content (posts / videos / tweets) per network
  name: Socialbakers Posts API
  slug: socialbakers-posts-api
- description: Time-series and aggregate metrics per social profile
  name: Socialbakers Profile Metrics API
  slug: socialbakers-profile-metrics-api
- description: Managed profiles, labels, label groups, listening queries, ad accounts
  name: Socialbakers Reference API
  slug: socialbakers-reference-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads API
  slug: open-socialbakers-ads-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Assets API
  slug: open-socialbakers-assets-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Care API
  slug: open-socialbakers-care-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Community API
  slug: open-socialbakers-community-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Listening API
  slug: open-socialbakers-listening-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Posts API
  slug: open-socialbakers-posts-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Profile Metrics API
  slug: open-socialbakers-profile-metrics-api
- collection_type: open
  name: Emplifi (Socialbakers) Public Ads Reference API
  slug: open-socialbakers-reference-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/socialbakers-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/socialbakers-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/socialbakers-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/socialbakers-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/socialbakers-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/socialbakers-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.emplifi.io/platform/latest/home/release-notes.md
- group: auth
  title: ''
  type: TrustCenter
  url: security/socialbakers-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://emplifi.io/legal/trust-center/
- group: other
  title: ''
  type: Overlay
  url: overlays/socialbakers-emplifi-public-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socialbakers-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.emplifi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emplifi.io/platform/latest/home
- group: docs
  title: ''
  type: APIReference
  url: https://api.emplifi.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emplifi.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/socialbakers-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socialbakers-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.emplifi.io/platform/latest/home/emplifi-public-api-integration.md
- group: operate
  title: ''
  type: Support
  url: https://support.emplifi.io/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://emplifi.io/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Emplifi
- group: company
  title: ''
  type: Blog
  url: https://emplifi.io/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://emplifi.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emplifi.io/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emplifi.io/legal/website-terms-of-use/
created: '2026-07-17'
description: Socialbakers was a pioneering social media analytics and marketing platform (founded 2008 in Prague) that let brands and agencies benchmark, measure and optimize their presence across Facebook, Instagram, X/Twitter, YouTube, LinkedIn, Pinterest, TikTok and Snapchat. In 2021 Socialbakers was acquired by Astute and rebranded to Emplifi, a unified social customer experience platform combining social marketing, commerce and care. The former Socialbakers Public API lives on as the Emplifi Public API (v3) at api.emplifi.io, exposing profile and post metrics, published content, social listening, community engagement, Facebook Ads, digital asset management and customer care data. Authentication is HTTP Basic (API token/secret) or OAuth 2.0 authorization code, with hourly rate limits and cursor-paginated content endpoints.
image: https://base.cdn.emplifi.io/suite/main/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Socialbakers MCP Server
  slug: socialbakers-mcp-server
modified: '2026-08-13'
name: Socialbakers
nav: Providers
network: true
overview: 'Socialbakers publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Assets API, Care API, and 5 more. Tagged areas include Company, Marketing, Social-Media, Analytics, and Social Media Analytics.


  Socialbakers'' developer surface includes changelog, release notes, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Socialbakers Plans Pricing
  plan_count: 9
  slug: socialbakers-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Socialbakers Rate Limits
  slug: socialbakers-rate-limits
scopes:
- name: Socialbakers Scopes
  scope_count: 0
  slug: socialbakers-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.9
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 16.7
    contract_quality: 52.2
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 55.3
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/socialbakers/refs/heads/main/screenshots/socialbakers-2026-08-17T081949.png
security:
- kind: authentication
  name: Socialbakers Authentication
  slug: socialbakers-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Socialbakers Domain Security
  slug: socialbakers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Socialbakers Trust Center
  slug: socialbakers-trust-center
  summary_line: SOC 2 Type II, SOC 1 Type II, ISO 27001, PCI, GDPR, CCPA, EU-US Data Privacy Framework, UK extension to the EU-US Data Privacy Framework, Swiss-US Data Privacy Framework, EcoVadis Bronze Sustainability Rating
slug: socialbakers
tags:
- Company
- Marketing
- Social-Media
- Analytics
- Social Media Analytics
- Social Listening
- Marketing Analytics
- Digital Asset Management
- Customer Care
- Emplifi
website: https://api.emplifi.io/
---
