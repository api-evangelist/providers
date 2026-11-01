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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Casap Agentic Access
  operation_count: 6
  slug: casap-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.casaphq.com
  baseurl_source: declared
  description: The Auth API from Casap — 1 operation(s) for auth.
  name: Casap Auth API
  slug: casap-auth-api
- baseURL: https://api.casaphq.com
  baseurl_source: declared
  description: The Disputes API from Casap — 4 operation(s) for disputes.
  name: Casap Disputes API
  slug: casap-disputes-api
- baseURL: https://api.casaphq.com
  baseurl_source: declared
  description: The Accounts API from Casap — 1 operation(s) for accounts.
  name: Casap Accounts API
  slug: casap-accounts-api
- baseURL: https://api.casaphq.com
  baseurl_source: declared
  description: The Intakes API from Casap — 1 operation(s) for intakes.
  name: Casap Intakes API
  slug: casap-intakes-api
- baseURL: https://api.casaphq.com
  baseurl_source: declared
  description: The Organizations API from Casap — 3 operation(s) for organizations.
  name: Casap Organizations API
  slug: casap-organizations-api
artifact_total: 12
collections:
- collection_type: open
  name: Casap Auth API
  slug: open-casap-auth-api
- collection_type: open
  name: Casap Auth Disputes API
  slug: open-casap-disputes-api
common:
- group: other
  href: https://artifacts.apis.io/casap/capabilities/casap-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/casap-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/casap/well-known/casap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/casap-well-known.yml
- group: agent
  href: https://artifacts.apis.io/casap/llms/casap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/casap-llms.txt
- group: agent
  href: https://artifacts.apis.io/casap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/casap/lifecycle/casap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/casap-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/casap/overlays/casap-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/casap-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/casap/conformance/casap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/casap-conformance.yml
- group: agent
  href: https://artifacts.apis.io/casap/mcp/casap-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/casap-mcp.yml
- group: design
  href: https://artifacts.apis.io/casap/data-model/casap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/casap-data-model.yml
- group: design
  href: https://artifacts.apis.io/casap/conventions/casap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/casap-conventions.yml
- group: design
  href: https://artifacts.apis.io/casap/errors/casap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/casap-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/casap/security/casap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casap-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/casap/agentic-access/casap-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/casap-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/casap/authentication/casap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/casap-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.casaphq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.casaphq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.casaphq.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.casaphq.com/casap-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.casaphq.com
- group: operate
  title: ''
  type: Support
  url: https://www.casaphq.com/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://www.casaphq.com/news
- group: operate
  title: ''
  type: StatusPage
  url: https://www.casaphq.com/status
- group: start
  title: ''
  type: Login
  url: https://disputes.casaphq.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.casaphq.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.casaphq.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.casaphq.com
created: '2026-07-17'
description: Casap is an award-winning agentic-AI dispute automation platform for banks, credit unions, and fintechs. It automates payment dispute (chargeback) intake, investigation, and resolution end to end, reducing operational cost and manual work while improving regulatory compliance and consumer satisfaction. The Casap REST API lets financial institutions programmatically create disputes, check dispute status, upload evidence files, and reopen disputes, backed by a hosted disputes dashboard, PCI-DSS and SOC 2 (AICPA) controls, and integrations with card networks (Visa, Mastercard) and core banking systems (Symitar/Jack Henry, STAR). Casap won Best of Show at FinovateFall 2025.
image: https://cdn.prod.website-files.com/6670a4d559962296d4e052c9/669eb1e52506764a3f5fbef6_Casap%20Website%20Group%2018.webp
layout: provider
modified: '2026-07-18'
name: Casap
nav: Providers
network: true
overview: 'Casap publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Disputes API, Accounts API, and 2 more. Tagged areas include Company, Fintech, Disputes, Chargebacks, and Fraud Prevention.


  Casap''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 20 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 37.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/casap/casap-2026-07-25T204712.png
security:
- kind: authentication
  name: Casap Authentication
  slug: casap-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Casap Domain Security
  slug: casap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Create a payment dispute
  slug: casap-create-dispute
- name: Track and manage a dispute
  slug: casap-track-and-manage-dispute
slug: casap
tags:
- Company
- Fintech
- Disputes
- Chargebacks
- Fraud Prevention
- Payments
- Banking
- Dispute Resolution
- AI Agents
website: https://www.casaphq.com
---
