---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
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
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The AdBudgetPricing API from LinkedIn Marketing API — 1 operation(s) for adbudgetpricing.
  name: LinkedIn Marketing API AdBudgetPricing API
  slug: linkedin-ads-adbudgetpricing-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The AdTargetingFacets API from LinkedIn Marketing API — 1 operation(s) for adtargetingfacets.
  name: LinkedIn Marketing API AdTargetingFacets API
  slug: linkedin-ads-adtargetingfacets-api
- baseURL: https://api.linkedin.com/rest
  baseurl_source: declared
  description: The Ad Accounts API from LinkedIn Marketing API — 5 operation(s) for ad accounts.
  name: LinkedIn Marketing API Ad Accounts API
  slug: linkedin-ads-ad-accounts-api
- baseURL: https://api.linkedin.com/rest
  baseurl_source: declared
  description: The Ad Targeting Entities API from LinkedIn Marketing API — 1 operation(s) for ad targeting entities.
  name: LinkedIn Marketing API Ad Targeting Entities API
  slug: linkedin-ads-ad-targeting-entities-api
- baseURL: https://api.linkedin.com/rest
  baseurl_source: declared
  description: The Audience Counts API from LinkedIn Marketing API — 1 operation(s) for audience counts.
  name: LinkedIn Marketing API Audience Counts API
  slug: linkedin-ads-audience-counts-api
artifact_total: 30
asyncapis:
- description: ''
  name: Linkedin Ads Webhooks
  slug: linkedin-ads-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/linkedin-ads/finops/linkedin-ads-finops.yml
  title: ''
  type: FinOps
  url: finops/linkedin-ads-finops.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/rules/linkedin-ads-rules.yml
  title: ''
  type: Spectral
  url: rules/linkedin-ads-rules.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/json-ld/linkedin-ads-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkedin-ads-context.jsonld
- group: design
  href: https://artifacts.apis.io/linkedin-ads/vocabulary/linkedin-ads-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linkedin-ads-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/linkedin-ads/hosts/linkedin-ads-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkedin-ads-hosts.yml
- group: build
  href: https://artifacts.apis.io/linkedin-ads/integrations/linkedin-ads-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/linkedin-ads-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/linkedin-ads/vendors/linkedin-ads-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkedin-ads-vendors.yml
- group: other
  href: https://artifacts.apis.io/linkedin-ads/capabilities/linkedin-ads-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/linkedin-ads-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/linkedin-ads/overlays/linkedin-ads-adaccounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-ads-adaccounts-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin-ads/overlays/linkedin-ads-adtargetingentities-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-ads-adtargetingentities-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin-ads/overlays/linkedin-ads-audiencecounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-ads-audiencecounts-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/linkedin-ads/agentic-access/linkedin-ads-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linkedin-ads-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/linkedin-ads/security/linkedin-ads-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linkedin-ads-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/linkedin-ads/security/linkedin-ads-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkedin-ads-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/linkedin-ads/authentication/linkedin-ads-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linkedin-ads-authentication.yml
- group: auth
  href: https://artifacts.apis.io/linkedin-ads/scopes/linkedin-ads-scopes.yml
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
- group: company
  title: ''
  type: Blog
  url: https://www.linkedin.com/business/marketing/blog/linkedin-ads
- group: build
  href: https://artifacts.apis.io/linkedin-ads/packages/linkedin-ads-packages.yml
  title: ''
  type: Packages
  url: packages/linkedin-ads-packages.yml
- group: build
  href: https://artifacts.apis.io/linkedin-ads/packages/linkedin-ads-packages.yml
  title: ''
  type: SDKs
  url: packages/linkedin-ads-packages.yml
- group: agent
  href: https://artifacts.apis.io/linkedin-ads/well-known/linkedin-ads-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linkedin-ads-well-known.yml
- group: auth
  href: https://artifacts.apis.io/linkedin-ads/well-known/linkedin-ads-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/linkedin-ads-security.txt
- group: design
  href: https://artifacts.apis.io/linkedin-ads/conformance/linkedin-ads-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linkedin-ads-conformance.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/errors/linkedin-ads-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/linkedin-ads-error-codes.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/lifecycle/linkedin-ads-lifecycle.yml
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
  href: https://artifacts.apis.io/linkedin-ads/sandbox/linkedin-ads-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/linkedin-ads-sandbox.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/conventions/linkedin-ads-conventions.yml
  title: ''
  type: Conventions
  url: conventions/linkedin-ads-conventions.yml
- group: operate
  href: https://artifacts.apis.io/linkedin-ads/changelog/linkedin-ads-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/linkedin-ads-changelog.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/data-model/linkedin-ads-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linkedin-ads-data-model.yml
- group: design
  href: https://artifacts.apis.io/linkedin-ads/asyncapi/linkedin-ads-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/linkedin-ads-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/linkedin-ads/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/linkedin-ads/plans/linkedin-ads-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linkedin-ads-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/linkedin-ads/rate-limits/linkedin-ads-rate-limits.yml
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
finops:
- has_sources: true
  method: derived
  name: Linkedin Ads Finops
  primary_unit: ''
  service_category: ''
  slug: linkedin-ads-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linkedin-ads.png
json_schemas:
- name: AdAccount
  property_count: 8
  slug: linkedin-ads-ad-account
- name: AdCampaignGroup
  property_count: 5
  slug: linkedin-ads-ad-campaign-group
- name: AdCampaign
  property_count: 12
  slug: linkedin-ads-ad-campaign
- name: Creative
  property_count: 4
  slug: linkedin-ads-creative
jsonld:
- class_count: 5
  name: Linkedin Ads Context
  property_count: 24
  slug: linkedin-ads-context
layout: provider
modified: '2026-08-13'
name: LinkedIn Marketing API
nav: Providers
network: true
overview: 'LinkedIn Marketing API publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including AdBudgetPricing API, AdTargetingFacets API, Ad Accounts API, and 3 more. Tagged areas include Advertising, Marketing, LinkedIn, Lead Generation, and Audience Targeting.


  The LinkedIn Marketing API catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  LinkedIn Marketing API''s developer surface includes authentication, documentation, signup flow, engineering blog, sandbox, changelog, API reference, and 39 more developer resources.'
plans:
- name: Linkedin Ads Plans Pricing
  plan_count: 0
  slug: linkedin-ads-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Linkedin Ads Rate Limits
  slug: linkedin-ads-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: LinkedIn Marketing API API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: linkedin-ads-rules
scopes:
- name: Linkedin Ads Scopes
  scope_count: 13
  slug: linkedin-ads-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 36
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.5
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 66.5
    developer_ergonomics: 70.8
    discoverability: 80.4
    operational_transparency: 81.6
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/linkedin-ads/linkedin-ads-2026-06-20T184545.png
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
skill_count: 3
skills:
- name: linkedin-ads-launch-a-campaign
  slug: linkedin-ads-launch-a-campaign
- name: linkedin-ads-plan-budget-and-bids
  slug: linkedin-ads-plan-budget-and-bids
- name: linkedin-ads-size-an-audience
  slug: linkedin-ads-size-an-audience
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
