---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Intelycare Agentic Access
  operation_count: 6
  slug: intelycare-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.intelycare.com/external-scheduling/v1/
  baseurl_source: declared
  description: Easily manage check-in and check-out events for shifts. Our API allows you to programmatically submit and manage check-in and check-out events, providing you with the flexibility to adapt to your work
  name: IntelyCare Check In / Check Out API
  slug: intelycare-check-in-check-out-api
- baseURL: https://api.intelycare.com/external-scheduling/v1/
  baseurl_source: declared
  description: Integrate with the IntelyCare platform to create shift requests effortlessly. Our API allows you to programmatically submit and manage shift requests, providing you with the flexibility to adapt to yo
  name: IntelyCare Shift API
  slug: intelycare-shift-api
- baseURL: https://api.intelycare.com/external-scheduling/v1/
  baseurl_source: declared
  description: Real-time updates on the status of submitted shifts. The API response includes valuable information about the assigned IntelyPro, giving you insights into the workforce handling each shift.
  name: IntelyCare Webhook Events API
  slug: intelycare-webhook-events-api
- baseURL: https://api.intelycare.com/external-scheduling/v1/
  baseurl_source: declared
  description: 'Simplify billing reconciliation by exchanging timecard information seamlessly. Our API supports the exchange of accurate timekeeping data, ensuring a smooth and efficient process for both you and the '
  name: IntelyCare Time Card API
  slug: intelycare-time-card-api
artifact_total: 15
asyncapis:
- description: Real-time updates on the status of submitted shifts. IntelyCare POSTs a signed JSON payload to a client-configured HTTPS endpoint when a shift is accepted by a healthcare professional (an "IntelyPro")
  name: IntelyCare Shift Events
  slug: intelycare-shift-events-asyncapi
collections:
- collection_type: open
  name: IntelyCare API Documentation
  slug: open-intelycare-external-scheduling
common:
- group: commercial
  href: https://artifacts.apis.io/intelycare/plans/intelycare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/intelycare-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.intelycare.com/feed/
- group: other
  href: https://artifacts.apis.io/intelycare/capabilities/intelycare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/intelycare-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/intelycare/overlays/intelycare-external-scheduling-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/intelycare-external-scheduling-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/intelycare/mcp/intelycare-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/intelycare-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.intelycare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.intelycare.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.intelycare.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.intelycare.com/
- group: operate
  title: ''
  type: Support
  url: https://www.intelycare.com/company/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.intelycare.com/blog/nursing-professionals/
- group: commercial
  title: ''
  type: Pricing
  url: https://credenzahealth.com/facilities/employer-products
- group: start
  title: ''
  type: SignUp
  url: https://www.intelycare.com/for-nursing-professionals/apply/
- group: start
  title: ''
  type: Login
  url: https://app.intelycare.com/facility/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intelycare.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intelycare.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/intelycare/authentication/intelycare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/intelycare-authentication.yml
- group: design
  href: https://artifacts.apis.io/intelycare/conventions/intelycare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/intelycare-conventions.yml
- group: design
  href: https://artifacts.apis.io/intelycare/errors/intelycare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/intelycare-problem-types.yml
- group: design
  href: https://artifacts.apis.io/intelycare/data-model/intelycare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intelycare-data-model.yml
- group: design
  href: https://artifacts.apis.io/intelycare/lifecycle/intelycare-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/intelycare-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/intelycare/conformance/intelycare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intelycare-conformance.yml
- group: auth
  href: https://artifacts.apis.io/intelycare/security/intelycare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intelycare-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/intelycare/llms/intelycare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intelycare-llms.txt
- group: agent
  href: https://artifacts.apis.io/intelycare/agentic-access/intelycare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intelycare-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/intelycare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/intelycare/sandbox/intelycare-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/intelycare-sandbox.yml
- group: build
  href: https://artifacts.apis.io/intelycare/examples/intelycare-examples.yml
  title: ''
  type: Examples
  url: examples/intelycare-examples.yml
created: '2026-08-01'
description: IntelyCare is a healthcare workforce platform that connects post-acute and acute-care facilities with W2-employed per-diem nursing professionals ("IntelyPros") — RNs, LPNs and CNAs — through an app-based marketplace covering per-diem shifts, contract placements and travel assignments, plus credentialing, onboarding, continuing education (IntelyEdu) and 24/7 clinical support. For facilities it provides scheduling, shift-fill and timekeeping software. IntelyCare exposes a public External Scheduling REST API that lets a facility's own scheduling or EHR system programmatically create, update and cancel shift requests, exchange timecards for billing reconciliation, and post clock-in/clock-out events, with HMAC-signed webhooks pushing shift-accept and shift-release status back in real time. IntelyCare acquired CareRev in January 2026 and also operates the Credenza verified-nursing-identity job board.
finops:
- has_sources: true
  method: derived
  name: Intelycare Finops
  primary_unit: subscription
  service_category: ''
  slug: intelycare-finops
  template: false
image: https://www.intelycare.com/wp-content/uploads/2023/08/ic-logo-2-1.svg
layout: provider
modified: '2026-10-06'
name: IntelyCare
nav: Providers
network: true
overview: 'IntelyCare publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Check In / Check Out API, Shift API, Webhook Events API, and 1 more. Tagged areas include Healthcare, Healthcare Staffing, Nursing, Workforce Management, and Scheduling.


  The IntelyCare catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  IntelyCare''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Intelycare Plans Pricing
  plan_count: 3
  slug: intelycare-plans-pricing
- name: Intelycare Price Estimates
  plan_count: 0
  slug: intelycare-price-estimates
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: IntelyCare API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: intelycare-rules
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 56.5
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/intelycare/intelycare-2026-08-07T170739.png
security:
- kind: authentication
  name: Intelycare Authentication
  slug: intelycare-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Intelycare Domain Security
  slug: intelycare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Record time worked and reconcile an IntelyCare shift for billing
  slug: intelycare-record-time-and-reconcile
- name: Request and track an IntelyCare shift
  slug: intelycare-request-and-track-a-shift
slug: intelycare
tags:
- Healthcare
- Healthcare Staffing
- Nursing
- Workforce Management
- Scheduling
- Shift Management
- Timekeeping
- Marketplace
- Webhook
- Per Diem
- Credentialing
- Post-Acute Care
website: https://www.intelycare.com/
---
