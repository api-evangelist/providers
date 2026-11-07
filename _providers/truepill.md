---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://www.truepill.com'', ''status'': 301, ''note'': ''declared website redirects to https://rx.fuzehealth.com/ — a different registrable domain (truepill.com -> fuzehealth.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 69
  human_in_the_loop: 0
  name: Truepill Agentic Access
  operation_count: 158
  slug: truepill-agentic-access
  summary_line: 158 operations · 69 acting
api_count: 1
apis:
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: Telehealth consult creation, retrieval, media attachment and status simulation. Published at v0 under /consults/v0 — pre-1.0 by the provider's own numbering, with no stability statement.
  name: Truepill Consults API
  slug: truepill-consults-api
- baseURL: https://rxapi.fuzehealth.com/diagnostics/v0
  baseurl_source: declared
  description: At-home diagnostics — test catalogue, kit serial validation, order creation and registration, rejection detail and results retrieval. Published at v0, with a v2 results endpoint alongside it.
  name: Truepill Diagnostics API
  slug: truepill-diagnostics-api
- baseURL: https://rxapi.fuzehealth.com/v1
  baseurl_source: declared
  description: The scheduled-actions API from Truepill — 1 operation(s) for scheduled-actions.
  name: Truepill Scheduled Actions API
  slug: truepill-scheduled-actions-api
- baseURL: https://rxapi.fuzehealth.com/v1
  baseurl_source: declared
  description: The scheduled-fill-requests API from Truepill — 2 operation(s) for scheduled-fill-requests.
  name: Truepill Scheduled Fill Requests API
  slug: truepill-scheduled-fill-requests-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Auto Refill API from Truepill — 10 operation(s) for auto refill.
  name: Truepill Auto Refill API
  slug: truepill-auto-refill-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Availability API from Truepill — 2 operation(s) for availability.
  name: Truepill Availability API
  slug: truepill-availability-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Cancel Request API from Truepill — 2 operation(s) for cancel request.
  name: Truepill Cancel Request API
  slug: truepill-cancel-request-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Copay Request API from Truepill — 6 operation(s) for copay request.
  name: Truepill Copay Request API
  slug: truepill-copay-request-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Coverage Request API from Truepill — 2 operation(s) for coverage request.
  name: Truepill Coverage Request API
  slug: truepill-coverage-request-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Direct Transfer API from Truepill — 8 operation(s) for direct transfer.
  name: Truepill Direct Transfer API
  slug: truepill-direct-transfer-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The External Location Matches API from Truepill — 2 operation(s) for external location matches.
  name: Truepill External Location Matches API
  slug: truepill-external-location-matches-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The External Locations API from Truepill — 4 operation(s) for external locations.
  name: Truepill External Locations API
  slug: truepill-external-locations-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The External Transfers API from Truepill — 2 operation(s) for external transfers.
  name: Truepill External Transfers API
  slug: truepill-external-transfers-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Fill Request API from Truepill — 8 operation(s) for fill request.
  name: Truepill Fill Request API
  slug: truepill-fill-request-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Fill Requests API from Truepill — 2 operation(s) for fill requests.
  name: Truepill Fill Requests API
  slug: truepill-fill-requests-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Fuzion Test API from Truepill — 2 operation(s) for fuzion test.
  name: Truepill Fuzion Test API
  slug: truepill-fuzion-test-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Insurance API from Truepill — 6 operation(s) for insurance.
  name: Truepill Insurance API
  slug: truepill-insurance-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Media API from Truepill — 12 operation(s) for media.
  name: Truepill Media API
  slug: truepill-media-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Nearby Same Day Pickup Locations API from Truepill — 2 operation(s) for nearby same day pickup locations.
  name: Truepill Nearby Same Day Pickup Locations API
  slug: truepill-nearby-same-day-pickup-locations-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Open Api API from Truepill — 2 operation(s) for open api.
  name: Truepill Open API
  slug: truepill-open-api-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Order API from Truepill — 4 operation(s) for order.
  name: Truepill Order API
  slug: truepill-order-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Patient API from Truepill — 8 operation(s) for patient.
  name: Truepill Patient API
  slug: truepill-patient-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Pharmacy Coverage API from Truepill — 2 operation(s) for pharmacy coverage.
  name: Truepill Pharmacy Coverage API
  slug: truepill-pharmacy-coverage-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Prescriber API from Truepill — 4 operation(s) for prescriber.
  name: Truepill Prescriber API
  slug: truepill-prescriber-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Prescription API from Truepill — 12 operation(s) for prescription.
  name: Truepill Prescription API
  slug: truepill-prescription-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Prescriptions API from Truepill — 2 operation(s) for prescriptions.
  name: Truepill Prescriptions API
  slug: truepill-prescriptions-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Prior Authorization API from Truepill — 2 operation(s) for prior authorization.
  name: Truepill Prior Authorization API
  slug: truepill-prior-authorization-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Same Day Delivery API from Truepill — 4 operation(s) for same day delivery.
  name: Truepill Same Day Delivery API
  slug: truepill-same-day-delivery-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Schedule API from Truepill — 1 operation(s) for schedule.
  name: Truepill Schedule API
  slug: truepill-schedule-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Specialty Pharmacies API from Truepill — 2 operation(s) for specialty pharmacies.
  name: Truepill Specialty Pharmacies API
  slug: truepill-specialty-pharmacies-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Transfer Request API from Truepill — 4 operation(s) for transfer request.
  name: Truepill Transfer Request API
  slug: truepill-transfer-request-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Update Request API from Truepill — 2 operation(s) for update request.
  name: Truepill Update Request API
  slug: truepill-update-request-api
