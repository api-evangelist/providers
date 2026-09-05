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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Healthsherpa Agentic Access
  operation_count: 15
  slug: healthsherpa-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.one.healthsherpa.com
  baseurl_source: declared
  description: The Enrollment Sessions API from HealthSherpa — 1 operation(s) for enrollment sessions.
  name: HealthSherpa Enrollment Sessions API
  slug: healthsherpa-enrollment-sessions-api
- baseURL: https://api.one.healthsherpa.com
  baseurl_source: declared
  description: The Enrollments API from HealthSherpa — 7 operation(s) for enrollments.
  name: HealthSherpa Enrollments API
  slug: healthsherpa-enrollments-api
- baseURL: https://api.one.healthsherpa.com
  baseurl_source: declared
  description: The Quotes API from HealthSherpa — 1 operation(s) for quotes.
  name: HealthSherpa Quotes API
  slug: healthsherpa-quotes-api
- baseURL: https://api.one.healthsherpa.com
  baseurl_source: declared
  description: The Reference API from HealthSherpa — 3 operation(s) for reference.
  name: HealthSherpa Reference API
  slug: healthsherpa-reference-api
- baseURL: https://api.one.healthsherpa.com
  baseurl_source: declared
  description: The Utility API from HealthSherpa — 1 operation(s) for utility.
  name: HealthSherpa Utility API
  slug: healthsherpa-utility-api
artifact_total: 16
asyncapis:
- description: ''
  name: Healthsherpa Ichra Webhooks
  slug: healthsherpa-ichra-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HealthSherpa Public Enrollment Sessions API
  slug: open-healthsherpa-enrollment-sessions-api
- collection_type: open
  name: HealthSherpa Public Enrollment Sessions Enrollments API
  slug: open-healthsherpa-enrollments-api
- collection_type: open
  name: HealthSherpa Public Enrollment Sessions Quotes API
  slug: open-healthsherpa-quotes-api
- collection_type: open
  name: HealthSherpa Public Enrollment Sessions Reference API
  slug: open-healthsherpa-reference-api
- collection_type: open
  name: HealthSherpa Public Enrollment Sessions Utility API
  slug: open-healthsherpa-utility-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/healthsherpa-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://one.healthsherpa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://one.healthsherpa.com/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://one.healthsherpa.com/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://one.healthsherpa.com/vibe-coders.html
- group: start
  title: ''
  type: SignUp
  url: https://one.healthsherpa.com/register.html
- group: start
  title: ''
  type: Login
  url: https://one.healthsherpa.com/portal.html
- group: operate
  title: ''
  type: Support
  url: mailto:developers@one.healthsherpa.com
- group: company
  title: ''
  type: Website
  url: https://www.healthsherpa.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthsherpa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthsherpa-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/healthsherpa-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/healthsherpa-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/healthsherpa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/healthsherpa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthsherpa-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/healthsherpa-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthsherpa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthsherpa.com/agents_agencies
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/healthsherpa-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/healthsherpa-one-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/healthsherpa-ichra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthsherpa-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/healthsherpa-agentic-access.yml
created: '2026-07-17'
description: HealthSherpa is the leading ACA (Affordable Care Act) health insurance quoting and enrollment platform, and was the first company to partner with CMS to offer Enhanced Direct Enrollment (EDE) for agents. Its developer surface, HealthSherpa ONE (one.healthsherpa.com), exposes a public OpenAPI 3.1 REST API for on- and off-exchange ACA plan quoting, county/issuer/provider reference lookups, agent and self-service enrollment sessions, and an approval-gated direct enrollment API covering the full off-exchange (ICHRA) application lifecycle — create, update, submit, cancel, terminate, supporting-document upload, and payment redirect. Authentication is a single x-api-key header; enrollment writes support Idempotency-Key with 24-hour retention. Separate ICHRA and Medicare Partner APIs provide QuoteConnect/EnrollConnect, deeplinked enrollment, and webhooks. HealthSherpa publishes first-party Agent Skills, an llms.txt, and vibe-coding prompts for agents.
image: https://healthsherpa-21715791.hs-sites.com/hubfs/raw_assets/public/HealthSherpa%20Theme/HealthSherpa/images/favicon/apple-touch-icon.png
layout: provider
modified: '2026-07-19'
name: HealthSherpa
nav: Providers
network: true
overview: 'HealthSherpa publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Enrollment Sessions API, Enrollments API, Quotes API, and 2 more. Tagged areas include Company, Health Insurance, Healthcare, ACA, and Enrollment.


  The HealthSherpa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HealthSherpa''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 65.1
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthsherpa/refs/heads/main/screenshots/healthsherpa-2026-07-25T220840.png
security:
- kind: authentication
  name: Healthsherpa Authentication
  slug: healthsherpa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Healthsherpa Domain Security
  slug: healthsherpa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: ichra-platform-integration
  slug: ichra-platform-integration
slug: healthsherpa
tags:
- Company
- Health Insurance
- Healthcare
- ACA
- Enrollment
- Quoting
- Insurance
- Enhanced Direct Enrollment
- ICHRA
website: https://www.healthsherpa.com
---
