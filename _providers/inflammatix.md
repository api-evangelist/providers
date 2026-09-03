---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-02'
api_count: 17
apis:
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Categories API from Inflammatix — 2 operation(s) for categories.
  name: Inflammatix Categories API
  slug: inflammatix-categories-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Comments API from Inflammatix — 2 operation(s) for comments.
  name: Inflammatix Comments API
  slug: inflammatix-comments-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The CourseCategories API from Inflammatix — 2 operation(s) for coursecategories.
  name: Inflammatix Course Categories API
  slug: inflammatix-coursecategories-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Courses API from Inflammatix — 2 operation(s) for courses.
  name: Inflammatix Courses API
  slug: inflammatix-courses-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The CourseTags API from Inflammatix — 2 operation(s) for coursetags.
  name: Inflammatix Course Tags API
  slug: inflammatix-coursetags-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Lessons API from Inflammatix — 2 operation(s) for lessons.
  name: Inflammatix Lessons API
  slug: inflammatix-lessons-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Media API from Inflammatix — 2 operation(s) for media.
  name: Inflammatix Media API
  slug: inflammatix-media-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Pages API from Inflammatix — 2 operation(s) for pages.
  name: Inflammatix Pages API
  slug: inflammatix-pages-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Posts API from Inflammatix — 2 operation(s) for posts.
  name: Inflammatix Posts API
  slug: inflammatix-posts-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The PublicationCategories API from Inflammatix — 2 operation(s) for publicationcategories.
  name: Inflammatix Publication Categories API
  slug: inflammatix-publicationcategories-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Publications API from Inflammatix — 2 operation(s) for publications.
  name: Inflammatix Publications API
  slug: inflammatix-publications-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Quizzes API from Inflammatix — 2 operation(s) for quizzes.
  name: Inflammatix Quizzes API
  slug: inflammatix-quizzes-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Search API from Inflammatix — 1 operation(s) for search.
  name: Inflammatix Search API
  slug: inflammatix-search-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Statuses API from Inflammatix — 1 operation(s) for statuses.
  name: Inflammatix Statuses API
  slug: inflammatix-statuses-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Tags API from Inflammatix — 2 operation(s) for tags.
  name: Inflammatix Tags API
  slug: inflammatix-tags-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Taxonomies API from Inflammatix — 1 operation(s) for taxonomies.
  name: Inflammatix Taxonomies API
  slug: inflammatix-taxonomies-api
- baseURL: https://inflammatix.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Types API from Inflammatix — 1 operation(s) for types.
  name: Inflammatix Types API
  slug: inflammatix-types-api
artifact_total: 22
collections:
- collection_type: open
  name: Inflammatix Site Content API (WordPress REST)
  slug: open-inflammatix-content
- collection_type: open
  name: Inflammatix Support & Training Content API (WordPress REST)
  slug: open-inflammatix-support-content
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/inflammatix-content-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/inflammatix-support-content-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inflammatix-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://inflammatix.com/
- group: operate
  title: ''
  type: Support
  url: https://support.inflammatix.com/
- group: start
  title: ''
  type: Login
  url: https://support.inflammatix.com/login/
- group: company
  title: ''
  type: Blog
  url: https://inflammatix.com/newsroom/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://inflammatix.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://inflammatix.com/newsroom/press-releases/
- group: operate
  title: ''
  type: Roadmap
  url: https://inflammatix.com/pipeline/
- group: auth
  title: ''
  type: Compliance
  url: https://inflammatix.com/about-us/
- group: other
  title: ''
  type: Patents
  url: https://inflammatix.com/patents/
- group: other
  title: ''
  type: Research
  url: https://inflammatix.com/evidence/
- group: company
  title: ''
  type: Careers
  url: https://inflammatix.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://inflammatix.com/contact-inflammatix/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inflammatix.com/privacy-and-cookies-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inflammatix.com/terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inflammatix/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/inflammatix_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/inflammatix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inflammatix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inflammatix-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inflammatix-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inflammatix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inflammatix-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inflammatix-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inflammatix-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Inflammatix is a molecular diagnostics company headquartered in Sunnyvale, California that reads the patient's own immune response to speed up decisions in emergency and critical care. Its FDA-cleared TriVerity Test System measures a 29-mRNA host-response panel from whole blood on the benchtop Myrna instrument using RT-LAMP, returning three machine-learning-derived scores — bacterial infection likelihood, viral infection likelihood, and risk of severe illness within seven days — in about 30 minutes, with under a minute of no-prep sample handling. The company was co-founded out of Stanford by Tim Sweeney and Purvesh Khatri, is backed by Khosla Ventures, Northpond Ventures, Think.Health Ventures, Iberis Capital, OSF HealthCare and Vesalius BioCapital plus federal funding from NIH, BARDA, DRIVe and DARPA, and holds ISO 13485:2016 certification and a State of California medical device manufacturing license. Inflammatix publishes no developer API for its clinical products; the Myrna
  instrument advertises "multiple LIS connectivity options" and remote notification, but no public interface specification. The machine-readable surfaces it does serve are the WordPress REST content APIs behind inflammatix.com and its customer support/training portal, which expose the company's peer-reviewed publication library and the TriVerity/Myrna course catalogue as JSON.
image: https://inflammatix.com/wp-content/uploads/2025/05/logo-revdark-850-1024x242.webp
layout: provider
mcp_servers:
- description: ''
  name: Inflammatix MCP Server
  slug: inflammatix-mcp-server
modified: '2026-08-01'
name: Inflammatix
nav: Providers
network: true
overview: 'Inflammatix publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Course Categories API, and 14 more. Tagged areas include Company, Health, Healthcare, Diagnostics, and Medical Devices.


  Inflammatix''s developer surface includes support, engineering blog, authentication, and 25 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 16.3
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 29.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 19
      marker_coverage: 100.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inflammatix/refs/heads/main/screenshots/inflammatix-2026-08-07T170701.png
security:
- kind: authentication
  name: Inflammatix Authentication
  slug: inflammatix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inflammatix Domain Security
  slug: inflammatix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inflammatix
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Medical Devices
- In Vitro Diagnostics
- Molecular Diagnostics
- Sepsis
- Machine-Learning
- Life Sciences
- Point of Care
- Content
website: https://inflammatix.com/
---
