---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://uplimit.com/api/organization
  baseurl_source: declared
  description: The Course API from Uplimit — 3 operation(s) for course.
  name: Uplimit Course API
  slug: uplimit-course-api
- baseURL: https://uplimit.com/api/organization
  baseurl_source: declared
  description: The Export API from Uplimit — 2 operation(s) for export.
  name: Uplimit Export API
  slug: uplimit-export-api
- baseURL: https://uplimit.com/api/organization
  baseurl_source: declared
  description: The Platform API from Uplimit — 1 operation(s) for platform.
  name: Uplimit Platform API
  slug: uplimit-platform-api
- baseURL: https://uplimit.com/api/organization
  baseurl_source: declared
  description: The Session API from Uplimit — 4 operation(s) for session.
  name: Uplimit Session API
  slug: uplimit-session-api
- baseURL: https://uplimit.com/api/organization
  baseurl_source: declared
  description: The User API from Uplimit — 10 operation(s) for user.
  name: Uplimit User API
  slug: uplimit-user-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uplimit Organization Course API
  slug: open-uplimit-course-api
- collection_type: open
  name: Uplimit Organization Course Enrollment API
  slug: open-uplimit-enrollment-api
- collection_type: open
  name: Uplimit Organization Course Export API
  slug: open-uplimit-export-api
- collection_type: open
  name: Uplimit Organization Course Platform API
  slug: open-uplimit-platform-api
- collection_type: open
  name: Uplimit Organization Course Session API
  slug: open-uplimit-session-api
- collection_type: open
  name: Uplimit Organization Course User API
  slug: open-uplimit-user-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/capabilities/uplimit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/uplimit-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/security/uplimit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uplimit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uplimit.com
- group: company
  title: ''
  type: Blog
  url: https://uplimit.com/blog
- group: company
  title: ''
  type: About
  url: https://uplimit.com/about
- group: operate
  title: ''
  type: Contact
  url: https://uplimit.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uplimit.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uplimit.com/about/privacy
- group: company
  title: ''
  type: Careers
  url: https://uplimit.com/go/work-at-uplimit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uplimit
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/packages/uplimit-packages.yml
  title: ''
  type: Packages
  url: packages/uplimit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/packages/uplimit-packages.yml
  title: ''
  type: SDKs
  url: packages/uplimit-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/well-known/uplimit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uplimit-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/mcp/uplimit-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uplimit-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/llms/uplimit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uplimit-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/overlays/uplimit-organization-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uplimit-organization-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/conformance/uplimit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uplimit-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/errors/uplimit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uplimit-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/lifecycle/uplimit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uplimit-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uplimit.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/authentication/uplimit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uplimit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/conventions/uplimit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uplimit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/data-model/uplimit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uplimit-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Uplimit (formerly CoRise, operated by Veda Education, Inc.) is an AI-native corporate learning platform backed by Greylock and Cowboy Ventures. It generates personalized, adaptive training programs with AI instructors, voice and visual practice simulations, real-time feedback, and per-learner mastery measurement for use cases like leadership training, onboarding, customer education, and sales readiness. Its Organization API lets enterprise customers manage users, course and session enrollments, SSO identity bindings, and learner-activity exports, with first-party generated Go, Python, and TypeScript clients published on GitHub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uplimit.png
layout: provider
modified: '2026-07-21'
name: Uplimit
nav: Providers
network: true
overview: 'Uplimit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Course API, Export API, Platform API, and 2 more. Tagged areas include Company, Future Of Work, Learning, Education, and Training.


  Uplimit''s developer surface includes engineering blog, authentication, and 22 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 58.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    operational_transparency: 18.4
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/uplimit/refs/heads/main/screenshots/uplimit-2026-09-02T165038.png
security:
- kind: authentication
  name: Uplimit Authentication
  slug: uplimit-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Uplimit Domain Security
  slug: uplimit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uplimit
tags:
- Company
- Future Of Work
- Learning
- Education
- Training
- Artificial Intelligence
- Corporate Training
website: https://uplimit.com
---
