---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Article
  name: Santé Académie Article API
  slug: santeacademie-article-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: CustomCatalog
  name: Santé Académie Custom Catalog API
  slug: santeacademie-customcatalog-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Faq
  name: Santé Académie Faq API
  slug: santeacademie-faq-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Health Facility
  name: Santé Académie Health Facility API
  slug: santeacademie-health-facility-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Job
  name: Santé Académie Job API
  slug: santeacademie-job-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: JobSpace
  name: Santé Académie Job Space API
  slug: santeacademie-jobspace-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: MediaCategory
  name: Santé Académie Media Category API
  slug: santeacademie-mediacategory-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Pharmacy
  name: Santé Académie Pharmacy API
  slug: santeacademie-pharmacy-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Resource
  name: Santé Académie Resource API
  slug: santeacademie-resource-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Sitemap
  name: Santé Académie Sitemap API
  slug: santeacademie-sitemap-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Testimonial
  name: Santé Académie Testimonial API
  slug: santeacademie-testimonial-api
- baseURL: https://frontstage.santeacademie.com
  baseurl_source: declared
  description: Topic
  name: Santé Académie Topic API
  slug: santeacademie-topic-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/santeacademie/capabilities/santeacademie-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/santeacademie-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/santeacademie/overlays/santeacademie-frontstage-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/santeacademie-frontstage-overlay.yaml
- group: other
  href: https://artifacts.apis.io/santeacademie/overlays/santeacademie-connector-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/santeacademie-connector-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.santeacademie.com/
- group: start
  title: ''
  type: Login
  url: https://play.santeacademie.com/
- group: operate
  title: ''
  type: Support
  url: https://support.santeacademie.com/fr/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.santeacademie.com/fr/
- group: company
  title: ''
  type: Blog
  url: https://www.santeacademie.com/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/santeacademie
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.notion.so/CGU-V-de-Sant-Acad-mie-b4730d8bf25b47bca95d0e3b2c40ba08
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.notion.so/santeacademie/Politique-de-confidentialit-af621df7e4be4f4182e0879851735568
- group: operate
  title: ''
  type: StatusPage
  url: https://status.santeacademie.com/
- group: design
  href: https://artifacts.apis.io/santeacademie/lifecycle/santeacademie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/santeacademie-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/santeacademie/authentication/santeacademie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/santeacademie-authentication.yml
- group: design
  href: https://artifacts.apis.io/santeacademie/conventions/santeacademie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/santeacademie-conventions.yml
- group: design
  href: https://artifacts.apis.io/santeacademie/conformance/santeacademie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/santeacademie-conformance.yml
- group: auth
  href: https://artifacts.apis.io/santeacademie/conformance/santeacademie-conformance.yml
  title: ''
  type: Compliance
  url: conformance/santeacademie-conformance.yml
- group: design
  href: https://artifacts.apis.io/santeacademie/errors/santeacademie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/santeacademie-problem-types.yml
- group: design
  href: https://artifacts.apis.io/santeacademie/data-model/santeacademie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/santeacademie-data-model.yml
- group: auth
  href: https://artifacts.apis.io/santeacademie/security/santeacademie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/santeacademie-domain-security.yml
- group: build
  href: https://artifacts.apis.io/santeacademie/packages/santeacademie-packages.yml
  title: ''
  type: Packages
  url: packages/santeacademie-packages.yml
- group: agent
  href: https://artifacts.apis.io/santeacademie/llms/santeacademie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/santeacademie-llms.txt
- group: agent
  href: https://artifacts.apis.io/santeacademie/mcp/santeacademie-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/santeacademie-mcp.yml
- group: agent
  href: https://artifacts.apis.io/santeacademie/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/santeacademie/plans/santeacademie-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/santeacademie-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/santeacademie/rate-limits/santeacademie-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/santeacademie-rate-limits.yml
created: '2026-08-17'
description: Santé Académie is a French continuing-professional-development (DPC) training provider for healthcare professionals — physicians, nurses, pharmacists, pharmacy technicians, nursing assistants and health-facility training managers — delivering e-learning, virtual classrooms and in-person courses funded through ANDPC, FIF-PL, FAF-PM, ANFH and OPCO schemes. The company is Qualiopi-certified, registered with France Compétences and approved by the Agence Nationale du DPC, and says more than 35,000 healthcare professionals have trained on its platform. Its public technical surface is a pair of unauthenticated read-only catalog APIs served from frontstage.santeacademie.com — the API Platform "Frontstage API" and a swagger-php "Connector API" — which expose the training catalog (topics, resources, courses, trainers, funding schemes, professions/métiers, FAQs, testimonials, pharmacy and health-facility lookup) that powers its own websites and learner app.
image: https://www.santeacademie.com/favicon.ico
layout: provider
modified: '2026-08-17'
name: Santé Académie
nav: Providers
network: true
overview: 'Santé Académie publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Article API, Custom Catalog API, Faq API, and 9 more. Tagged areas include Company, EdTech, Healthcare Training, Continuing Education, and DPC.


  The Santé Académie catalog on APIs.io includes 1 Spectral governance ruleset.


  Santé Académie''s developer surface includes support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Santeacademie Plans Pricing
  plan_count: 0
  slug: santeacademie-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Santeacademie Rate Limits
  slug: santeacademie-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Santé Académie API Rules
  rule_count: 48
  severity_counts:
    error: 39
    hint: 0
    info: 5
    warn: 4
  slug: santeacademie-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 40.9
    developer_ergonomics: 28.0
    discoverability: 73.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 35.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/santeacademie/santeacademie-2026-09-02T154403.png
security:
- kind: authentication
  name: Santeacademie Authentication
  slug: santeacademie-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Santeacademie Domain Security
  slug: santeacademie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: santeacademie-browse-webinars-and-content
  slug: santeacademie-browse-webinars-and-content
- name: santeacademie-enumerate-catalog
  slug: santeacademie-enumerate-catalog
- name: santeacademie-find-funded-dpc-training
  slug: santeacademie-find-funded-dpc-training
slug: santeacademie
tags:
- Company
- EdTech
- Healthcare Training
- Continuing Education
- DPC
- E-Learning
- France
- Healthcare Professionals
- Course Catalog
- LMS
website: https://www.santeacademie.com/
---
