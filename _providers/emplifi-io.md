---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Socialbakers Agentic Access
  operation_count: 41
  slug: socialbakers-agentic-access
  summary_line: 41 operations · 9 acting
api_count: 9
apis:
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Facebook Ads content and metrics
  name: Emplifi Ads API
  slug: emplifi-io-ads-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Digital asset management — collections and assets
  name: Emplifi Assets API
  slug: emplifi-io-assets-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Customer care cases and messages
  name: Emplifi Care API
  slug: emplifi-io-care-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Community content, labeling and engagement metrics
  name: Emplifi Community API
  slug: emplifi-io-community-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Social listening content and metrics
  name: Emplifi Listening API
  slug: emplifi-io-listening-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Published content (posts / videos / tweets) per network
  name: Emplifi Posts API
  slug: emplifi-io-posts-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Time-series and aggregate metrics per social profile
  name: Emplifi Profile Metrics API
  slug: emplifi-io-profile-metrics-api
- baseURL: https://api.emplifi.io
  baseurl_source: declared
  description: Managed profiles, labels, label groups, listening queries, ad accounts
  name: Emplifi Reference API
  slug: emplifi-io-reference-api
artifact_total: 30
collections:
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
- group: auth
  href: https://artifacts.apis.io/emplifi-io/scopes/emplifi-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/emplifi-io-scopes.yml
- group: operate
  href: https://artifacts.apis.io/emplifi-io/rate-limits/socialbakers-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/socialbakers-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.emplifi.io/
- group: agent
  href: https://artifacts.apis.io/emplifi-io/agentic-access/socialbakers-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/socialbakers-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/emplifi-io/mcp/socialbakers-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/socialbakers-mcp.yml
- group: build
  href: https://artifacts.apis.io/emplifi-io/mcp/socialbakers-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/socialbakers-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/emplifi-io/packages/socialbakers-packages.yml
  title: ''
  type: Packages
  url: packages/socialbakers-packages.yml
- group: commercial
  href: https://artifacts.apis.io/emplifi-io/plans/socialbakers-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socialbakers-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/emplifi-io/changelog/socialbakers-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/socialbakers-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.emplifi.io/platform/latest/home/release-notes.md
- group: auth
  href: https://artifacts.apis.io/emplifi-io/security/socialbakers-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/socialbakers-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://emplifi.io/legal/trust-center/
- group: other
  href: https://artifacts.apis.io/emplifi-io/overlays/socialbakers-emplifi-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/socialbakers-emplifi-public-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/emplifi-io/security/socialbakers-domain-security.yml
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
  href: https://artifacts.apis.io/emplifi-io/lifecycle/socialbakers-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/socialbakers-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/emplifi-io/llms/socialbakers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialbakers-llms.txt
- group: agent
  href: https://artifacts.apis.io/emplifi-io/skills/_index.yml
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
description: Emplifi (formerly Socialbakers) is a unified social customer experience platform combining social marketing, commerce and care. Socialbakers was a pioneering social media analytics and marketing platform, founded 2008 in Prague, that let brands and agencies benchmark, measure and optimize their presence across Facebook, Instagram, X/Twitter, YouTube, LinkedIn, Pinterest, TikTok and Snapchat; it joined Astute and rebranded as Emplifi in 2021 (socialbakers.com now redirects to emplifi.io). This record was listed as Socialbakers until 2026-09-24. The former Socialbakers Public API lives on as the Emplifi Public API (v3) at api.emplifi.io, exposing profile and post metrics, published content, social listening, community engagement, Facebook Ads, digital asset management and customer care data. Authentication is HTTP Basic (API token/secret) or OAuth 2.0 authorization code, with hourly rate limits and cursor-paginated content endpoints.
finops:
- has_sources: true
  method: derived
  name: Emplifi Io Finops
  primary_unit: subscription
  service_category: ''
  slug: emplifi-io-finops
  template: false
image: https://base.cdn.emplifi.io/suite/main/favicon.ico
layout: provider
modified: '2026-08-13'
name: Emplifi
nav: Providers
network: true
overview: 'Emplifi publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ads API, Assets API, Care API, and 5 more. Tagged areas include Company, Marketing, Social Media, Analytics, and Social Media Analytics.


  The Emplifi catalog on APIs.io includes 1 Spectral governance ruleset.


  Emplifi''s developer surface includes changelog, release notes, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Emplifi Io Price Estimates
  plan_count: 0
  slug: emplifi-io-price-estimates
- name: Socialbakers Plans Pricing
  plan_count: 9
  slug: socialbakers-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Socialbakers Rate Limits
  slug: socialbakers-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Emplifi API Rules
  rule_count: 56
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 2
  slug: emplifi-io-rules
scopes:
- name: Emplifi Io Scopes
  scope_count: 0
  slug: emplifi-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
- name: Socialbakers Scopes
  scope_count: 0
  slug: socialbakers-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 55.5
    catalog_earned_first_party: 8.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 13.9
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 55.3
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/emplifi-io/socialbakers-2026-08-17T081949.png
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
skill_count: 3
skills:
- name: Retrieve published posts with pagination
  slug: socialbakers-list-posts
- name: Manage digital asset collections
  slug: socialbakers-manage-assets
- name: Pull social profile metrics
  slug: socialbakers-profile-metrics
slug: emplifi-io
tags:
- Company
- Marketing
- Social Media
- Analytics
- Social Media Analytics
- Social Listening
- Marketing Analytics
- Digital Asset Management
- Customer Care
- Emplifi
website: https://www.emplifi.io/
---
