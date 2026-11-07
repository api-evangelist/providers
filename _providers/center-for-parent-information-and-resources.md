---
access_model:
  confidence: high
  label: Free and anonymous — no signup, no credential, no quota
  onboarding: unknown
  pricing: free
  public: true
  source:
  - live anonymous 200 responses from https://www.parentcenterhub.org/wp-json/cn-api/v1/entry on 2026-09-05
  trial: false
  try_now: true
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
    error_semantics: documented
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
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Center for Parent Information and Resources website at www.parentcenterhub.org: the route index of the site''s content management system, catalogued as on'
  name: Center for Parent Information and Resources Website (WordPress REST)
  slug: parentcenterhub-org-website-wordpress-rest
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/security/center-for-parent-information-and-resources-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/center-for-parent-information-and-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parentcenterhub.org
- group: company
  title: ''
  type: Newsletter
  url: https://www.parentcenterhub.org/buzz/
- group: company
  title: ''
  type: Blog
  url: https://www.parentcenterhub.org/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.parentcenterhub.org/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://www.parentcenterhub.org/contact-us/
- group: company
  title: ''
  type: About
  url: https://www.parentcenterhub.org/whatiscpir/
- group: other
  title: ''
  type: Events
  url: https://calendar.google.com/calendar/embed?src=cpir.calendar%40gmail.com&ctz=America%2FNew_York
- group: start
  title: ''
  type: Login
  url: https://www.parentcenterhub.org/parentcenter-login
- group: agent
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/llms/center-for-parent-information-and-resources-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/center-for-parent-information-and-resources-llms.txt
- group: design
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/conventions/center-for-parent-information-and-resources-conventions.yml
  title: ''
  type: Conventions
  url: conventions/center-for-parent-information-and-resources-conventions.yml
- group: design
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/errors/center-for-parent-information-and-resources-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/center-for-parent-information-and-resources-problem-types.yml
- group: design
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/lifecycle/center-for-parent-information-and-resources-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/center-for-parent-information-and-resources-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/conformance/center-for-parent-information-and-resources-conformance.yml
  title: ''
  type: Conformance
  url: conformance/center-for-parent-information-and-resources-conformance.yml
- group: design
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/data-model/center-for-parent-information-and-resources-data-model.yml
  title: ''
  type: DataModel
  url: data-model/center-for-parent-information-and-resources-data-model.yml
- group: operate
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/rate-limits/center-for-parent-information-and-resources-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/center-for-parent-information-and-resources-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/plans/center-for-parent-information-and-resources-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/center-for-parent-information-and-resources-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/packages/center-for-parent-information-and-resources-packages.yml
  title: ''
  type: Packages
  url: packages/center-for-parent-information-and-resources-packages.yml
- group: agent
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/mcp/center-for-parent-information-and-resources-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/center-for-parent-information-and-resources-mcp.yml
- group: auth
  href: https://artifacts.apis.io/center-for-parent-information-and-resources/authentication/center-for-parent-information-and-resources-authentication.yml
  title: ''
  type: Authentication
  url: authentication/center-for-parent-information-and-resources-authentication.yml
created: '2024-12-03'
description: 'The Center for Parent Information and Resources (CPIR) is the federally funded central hub of information and products for the national network of Parent Training and Information Centers (PTIs) and Community Parent Resource Centers (CPRCs). An OSEP-funded project operated by the SPAN Parent Advocacy Network, CPIR supports families and youth with a focus on children with disabilities, delivering resources through the Parent Center Hub website, the Buzz from the Hub newsletter, webinars, glossaries and an events calendar. CPIR runs no developer program and publishes no API documentation, but its own host serves a real anonymous read-only JSON API: the WordPress REST API at parentcenterhub.org/wp-json exposed 34 namespaces and 717 routes on 2026-09-05, including the Connections directory namespace cn-api/v1 that carries the national Parent Center directory (784+ geocoded centers across 55 state and territory terms), plus ISO 3166-1 country reference data, US state geography and
  GeoJSON, an oEmbed 1.0 provider endpoint, and schema.org structured data. The WordPress content collections (posts, pages, media, users, search) are closed to anonymous callers and return 401 rest_forbidden; article content is available through the site RSS feed.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/center-for-parent-information-and-resources.png
layout: provider
modified: '2026-09-05'
name: Center for Parent Information and Resources
nav: Providers
network: true
overview: 'Center for Parent Information and Resources publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Disability, Education, Families, Federal Government, and Parent Centers.


  Center for Parent Information and Resources'' developer surface includes engineering blog, support, authentication, and 18 more developer resources.'
plans:
- name: Center For Parent Information And Resources Plans Pricing
  plan_count: 0
  slug: center-for-parent-information-and-resources-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Center For Parent Information And Resources Rate Limits
  slug: center-for-parent-information-and-resources-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/center-for-parent-information-and-resources/center-for-parent-information-and-resources-2026-06-20T174123.png
security:
- kind: authentication
  name: Center For Parent Information And Resources Authentication
  slug: center-for-parent-information-and-resources-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Center For Parent Information And Resources Domain Security
  slug: center-for-parent-information-and-resources-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: find-a-parent-center
  slug: center-for-parent-information-and-resources-find-a-parent-center
- name: map-the-parent-center-network
  slug: center-for-parent-information-and-resources-map-the-parent-center-network
- name: reference-cpir-content
  slug: center-for-parent-information-and-resources-reference-cpir-content
slug: center-for-parent-information-and-resources
tags:
- Disability
- Education
- Families
- Federal Government
- Parent Centers
- Parent Training
- Parents
- Special Needs
website: https://www.parentcenterhub.org
---
