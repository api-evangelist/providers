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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Holvi Agentic Access
  operation_count: 9
  slug: holvi-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.psd2.holvi.com
  baseurl_source: declared
  description: AISP endpoints - read Holvi customer payment accounts and payments.
  name: Holvi Account Information API
  slug: holvi-account-information-api
- baseURL: https://api.psd2.holvi.com
  baseurl_source: declared
  description: PSU authentication and consent token exchange.
  name: Holvi Consent API
  slug: holvi-consent-api
- baseURL: https://api.psd2.holvi.com
  baseurl_source: declared
  description: PISP endpoints - initiate and confirm SEPA / SEPA Instant / SWIFT payments.
  name: Holvi Payment Initiation API
  slug: holvi-payment-initiation-api
- baseURL: https://api.psd2.holvi.com
  baseurl_source: declared
  description: TPP certificate lifecycle.
  name: Holvi Third Party Provider API
  slug: holvi-third-party-provider-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Holvi PSD2 Account Information API
  slug: open-holvi-account-information-api
- collection_type: open
  name: Holvi PSD2 Account Information Consent API
  slug: open-holvi-consent-api
- collection_type: open
  name: Holvi PSD2 Account Information Payment Initiation API
  slug: open-holvi-payment-initiation-api
- collection_type: open
  name: Holvi PSD2 Account Information Third Party Provider API
  slug: open-holvi-third-party-provider-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/holvi-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/holvi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/holvi-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holvi-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/holvi-psd2-openapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/holvi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/holvi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/holvi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/holvi-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/holvi-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/holvi-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/holvi-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/holvi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.holvi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://holvi-developer.zendesk.com/hc/en-gb
- group: docs
  title: ''
  type: Documentation
  url: https://holvi.github.io/psd2-api/
- group: docs
  title: ''
  type: APIReference
  url: https://holvi.github.io/psd2-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://holvi.github.io/psd2-api/initial_steps/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://holvi.github.io/psd2-api/changelog.html
- group: operate
  title: ''
  type: Support
  url: https://support.holvi.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://blog.holvi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/holvi
- group: commercial
  title: ''
  type: Pricing
  url: https://www.holvi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://login.app.holvi.com/register
- group: start
  title: ''
  type: Login
  url: https://login.app.holvi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.holvi.com/hc/en-gb/articles/33569262656402-Terms-of-Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.holvi.com/hc/en-gb/articles/29831985498258-Privacy-Notice
created: '2026-07-17'
description: Holvi is a Finnish digital business-banking service for freelancers, founders and small businesses, founded in Helsinki in 2011 and operating as a regulated Authorised Payment Institution supervised by the Finnish Financial Supervisory Authority. It combines a business account with its own IBAN, a Holvi Business Mastercard, invoicing, expense tracking, VAT calculation and bookkeeping preparation in one dashboard, serving more than 150,000 businesses across Europe with a focus on Finland, Germany and Austria. For developers, Holvi publishes a PSD2 API v2.0 for licensed Third Party Providers, exposing account information (AISP) and payment initiation (PISP, SEPA / SEPA Instant / SWIFT) with Strong Customer Authentication and optional Verification of Payee.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/holvi.png
layout: provider
modified: '2026-07-19'
name: Holvi
nav: Providers
network: true
overview: 'Holvi publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Consent API, Payment Initiation API, and 1 more. Tagged areas include Company, Banking, Fintech, Payments, and Business Banking.


  Holvi''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, engineering blog, and 21 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 56.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 36.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/holvi/refs/heads/main/screenshots/holvi-2026-07-25T221323.png
security:
- kind: authentication
  name: Holvi Authentication
  slug: holvi-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Holvi Domain Security
  slug: holvi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: holvi
tags:
- Company
- Banking
- Fintech
- Payments
- Business Banking
- PSD2
- Open Banking
- SEPA
- Finland
website: https://www.holvi.com/
---
