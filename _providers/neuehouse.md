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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the NeueHouse website at www.neuehouse.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate A'
  name: NeueHouse Website (WordPress REST)
  slug: neuehouse-com-website-wordpress-rest
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/neuehouse/capabilities/neuehouse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/neuehouse-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.neuehouse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.org/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.neuehouse.com/wp-json/
- group: operate
  title: ''
  type: Support
  url: https://www.neuehouse.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.neuehouse.com/membership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neuehouse.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neuehouse.com/privacy-policy/
- group: commercial
  href: https://artifacts.apis.io/neuehouse/plans/neuehouse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neuehouse-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/neuehouse/rate-limits/neuehouse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/neuehouse-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/neuehouse/authentication/neuehouse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/neuehouse-authentication.yml
- group: design
  href: https://artifacts.apis.io/neuehouse/conventions/neuehouse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/neuehouse-conventions.yml
- group: design
  href: https://artifacts.apis.io/neuehouse/errors/neuehouse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/neuehouse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/neuehouse/data-model/neuehouse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/neuehouse-data-model.yml
- group: design
  href: https://artifacts.apis.io/neuehouse/conformance/neuehouse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/neuehouse-conformance.yml
- group: design
  href: https://artifacts.apis.io/neuehouse/lifecycle/neuehouse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/neuehouse-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/neuehouse/security/neuehouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neuehouse-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/neuehouse/mcp/neuehouse-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/neuehouse-mcp.yml
- group: build
  href: https://artifacts.apis.io/neuehouse/mcp/neuehouse-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/neuehouse-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/neuehouse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/neuehouse/llms/neuehouse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neuehouse-llms.txt
- group: build
  href: https://artifacts.apis.io/neuehouse/packages/neuehouse-packages.yml
  title: ''
  type: Packages
  url: packages/neuehouse-packages.yml
- group: other
  href: https://artifacts.apis.io/neuehouse/overlays/neuehouse-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/neuehouse-content-api-overlay.yaml
- group: design
  title: ''
  type: HouseRules
  url: https://www.neuehouse.com/house-rules/
- group: commercial
  title: ''
  type: MembershipAgreement
  url: https://www.neuehouse.com/membership-agreement/
- group: other
  title: ''
  type: Accessibility
  url: https://www.neuehouse.com/accessibility/
- group: other
  title: ''
  type: Events
  url: https://luma.com/neuehouse
- group: other
  title: ''
  type: RSS
  url: https://www.neuehouse.com/feed/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/neuehouse_stock/
created: '2026-08-26'
description: 'NeueHouse is a private work and cultural home for creatives — a members-only workspace, screening room, podcast studio and events club founded in New York in 2011. It is a hospitality brand rather than a software company and it runs no developer program, publishes no API documentation and issues no API credentials. It does, however, serve a live, anonymous, machine-readable content API from its own host: the site runs on WordPress and its WordPress REST API is exposed at https://www.neuehouse.com/wp-json/, where the route index declares 313 routes across 16 namespaces. Alongside the WordPress defaults the deployment registers four NeueHouse-specific content types that read anonymously — event (467 records of cultural programming), press (66), location (3 houses) and neuejournal (empty) — making the events and press archives genuinely useful to an outside consumer. NeueHouse ceased operations in September 2025 and filed Chapter 7; Convene Hospitality Group acquired the brand,
  intellectual property and the Madison Square flagship out of bankruptcy and relaunched the brand in January 2026. The Los Angeles houses were not acquired and are not reopening, although their records are still served by the content API.'
image: https://neuehouse.com/wp-content/uploads/2023/05/NeueHouse-Social-Logo.png
layout: provider
modified: '2026-08-26'
name: NeueHouse
nav: Providers
network: true
overview: 'NeueHouse publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Co-Working, Event, Content, and WordPress.


  NeueHouse''s developer surface includes documentation, API reference, support, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Neuehouse Plans Pricing
  plan_count: 0
  slug: neuehouse-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Neuehouse Rate Limits
  slug: neuehouse-rate-limits
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/neuehouse/neuehouse-2026-09-02T150735.png
security:
- kind: authentication
  name: Neuehouse Authentication
  slug: neuehouse-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Neuehouse Domain Security
  slug: neuehouse-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: neuehouse-browse-programming
  slug: neuehouse-browse-programming
- name: neuehouse-locate-houses
  slug: neuehouse-locate-houses
slug: neuehouse
tags:
- Hospitality
- Co-Working
- Event
- Content
- WordPress
- Membership
- Real Estate
- Media
- Workspace
website: https://www.neuehouse.com/
---
