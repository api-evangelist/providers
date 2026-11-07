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
  - sandbox
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Uncapped Agentic Access
  operation_count: 14
  slug: uncapped-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- baseURL: https://portal.weareuncapped.com/api/partners
  baseurl_source: declared
  description: Applicant API for external access
  name: Uncapped Applicants API
  slug: uncapped-applicants-api
- baseURL: https://portal.weareuncapped.com/api/partners
  baseurl_source: declared
  description: Application API for external access
  name: Uncapped Applications API
  slug: uncapped-applications-api
- baseURL: https://portal.weareuncapped.com/api/partners
  baseurl_source: declared
  description: Authentication API for external access
  name: Uncapped Authentication API
  slug: uncapped-authentication-api
- baseURL: https://portal.weareuncapped.com/api/partners
  baseurl_source: declared
  description: Estimations API for external access
  name: Uncapped Estimations API
  slug: uncapped-estimations-api
- baseURL: https://portal.weareuncapped.com/api/partners
  baseurl_source: declared
  description: Webhook Subscriptions API for external access
  name: Uncapped Webhook Subscriptions API
  slug: uncapped-webhook-subscriptions-api
artifact_total: 18
asyncapis:
- description: ''
  name: Uncapped Webhooks
  slug: uncapped-webhooks
collections:
- collection_type: open
  name: api-partners Applicants API
  slug: open-uncapped-applicants-api
- collection_type: open
  name: api-partners Applicants Applications API
  slug: open-uncapped-applications-api
- collection_type: open
  name: api-partners Applicants Authentication API
  slug: open-uncapped-authentication-api
- collection_type: open
  name: api-partners Applicants Estimations API
  slug: open-uncapped-estimations-api
- collection_type: open
  name: api-partners Applicants Webhook Subscriptions API
  slug: open-uncapped-webhook-subscriptions-api
common:
- group: company
  title: ''
  type: Blog
  url: https://weareuncapped.com/blog
- group: other
  href: https://artifacts.apis.io/uncapped/capabilities/uncapped-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/uncapped-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/uncapped/overlays/uncapped-partners-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uncapped-partners-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/uncapped/security/uncapped-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uncapped-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/uncapped/agentic-access/uncapped-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/uncapped-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/uncapped/authentication/uncapped-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uncapped-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://weareuncapped.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.weareuncapped.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.weareuncapped.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.weareuncapped.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://developers.weareuncapped.com/api-reference
- group: operate
  href: https://artifacts.apis.io/uncapped/changelog/uncapped-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uncapped-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.weareuncapped.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weareuncapped-com
- group: design
  href: https://artifacts.apis.io/uncapped/asyncapi/uncapped-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uncapped-webhooks.yml
- group: design
  href: https://artifacts.apis.io/uncapped/errors/uncapped-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uncapped-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uncapped/conventions/uncapped-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uncapped-conventions.yml
- group: design
  href: https://artifacts.apis.io/uncapped/lifecycle/uncapped-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uncapped-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/uncapped/sandbox/uncapped-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/uncapped-sandbox.yml
- group: design
  href: https://artifacts.apis.io/uncapped/conformance/uncapped-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uncapped-conformance.yml
- group: design
  href: https://artifacts.apis.io/uncapped/data-model/uncapped-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uncapped-data-model.yml
- group: agent
  href: https://artifacts.apis.io/uncapped/mcp/uncapped-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uncapped-mcp.yml
- group: agent
  href: https://artifacts.apis.io/uncapped/llms/uncapped-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uncapped-llms.txt
- group: agent
  href: https://artifacts.apis.io/uncapped/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Uncapped provides working capital to online businesses, offering revenue-based financing products including merchant cash advances (MCA), term loans, and lines of credit (LOC). Through the Uncapped Partners API, platforms and marketplaces can embed business funding directly into their product without taking on origination, compliance, or servicing - submitting anonymised applicant performance data, generating pre-offer estimations, displaying ready-to-use funding Signals in their UI, and reacting to application and estimation lifecycle events via webhooks.
image: https://developers.weareuncapped.com/apple-touch-icon.png
layout: provider
modified: '2026-10-06'
name: Uncapped
nav: Providers
network: true
overview: 'Uncapped publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applicants API, Applications API, Authentication API, and 2 more. Tagged areas include Company, Fintech, Lending, Embedded Finance, and Revenue-Based Financing.


  The Uncapped catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Uncapped''s developer surface includes engineering blog, authentication, documentation, getting-started guide, API reference, changelog, sandbox, and 17 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Uncapped API Rules
  rule_count: 61
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 2
  slug: uncapped-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 60.8
    developer_ergonomics: 23.2
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 32.6
  provenance:
    agentic_access: derived
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/uncapped/uncapped-2026-08-17T082550.png
security:
- kind: authentication
  name: Uncapped Authentication
  slug: uncapped-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uncapped Domain Security
  slug: uncapped-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Pre-load Signals for a cohort with batch estimations and webhooks
  slug: uncapped-batch-estimations-with-webhooks
- name: Generate a pre-offer estimation and display funding Signals
  slug: uncapped-estimate-and-display-signals
- name: Track funding applications end to end
  slug: uncapped-track-applications
slug: uncapped
tags:
- Company
- Fintech
- Lending
- Embedded Finance
- Revenue-Based Financing
- Working Capital
- E-Commerce
website: https://weareuncapped.com
---
