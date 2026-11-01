---
access_model:
  confidence: high
  label: Self-serve signup with a 30-day trial
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - https://knownwell.com/pricing/
  - https://knownwell.com/free-trial/
  - https://api.knownwell.com/ci/docs
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Knownwell Agentic Access
  operation_count: 25
  slug: knownwell-agentic-access
  summary_line: 25 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The alignment API from Knownwell — 2 operation(s) for alignment. Returns the Red/Amber/Green alignment read a client team files by hand each week, alongside the machine-computed Knownwell score, so th
  name: Knownwell Alignment API
  slug: knownwell-alignment-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The api-keys API from Knownwell — 2 operation(s) for api-keys.
  name: Knownwell API Keys API
  slug: knownwell-api-keys-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The clients API from Knownwell — 14 operation(s) for clients.
  name: Knownwell Clients API
  slug: knownwell-clients-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The documentation API from Knownwell — 1 operation(s) for documentation.
  name: Knownwell Documentation API
  slug: knownwell-documentation-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The health API from Knownwell — 1 operation(s) for health.
  name: Knownwell Health API
  slug: knownwell-health-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The portfolios API from Knownwell — 2 operation(s) for portfolios.
  name: Knownwell Portfolios API
  slug: knownwell-portfolios-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The root API from Knownwell — 1 operation(s) for root.
  name: Knownwell Root API
  slug: knownwell-root-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The status API from Knownwell — 1 operation(s) for status.
  name: Knownwell Status API
  slug: knownwell-status-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The streams API from Knownwell — 1 operation(s) for streams.
  name: Knownwell Streams API
  slug: knownwell-streams-api
- baseURL: https://api.knownwell.com/ci/v1
  baseurl_source: declared
  description: The topics API from Knownwell — 1 operation(s) for topics.
  name: Knownwell Topics API
  slug: knownwell-topics-api
artifact_total: 31
collections:
- collection_type: open
  name: Knownwell api-keys API
  slug: open-knownwell-api-keys-api
- collection_type: open
  name: Knownwell api-keys clients API
  slug: open-knownwell-clients-api
- collection_type: open
  name: Knownwell api-keys documentation API
  slug: open-knownwell-documentation-api
- collection_type: open
  name: Knownwell api-keys health API
  slug: open-knownwell-health-api
- collection_type: open
  name: Knownwell api-keys portfolios API
  slug: open-knownwell-portfolios-api
- collection_type: open
  name: Knownwell api-keys root API
  slug: open-knownwell-root-api
- collection_type: open
  name: Knownwell api-keys status API
  slug: open-knownwell-status-api
- collection_type: open
  name: Knownwell api-keys streams API
  slug: open-knownwell-streams-api
- collection_type: open
  name: Knownwell api-keys topics API
  slug: open-knownwell-topics-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://knownwell.com/feed/
- group: other
  href: https://artifacts.apis.io/knownwell/overlays/knownwell-ci-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knownwell-ci-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/knownwell/agentic-access/knownwell-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/knownwell-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/knownwell/security/knownwell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knownwell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://knownwell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.knownwell.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.knownwell.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.knownwell.com/docs#introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://api.knownwell.com/docs#get-started
- group: build
  title: ''
  type: Postman
  url: https://api.knownwell.com/static/knownwell-api-postman-collection.json
- group: company
  title: ''
  type: Blog
  url: https://knownwell.com/insights/
- group: operate
  title: ''
  type: Support
  url: https://knownwell.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://knownwell.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://knownwell.com/experience-the-knownwell-platform-checkout/
- group: start
  title: ''
  type: Login
  url: https://ci.knownwell.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://knownwell.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knownwell.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knownwell.com
- group: auth
  href: https://artifacts.apis.io/knownwell/security/knownwell-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/knownwell-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://knownwell.com/security/
- group: auth
  title: ''
  type: Security
  url: https://knownwell.com/security/
- group: auth
  href: https://artifacts.apis.io/knownwell/security/knownwell-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/knownwell-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/knownwell/llms/knownwell-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/knownwell-llms.txt
- group: auth
  href: https://artifacts.apis.io/knownwell/authentication/knownwell-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knownwell-authentication.yml
