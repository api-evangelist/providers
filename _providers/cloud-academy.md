---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://cloudacademy.com'', ''status'': 301, ''note'': ''declared website redirects to https://platform.qa.com/login/ — a different registrable domain (cloudacademy.com -> qa.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 36
  human_in_the_loop: 4
  name: Cloud Academy Agentic Access
  operation_count: 52
  slug: cloud-academy-agentic-access
  summary_line: 52 operations · 36 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://platform.qa.com/restapi
  baseurl_source: declared
  description: The Learning Management System API from Cloud Academy — 9 operation(s) for learning management system.
  name: Cloud Academy Learning Management System API
  slug: cloud-academy-learning-management-system-api
- baseURL: https://platform.qa.com/restapi
  baseurl_source: declared
  description: The Organizations API from Cloud Academy — 5 operation(s) for organizations.
  name: Cloud Academy Organizations API
  slug: cloud-academy-organizations-api
- baseURL: https://platform.qa.com/restapi
  baseurl_source: declared
  description: The Reports API from Cloud Academy — 32 operation(s) for reports.
  name: Cloud Academy Reports API
  slug: cloud-academy-reports-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QA Learning Management System API
  slug: open-cloud-academy-learning-management-system-api
- collection_type: open
  name: QA Learning Management System Organizations API
  slug: open-cloud-academy-organizations-api
- collection_type: open
  name: QA Learning Management System Reports API
  slug: open-cloud-academy-reports-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/capabilities/cloud-academy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloud-academy-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/overlays/cloud-academy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloud-academy-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cloudacademy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.qa.com/restapi/docs/swagger/
- group: docs
  title: ''
  type: Documentation
  url: https://support.platform.qa.com/hc/en-us/articles/360040446031-Cloud-Academy-API
- group: docs
  title: ''
  type: APIReference
  url: https://platform.qa.com/restapi/docs/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.platform.qa.com/hc/en-us/articles/360040446031-Cloud-Academy-API
- group: operate
  title: ''
  type: Support
  url: https://support.platform.qa.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.qa.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudacademy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.platform.qa.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/lifecycle/cloud-academy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cloud-academy-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.qa.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://platform.qa.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qa.com/legal-privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qa.com/legal-privacy/privacy-notice/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/authentication/cloud-academy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloud-academy-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/scopes/cloud-academy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloud-academy-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/conventions/cloud-academy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloud-academy-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/errors/cloud-academy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloud-academy-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/rate-limits/cloud-academy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloud-academy-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/lifecycle/cloud-academy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloud-academy-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/conformance/cloud-academy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloud-academy-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/data-model/cloud-academy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloud-academy-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/mcp/cloud-academy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cloud-academy-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/llms/cloud-academy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloud-academy-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/agentic-access/cloud-academy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloud-academy-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/security/cloud-academy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloud-academy-domain-security.yml
created: '2026-07-17'
description: Cloud Academy is a hands-on technology skills training platform, now operating as the QA Learning Platform (cloudacademy.com redirects to platform.qa.com). It combines self-paced course content with hands-on labs, learning paths, quizzes, and exams across cloud, security, and software disciplines. Its public REST API lets enterprise administrators integrate the platform with internal business systems — browsing the content catalog, managing organization teams and members, and generating asynchronous reports on learner activity, progress, and skills. Authentication is OAuth2 client-credentials and the public API is rate-limited to 100 requests per minute. Cloud Academy was surfaced as a 500 Global portfolio company and enriched into the API Evangelist network from its live Swagger definition.
image: https://assets.platform.qa.com/hanami/static/favicon-platform/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Cloud Academy
nav: Providers
network: true
overview: 'Cloud Academy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Learning Management System API, Organizations API, and Reports API. Tagged areas include Company, Training, Education, Learning Management, and Cloud Computing.


  Cloud Academy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 3
  name: Cloud Academy Rate Limits
  slug: cloud-academy-rate-limits
scopes:
- name: Cloud Academy Scopes
  scope_count: 0
  slug: cloud-academy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 51.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/screenshots/cloud-academy-2026-07-25T205650.png
security:
- kind: authentication
  name: Cloud Academy Authentication
  slug: cloud-academy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cloud Academy Domain Security
  slug: cloud-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloud-academy
tags:
- Company
- Training
- Education
- Learning Management
- Cloud Computing
- Skills
- Reporting
- E-Learning
website: https://cloudacademy.com
---
