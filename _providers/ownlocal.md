---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 5
apis:
- baseURL: https://admin.austin.ownlocal.com
  baseurl_source: declared
  description: Print ads converted into digital ad units — create, list, retrieve, update and upload the source PDF for an ad.
  name: OwnLocal Ads API
  slug: ownlocal-ads-api
- baseURL: https://admin.austin.ownlocal.com
  baseurl_source: declared
  description: Local business (advertiser) records — create, list, retrieve, and attach logo/imagery.
  name: OwnLocal Businesses API
  slug: ownlocal-businesses-api
- baseURL: https://admin.austin.ownlocal.com
  baseurl_source: declared
  description: The OwnLocal business category and sub-category vocabulary used to classify businesses and filter ads.
  name: OwnLocal Categories API
  slug: ownlocal-categories-api
- baseURL: https://admin.austin.ownlocal.com
  baseurl_source: declared
  description: Performance reporting for ads and businesses — impressions, interaction breakdowns, leads, digital lift and search-rank history.
  name: OwnLocal Reports Data API
  slug: ownlocal-reports-data-api-api
artifact_total: 16
collections:
- collection_type: open
  name: OwnLocal API — Ads
  slug: open-ownlocal-ads
- collection_type: open
  name: OwnLocal API — Businesses
  slug: open-ownlocal-businesses
- collection_type: open
  name: OwnLocal API — Categories
  slug: open-ownlocal-categories
- collection_type: open
  name: OwnLocal API — Reports Data API
  slug: open-ownlocal-reports-data-api
common:
- group: other
  href: https://artifacts.apis.io/ownlocal/capabilities/ownlocal-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ownlocal-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/ownlocal/overlays/ownlocal-ads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ownlocal-ads-overlay.yaml
- group: other
  href: https://artifacts.apis.io/ownlocal/overlays/ownlocal-businesses-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ownlocal-businesses-overlay.yaml
- group: other
  href: https://artifacts.apis.io/ownlocal/overlays/ownlocal-categories-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ownlocal-categories-overlay.yaml
- group: other
  href: https://artifacts.apis.io/ownlocal/overlays/ownlocal-reports-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ownlocal-reports-data-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ownlocal/mcp/ownlocal-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ownlocal-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://ownlocal.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.ownlocal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.docs.ownlocal.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ownlocal.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.ownlocal.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OwnLocal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ownlocal.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ownlocal.com/
- group: auth
  href: https://artifacts.apis.io/ownlocal/authentication/ownlocal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ownlocal-authentication.yml
- group: design
  href: https://artifacts.apis.io/ownlocal/conventions/ownlocal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ownlocal-conventions.yml
- group: design
  href: https://artifacts.apis.io/ownlocal/data-model/ownlocal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ownlocal-data-model.yml
- group: design
  href: https://artifacts.apis.io/ownlocal/errors/ownlocal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ownlocal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ownlocal/lifecycle/ownlocal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ownlocal-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ownlocal/conformance/ownlocal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ownlocal-conformance.yml
- group: operate
  href: https://artifacts.apis.io/ownlocal/rate-limits/ownlocal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ownlocal-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ownlocal/plans/ownlocal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ownlocal-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/ownlocal/packages/ownlocal-packages.yml
  title: ''
  type: Packages
  url: packages/ownlocal-packages.yml
- group: agent
  href: https://artifacts.apis.io/ownlocal/llms/ownlocal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ownlocal-llms.txt
- group: agent
  href: https://artifacts.apis.io/ownlocal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/ownlocal/security/ownlocal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ownlocal-domain-security.yml
created: '2026-07-17'
description: OwnLocal is an Austin, Texas based automated digital advertising platform for local media companies, founded in 2010 by Lloyd Armbrust and Jason Novek. It helps newspapers, local publishers and media companies power their digital services by automatically converting traditional print advertisements into online marketing campaigns — its AdForge and Origami products turn a submitted print ad PDF into a responsive digital ad unit, a business directory listing and an SEO/search presence, extending advertiser reach across search, social and display channels. OwnLocal publishes a partner-facing REST API (the OwnLocal API, v1) documented with Slate at api.docs.ownlocal.com and backed by a live Swagger 2.0 definition served from its own Swagger UI, covering ads, businesses, categories and performance reporting. API keys are issued by OwnLocal support rather than self-serve. OwnLocal was a 500 Global portfolio company and has acquired Whoosh Traffic, Sidengo, Inbound Press and Wanderful
  Media.
image: https://ucarecdn.com/0f20cb5b-5f4e-4207-be36-a5ee95dd54b5/ogimage1800optimized.png
layout: provider
modified: '2026-08-12'
name: OwnLocal
nav: Providers
network: true
overview: 'OwnLocal publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ads API, Businesses API, Categories API, and 1 more. Tagged areas include Company, Advertising, Local Media, Digital Advertising, and Marketing.


  The OwnLocal catalog on APIs.io includes 1 Spectral governance ruleset.


  OwnLocal''s developer surface includes documentation, API reference, support, authentication, and 22 more developer resources.'
plans:
- name: Ownlocal Plans Pricing
  plan_count: 0
  slug: ownlocal-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Ownlocal Rate Limits
  slug: ownlocal-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: OwnLocal API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 1
  slug: ownlocal-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 35.1
    discoverability: 78.6
    operational_transparency: 18.4
  previous_composite: 32.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ownlocal/ownlocal-2026-08-07T191206.png
security:
- kind: authentication
  name: Ownlocal Authentication
  slug: ownlocal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ownlocal Domain Security
  slug: ownlocal-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: ownlocal-onboard-local-business
  slug: ownlocal-onboard-local-business
- name: ownlocal-report-ad-performance
  slug: ownlocal-report-ad-performance
- name: ownlocal-submit-print-ad
  slug: ownlocal-submit-print-ad
slug: ownlocal
tags:
- Company
- Advertising
- Local Media
- Digital Advertising
- Marketing
- Newspapers
- AdTech
- Print to Digital
- Business Listings
- Local Business Data
- Ad Reporting
- Publishers
website: https://ownlocal.com
---