- group: design
  href: https://artifacts.apis.io/knownwell/conventions/knownwell-conventions.yml
  title: ''
  type: Conventions
  url: conventions/knownwell-conventions.yml
- group: operate
  href: https://artifacts.apis.io/knownwell/rate-limits/knownwell-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knownwell-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/knownwell/errors/knownwell-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/knownwell-problem-types.yml
- group: design
  href: https://artifacts.apis.io/knownwell/lifecycle/knownwell-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/knownwell-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/knownwell/conformance/knownwell-conformance.yml
  title: ''
  type: Conformance
  url: conformance/knownwell-conformance.yml
- group: design
  href: https://artifacts.apis.io/knownwell/data-model/knownwell-data-model.yml
  title: ''
  type: DataModel
  url: data-model/knownwell-data-model.yml
- group: build
  href: https://artifacts.apis.io/knownwell/examples/knownwell-code-examples.yml
  title: ''
  type: Examples
  url: examples/knownwell-code-examples.yml
- group: agent
  href: https://artifacts.apis.io/knownwell/mcp/knownwell-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/knownwell-mcp.yml
- group: agent
  href: https://artifacts.apis.io/knownwell/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/knownwell/plans/knownwell-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knownwell-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/knownwell/sandbox/knownwell-sandbox.yml
  title: ''
  type: Console
  url: sandbox/knownwell-sandbox.yml
created: '2026-07-17'
description: Knownwell is an AI-powered commercial intelligence platform for B2B professional services firms, built around client retention and expansion rather than new-logo acquisition. The platform ingests communications, CRM records, and enterprise data through connectors to Microsoft 365, Google Workspace, Salesforce, HubSpot, Slack, Teams, and conversation intelligence tools, then synthesizes an objective Knownwell score for every client relationship. Teams use it to detect churn risk before a renewal conversation, surface growth opportunities across a portfolio, and track relationship health over time without manual data entry. Knownwell publishes a read-only public REST API at api.knownwell.com/ci/v1 that exposes client scores, score history, portfolios, streams, topics, priorities, notes, key people, and the weekly Red/Amber/Green alignment reads a client team files by hand, authenticated with an X-API-Key header. Platform pricing is published as a live per-client volume calculator
  rather than named tiers, with a 30-day trial and no per-seat charge. Knownwell was acquired by 2X to form a human-agentic GTM services company.
finops:
- has_sources: true
  method: derived
  name: Knownwell Finops
  primary_unit: ''
  service_category: ''
  slug: knownwell-finops
  template: true
image: https://knownwell.com/wp-content/uploads/2023/08/favicon21.svg
layout: provider
modified: '2026-10-06'
name: Knownwell
nav: Providers
network: true
overview: 'Knownwell publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alignment API, API Keys API, Clients API, and 7 more. Tagged areas include Company, Commercial Intelligence, Client Intelligence, Customer Success, and Revenue Operations.


  Knownwell''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Knownwell Plans Pricing
  plan_count: 0
  slug: knownwell-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Knownwell Rate Limits
  slug: knownwell-rate-limits
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 57.9
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/knownwell/knownwell-2026-07-25T224012.png
security:
- kind: authentication
  name: Knownwell Authentication
  slug: knownwell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Knownwell Domain Security
  slug: knownwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Knownwell Vulnerability Disclosure
  slug: knownwell-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Knownwell Trust Center
  slug: knownwell-trust-center
  summary_line: SOC 2, Data Privacy Framework
skill_count: 4
skills:
- name: Reconcile Knownwell alignment reads against the score
  slug: knownwell-alignment-reconciliation
- name: Run a Knownwell portfolio health review
  slug: knownwell-portfolio-health-review
- name: Drill into a Knownwell client's streams
  slug: knownwell-stream-drilldown
- name: Triage at-risk Knownwell clients
  slug: knownwell-triage-at-risk-clients
slug: knownwell
tags:
- Company
- Commercial Intelligence
- Client Intelligence
- Customer Success
- Revenue Operations
- Professional Services
- Artificial Intelligence
- Analytics
- CRM
- Churn Risk
website: https://knownwell.com/
---
