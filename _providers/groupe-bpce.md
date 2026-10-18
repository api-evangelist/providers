---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Groupe Bpce Agentic Access
  operation_count: 49
  slug: groupe-bpce-agentic-access
  summary_line: 49 operations · 16 acting
api_count: 17
apis:
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: The AISP API from Groupe BPCE — 9 operation(s) for aisp.
  name: Groupe BPCE AISP API
  slug: groupe-bpce-aisp-api
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: The CBPII API from Groupe BPCE — 1 operation(s) for cbpii.
  name: Groupe BPCE CBPII API
  slug: groupe-bpce-cbpii-api
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: 'External Accounts Management: Searching for accounts or declaring new ones.'
  name: Groupe BPCE External Accounts API
  slug: groupe-bpce-external-accounts-api
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: Internal Accounts Management.
  name: Groupe BPCE Internal Accounts API
  slug: groupe-bpce-internal-accounts-api
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: The PISP API from Groupe BPCE — 5 operation(s) for pisp.
  name: Groupe BPCE PISP API
  slug: groupe-bpce-pisp-api
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: OAuth2 Dynamic Client Registration & Management
  name: Groupe BPCE Registration API
  slug: groupe-bpce-registration-api
- baseURL: https://www.{etab}.oba-bad-me-live-api.banquepopulaire.fr/stet/psd2/v1.6.2
  baseurl_source: declared
  description: Creating and validating transfers.
  name: Groupe BPCE Transfers API
  slug: groupe-bpce-transfers-api
artifact_total: 37
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/capabilities/groupe-bpce-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/groupe-bpce-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/agentic-access/groupe-bpce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/groupe-bpce-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/rate-limits/groupe-bpce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/groupe-bpce-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/plans/groupe-bpce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/groupe-bpce-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/rules/groupe-bpce-rules.yml
  title: ''
  type: Spectral
  url: rules/groupe-bpce-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/rules/groupe-bpce-bpce-api-guidelines-rulesets-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/groupe-bpce-bpce-api-guidelines-rulesets-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/json-ld/groupe-bpce-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/groupe-bpce-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/vocabulary/groupe-bpce-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/groupe-bpce-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/data-model/groupe-bpce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/groupe-bpce-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/changelog/groupe-bpce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/groupe-bpce-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/conventions/groupe-bpce-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/groupe-bpce-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/conventions/groupe-bpce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/groupe-bpce-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/sandbox/groupe-bpce-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/groupe-bpce-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/security/groupe-bpce-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/groupe-bpce-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apistore.groupebpce.com/api/account-information-services-3
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/lifecycle/groupe-bpce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/groupe-bpce-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/errors/groupe-bpce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/groupe-bpce-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/conformance/groupe-bpce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/groupe-bpce-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/overlays/groupe-bpce-natixis-psd2-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/groupe-bpce-natixis-psd2-accounts-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/well-known/groupe-bpce-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/groupe-bpce-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/well-known/groupe-bpce-groupebpce-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/groupe-bpce-groupebpce-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/well-known/groupe-bpce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/groupe-bpce-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/hosts/groupe-bpce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/groupe-bpce-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/vendors/groupe-bpce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/groupe-bpce-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/scopes/groupe-bpce-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/groupe-bpce-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/authentication/groupe-bpce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/groupe-bpce-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/security/groupe-bpce-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/groupe-bpce-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/security/groupe-bpce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/groupe-bpce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://groupebpce.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/BPCE/bpce-api-guidelines-rulesets/blob/14005808ecd2f75f7c05c67f4625cb4e6542e65a/rulesets/oas-ruleset.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apistore.groupebpce.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apistore.groupebpce.com/apis
- group: docs
  title: ''
  type: Documentation
  url: https://apistore.groupebpce.com/developer-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://apistore.groupebpce.com/solution/psd2-regulatory-apis
- group: operate
  title: ''
  type: Support
  url: https://apistore.groupebpce.com/support-technique
- group: operate
  title: ''
  type: FAQ
  url: https://apistore.groupebpce.com/faq
- group: operate
  title: ''
  type: Contact
  url: https://apistore.groupebpce.com/support-commercial
- group: start
  title: ''
  type: Login
  url: https://apistore.groupebpce.com/user/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apistore.groupebpce.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apistore.groupebpce.com/protection-of-personal-data
