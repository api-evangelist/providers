---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Quote-side policy lifecycle — create and patch proposals, add and remove policy lines, coverages, schedules and linked schedules, list insurance programs, carriers, policy lines and states, run or que
  name: Origami Risk Quotes and Proposals API
  slug: origami-risk-quotes-and-proposals-api
- description: Issue-side policy administration — accept, reject, undo-accept, undo-reject and undo-binding a bound proposal to issue a policy, then endorse, cancel, reinstate, change billing frequency and take paym
  name: Origami Risk Policies API
  slug: origami-risk-policies-api
- description: Billing account operations including making and reversing payments, plus an online policy payment surface integrated with the One Inc payment gateway covering payment submission, payment-method acknow
  name: Origami Risk Billing and Payments API
  slug: origami-risk-billing-accounts-api
- description: Real-time and queued platform actions triggered against any domain record — including creating a claim from an incident (the FNOL path), FirstReport, Reserve, Review, RootCause, EDIReport state report
  name: Origami Risk Actions API
  slug: origami-risk-actions-api
- description: Inbound webhook surface for the Origami Risk platform. An Origami "webhook handler" is a bespoke endpoint built inside Origami by the services team that an external system posts data into — list the c
  name: Origami Risk Webhooks API
  slug: origami-risk-webhooks-api
- description: Reporting surface for requesting a report run, retrieving report details and options, validating a report filter, and converting between the platform's view-filter string form and its JSON tree form.
  name: Origami Risk Reports API
  slug: origami-risk-reports-api
- baseURL: https://{environment}.origamirisk.com/OrigamiApi-v2
  baseurl_source: declared
  description: The Authentication API from Origami Risk — 4 operation(s) for authentication.
  name: Origami Risk Authentication API
  slug: origami-risk-authentication-api
- baseURL: https://{environment}.origamirisk.com/OrigamiApi-v2
  baseurl_source: declared
  description: The HasTokenExpired API from Origami Risk — 1 operation(s) for hastokenexpired.
  name: Origami Risk Has Token Expired API
  slug: origami-risk-hastokenexpired-api
- baseURL: https://{environment}.origamirisk.com/OrigamiApi-v2
  baseurl_source: declared
  description: The New Endpoint 1 API from Origami Risk — 1 operation(s) for new endpoint 1.
  name: Origami Risk New Endpoint 1 API
  slug: origami-risk-new-endpoint-1-api
- baseURL: https://{environment}.origamirisk.com/OrigamiApi-v2
  baseurl_source: declared
  description: The New Endpoint API from Origami Risk — 1 operation(s) for new endpoint.
  name: Origami Risk New Endpoint API
  slug: origami-risk-new-endpoint-api
- baseURL: https://{environment}.origamirisk.com/OrigamiApi-v2
  baseurl_source: declared
  description: The Requests API from Origami Risk — 3 operation(s) for requests.
  name: Origami Risk Requests API
  slug: origami-risk-requests-api
artifact_total: 28
asyncapis:
- description: ''
  name: Origami Risk Webhooks
  slug: origami-risk-webhooks
collections:
- collection_type: open
  name: Origami Risk Authentication
  slug: open-origami-risk-authentication
- collection_type: open
  name: Origami Risk Public API
  slug: open-origami-risk-public-api
- collection_type: open
  name: Rating API
  slug: open-origami-risk-rating-api
- collection_type: open
  name: Rating API
  slug: open-origami-risk-standard-rating-api
common:
- group: commercial
  href: https://artifacts.apis.io/origami-risk/plans/origami-risk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/origami-risk-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.origamirisk.com/feed/
- group: other
  href: https://artifacts.apis.io/origami-risk/overlays/origami-risk-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origami-risk-authentication-overlay.yaml
- group: other
  href: https://artifacts.apis.io/origami-risk/overlays/origami-risk-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origami-risk-public-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/origami-risk/skills/origami-risk-domain-data-access.md
  title: ''
  type: AgentSkill
  url: skills/origami-risk-domain-data-access.md
- group: other
  href: https://artifacts.apis.io/origami-risk/overlays/origami-risk-standard-rating-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origami-risk-standard-rating-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/origami-risk/overlays/origami-risk-rating-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/origami-risk-rating-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/origami-risk/skills/origami-risk-standard-rating-service.md
  title: ''
  type: AgentSkill
  url: skills/origami-risk-standard-rating-service.md
- group: auth
  href: https://artifacts.apis.io/origami-risk/security/origami-risk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/origami-risk-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.origamirisk.com/
- group: auth
  href: https://artifacts.apis.io/origami-risk/security/origami-risk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/origami-risk-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/origami-risk/authentication/origami-risk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/origami-risk-authentication.yml
- group: design
  href: https://artifacts.apis.io/origami-risk/conventions/origami-risk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/origami-risk-conventions.yml
- group: design
  href: https://artifacts.apis.io/origami-risk/errors/origami-risk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/origami-risk-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/origami-risk/rate-limits/origami-risk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/origami-risk-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/origami-risk/lifecycle/origami-risk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/origami-risk-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.origamirisk.com/
- group: operate
  title: ''
  type: SLA
  url: https://www.origamirisk.com/serviceterms/sla/
