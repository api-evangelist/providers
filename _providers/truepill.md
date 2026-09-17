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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-09-16'
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
  description: The api API from Truepill — 61 operation(s) for api.
  name: Truepill API
  slug: truepill-api-api
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
- baseURL: https://rxapi.fuzehealth.com/v1
  baseurl_source: declared
  description: The v0 API from Truepill — 1 operation(s) for v0.
  name: Truepill V0 API
  slug: truepill-v0-api
- baseURL: https://rxapi.fuzehealth.com/v1
  baseurl_source: declared
  description: The v1 API from Truepill — 58 operation(s) for v1.
  name: Truepill V1 API
  slug: truepill-v1-api
- baseURL: https://rxapi.fuzehealth.com/v1
  baseurl_source: declared
  description: The v2 API from Truepill — 3 operation(s) for v2.
  name: Truepill V2 API
  slug: truepill-v2-api
artifact_total: 22
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
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-insurance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-insurance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-patients-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-patients-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-prescriptions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-prescriptions-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-transfers-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-transfers-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-webhooks-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-webhooks-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-fulfillment-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-fulfillment-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/overlays/truepill-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truepill-media-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/capabilities/truepill-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/truepill-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/agentic-access/truepill-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/truepill-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/security/truepill-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/truepill-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/authentication/truepill-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/plans/truepill-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/truepill-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/rate-limits/truepill-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/truepill-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/finops/truepill-finops.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/lifecycle/truepill-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/truepill-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/conventions/truepill-conventions.yml
  title: ''
  type: Conventions
  url: conventions/truepill-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/conformance/truepill-conformance.yml
  title: ''
  type: Conformance
  url: conformance/truepill-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/data-model/truepill-data-model.yml
  title: ''
  type: DataModel
  url: data-model/truepill-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/packages/truepill-packages.yml
  title: ''
  type: Packages
  url: packages/truepill-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/sandbox/truepill-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/truepill-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/asyncapi/truepill-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/truepill-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/errors/truepill-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/truepill-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/errors/truepill-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/truepill-error-codes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/errors/truepill-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/truepill-decline-codes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/truepill/refs/heads/main/llms/truepill-llms.txt
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
overview: 'Truepill publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Consults API, Diagnostics API, and 6 more. Tagged areas include Pharmacy, Healthcare, Prescription Fulfillment, Telehealth, and Diagnostics.


  The Truepill catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Truepill''s developer surface includes authentication, documentation, API reference, getting-started guide, support, sandbox, and 32 more developer resources.'
plans:
- name: Truepill Plans Pricing
  plan_count: 1
  slug: truepill-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Truepill Rate Limits
  slug: truepill-rate-limits
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 57.5
    developer_ergonomics: 64.9
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