- group: company
  title: ''
  type: Blog
  url: https://www.groupebpce.com/toute-l-actualite/
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.groupebpce.fr/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BPCE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bpce
created: '2026-10-09'
description: Groupe BPCE is the second-largest banking group in France, operating retail banking and insurance through its main brands Banque Populaire, Caisse d'Epargne and Natixis (per groupebpce.com). Through its Group BPCE API STORE (apistore.groupebpce.com) it publishes an API product catalog and developer center covering payment and collection services and PSD2 (DSP2) regulatory APIs for account information, payment initiation and funds confirmation for authorized payment service providers, with technical and sales support. It also publishes its API design guidelines and Spectral rulesets on GitHub (github.com/BPCE).
image: https://avatars.githubusercontent.com/u/105843508?v=4
json_schemas:
- name: Access
  property_count: 7
  slug: groupe-bpce-access
- name: ConfirmationResource
  property_count: 2
  slug: groupe-bpce-confirmation-resource
- name: Error
  property_count: 3
  slug: groupe-bpce-error
- name: ExternalAccount
  property_count: 0
  slug: groupe-bpce-external-account
- name: HalAccounts
  property_count: 2
  slug: groupe-bpce-hal-accounts
- name: HalAuthenticationRequest
  property_count: 3
  slug: groupe-bpce-hal-authentication-request
- name: HalBalances
  property_count: 2
  slug: groupe-bpce-hal-balances
- name: HalBeneficiaries
  property_count: 2
  slug: groupe-bpce-hal-beneficiaries
- name: HalCreditTransfertTransactions
  property_count: 2
  slug: groupe-bpce-hal-credit-transfert-transactions
- name: HalOwners
  property_count: 3
  slug: groupe-bpce-hal-owners
- name: HalPaymentCoverageReport
  property_count: 3
  slug: groupe-bpce-hal-payment-coverage-report
- name: HalPaymentRequest
  property_count: 2
  slug: groupe-bpce-hal-payment-request
- name: HalTransactions
  property_count: 2
  slug: groupe-bpce-hal-transactions
- name: InternalAccount
  property_count: 0
  slug: groupe-bpce-internal-account
- name: PaymentCoverageRequestResource
  property_count: 4
  slug: groupe-bpce-payment-coverage-request-resource
- name: RegistrationRecord
  property_count: 24
  slug: groupe-bpce-registration-record
- name: RegistrationRequest
  property_count: 19
  slug: groupe-bpce-registration-request
- name: TransferRequestLine
  property_count: 0
  slug: groupe-bpce-transfer-request-line
- name: TransferRequestLineSummary
  property_count: 11
  slug: groupe-bpce-transfer-request-line-summary
- name: TransferRequestSummary
  property_count: 8
  slug: groupe-bpce-transfer-request-summary
jsonld:
- class_count: 120
  name: Groupe Bpce Context
  property_count: 277
  slug: groupe-bpce-context
layout: provider
modified: '2026-10-09'
name: Groupe BPCE
nav: Providers
network: true
overview: 'Groupe BPCE publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including AISP API, CBPII API, External Accounts API, and 4 more. Tagged areas include Company, Banking, Financial Services, Open Banking, and PSD2.


  The Groupe BPCE catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Groupe BPCE''s developer surface includes changelog, sandbox, authentication, API reference, documentation, getting-started guide, support, and 38 more developer resources.'
plans:
- name: Groupe Bpce Plans Pricing
  plan_count: 1
  slug: groupe-bpce-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Groupe Bpce Rate Limits
  slug: groupe-bpce-rate-limits
rules:
- authorship: provider
  effective_rule_count: 43
  extends:
  - spectral:oas
  name: Groupe BPCE — bpce api guidelines rulesets rules
  rule_count: 2
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 1
  slug: groupe-bpce-bpce-api-guidelines-rulesets-spectral-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Groupe BPCE API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: groupe-bpce-rules
scopes:
- name: Groupe Bpce Scopes
  scope_count: 12
  slug: groupe-bpce-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 67.6
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
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
    score: 37.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/groupe-bpce/refs/heads/main/screenshots/groupe-bpce-2026-10-11T105034.png
security:
- kind: authentication
  name: Groupe Bpce Authentication
  slug: groupe-bpce-authentication
  summary_line: mutualTLS/oauth2 · 5 schemes
- kind: domain-security
  name: Groupe Bpce Domain Security
  slug: groupe-bpce-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Groupe Bpce Vulnerability Disclosure
  slug: groupe-bpce-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: groupe-bpce
tags:
- Company
- Banking
- Financial Services
- Open Banking
- PSD2
- Payments
- Insurance
- France
website: https://groupebpce.com/
---
