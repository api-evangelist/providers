---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Jithox Com Agentic Access
  operation_count: 5
  slug: jithox-com-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://jithox.com
  baseurl_source: declared
  description: The Iban API from jithox-com — 1 operation(s) for iban.
  name: jithox-com Iban API
  slug: jithox-com-iban-api
- baseURL: https://jithox.com
  baseurl_source: declared
  description: The Invoice API from jithox-com — 1 operation(s) for invoice.
  name: jithox-com Invoice API
  slug: jithox-com-invoice-api
- baseURL: https://jithox.com
  baseurl_source: declared
  description: The Payment API from jithox-com — 1 operation(s) for payment.
  name: jithox-com Payment API
  slug: jithox-com-payment-api
- baseURL: https://jithox.com
  baseurl_source: declared
  description: The Peppol API from jithox-com — 1 operation(s) for peppol.
  name: jithox-com Peppol API
  slug: jithox-com-peppol-api
- baseURL: https://jithox.com
  baseurl_source: declared
  description: The Vat API from jithox-com — 1 operation(s) for vat.
  name: jithox-com Vat API
  slug: jithox-com-vat-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/jithox-com/agentic-access/jithox-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jithox-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/jithox-com/plans/jithox-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jithox-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jithox-com/rules/jithox-com-rules.yml
  title: ''
  type: Spectral
  url: rules/jithox-com-rules.yml
- group: design
  href: https://artifacts.apis.io/jithox-com/json-ld/jithox-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jithox-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/jithox-com/vocabulary/jithox-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jithox-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jithox-com/data-model/jithox-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jithox-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/jithox-com/cli/jithox-com-cli.yml
  title: ''
  type: CLI
  url: cli/jithox-com-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://jithox.com/trust
- group: auth
  title: ''
  type: Security
  url: https://jithox.com/trust
- group: auth
  href: https://artifacts.apis.io/jithox-com/authentication/jithox-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jithox-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/jithox-com/errors/jithox-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jithox-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jithox-com/conformance/jithox-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jithox-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jithox-com/llms/jithox-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jithox-com-llms.txt
- group: other
  href: https://artifacts.apis.io/jithox-com/a2a/jithox-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/jithox-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/jithox-com/well-known/jithox-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jithox-com-security.txt
- group: auth
  href: https://artifacts.apis.io/jithox-com/well-known/jithox-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jithox-com-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/jithox-com/well-known/jithox-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jithox-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/jithox-com/well-known/jithox-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jithox-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/jithox-com/hosts/jithox-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jithox-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/jithox-com/vendors/jithox-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jithox-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://jithox.com/status
- group: start
  title: ''
  type: SignUp
  url: https://jithox.com/sign-up?return=mcp-account
- group: start
  title: ''
  type: Sandbox
  url: https://jithox.com/mcp/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://jithox.com/api/changelog/v1
- group: company
  title: ''
  type: Blog
  url: https://jithox.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://jithox.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/jithox-com/security/jithox-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jithox-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/jithox-com/security/jithox-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jithox-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jithox-com/security/jithox-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jithox-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jithox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jithox.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://jithox.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://jithox.com/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://jithox.com/mcp/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jithox.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jithox.com/privacy
created: '2026-10-29'
description: Jithox provides practical AI-powered products and tools aimed at automating back‑office tasks, offering both free and paid services. Their platform includes a catalog of AI tasks such as bank‑detail change checks and invoice reviews, with clear pricing and a developer portal for integration. The company emphasizes transparency with accessible documentation, trust resources, and a focus on practical AI applications for businesses.
image: https://jithox.com/opengraph-image.png
json_schemas:
- name: InvoiceReviewResponse
  property_count: 5
  slug: jithox-com-invoice-review-response
- name: LookupPeppolParticipantRequest
  property_count: 2
  slug: jithox-com-lookup-peppol-participant-request
- name: PreflightPaymentRequest
  property_count: 8
  slug: jithox-com-preflight-payment-request
- name: VerifyIbanRequest
  property_count: 2
  slug: jithox-com-verify-iban-request
- name: VerifyRequest
  property_count: 2
  slug: jithox-com-verify-request
- name: VerifyResponse
  property_count: 7
  slug: jithox-com-verify-response
jsonld:
- class_count: 37
  name: Jithox Com Context
  property_count: 138
  slug: jithox-com-context
layout: provider
modified: '2026-10-29'
name: jithox-com
nav: Providers
network: true
overview: 'jithox-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Iban API, Invoice API, Payment API, and 2 more. Tagged areas include Company, AI, Automation, BackOffice, and Tools.


  The jithox-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  jithox-com''s developer surface includes CLI, authentication, signup flow, sandbox, changelog, engineering blog, API reference, and 29 more developer resources.'
plans:
- name: Jithox Com Plans Pricing
  plan_count: 5
  slug: jithox-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: jithox-com API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 1
  slug: jithox-com-rules
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 69.0
    developer_ergonomics: 66.7
    discoverability: 66.1
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jithox Com Authentication
  slug: jithox-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jithox Com Domain Security
  slug: jithox-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jithox Com Vulnerability Disclosure
  slug: jithox-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jithox Com Trust Center
  slug: jithox-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: jithox-com
tags:
- Company
- AI
- Automation
- BackOffice
- Tools
website: https://jithox.com/
---
