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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Qbe Agentic Access
  operation_count: 17
  slug: qbe-agentic-access
  summary_line: 17 operations · 15 acting
api_count: 2
apis:
- baseURL: https://gateway.api-au.qbe.com/x-digital-brokers-qbe-anzo/api
  baseurl_source: declared
  description: The CTP Switch API from QBE Insurance — 2 operation(s) for ctp switch.
  name: QBE Insurance CTP Switch API
  slug: qbe-ctp-switch-api
- baseURL: https://gateway.api-au.qbe.com/x-digital-brokers-qbe-anzo/api
  baseurl_source: declared
  description: The Digital Brokers API from QBE Insurance — 15 operation(s) for digital brokers.
  name: QBE Insurance Digital Brokers API
  slug: qbe-digital-brokers-api
arazzos:
- description: Cancel an in-force QBE policy with a published cancellation reason code, confirm it, and attach the cancellation schedule.
  name: QBE policy cancellation
  slug: qbe-cancel-policy
- description: Open a mid-term endorsement on an in-force QBE policy, confirm it with a bind, and attach the endorsement schedule.
  name: QBE mid-term endorsement, confirmed
  slug: qbe-endorse-and-bind
- description: Create a commercial quote with QBE Australia, amend it, then convert it into a bound policy.
  name: QBE quote to bound policy
  slug: qbe-quote-to-bind
artifact_total: 11
collections:
- collection_type: open
  name: ANZO Digital Brokers Experience API
  slug: open-qbe-anzo-digital-brokers
- collection_type: open
  name: CTP Switch Service
  slug: open-qbe-ctp-switch-service
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/qbe-anzo-digital-brokers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/qbe-ctp-switch-service-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qbe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qbe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qbe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.qbe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://connect.api-au.qbe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://connect.api-au.qbe.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://connect.api-au.qbe.com/apis
- group: start
  title: ''
  type: PartnerPortal
  url: https://partnerportal-api.qbena.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://connect.api-au.qbe.com/getting-started
- group: start
  title: ''
  type: Login
  url: https://connect.api-au.qbe.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.qbe.com/au/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qbe.com/au/about/governance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qbe.com/us/legal/api-terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qbegroup
- group: auth
  title: ''
  type: Security
  url: https://www.qbe.com/responsible-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qbe-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qbe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qbe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qbe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qbe-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/qbe-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qbe-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qbe-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/qbe-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/qbe-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/qbe-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qbe-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qbe-quote-to-bind.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qbe-endorse-and-bind.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qbe-cancel-policy.yml
created: '2026-07-25'
description: 'QBE Insurance Group Limited is a Sydney-headquartered, ASX-listed global general insurance and reinsurance group, tracing back to 1886 in Townsville, Queensland, and operating today across Australia Pacific, North America and International divisions including a Lloyd''s of London syndicate. QBE writes commercial and personal property and casualty lines — property, liability, motor and compulsory third party (CTP), workers compensation, marine, aviation, trade credit, crop and specialty — distributed overwhelmingly through brokers and agents rather than direct to consumers. Its API posture reflects that distribution model and is partner-gated by design: QBE Australia runs a real, publicly browsable Azure API Management developer portal at connect.api-au.qbe.com whose catalogue, operations, schemas and examples can be read anonymously, but every product requires an approved subscription (approvalRequired true) and the broker API is keyed to named partner platforms. The portal
  exposes genuine quote, bind, endorse, renew, cancel and refer operations for the commercial policy lifecycle — the four real insurance verbs, minus claims/FNOL, which QBE does not expose publicly. A separate QBE North America partner API hub at partnerportal-api.qbena.com serves an empty Azure APIM catalogue to anonymous callers but does publish seven named API products in its own content pages — Quote, Bind, Master Liability, Property Inquiry, Zip Code Validate and Reconciliation and Cancellation for Renters, plus Quote for Homeowners — behind a documented client-id/secret to JWT token exchange; no endpoints or specs are exposed. QBE Hong Kong documents a partner API behind qbe.com pages that are bot-blocked to anonymous fetchers. Australia is the home market; the Consumer Data Right was designated for general insurance and then deferred, so nothing here is compelled by regulation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: QBE Insurance
nav: Providers
network: true
overview: 'QBE Insurance publishes 2 APIs on the [APIs.io](https://apis.io/) network: CTP Switch API and Digital Brokers API. Tagged areas include Insurance, Australia, Property and Casualty, Commercial Insurance, and Underwriting.


  QBE Insurance''s developer surface includes authentication, documentation, API reference, getting-started guide, support, sandbox, and 27 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 8.3
    contract_quality: 15.7
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 8.3
    operational_transparency: 13.2
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qbe/refs/heads/main/screenshots/qbe-2026-09-02T152422.png
security:
- kind: authentication
  name: Qbe Authentication
  slug: qbe-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Qbe Domain Security
  slug: qbe-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qbe Vulnerability Disclosure
  slug: qbe-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: qbe
tags:
- Insurance
- Australia
- Property and Casualty
- Commercial Insurance
- Underwriting
- Policy Administration
- Quotes
- Brokers
- Reinsurance
- Carrier
- Partner API
website: https://www.qbe.com/
---
