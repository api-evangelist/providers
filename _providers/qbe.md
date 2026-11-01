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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Qbe Agentic Access
  operation_count: 17
  slug: qbe-agentic-access
  summary_line: 17 operations · 15 acting
api_count: 2
apis:
- baseURL: https://gateway.api-au.qbe.com/ctp-service
  baseurl_source: declared
  description: The CTP Switch API from QBE Insurance — 2 operation(s) for ctp switch.
  name: QBE Insurance CTP Switch API
  slug: qbe-ctp-switch-api
- baseURL: https://gateway.api-au.qbe.com/x-digital-brokers-qbe-anzo/api
  baseurl_source: declared
  description: The Digital Brokers API from QBE Insurance — 15 operation(s) for digital brokers.
  name: QBE Insurance Digital Brokers API
  slug: qbe-digital-brokers-api
- description: QBE North America's API Product Hub for agency and property-manager partners, offering Renters (HO4, multi-dwelling unit) and Homeowners APIs such as the real-time Homeowners Quote API; access is requ
  name: QBE North America Partner API Hub
  slug: qbe-north-america-partner-api
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
artifact_total: 25
collections:
- collection_type: open
  name: ANZO Digital Brokers Experience API
  slug: open-qbe-anzo-digital-brokers
- collection_type: open
  name: CTP Switch Service
  slug: open-qbe-ctp-switch-service
common:
- group: design
  href: https://artifacts.apis.io/qbe/rules/qbe-rules.yml
  title: ''
  type: Spectral
  url: rules/qbe-rules.yml
- group: design
  href: https://artifacts.apis.io/qbe/json-ld/qbe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qbe-context.jsonld
- group: other
  href: https://artifacts.apis.io/qbe/overlays/qbe-ctp-switch-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qbe-ctp-switch-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/qbe/hosts/qbe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qbe-hosts.yml
- group: build
  href: https://artifacts.apis.io/qbe/integrations/qbe-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/qbe-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/qbe/vendors/qbe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qbe-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.qbe.com/newsroom
- group: agent
  href: https://artifacts.apis.io/qbe/agentic-access/qbe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qbe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/qbe/security/qbe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qbe-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/qbe/authentication/qbe-authentication.yml
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
  href: https://artifacts.apis.io/qbe/security/qbe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qbe-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/qbe/conventions/qbe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qbe-conventions.yml
- group: design
  href: https://artifacts.apis.io/qbe/errors/qbe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qbe-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qbe/lifecycle/qbe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qbe-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/qbe/conformance/qbe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qbe-conformance.yml
- group: design
  href: https://artifacts.apis.io/qbe/vocabulary/qbe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qbe-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/qbe/data-model/qbe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qbe-data-model.yml
- group: start
  href: https://artifacts.apis.io/qbe/sandbox/qbe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/qbe-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/qbe/mcp/qbe-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/qbe-mcp.yml
- group: agent
  href: https://artifacts.apis.io/qbe/llms/qbe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qbe-llms.txt
- group: agent
  href: https://artifacts.apis.io/qbe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/qbe/arazzo/qbe-quote-to-bind.yml
  title: ''
  type: Arazzo
  url: arazzo/qbe-quote-to-bind.yml
- group: design
  href: https://artifacts.apis.io/qbe/arazzo/qbe-endorse-and-bind.yml
  title: ''
  type: Arazzo
  url: arazzo/qbe-endorse-and-bind.yml
- group: design
  href: https://artifacts.apis.io/qbe/arazzo/qbe-cancel-policy.yml
  title: ''
  type: Arazzo
  url: arazzo/qbe-cancel-policy.yml
created: '2026-07-25'
description: 'QBE Insurance Group Limited is a Sydney-headquartered, ASX-listed global general insurance and reinsurance group, tracing back to 1886 in Townsville, Queensland, and operating today across Australia Pacific, North America and International divisions including a Lloyd''s of London syndicate. QBE writes commercial and personal property and casualty lines — property, liability, motor and compulsory third party (CTP), workers compensation, marine, aviation, trade credit, crop and specialty — distributed overwhelmingly through brokers and agents rather than direct to consumers. Its API posture reflects that distribution model and is partner-gated by design: QBE Australia runs a real, publicly browsable Azure API Management developer portal at connect.api-au.qbe.com whose catalogue, operations, schemas and examples can be read anonymously, but every product requires an approved subscription (approvalRequired true) and the broker API is keyed to named partner platforms. The portal
  exposes genuine quote, bind, endorse, renew, cancel and refer operations for the commercial policy lifecycle — the four real insurance verbs, minus claims/FNOL, which QBE does not expose publicly. A separate QBE North America partner API hub at partnerportal-api.qbena.com serves an empty Azure APIM catalogue to anonymous callers but does publish seven named API products in its own content pages — Quote, Bind, Master Liability, Property Inquiry, Zip Code Validate and Reconciliation and Cancellation for Renters, plus Quote for Homeowners — behind a documented client-id/secret to JWT token exchange; no endpoints or specs are exposed. QBE Hong Kong documents a partner API behind qbe.com pages that are bot-blocked to anonymous fetchers. Australia is the home market; the Consumer Data Right was designated for general insurance and then deferred, so nothing here is compelled by regulation.'
image: https://avatars.githubusercontent.com/u/55916773?s=280&v=4
json_schemas:
- name: AuthPoliciesPolicyIdEndorsePost200ApplicationJsonResponse
  property_count: 0
  slug: qbe-auth-policies-policy-id-endorse-post200-application-json-response
- name: AuthPoliciesPolicyIdReferPost200ApplicationJsonResponse
  property_count: 0
  slug: qbe-auth-policies-policy-id-refer-post200-application-json-response
- name: AuthQuotesPost201ApplicationJsonResponse
  property_count: 0
  slug: qbe-auth-quotes-post201-application-json-response
- name: AuthQuotesQuoteIdBindPost201ApplicationJsonResponse
  property_count: 0
  slug: qbe-auth-quotes-quote-id-bind-post201-application-json-response
- name: AuthQuotesQuoteIdReferPost200ApplicationJsonResponse
  property_count: 0
  slug: qbe-auth-quotes-quote-id-refer-post200-application-json-response
- name: Generated-2
  property_count: 1
  slug: qbe-generated-2
jsonld:
- class_count: 120
  name: Qbe Context
  property_count: 184
  slug: qbe-context
layout: provider
modified: '2026-10-20'
name: QBE Insurance
nav: Providers
network: true
overview: 'QBE Insurance publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including CTP Switch API, Digital Brokers API, and 1 more. Tagged areas include Insurance, Australia, Property and Casualty, Commercial Insurance, and Underwriting.


  The QBE Insurance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  QBE Insurance''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, sandbox, and 29 more developer resources.'
plans:
- name: Qbe Plans Pricing
  plan_count: 0
  slug: qbe-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Qbe Rate Limits
  slug: qbe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: QBE Insurance API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 3
  slug: qbe-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 28.8
    developer_ergonomics: 66.1
    discoverability: 57.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 39.3
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
    score: 27.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/qbe/qbe-2026-09-02T152422.png
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
skill_count: 3
skills:
- name: qbe-endorse-policy
  slug: qbe-endorse-policy
- name: qbe-quote-to-bind
  slug: qbe-quote-to-bind
- name: qbe-renew-or-cancel
  slug: qbe-renew-or-cancel
slug: qbe
tags:
- Insurance
- Australia
- Property and Casualty
- Commercial Insurance
- Underwriting
- Policy Administration
- Quotes
- Reinsurance
- Carrier
- Partner API
website: https://www.qbe.com/
---
