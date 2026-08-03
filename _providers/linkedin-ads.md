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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Linkedin Ads Agentic Access
  operation_count: 9
  slug: linkedin-ads-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 6
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
artifact_total: 12
collections:
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
  type: Signup
  url: https://www.linkedin.com/developers/apps/new
- group: operate
  title: ''
  type: Support
  url: https://linkedin.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.linkedin.com/business/marketing/blog/linkedin-ads
created: '2026-05-11'
description: The LinkedIn Marketing API Program provides REST APIs that help businesses create LinkedIn marketing campaigns, report on campaign performance, manage leads from Lead Gen Forms, target matched audiences, and grow company Pages. It covers Advertising, Reporting and Analytics, Lead Sync, Matched Audiences, Audience Insights, Media Planning, Conversions, Community Management, Event Management, and Company Intelligence APIs. Authentication uses OAuth 2.0 three-legged (authorization code) flow with versioned API access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linkedin-ads.png
layout: provider
modified: '2026-05-11'
name: LinkedIn Marketing API
nav: Providers
network: true
overview: 'LinkedIn Marketing API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AdAccounts API, AdBudgetPricing API, AdTargetingEntities API, and 2 more. Tagged areas include Advertising, Marketing, LinkedIn, Lead Generation, and Audience Targeting.


  LinkedIn Marketing API''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 63
scopes:
- name: Linkedin Ads Scopes
  scope_count: 4
  slug: linkedin-ads-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 28.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 57.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkedin-ads/refs/heads/main/screenshots/linkedin-ads-2026-06-20T184545.png
security:
- kind: authentication
  name: Linkedin Ads Authentication
  slug: linkedin-ads-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Linkedin Ads Domain Security
  slug: linkedin-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linkedin Ads Vulnerability Disclosure
  slug: linkedin-ads-vulnerability-disclosure
  summary_line: security.txt · contact published
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
