---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://retro.umoiq.com/service
  baseurl_source: declared
  description: The command-driven public feed, in XML and JSON forms.
  name: Cubic Public Feed API
  slug: cubic-public-feed-api
artifact_total: 9
common:
- group: other
  href: https://artifacts.apis.io/cubic/capabilities/cubic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cubic-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/cubic/finops/cubic-finops.yml
  title: ''
  type: FinOps
  url: finops/cubic-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://retro.umoiq.com/xmlFeedDocs/NextBusXMLFeed.pdf
- group: company
  title: ''
  type: Website
  url: https://www.cubic.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cubic
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cubic.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.cubic.com/about/people/all
- group: company
  title: ''
  type: Newsroom
  url: https://www.cubic.com/news-events
- group: operate
  title: ''
  type: Support
  url: https://www.cubic.com/support
- group: company
  title: ''
  type: Careers
  url: https://www.cubic.com/careers
- group: auth
  href: https://artifacts.apis.io/cubic/security/cubic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubic-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cubic/llms/cubic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cubic-llms.txt
- group: commercial
  href: https://artifacts.apis.io/cubic/plans/cubic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cubic-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cubic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/cubic/regulatory/cubic-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/cubic-regulatory-posture.yml
- group: design
  href: https://artifacts.apis.io/cubic/conventions/cubic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cubic-conventions.yml
- group: design
  href: https://artifacts.apis.io/cubic/errors/cubic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cubic-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/cubic/authentication/cubic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cubic-authentication.yml
- group: operate
  href: https://artifacts.apis.io/cubic/rate-limits/cubic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cubic-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cubic/lifecycle/cubic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cubic-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cubic/changelog/cubic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cubic-changelog.yml
- group: design
  href: https://artifacts.apis.io/cubic/conformance/cubic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cubic-conformance.yml
- group: design
  href: https://artifacts.apis.io/cubic/data-model/cubic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cubic-data-model.yml
- group: build
  href: https://artifacts.apis.io/cubic/examples/cubic-umo-iq-public-feed-examples.yml
  title: ''
  type: Examples
  url: examples/cubic-umo-iq-public-feed-examples.yml
- group: other
  href: https://artifacts.apis.io/cubic/overlays/cubic-umo-iq-public-feed-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cubic-umo-iq-public-feed-overlay.yaml
- group: start
  href: https://artifacts.apis.io/cubic/sandbox/cubic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cubic-sandbox.yml
- group: build
  href: https://artifacts.apis.io/cubic/packages/cubic-packages.yml
  title: ''
  type: Packages
  url: packages/cubic-packages.yml
created: '2026-04-19'
description: 'Cubic Corporation is a San Diego defense and public-transportation technology company (Cubic Transportation Systems and Cubic Defense) that delivers fare-collection, traffic management and mission systems under agency and government contracts. Its one publicly documented API is the Umo IQ Public Feed (the former NextBus feed) served by Cubic Transportation Systems at retro.umoiq.com: an anonymous XML/JSON query-command feed of transit agencies, routes, stops, arrival predictions, schedules, service messages and live vehicle locations for the agencies Cubic serves. Cubic''s other integration surfaces (GRIDSMART, Trafficware, the Umo agency portal API) sit behind customer logins.'
finops:
- has_sources: true
  method: derived
  name: Cubic Finops
  primary_unit: ''
  service_category: ''
  slug: cubic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cubic.png
layout: provider
modified: '2026-09-19'
name: Cubic
nav: Providers
network: true
overview: 'Cubic publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public Feed API. Tagged areas include Defense, Transportation, Technology, Public Transit, and Fare Collection.


  The Cubic catalog on APIs.io includes 1 Spectral governance ruleset.


  Cubic''s developer surface includes pricing, support, authentication, changelog, code examples, sandbox, and 21 more developer resources.'
plans:
- name: Cubic Plans Pricing
  plan_count: 2
  slug: cubic-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Cubic Rate Limits
  slug: cubic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Cubic API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: cubic-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 30.4
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 41.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cubic/cubic-2026-06-20T175329.png
security:
- kind: authentication
  name: Cubic Authentication
  slug: cubic-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cubic Domain Security
  slug: cubic-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: next-arrivals-at-a-stop
  slug: cubic-next-arrivals-at-a-stop
- name: track-a-bus
  slug: cubic-track-a-bus
slug: cubic
tags:
- Defense
- Transportation
- Technology
- Public Transit
- Fare Collection
- Real-Time Data
- Vehicle Location
- Intelligent Transportation Systems
website: https://www.cubic.com
---
