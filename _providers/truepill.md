---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 69
  human_in_the_loop: 0
  name: Truepill Agentic Access
  operation_count: 158
  slug: truepill-agentic-access
  summary_line: 158 operations · 69 acting
api_count: 1
apis:
- description: Insurance objects, copay requests, and claim adjudication.
  name: Truepill Insurance API
  slug: truepill-insurance-api
- description: Patient records and demographics.
  name: Truepill Patients API
  slug: truepill-patients-api
- description: Prescription details and routing.
  name: Truepill Prescriptions API
  slug: truepill-prescriptions-api
- description: Pharmacy-to-pharmacy prescription transfers.
  name: Truepill Transfers API
  slug: truepill-transfers-api
- description: Asynchronous event retrieval.
  name: Truepill Webhooks API
  slug: truepill-webhooks-api
- description: Fill requests, orders, NDC availability, prescribers, same-day delivery and specialty-pharmacy routing — the dispensing core of the FuzeRx platform. 42 operations. Submissions are accepted asynchronou
  name: Truepill Fulfillment API
  slug: truepill-fulfillment-api
- description: Telehealth consult creation, retrieval, media attachment and status simulation. Published at v0 under /consults/v0 — pre-1.0 by the provider's own numbering, with no stability statement.
  name: Truepill Consults API
  slug: truepill-consults-api
- description: At-home diagnostics — test catalogue, kit serial validation, order creation and registration, rejection detail and results retrieval. Published at v0, with a v2 results endpoint alongside it.
  name: Truepill Diagnostics API
  slug: truepill-diagnostics-api
- description: File records for patient identification photos and selfies, backed by Google Cloud Storage signed URLs — the API mints a read or write signed URL and the client transfers the bytes directly, so no ima
  name: Truepill Media API
  slug: truepill-media-api
artifact_total: 23
asyncapis:
- description: ''
  name: Truepill Webhooks
  slug: truepill-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Truepill (FuzeRx) Insurance API
  slug: open-truepill-insurance-api
- collection_type: open
  name: Truepill (FuzeRx) Insurance Patients API
  slug: open-truepill-patients-api
- collection_type: open
  name: Truepill (FuzeRx) Insurance Prescriptions API
  slug: open-truepill-prescriptions-api
- collection_type: open
  name: Truepill (FuzeRx) Insurance Transfers API
  slug: open-truepill-transfers-api
- collection_type: open
  name: Truepill (FuzeRx) Insurance Webhooks API
  slug: open-truepill-webhooks-api
- collection_type: open
  name: Truepill (FuzeRx) API
  slug: open-truepill
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/truepill-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truepill-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truepill-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truepill-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truepill
- group: company
  title: ''
  type: Website
  url: https://www.truepill.com
- group: docs
  title: ''
  type: Documentation
  url: https://rxdocs.fuzehealth.com
- group: commercial
  title: ''
  type: Plans
  url: plans/truepill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truepill-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truepill-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rx.fuzehealth.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://rxdocs.fuzehealth.com
- group: start
  title: ''
  type: GettingStarted
  url: https://rx.fuzehealth.com/api-docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://rx.fuzehealth.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truepill
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rx.fuzehealth.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rx.fuzehealth.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rx.fuzehealth.com
- group: auth
  title: ''
  type: Compliance
  url: https://rxdocs.fuzehealth.com/#hipaa-amp-security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truepill-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truepill-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truepill-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/truepill-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/truepill-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/truepill-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/truepill-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truepill-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/truepill-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/truepill-decline-codes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truepill-llms.txt
created: '2026-06-21'
description: Truepill is a pharmacy and healthcare-infrastructure company providing API-driven prescription fulfillment, pharmacy dispensing, insurance/copay adjudication, telehealth, and at-home diagnostics. Following LetsGetChecked's 2024 acquisition of Truepill, the combined company rebranded as Fuze Health in May 2025, and the developer platform now ships as FuzeRx. The REST API exposes JSON endpoints for patients, prescriptions, transfers, insurance/copay, and webhook events under https://rxapi.fuzehealth.com/v1.
finops:
- name: Truepill Finops
  service_category: Healthcare and Pharmacy
  slug: truepill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truepill.png
layout: provider
modified: '2026-08-15'
name: Truepill
nav: Providers
network: true
overview: 'Truepill publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Insurance API, Patients API, Prescriptions API, and 6 more. Tagged areas include Pharmacy, Healthcare, Prescription Fulfillment, Telehealth, and Diagnostics.


  The Truepill catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Truepill''s developer surface includes authentication, documentation, API reference, getting-started guide, support, sandbox, and 25 more developer resources.'
plans:
- name: Truepill Plans Pricing
  plan_count: 1
  slug: truepill-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Truepill Rate Limits
  slug: truepill-rate-limits
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 23
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 59.3
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/screenshots/truepill-2026-08-17T082448.png
security:
- kind: authentication
  name: Truepill Authentication
  slug: truepill-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Truepill Domain Security
  slug: truepill-domain-security
  summary_line: TLSv1.3 · DMARC
slug: truepill
tags:
- Pharmacy
- Healthcare
- Prescription Fulfillment
- Telehealth
- Diagnostics
- Insurance
- Copay Adjudication
- Prior Authorization
- Electronic Prescribing
- Pharmacy Transfers
- Webhook
- HIPAA
website: https://www.truepill.com
---
