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
  - sandbox
  - '{''url'': ''https://stellaconnect.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.medallia.com/ — a different registrable domain (stellaconnect.com -> medallia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Stellaconnect Agentic Access
  operation_count: 14
  slug: stellaconnect-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 3
apis:
- baseURL: https://api.stellaconnect.net
  baseurl_source: declared
  description: The Coaching API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for coaching.
  name: Stella Connect (Medallia Agent Connect) Coaching API
  slug: stellaconnect-coaching-api
- baseURL: https://api.stellaconnect.net
  baseurl_source: declared
  description: The Data API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for data.
  name: Stella Connect (Medallia Agent Connect) Data API
  slug: stellaconnect-data-api
- baseURL: https://api.stellaconnect.net
  baseurl_source: declared
  description: The Employees API from Stella Connect (Medallia Agent Connect) — 5 operation(s) for employees.
  name: Stella Connect (Medallia Agent Connect) Employees API
  slug: stellaconnect-employees-api
- baseURL: https://api.stellaconnect.net
  baseurl_source: declared
  description: The Qa API from Stella Connect (Medallia Agent Connect) — 3 operation(s) for qa.
  name: Stella Connect (Medallia Agent Connect) Qa API
  slug: stellaconnect-qa-api
- baseURL: https://api.stellaconnect.net
  baseurl_source: declared
  description: The Recoveries API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for recoveries.
  name: Stella Connect (Medallia Agent Connect) Recoveries API
  slug: stellaconnect-recoveries-api
- baseURL: https://api.stellaconnect.net
  baseurl_source: declared
  description: The Requests API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for requests.
  name: Stella Connect (Medallia Agent Connect) Requests API
  slug: stellaconnect-requests-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agent Connect Coaching API
  slug: open-stellaconnect-coaching-api
- collection_type: open
  name: Agent Connect Coaching Data API
  slug: open-stellaconnect-data-api
- collection_type: open
  name: Agent Connect Coaching Employees API
  slug: open-stellaconnect-employees-api
- collection_type: open
  name: Agent Connect Coaching Qa API
  slug: open-stellaconnect-qa-api
- collection_type: open
  name: Agent Connect Coaching Recoveries API
  slug: open-stellaconnect-recoveries-api
- collection_type: open
  name: Agent Connect Coaching Requests API
  slug: open-stellaconnect-requests-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/stellaconnect-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stellaconnect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stellaconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stellaconnect.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.medallia.com/en/agent-connect
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medallia.com/en/agent-connect/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.medallia.com/en/agent-connect/api/requests/request-from-any-system
- group: auth
  title: ''
  type: Authentication
  url: authentication/stellaconnect-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stellaconnect-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stellaconnect-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://agentconnect.status.medallia.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stellaconnect-lifecycle.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.medallia.com/en/agent-connect/technical-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stellaservice
- group: start
  title: ''
  type: Login
  url: https://stellaconnect.net
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medallia.com/about/legal/terms/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medallia.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.medallia.com/en/agent-connect/security-policies-and-controls/policies-compliance-and-certification
- group: design
  title: ''
  type: Conformance
  url: conformance/stellaconnect-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stellaconnect-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stellaconnect-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stellaconnect-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stellaconnect-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stellaconnect-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/stellaconnect-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stellaconnect-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stellaconnect-requests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/stellaconnect-data-return-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/stellaconnect-user-management-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stellaconnect-trigger-feedback-survey.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stellaconnect-export-feedback-and-qa-data.md
created: '2026-07-17'
description: Stella Connect, built by StellaService and acquired by Medallia in 2020, is now Medallia Agent Connect — a customer service team platform that pairs real-time customer feedback with agent coaching, quality assurance (QA), and recognition for contact center front-line teams. The product still runs on stellaconnect.net, and its Agent Connect API at api.stellaconnect.net exposes a Requests API for triggering feedback and service recovery surveys from any CRM or helpdesk, a Data Return API for pulling feedback, coaching sessions, QA reviews, audits, and calibrations, and a User Management API for employee lifecycle operations, secured with API keys and HMAC-signed JWTs.
image: https://docs-assets.medallia.com/icons/medallia.svg
layout: provider
modified: '2026-07-21'
name: Stella Connect (Medallia Agent Connect)
nav: Providers
network: true
overview: 'Stella Connect (Medallia Agent Connect) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Coaching API, Data API, Employees API, and 3 more. Tagged areas include Customer Service, Customer Feedback, Quality Assurance, Coaching, and Contact Centers.


  Stella Connect (Medallia Agent Connect)''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, sandbox, and 24 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 5
  name: Stellaconnect Rate Limits
  slug: stellaconnect-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 49.8
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stellaconnect/refs/heads/main/screenshots/stellaconnect-2026-08-17T082119.png
security:
- kind: authentication
  name: Stellaconnect Authentication
  slug: stellaconnect-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Stellaconnect Domain Security
  slug: stellaconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stellaconnect
tags:
- Customer Service
- Customer Feedback
- Quality Assurance
- Coaching
- Contact Centers
- Surveys
- Customer Experience
- Software-as-a-Service
website: https://stellaconnect.com
---
