---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for the Next Generation Cision Communications Cloud, Cision's earned media monitoring and analytics platform. Runs off searches already created in the platform and returns either a list of ar
  name: Next Generation Cision Communications Cloud API
  slug: cision-communications-cloud-api
- description: Public data API behind Cision Web Solutions, Cision's embeddable investor relations and online newsroom module library. Serves press release feeds and media feeds (JSON, XML and RSS), share price hist
  name: Cision Web Solutions Public API
  slug: cision-web-solutions-api
- baseURL: https://api.cision.one
  baseurl_source: declared
  description: The mentions API from Cision — 1 operation(s) for mentions.
  name: Cision Mentions API
  slug: cision-mentions-api
- baseURL: https://api.cision.one
  baseurl_source: declared
  description: The stream API from Cision — 2 operation(s) for stream.
  name: Cision Stream API
  slug: cision-stream-api
artifact_total: 14
asyncapis:
- description: ''
  name: Cision Webhooks
  slug: cision-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/cision/authentication/cision-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cision-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cision/security/cision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cision.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cision.atlassian.net/wiki/spaces/CSM/pages/26385776684/CisionOne+-+API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cision
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cision
- group: company
  title: ''
  type: Blog
  url: https://www.cision.com/us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cision.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://oneuptime.cision.com/
- group: other
  title: ''
  type: X
  url: https://x.com/cision
- group: commercial
  href: https://artifacts.apis.io/cision/plans/cision-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cision-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cision/rate-limits/cision-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cision-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cision/finops/cision-finops.yml
  title: ''
  type: FinOps
  url: finops/cision-finops.yml
- group: company
  title: ''
  type: News
  url: https://www.cision.com/pr-distribution-and-placement/prnewswire/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cision.one/docs/api/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://cision.atlassian.net/wiki/spaces/CSM/pages/25764989843/Settings+-+Cision+API
- group: operate
  title: ''
  type: HelpCenter
  url: https://cision.atlassian.net/wiki/spaces/CSM/overview
- group: operate
  title: ''
  type: Support
  url: https://www.cision.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.cision.one/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cision.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cision.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cision.com/legal/security-statement/
- group: docs
  href: https://artifacts.apis.io/cision/openapi/_original/cision-cisionone-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cision-cisionone-openapi.yml
- group: other
  href: https://artifacts.apis.io/cision/overlays/cision-cisionone-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cision-cisionone-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cision/conventions/cision-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cision-conventions.yml
- group: design
  href: https://artifacts.apis.io/cision/errors/cision-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cision-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cision/data-model/cision-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cision-data-model.yml
- group: design
  href: https://artifacts.apis.io/cision/lifecycle/cision-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cision-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cision/changelog/cision-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cision-changelog.yml
- group: design
  href: https://artifacts.apis.io/cision/conformance/cision-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cision-conformance.yml
- group: build
  href: https://artifacts.apis.io/cision/packages/cision-packages.yml
  title: ''
  type: Packages
  url: packages/cision-packages.yml
- group: design
  href: https://artifacts.apis.io/cision/components/cision-components.yml
  title: ''
  type: Components
  url: components/cision-components.yml
- group: design
  href: https://artifacts.apis.io/cision/asyncapi/cision-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cision-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/cision/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cision/llms/cision-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cision-llms.txt
created: '2026-06-13'
description: Cision is an AI-powered PR and earned media software platform offering REST APIs for media database access, press release distribution, media monitoring, analytics, and influencer identification. CisionOne provides a REST API that connects media monitoring data with internal tools, BI platforms, and reporting systems.
finops:
- has_sources: true
  method: derived
  name: Cision Finops
  primary_unit: ''
  service_category: ''
  slug: cision-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cision.png
jsonld:
- class_count: 0
  name: Cision Context
  property_count: 5
  slug: cision-context
layout: provider
modified: '2026-09-16'
name: Cision
nav: Providers
network: true
overview: 'Cision publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Mentions API, Stream API, and 2 more. Tagged areas include PR Software, Public Relations, Earned Media, Media Monitoring, and Press Release Distribution.


  The Cision catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Cision''s developer surface includes authentication, documentation, engineering blog, pricing, product news, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Cision Plans Pricing
  plan_count: 0
  slug: cision-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Cision Rate Limits
  slug: cision-rate-limits
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 50.0
    catalog_earned_first_party: 8.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 49.4
    discoverability: 67.9
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 60.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cision/cision-2026-06-20T174406.png
security:
- kind: authentication
  name: Cision Authentication
  slug: cision-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cision Domain Security
  slug: cision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Authenticate and export from the Cision Communications Cloud API
  slug: cision-communications-cloud-authenticate-and-export
- name: Pull media coverage from a CisionOne Mention Stream
  slug: cision-pull-mention-stream-coverage
- name: Report earned media metrics for a CisionOne stream
  slug: cision-report-earned-media-metrics
slug: cision
tags:
- PR Software
- Public Relations
- Earned Media
- Media Monitoring
- Press Release Distribution
- Media Database
- Influencer Identification
- Analytics
website: https://www.cision.com/
---
