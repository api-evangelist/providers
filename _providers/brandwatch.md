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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: 'Query Brandwatch''s content library or imported data to return aggregated statistics and computed analysis. Enables programmatic access to brand mention analytics, sentiment scores, volume trends, and '
  name: Brandwatch Analysis API
  slug: analysis-api
- description: Import unstructured data from any source for analysis alongside consumer conversation data. Enables organizations to blend proprietary data with Brandwatch's social intelligence for unified analytics.
  name: Brandwatch Data Upload API
  slug: data-upload-api
- description: Integrate owned social media metrics into external analytics solutions for custom reporting. Enables organizations to combine their social channel performance data with Brandwatch's audience intellige
  name: Brandwatch Measure API
  slug: measure-api
- description: Export social publishing data to integrate with content management systems. Enables workflow automation between Brandwatch's publishing tools and external CMS platforms for unified content operations.
  name: Brandwatch Publish API
  slug: publish-api
- description: Consolidate conversations from social media inboxes with customer inquiries across platforms. Enables integration of Brandwatch's engagement tools with CRM and customer service systems for unified con
  name: Brandwatch Engage API
  slug: engage-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The Client API from Brandwatch — 1 operation(s) for client.
  name: Brandwatch Client API
  slug: brandwatch-client-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The Data API from Brandwatch — 2 operation(s) for data.
  name: Brandwatch Data API
  slug: brandwatch-data-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The Me API from Brandwatch — 1 operation(s) for me.
  name: Brandwatch Me API
  slug: brandwatch-me-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The Oauth API from Brandwatch — 1 operation(s) for oauth.
  name: Brandwatch OAUTH API
  slug: brandwatch-oauth-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The Project API from Brandwatch — 1 operation(s) for project.
  name: Brandwatch Project API
  slug: brandwatch-project-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The Projects API from Brandwatch — 26 operation(s) for projects.
  name: Brandwatch Projects API
  slug: brandwatch-projects-api
- baseURL: https://api.brandwatch.com
  baseurl_source: declared
  description: The User API from Brandwatch — 1 operation(s) for user.
  name: Brandwatch User API
  slug: brandwatch-user-api
artifact_total: 22
collections:
- collection_type: open
  name: Consumer Research API
  slug: open-brandwatch-consumer-research-authentication
- collection_type: open
  name: Consumer Research API
  slug: open-brandwatch-consumer-research
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/brandwatch-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-08-13'
name: Brandwatch
nav: Providers
network: true
overview: 'Brandwatch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Client API, Data API, Me API, and 4 more. Tagged areas include Analytics, Social-Media, Social Media Monitoring, Consumer Intelligence, and Brand Management.


  Brandwatch''s developer surface includes authentication, documentation, engineering blog, getting-started guide, support, pricing, changelog, and 36 more developer resources.'
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
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 53.8
    developer_ergonomics: 41.1
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 52.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
