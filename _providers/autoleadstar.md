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
  - sandbox
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: A first-party Model Context Protocol tool manifest published by Fullpath for AI assistants. Thirteen tools with real JSON Schema inputSchemas covering consent management, shoppers, audiences, tasks, l
  name: Fullpath MCP Tools
  slug: fullpath-mcp-tools
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Operations related to activities
  name: AutoLeadStar Activities API
  slug: autoleadstar-activities-api
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Operations related to appointments
  name: AutoLeadStar Appointments API
  slug: autoleadstar-appointments-api
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Operations related to audiences
  name: AutoLeadStar Audiences API
  slug: autoleadstar-audiences-api
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Vendor Consent Management API for listing integrated dealers and reading/writing communication consent. Defaults to `https://fullpath.com/api/v2/external/consent-management`.
  name: AutoLeadStar Consents API
  slug: autoleadstar-consents-api
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Operations related to leads
  name: AutoLeadStar Leads API
  slug: autoleadstar-leads-api
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Operations related to shoppers
  name: AutoLeadStar Shoppers API
  slug: autoleadstar-shoppers-api
- baseURL: https://api.fullpath.com/v1
  baseurl_source: declared
  description: Operations related to tasks
  name: AutoLeadStar Tasks API
  slug: autoleadstar-tasks-api
artifact_total: 27
collections:
- collection_type: open
  name: Autoleadstar Activities API
  slug: open-autoleadstar-activities-api
- collection_type: open
  name: Autoleadstar Appointments API
  slug: open-autoleadstar-appointments-api
- collection_type: open
  name: Autoleadstar Audiences API
  slug: open-autoleadstar-audiences-api
- collection_type: open
  name: Autoleadstar Consents API
  slug: open-autoleadstar-consents-api
- collection_type: open
  name: Autoleadstar Leads API
  slug: open-autoleadstar-leads-api
- collection_type: open
  name: Autoleadstar Shoppers API
  slug: open-autoleadstar-shoppers-api
- collection_type: open
  name: Autoleadstar Tasks API
  slug: open-autoleadstar-tasks-api
common:
- group: operate
  href: https://artifacts.apis.io/autoleadstar/rate-limits/autoleadstar-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autoleadstar-rate-limits.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fullpath.com/feed/
- group: other
  href: https://artifacts.apis.io/autoleadstar/capabilities/autoleadstar-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/autoleadstar-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/autoleadstar/overlays/autoleadstar-fullpath-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/autoleadstar-fullpath-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/autoleadstar/security/autoleadstar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoleadstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fullpath.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fullpath.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fullpath.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.fullpath.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fullpath.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://fullpath.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.fullpath.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fullpath.com/legal-and-trust/?nav=websiteterms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fullpath.com/legal-and-trust/?nav=privacypolicy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.fullpath.com/feature-releases/
- group: operate
  href: https://artifacts.apis.io/autoleadstar/changelog/autoleadstar-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/autoleadstar-changelog.yml
- group: agent
  href: https://artifacts.apis.io/autoleadstar/llms/autoleadstar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoleadstar-llms.txt
- group: agent
  href: https://artifacts.apis.io/autoleadstar/well-known/autoleadstar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoleadstar-well-known.yml
- group: auth
  href: https://artifacts.apis.io/autoleadstar/well-known/autoleadstar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autoleadstar-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.fullpath.com/vulnerability-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/autoleadstar/security/autoleadstar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoleadstar-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autoleadstar/security/autoleadstar-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/autoleadstar-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fullpath.com/legal-and-trust/
- group: design
  href: https://artifacts.apis.io/autoleadstar/conformance/autoleadstar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autoleadstar-conformance.yml
- group: design
  href: https://artifacts.apis.io/autoleadstar/conventions/autoleadstar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/autoleadstar-conventions.yml
- group: build
  href: https://artifacts.apis.io/autoleadstar/packages/autoleadstar-packages.yml
  title: ''
  type: Packages
  url: packages/autoleadstar-packages.yml
- group: commercial
  href: https://artifacts.apis.io/autoleadstar/plans/autoleadstar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoleadstar-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autoleadstar/lifecycle/autoleadstar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/autoleadstar-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/autoleadstar/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: AutoLeadStar is an automotive marketing technology company founded in 2015 in Jerusalem, Israel, that rebranded as Fullpath in March 2023 after raising a $40M Series C. It builds an enhanced Customer Data Platform (CDP) and AI ecosystem for franchise car dealerships, unifying first-party data from the dealership CRM, DMS, website, inventory feed and advertising accounts into a single shopper profile, then activating it through digital advertising, VIN-specific campaigns, equity mining, email/SMS audience activation, website personalization and an AI chat agent. The company opened a public API for the platform in November 2022 and today publishes a Scalar-rendered OpenAPI 3.0 reference at developers.fullpath.com covering shoppers, audiences, leads, tasks, appointments, activities and a vendor Consent Management API, alongside a downloadable Model Context Protocol tool manifest. Fullpath reports more than 2,000 dealership clients across North America and 200+ pre-built integrations,
  and was acquired by Cox Automotive.
finops:
- has_sources: true
  method: derived
  name: Autoleadstar Finops
  primary_unit: ''
  service_category: ''
  slug: autoleadstar-finops
  template: true
image: https://developers.fullpath.com/fullpath-logo.png
layout: provider
mcp_servers:
- description: Fullpath publishes a first-party Model Context Protocol tool manifest at developers.fullpath.com/mcp-tools.json — thirteen tools with real JSON Schema inputSchemas, saved verbatim here as autoleadstar
  name: Fullpath MCP Tools
  slug: fullpath-mcp-tools
modified: '2026-10-06'
name: AutoLeadStar
nav: Providers
network: true
overview: 'AutoLeadStar publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Appointments API, Audiences API, and 5 more. Tagged areas include Company, Automotive, Customer Data Platform, Marketing Automation, and Dealership.


  AutoLeadStar''s developer surface includes documentation, API reference, engineering blog, support, signup flow, changelog, and 23 more developer resources.'
plans:
- name: Autoleadstar Plans Pricing
  plan_count: 0
  slug: autoleadstar-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Autoleadstar Rate Limits
  slug: autoleadstar-rate-limits
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 52.5
    developer_ergonomics: 55.4
    discoverability: 65.0
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 52.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/autoleadstar/autoleadstar-2026-08-07T161958.png
security:
- kind: authentication
  name: Autoleadstar Authentication
  slug: autoleadstar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Autoleadstar Domain Security
  slug: autoleadstar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Autoleadstar Vulnerability Disclosure
  slug: autoleadstar-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Autoleadstar Trust Center
  slug: autoleadstar-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 42001
skill_count: 4
skills:
- name: Build a shopper 360 profile
  slug: autoleadstar-build-a-shopper-360
- name: Export a dealership audience
  slug: autoleadstar-export-an-audience
- name: Record and verify communication consent
  slug: autoleadstar-record-communication-consent
- name: Sync the dealership sales pipeline
  slug: autoleadstar-sync-the-sales-pipeline
slug: autoleadstar
tags:
- Company
- Automotive
- Customer Data Platform
- Marketing Automation
- Dealership
- Advertising
- Artificial Intelligence
- Consent Management
- CRM
- Israel
website: https://www.fullpath.com/
---
