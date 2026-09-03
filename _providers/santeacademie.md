---
access_model:
  confidence: medium
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-03'
api_count: 4
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
artifact_total: 16
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/santeacademie-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/santeacademie-frontstage-overlay.yaml
- group: other
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
  title: ''
  type: Lifecycle
  url: lifecycle/santeacademie-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/santeacademie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/santeacademie-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/santeacademie-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/santeacademie-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/santeacademie-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/santeacademie-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santeacademie-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/santeacademie-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/santeacademie-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/santeacademie-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/santeacademie-plans-pricing.yml
- group: operate
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
overview: 'Santé Académie publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Article API, Custom Catalog API, Faq API, and 9 more. Tagged areas include Company, EdTech, Healthcare Training, Continuing Education, and DPC.


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
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 41.7
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.4
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
    score: 55.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/santeacademie/refs/heads/main/screenshots/santeacademie-2026-09-02T154403.png
security:
- kind: authentication
  name: Santeacademie Authentication
  slug: santeacademie-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Santeacademie Domain Security
  slug: santeacademie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
