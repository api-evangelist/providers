---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Intelycare Agentic Access
  operation_count: 6
  slug: intelycare-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- description: REST API for integrating a facility's scheduling, EHR or workforce system with the IntelyCare Staffing platform. Clients create, update and delete shift requests, submit and update timecards for billi
  name: IntelyCare External Scheduling API
  slug: intelycare-external-scheduling-api
artifact_total: 6
asyncapis:
- description: Real-time updates on the status of submitted shifts. IntelyCare POSTs a signed JSON payload to a client-configured HTTPS endpoint when a shift is accepted by a healthcare professional (an "IntelyPro")
  name: IntelyCare Shift Events
  slug: intelycare-shift-events-asyncapi
common:
- group: agent
  title: ''
  type: MCPServer
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
  title: ''
  type: Authentication
  url: authentication/intelycare-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/intelycare-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/intelycare-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/intelycare-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intelycare-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/intelycare-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intelycare-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intelycare-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intelycare-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/intelycare-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/intelycare-examples.yml
created: '2026-08-01'
description: IntelyCare is a healthcare workforce platform that connects post-acute and acute-care facilities with W2-employed per-diem nursing professionals ("IntelyPros") — RNs, LPNs and CNAs — through an app-based marketplace covering per-diem shifts, contract placements and travel assignments, plus credentialing, onboarding, continuing education (IntelyEdu) and 24/7 clinical support. For facilities it provides scheduling, shift-fill and timekeeping software. IntelyCare exposes a public External Scheduling REST API that lets a facility's own scheduling or EHR system programmatically create, update and cancel shift requests, exchange timecards for billing reconciliation, and post clock-in/clock-out events, with HMAC-signed webhooks pushing shift-accept and shift-release status back in real time. IntelyCare acquired CareRev in January 2026 and also operates the Credenza verified-nursing-identity job board.
image: https://www.intelycare.com/wp-content/uploads/2023/08/ic-logo-2-1.svg
layout: provider
mcp_servers:
- description: ''
  name: intelycare-mcp.yml
  slug: intelycare-mcpyml
modified: '2026-08-01'
name: IntelyCare
nav: Providers
network: true
overview: 'IntelyCare publishes 1 API on the [APIs.io](https://apis.io/) network: External Scheduling API. Tagged areas include healthcare, healthcare-staffing, nursing, workforce-management, and scheduling.


  The IntelyCare catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IntelyCare''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 112
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 68.7
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intelycare/refs/heads/main/screenshots/intelycare-2026-08-07T170739.png
security:
- kind: authentication
  name: Intelycare Authentication
  slug: intelycare-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Intelycare Domain Security
  slug: intelycare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intelycare
tags:
- healthcare
- healthcare-staffing
- nursing
- workforce-management
- scheduling
- shift-management
- timekeeping
- marketplace
- webhooks
- per-diem
- credentialing
- post-acute-care
website: https://www.intelycare.com/
---