- group: operate
  href: https://artifacts.apis.io/origami-risk/changelog/origami-risk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/origami-risk-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.origamirisk.com/platform/product-updates/
- group: start
  href: https://artifacts.apis.io/origami-risk/sandbox/origami-risk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/origami-risk-sandbox.yml
- group: design
  href: https://artifacts.apis.io/origami-risk/conformance/origami-risk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/origami-risk-conformance.yml
- group: design
  href: https://artifacts.apis.io/origami-risk/data-model/origami-risk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/origami-risk-data-model.yml
- group: design
  href: https://artifacts.apis.io/origami-risk/asyncapi/origami-risk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/origami-risk-webhooks.yml
- group: build
  href: https://artifacts.apis.io/origami-risk/packages/origami-risk-packages.yml
  title: ''
  type: Packages
  url: packages/origami-risk-packages.yml
- group: agent
  href: https://artifacts.apis.io/origami-risk/mcp/origami-risk-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/origami-risk-mcp.yml
- group: agent
  href: https://artifacts.apis.io/origami-risk/llms/origami-risk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/origami-risk-llms.txt
- group: agent
  href: https://artifacts.apis.io/origami-risk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.origamirisk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.origamirisk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.origamirisk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.origamirisk.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.origamirisk.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.origamirisk.com/reference/authentication-methods
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.origamirisk.com/reference/limits
- group: other
  title: ''
  type: ProductOverview
  url: https://www.origamirisk.com/platform/api-access/
- group: company
  title: ''
  type: Partners
  url: https://www.origamirisk.com/partners/
- group: start
  title: ''
  type: Login
  url: https://developers.origamirisk.com/login?redirect_uri=/
- group: operate
  title: ''
  type: Support
  url: https://www.origamirisk.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.origamirisk.com/resources/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.origamirisk.com/serviceterms/aipricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.origamirisk.com/origami-risk-website-terms-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.origamirisk.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/origamirisk
created: '2026-07-25'
description: Origami Risk is a Chicago-headquartered risk, safety and insurance SaaS company founded in 2009 that began as a single-version cloud RMIS (risk management information system) and grew into a core-systems platform for the United States property and casualty market. It sells policy administration, digital underwriting, rating, billing, premium audit, claims administration, compliance and EHS/GRC modules to carriers, MGAs, program administrators, third-party administrators, risk pools, brokers, healthcare systems and large self-insureds, across workers' compensation, medical professional liability, personal auto and homeowners lines. Unlike most US insurance organizations, Origami Risk sits in the software layer between carriers and distribution and therefore does publish a genuinely public, self-serve developer portal at developers.origamirisk.com — a ReadMe-hosted reference readable without login, covering quote and proposal creation, rating, bind, policy issue/endorse/cancel,
  billing and payments, claims-from-incident and first-report actions, files, reports, domain metadata and outbound webhooks. Four OpenAPI definitions are downloadable from the portal's spec registry, though three of the four are thin scaffolds and the bulk of the reference is hand-authored per-endpoint documentation rather than a complete machine-readable spec. Access to a live tenant is still commercial — the base URL is a per-customer https://{environment}.origamirisk.com host and authentication is token-based or HMAC against a provisioned account — and no ACORD, AL3, IVANS or NGDS conformance is claimed anywhere in the marketing site or the developer portal.
finops:
- has_sources: true
  method: derived
  name: Origami Risk Finops
  primary_unit: ''
  service_category: ''
  slug: origami-risk-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-10-06'
name: Origami Risk
nav: Providers
network: true
overview: 'Origami Risk publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Has Token Expired API, New Endpoint 1 API, and 8 more. Tagged areas include Insurance, United States, Property and Casualty, Policy Administration, and Claims.


  The Origami Risk catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Origami Risk''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Origami Risk Plans Pricing
  plan_count: 0
  slug: origami-risk-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Origami Risk Rate Limits
  slug: origami-risk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Origami Risk API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: origami-risk-rules
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 48.5
    developer_ergonomics: 55.4
    discoverability: 71.4
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 52.7
  provenance:
    conformance: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 26.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/origami-risk/origami-risk-2026-08-07T190927.png
security:
- kind: authentication
  name: Origami Risk Authentication
  slug: origami-risk-authentication
  summary_line: apiKey/token-endpoint/hmac · 6 schemes
- kind: domain-security
  name: Origami Risk Domain Security
  slug: origami-risk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Origami Risk Trust Center
  slug: origami-risk-trust-center
  summary_line: trust center published
skill_count: 5
skills:
- name: Read and write Origami Risk domain data safely
  slug: origami-risk-domain-data-access
- name: Create a claim from an incident (FNOL) on Origami Risk
  slug: origami-risk-fnol-claim-from-incident
- name: Issue and service a policy on Origami Risk
  slug: origami-risk-issue-and-service-policy
- name: Quote a risk and bind it into a policy on Origami Risk
  slug: origami-risk-quote-to-bind
- name: Submit a rating request to the Origami Risk Standard Rating service
  slug: origami-risk-standard-rating-service
slug: origami-risk
tags:
- Insurance
- United States
- Property and Casualty
- Policy Administration
- Claims
- Underwriting
- Core Systems
- Risk Management
- Workers Compensation
- Insurtech
- Billing
website: https://www.origamirisk.com/
---
