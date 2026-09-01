---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The institution-facing integration surface behind vle.kortext.com — 1EdTech LTI 1.1 launch and LTI 1.3 Deep Linking endpoints that place Kortext content and KeyLinks reading lists inside Blackboard, M
  name: Kortext VLE / LTI Integration API
  slug: kortext-vle-lti-integration-api
- description: The authenticated application API behind app.kortext.com serving the Kortext study reader and companion apps — identity, content, upload, cover, features, assessments, events and the genai and study-t
  name: Kortext Platform API
  slug: kortext-platform-api
- description: The Chat API from Kortext — 31 operation(s) for chat.
  name: Kortext Chat API
  slug: kortext-chat-api
- description: The Content API from Kortext — 20 operation(s) for content.
  name: Kortext Content API
  slug: kortext-content-api
- description: The Health Checks API from Kortext — 2 operation(s) for health checks.
  name: Kortext Health Checks API
  slug: kortext-health-checks-api
- description: The Labs API from Kortext — 1 operation(s) for labs.
  name: Kortext Labs API
  slug: kortext-labs-api
- description: The Podcast API from Kortext — 3 operation(s) for podcast.
  name: Kortext Podcast API
  slug: kortext-podcast-api
- description: The Quiz API from Kortext — 8 operation(s) for quiz.
  name: Kortext Quiz API
  slug: kortext-quiz-api
- description: The Reading List API from Kortext — 1 operation(s) for reading list.
  name: Kortext Reading List API
  slug: kortext-reading-list-api
- description: The Test API from Kortext — 2 operation(s) for test.
  name: Kortext Test API
  slug: kortext-test-api
artifact_total: 14
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kortext-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kortext-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kortext.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-demo.labs.kortext.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api-demo.labs.kortext.com/redoc
- group: operate
  title: ''
  type: Support
  url: https://uk.support.kortext.com/s/
- group: company
  title: ''
  type: Blog
  url: https://kortext.com/us/news/
- group: start
  title: ''
  type: SignUp
  url: https://app.kortext.com/identity/signup
- group: start
  title: ''
  type: Login
  url: https://app.kortext.com/identity/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kortext.com/us/website-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kortext.com/us/privacy-policy/
- group: other
  title: ''
  type: Store
  url: https://store.kortext.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-demo.labs.kortext.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://kortext.com/blog/platform-updates/how-we-integrate-with-your-workflow/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.na1.kortext.com/s/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kortext-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kortext-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kortext-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kortext-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kortext-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kortext-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kortext-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kortext-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kortext-labs-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kortext-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kortext-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kortext-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://kortext.com/blog/platform-updates/
- group: other
  title: ''
  type: Accessibility
  url: https://kortext.com/us/accessibility-commitment-statement/
- group: other
  title: ''
  type: CookiePolicy
  url: https://kortext.com/us/cookie-policy/
created: '2026-08-23'
description: Kortext is a UK-headquartered digital learning and student engagement company, founded in 2013 and led by CEO James Gray, that supplies etextbooks, course content, AI study tools and learning analytics to higher education institutions in the UK, US, Ireland, Australia and the Middle East. Its platform family covers content delivery and reading (Kortext study, read.kortext.com), the AI-assisted study layer (Kortext study+, Kortext IQ), teaching and reading-list tools (Kortext teach, KeyLinks), library acquisition workflows (Kortext acquire), engagement analytics (Kortext insights) and the unified Kortext fusion content and data layer. Publisher partners include Pearson, Wiley, McGraw Hill, Taylor & Francis, Oxford University Press and Palgrave, and in 2025 Follett Higher Education moved its North American ebook delivery onto Kortext. Institutional integration runs over 1EdTech LTI 1.1 and LTI 1.3 (including Deep Linking) into Blackboard, Moodle, Canvas and other VLEs, plus EDI
  and API integration with library management systems such as Ex Libris Alma. Kortext does not operate a public developer portal; its production APIs are authenticated and undocumented publicly, and the only openly published machine-readable contract is the OpenAPI 3.1 description of its AI "labs" study-tools API.
image: https://kortext.com/us/wp-content/uploads/2024/07/Kortext-White-EST-logo-transparent-980x255.png
layout: provider
modified: '2026-08-23'
name: Kortext
nav: Providers
network: true
overview: 'Kortext publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Content API, Health Checks API, and 5 more. Tagged areas include Education, EdTech, Higher Education, Digital Textbooks, and Learning Analytics.


  Kortext''s developer surface includes documentation, API reference, support, engineering blog, signup flow, getting-started guide, authentication, and 24 more developer resources.'
plans:
- name: Kortext Plans Pricing
  plan_count: 0
  slug: kortext-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Kortext Rate Limits
  slug: kortext-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 47.7
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 44.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Kortext Authentication
  slug: kortext-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kortext Domain Security
  slug: kortext-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kortext
tags:
- Education
- EdTech
- Higher Education
- Digital Textbooks
- Learning Analytics
- Artificial Intelligence
- Content Delivery
- LTI
- Libraries
- Student Engagement
- Publishing
website: https://kortext.com/
---