- baseURL: https://rxapi.fuzehealth.com/consults/v0
  baseurl_source: declared
  description: The Webhook Events API from Truepill — 4 operation(s) for webhook events.
  name: Truepill Webhook Events API
  slug: truepill-webhook-events-api
artifact_total: 52
asyncapis:
- description: ''
  name: Truepill Webhooks
  slug: truepill-webhooks
collections:
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
  href: https://artifacts.apis.io/truepill/overlays/truepill-insurance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-insurance-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/overlays/truepill-patients-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-patients-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/overlays/truepill-prescriptions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-prescriptions-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/overlays/truepill-transfers-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-transfers-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/overlays/truepill-webhooks-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-webhooks-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/overlays/truepill-fulfillment-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-fulfillment-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/overlays/truepill-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-media-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/truepill/capabilities/truepill-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/truepill-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/truepill/agentic-access/truepill-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/truepill-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/truepill/security/truepill-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/truepill-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/truepill/authentication/truepill-authentication.yml
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
  href: https://artifacts.apis.io/truepill/plans/truepill-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/truepill-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/truepill/rate-limits/truepill-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/truepill-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/truepill/finops/truepill-finops.yml
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
  href: https://artifacts.apis.io/truepill/lifecycle/truepill-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/truepill-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/truepill/conventions/truepill-conventions.yml
  title: ''
  type: Conventions
  url: conventions/truepill-conventions.yml
- group: design
  href: https://artifacts.apis.io/truepill/conformance/truepill-conformance.yml
  title: ''
  type: Conformance
  url: conformance/truepill-conformance.yml
- group: design
  href: https://artifacts.apis.io/truepill/data-model/truepill-data-model.yml
  title: ''
  type: DataModel
  url: data-model/truepill-data-model.yml
- group: build
  href: https://artifacts.apis.io/truepill/packages/truepill-packages.yml
  title: ''
  type: Packages
  url: packages/truepill-packages.yml
- group: start
  href: https://artifacts.apis.io/truepill/sandbox/truepill-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/truepill-sandbox.yml
- group: design
  href: https://artifacts.apis.io/truepill/asyncapi/truepill-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/truepill-webhooks.yml
- group: design
  href: https://artifacts.apis.io/truepill/errors/truepill-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/truepill-problem-types.yml
- group: design
  href: https://artifacts.apis.io/truepill/errors/truepill-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/truepill-error-codes.yml
- group: build
  href: https://artifacts.apis.io/truepill/errors/truepill-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/truepill-decline-codes.yml
- group: agent
  href: https://artifacts.apis.io/truepill/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/truepill/llms/truepill-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/truepill-llms.txt
created: '2026-06-21'
description: Truepill is a pharmacy and healthcare-infrastructure company providing API-driven prescription fulfillment, pharmacy dispensing, insurance/copay adjudication, telehealth, and at-home diagnostics. Following LetsGetChecked's 2024 acquisition of Truepill, the combined company rebranded as Fuze Health in May 2025, and the developer platform now ships as FuzeRx. The REST API exposes JSON endpoints for patients, prescriptions, transfers, insurance/copay, and webhook events under https://rxapi.fuzehealth.com/v1.
finops:
- has_sources: true
  method: derived
  name: Truepill Finops
  primary_unit: ''
  service_category: ''
  slug: truepill-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truepill.png
layout: provider
modified: '2026-08-15'
name: Truepill
nav: Providers
network: true
overview: 'Truepill publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Consults API, Diagnostics API, Scheduled Actions API, and 30 more. Tagged areas include Pharmacy, Healthcare, Prescription Fulfillment, Telehealth, and Diagnostics.


  The Truepill catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Truepill''s developer surface includes authentication, documentation, API reference, getting-started guide, support, sandbox, and 32 more developer resources.'
plans:
- name: Truepill Plans Pricing
  plan_count: 1
  slug: truepill-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Truepill Rate Limits
  slug: truepill-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Truepill API Rules
  rule_count: 46
  severity_counts:
    error: 34
    hint: 0
    info: 2
    warn: 10
  slug: truepill-rules
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 46.1
    contract_governance: 31.8
    contract_quality: 55.8
    developer_ergonomics: 64.9
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 33
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/truepill/truepill-2026-08-17T082448.png
security:
- kind: authentication
  name: Truepill Authentication
  slug: truepill-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Truepill Domain Security
  slug: truepill-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: Consume and reconcile FuzeRx webhook events
  slug: truepill-consume-webhook-events
- name: Determine a patient's copay and coverage (FuzeRx)
  slug: truepill-copay-and-coverage
- name: Create a patient and submit a fill request (FuzeRx)
  slug: truepill-create-patient-and-fill
- name: Run a FuzeRx integration end-to-end in the sandbox
  slug: truepill-sandbox-simulation
- name: Transfer a prescription into FuzeRx from another pharmacy
  slug: truepill-transfer-prescription-in
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
