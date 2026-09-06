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
    error_semantics: verified
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
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Steadily Agentic Access
  operation_count: 39
  slug: steadily-agentic-access
  summary_line: 39 operations · 14 acting
api_count: 3
apis:
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: 'Steadily uses Bearer Tokens to authenticate requests to the quoting endpoints on behalf of some appointed agent. There''s two steps to this process: 1. Use your agency''s Steadily API Key to request a b'
  name: Steadily Account API
  slug: steadily-account-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: A Draft Quote is an editable draft of a policy. Create a new draft quote by passing in basic insured and property information to `POST /v1/agency/draft_quote` with an authenticated bearer token header
  name: Steadily Draft Quote API
  slug: steadily-draft-quote-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: Submit and retrieve lead referrals. Use the refer lead endpoint to submit a lead with full quote details and start the insurance quote process. You'll get back a quote estimate and a start_url for the
  name: Steadily Lead Referrals API
  slug: steadily-lead-referrals-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: Policy information and change requests for third-party lender integrations
  name: Steadily Lender API
  slug: steadily-lender-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: A Policy is an issued insurance policy. The declaration document and policy packet are available.
  name: Steadily Policy API
  slug: steadily-policy-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: The Instant Estimate API is a one-step express API to quickly get a landlord insurance estimate you can display within your platform. To get started, you only need to send the address and a unique pro
  name: Steadily Quote Estimates API
  slug: steadily-quote-estimates-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: An Offer is an immutable offer for coverage extended to a customer. Offers are generated from draft quotes and provides a PDF quote document. Creating an offer requires no outstanding underwriting ale
  name: Steadily Quote Offer API
  slug: steadily-quote-offer-api
- baseURL: https://api.steadily.com
  baseurl_source: declared
  description: Reporting on the referrals you've sent Steadily and the referral fees you've earned. The lead, account, and policy endpoints follow each referral through its lifetime. The summary views provide aggreg
  name: Steadily Reporting API
  slug: steadily-reporting-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Partner Account API
  slug: open-steadily-account-api
- collection_type: open
  name: Partner Account Draft Quote API
  slug: open-steadily-draft-quote-api
- collection_type: open
  name: Partner Account Lead Referrals API
  slug: open-steadily-lead-referrals-api
- collection_type: open
  name: Partner Account Lender API
  slug: open-steadily-lender-api
- collection_type: open
  name: Partner Account Policy API
  slug: open-steadily-policy-api
- collection_type: open
  name: Partner Account Quote Estimates API
  slug: open-steadily-quote-estimates-api
- collection_type: open
  name: Partner Account Quote Offer API
  slug: open-steadily-quote-offer-api
- collection_type: open
  name: Partner Account Reporting API
  slug: open-steadily-reporting-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/steadily-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/steadily-estimate-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/steadily-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steadily-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/steadily-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.steadily.com/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steadily-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/steadily-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/steadily-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/steadily-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/steadily-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/steadily-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/steadily-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/steadily-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.steadily.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.steadily.com/redoc
- group: docs
  title: ''
  type: APIReference
  url: https://api.steadily.com/estimate-api/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://www.steadily.com/api
- group: company
  title: ''
  type: Blog
  url: https://www.steadily.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.steadily.com/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.steadily.com
- group: start
  title: ''
  type: SignUp
  url: https://www.steadily.com/partners
- group: company
  title: ''
  type: Website
  url: https://steadily.com
created: '2026-07-17'
description: Steadily is a US landlord-insurance provider — built by landlords, for landlords — writing rental-property policies in all 50 states with online quotes in minutes and coverage designed around how rental properties actually work. Its Partner API, a FastAPI-based REST service at api.steadily.com, lets property managers, lenders, and marketplaces generate instant insurance estimates, refer leads, and track bound policies. Appointed independent agencies use the companion Rater Quotes API to create, price, underwrite, and offer quotes directly from their rater. Steadily was founded by a landlord who could not find decent insurance for his own rental property.
image: https://app.steadily.com/static/images/steadily-logo.svg
layout: provider
modified: '2026-07-21'
name: Steadily
nav: Providers
network: true
overview: 'Steadily publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Draft Quote API, Lead Referrals API, and 5 more. Tagged areas include Company, Fintech, Insurance, Landlord Insurance, and Insurtech.


  Steadily''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 52.9
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
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
    regime: Insurance
    regime_id: insurance
    score: 40.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/steadily/refs/heads/main/screenshots/steadily-2026-09-02T160824.png
security:
- kind: authentication
  name: Steadily Authentication
  slug: steadily-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Steadily Domain Security
  slug: steadily-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Steadily Vulnerability Disclosure
  slug: steadily-vulnerability-disclosure
  summary_line: disclosure policy published
slug: steadily
tags:
- Company
- Fintech
- Insurance
- Landlord Insurance
- Insurtech
- Real-Estate
- Rental Property
website: https://steadily.com
---
