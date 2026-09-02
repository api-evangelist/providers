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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Linkedin Ads Agentic Access
  operation_count: 9
  slug: linkedin-ads-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- description: 'REST API for managing LinkedIn advertising campaigns, creatives, reporting, lead sync, matched audiences, conversions tracking, media planning, and community management. Authentication uses OAuth 2.0 '
  name: LinkedIn Marketing API
  slug: marketing-api
- description: The AdAccounts API from LinkedIn Marketing API — 5 operation(s) for adaccounts.
  name: LinkedIn Marketing API AdAccounts API
  slug: linkedin-ads-adaccounts-api
- description: The AdBudgetPricing API from LinkedIn Marketing API — 1 operation(s) for adbudgetpricing.
  name: LinkedIn Marketing API AdBudgetPricing API
  slug: linkedin-ads-adbudgetpricing-api
- description: The AdTargetingEntities API from LinkedIn Marketing API — 1 operation(s) for adtargetingentities.
  name: LinkedIn Marketing API AdTargetingEntities API
  slug: linkedin-ads-adtargetingentities-api
- description: The AdTargetingFacets API from LinkedIn Marketing API — 1 operation(s) for adtargetingfacets.
  name: LinkedIn Marketing API AdTargetingFacets API
  slug: linkedin-ads-adtargetingfacets-api
- description: The AudienceCounts API from LinkedIn Marketing API — 1 operation(s) for audiencecounts.
  name: LinkedIn Marketing API AudienceCounts API
  slug: linkedin-ads-audiencecounts-api
artifact_total: 21
asyncapis:
- description: ''
  name: Linkedin Ads Webhooks
  slug: linkedin-ads-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LinkedIn Marketing AdAccounts API
  slug: open-linkedin-ads-adaccounts-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdBudgetPricing API
  slug: open-linkedin-ads-adbudgetpricing-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdTargetingEntities API
  slug: open-linkedin-ads-adtargetingentities-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdTargetingFacets API
  slug: open-linkedin-ads-adtargetingfacets-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AudienceCounts API
  slug: open-linkedin-ads-audiencecounts-api
- collection_type: open
  name: LinkedIn Marketing API
  slug: open-linkedin-ads
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linkedin-ads-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linkedin-ads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkedin-ads-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linkedin-ads-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linkedin-ads-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://business.linkedin.com/marketing-solutions
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/marketing/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.linkedin.com/product-catalog/marketing
- group: start
  title: ''
  type: SignUp
  url: https://www.linkedin.com/developers/apps/new
- group: operate
  title: ''
  type: Support
  url: https://linkedin.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.linkedin.com/business/marketing/blog/linkedin-ads
- group: build
  title: ''
  type: Packages
  url: packages/linkedin-ads-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/linkedin-ads-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/linkedin-ads-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/linkedin-ads-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linkedin-ads-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/linkedin-ads-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linkedin-ads-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linkedin-ads-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.linkedin-apistatus.com
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/linkedin/shared/breaking-change-policy
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/linkedin?view_policy=true
- group: start
  title: ''
  type: Sandbox
  url: sandbox/linkedin-ads-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linkedin-ads-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linkedin-ads-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/linkedin-ads-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/linkedin-ads-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/linkedin-ads-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linkedin-ads-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/ads-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/linkedin/marketing/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://business.linkedin.com/marketing-solutions/ads/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.linkedin.com/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linkedin.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkedin-developers
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-marketing-solutions-versioned-apis/overview
created: '2026-05-11'
description: The LinkedIn Marketing API Program provides REST APIs that help businesses create LinkedIn marketing campaigns, report on campaign performance, manage leads from Lead Gen Forms, target matched audiences, and grow company Pages. It covers Advertising, Reporting and Analytics, Lead Sync, Matched Audiences, Audience Insights, Media Planning, Conversions, Community Management, Event Management, and Company Intelligence APIs. Authentication uses OAuth 2.0 three-legged (authorization code) flow with versioned API access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linkedin-ads.png
layout: provider
modified: '2026-08-13'
name: LinkedIn Marketing API
nav: Providers
network: true
overview: 'LinkedIn Marketing API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AdAccounts API, AdBudgetPricing API, AdTargetingEntities API, and 2 more. Tagged areas include Advertising, Marketing, LinkedIn, Lead Generation, and Audience Targeting.


  The LinkedIn Marketing API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LinkedIn Marketing API''s developer surface includes authentication, documentation, signup flow, support, engineering blog, sandbox, changelog, and 30 more developer resources.'
plans:
- name: Linkedin Ads Plans Pricing
  plan_count: 2
  slug: linkedin-ads-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Linkedin Ads Rate Limits
  slug: linkedin-ads-rate-limits
scopes:
- name: Linkedin Ads Scopes
  scope_count: 13
  slug: linkedin-ads-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 58.1
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkedin-ads/refs/heads/main/screenshots/linkedin-ads-2026-06-20T184545.png
security:
- kind: authentication
  name: Linkedin Ads Authentication
  slug: linkedin-ads-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Linkedin Ads Domain Security
  slug: linkedin-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linkedin Ads Vulnerability Disclosure
  slug: linkedin-ads-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: linkedin-ads
tags:
- Advertising
- Marketing
- LinkedIn
- Lead Generation
- Audience Targeting
- Conversions API
- Social Marketing
website: https://business.linkedin.com/marketing-solutions
---
