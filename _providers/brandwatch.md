---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://www.brandwatch.com/plans/
  - https://developers.brandwatch.com/docs/authenticate
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: 'Query Brandwatch''s content library or imported data to return aggregated statistics and computed analysis. Enables programmatic access to brand mention analytics, sentiment scores, volume trends, and '
  name: Brandwatch Analysis API
  slug: analysis-api
- description: Import unstructured data from any source for analysis alongside consumer conversation data. Enables organizations to blend proprietary data with Brandwatch's social intelligence for unified analytics.
  name: Brandwatch Data Upload API
  slug: data-upload-api
- description: Export analysis results for further research and integration with existing systems. Supports real-time data streaming alongside consumer conversation data for continuous monitoring and research workfl
  name: Brandwatch Consumer Research API
  slug: consumer-research-api
- description: Integrate owned social media metrics into external analytics solutions for custom reporting. Enables organizations to combine their social channel performance data with Brandwatch's audience intellige
  name: Brandwatch Measure API
  slug: measure-api
- description: Export social publishing data to integrate with content management systems. Enables workflow automation between Brandwatch's publishing tools and external CMS platforms for unified content operations.
  name: Brandwatch Publish API
  slug: publish-api
- description: Consolidate conversations from social media inboxes with customer inquiries across platforms. Enables integration of Brandwatch's engagement tools with CRM and customer service systems for unified con
  name: Brandwatch Engage API
  slug: engage-api
artifact_total: 17
collections:
- collection_type: open
  name: Consumer Research API
  slug: open-brandwatch-consumer-research-authentication
- collection_type: open
  name: Consumer Research API
  slug: open-brandwatch-consumer-research
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brandwatch-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brandwatch-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandwatch-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandwatchltd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brandwatch
- group: company
  title: ''
  type: Website
  url: https://www.brandwatch.com
- group: other
  title: ''
  type: APIProducts
  url: https://www.brandwatch.com/products/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.brandwatch.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.brandwatch.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.brandwatch.com/blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.brandwatch.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.brandwatch.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.brandwatch.com/customer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.brandwatch.com/
- group: operate
  title: ''
  type: Community
  url: https://community.brandwatch.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brandwatch.com/plans/
- group: start
  title: ''
  type: Login
  url: https://login.brandwatch.com/
- group: other
  title: ''
  type: OpenIDConnect
  url: https://signin.brandwatch.com/auth/realms/bwone/.well-known/openid-configuration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cision.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brandwatch.com/legal/user-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brandwatch.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brandwatch-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brandwatch-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brandwatch-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brandwatch-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.brandwatch.com/legal/information-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/brandwatch-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.brandwatch.com/legal/information-security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brandwatch-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brandwatch-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developers.brandwatch.com/.well-known/api-catalog
- group: build
  title: ''
  type: Packages
  url: packages/brandwatch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brandwatch-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brandwatch-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brandwatch-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brandwatch-finops.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brandwatch-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brandwatch-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brandwatch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brandwatch-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/brandwatch-consumer-research-overlay.yaml
created: '2025-03-01'
description: Brandwatch is a leading consumer intelligence and social media analytics platform providing access to trillions of consumer conversations. The platform offers six distinct APIs for analysis, data upload, consumer research, social metrics, publishing, and engagement. Businesses use Brandwatch to track brand mentions, monitor competitors, analyze sentiment, and integrate social data with existing analytics and CRM systems for strategic decision-making.
finops:
- name: Brandwatch Finops
  service_category: API
  slug: brandwatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brandwatch.png
layout: provider
mcp_servers:
- description: ''
  name: Brandwatch MCP Server
  slug: brandwatch-mcp-server
modified: '2026-08-13'
name: Brandwatch
nav: Providers
network: true
overview: 'Brandwatch publishes 1 API on the [APIs.io](https://apis.io/) network: Consumer Research API. Tagged areas include Analytics, Social-Media, Social Media Monitoring, Consumer Intelligence, and Brand Management.


  Brandwatch''s developer surface includes authentication, documentation, engineering blog, getting-started guide, support, pricing, changelog, and 35 more developer resources.'
plans:
- name: Brandwatch Plans Pricing
  plan_count: 0
  slug: brandwatch-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Brandwatch Rate Limits
  slug: brandwatch-rate-limits
scopes:
- name: Brandwatch Scopes
  scope_count: 3
  slug: brandwatch-scopes
  summary_line: 3 scopes · password
score:
  band: strong
  composite: 54.9
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 30.3
    contract_quality: 53.1
    developer_ergonomics: 43.5
    discoverability: 83.3
    governance: 30.3
    operational_transparency: 65.8
  previous_composite: 54.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brandwatch/refs/heads/main/screenshots/brandwatch-2026-06-20T173633.png
security:
- kind: authentication
  name: Brandwatch Authentication
  slug: brandwatch-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Brandwatch Domain Security
  slug: brandwatch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brandwatch Vulnerability Disclosure
  slug: brandwatch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Brandwatch Trust Center
  slug: brandwatch-trust-center
  summary_line: ISO/IEC 27001:2022
slug: brandwatch
tags:
- Analytics
- Social-Media
- Social Media Monitoring
- Consumer Intelligence
- Brand Management
- Sentiment Analysis
website: https://www.brandwatch.com
---
