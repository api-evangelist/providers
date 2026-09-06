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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.parentcenterhub.org/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the national Parent Center directory - the machine-readable form of the Find Your Parent Center finder. Each entry is a Parent Training and Information Center (P
  name: CPIR Parent Center Directory API
  slug: cpir-parent-center-directory-api
- baseURL: https://www.parentcenterhub.org/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated reference data served alongside the Parent Center directory: ISO 3166-1 country records with alpha-2 and alpha-3 codes, ISO 4217 currency and calling codes; administrative subd'
  name: CPIR Geography Reference API
  slug: cpir-geography-reference-api
- baseURL: https://www.parentcenterhub.org/wp-json
  baseurl_source: declared
  description: Public, unauthenticated oEmbed 1.0 provider endpoint for parentcenterhub.org. Given the URL of any CPIR page it returns a conformant oEmbed document naming the provider, title, author and embeddable H
  name: CPIR oEmbed API
  slug: cpir-oembed-api
- baseURL: https://www.parentcenterhub.org/wp-json
  baseurl_source: declared
  description: 'The anonymously readable metadata layer of the parentcenterhub.org WordPress REST API - the discovery root enumerating 34 namespaces and 717 routes with their argument schemas, the registered content '
  name: CPIR Site Metadata API
  slug: cpir-site-metadata-api
artifact_total: 8
common:
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/center-for-parent-information-and-resources-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/center-for-parent-information-and-resources-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/center-for-parent-information-and-resources-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/center-for-parent-information-and-resources-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/center-for-parent-information-and-resources-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/center-for-parent-information-and-resources-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/center-for-parent-information-and-resources-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/center-for-parent-information-and-resources-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/center-for-parent-information-and-resources-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/center-for-parent-information-and-resources-mcp.yml
- group: auth
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
overview: 'Center for Parent Information and Resources publishes 4 APIs on the [APIs.io](https://apis.io/) network, including CPIR Parent Center Directory API, CPIR Geography Reference API, CPIR oEmbed API, and 1 more. Tagged areas include Disability, Education, Families, Federal-Government, and Parent Centers.


  Center for Parent Information and Resources'' developer surface includes engineering blog, support, authentication, and 18 more developer resources.'
plans:
- name: Center For Parent Information And Resources Plans Pricing
  plan_count: 0
  slug: center-for-parent-information-and-resources-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Center For Parent Information And Resources Rate Limits
  slug: center-for-parent-information-and-resources-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 15.5
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 3.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/center-for-parent-information-and-resources/refs/heads/main/screenshots/center-for-parent-information-and-resources-2026-06-20T174123.png
security:
- kind: authentication
  name: Center For Parent Information And Resources Authentication
  slug: center-for-parent-information-and-resources-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Center For Parent Information And Resources Domain Security
  slug: center-for-parent-information-and-resources-domain-security
  summary_line: TLSv1.3
slug: center-for-parent-information-and-resources
tags:
- Disability
- Education
- Families
- Federal-Government
- Parent Centers
- Parent Training
- Parents
- Special Needs
website: https://www.parentcenterhub.org
---
