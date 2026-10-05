---
access_model:
  confidence: high
  label: Paid (free tier) · Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://ibanforge.com/pricing
  - https://api.ibanforge.com/v1/demo
  - https://api.ibanforge.com/mcp
  - https://api.ibanforge.com/v1/credits/bundles
  - https://api.ibanforge.com/.well-known/rate-limits.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Ibanforge Agentic Access
  operation_count: 39
  slug: ibanforge-agentic-access
  summary_line: 39 operations · 20 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: API key management — generate free keys and check usage
  name: IBANforge API Keys API
  phrasing_intents:
  - id: generateApiKey
    intent: Generate a free API key
    question: Can I get an API key with no email and no card?
  - id: openDeviceGrant
    intent: Start a device authorization request for a key
    question: How can an agent get an API key approved by a human without handling their email?
  - id: collectDeviceGrantKey
    intent: Collect the key after device approval
    question: How often should an agent poll for the key after asking a human to approve it?
  - id: lookupDeviceGrant
    intent: Look up a pending device request by its code
    question: What does a pending device request show before I approve it?
  - id: approveDeviceGrant
    intent: Approve a device request and issue the key
    question: Can I approve an agent's key request and raise it to 200 requests a month by verifying my mailbox?
  - id: denyDeviceGrant
    intent: Refuse a device key request
    question: What should I do with a device approval request that is not mine?
  - id: getApiKeyUsage
    intent: Check this month's usage of an API key
    question: How many requests do I have left on my API key this month?
  - id: getApiKeyReport
    intent: Read the activity report of the presented key
    question: Which endpoints has my API key called, and what failed?
  phrasing_ops: 13
  slug: ibanforge-api-keys-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: BIC/SWIFT lookup endpoints (paid via x402)
  name: IBANforge BIC API
  phrasing_intents:
  - id: lookupBIC
    intent: Look up a bank by BIC/SWIFT code
    question: Which bank does a given SWIFT code belong to?
  phrasing_ops: 1
  slug: ibanforge-bic-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Compliance check endpoint — IBAN validation + sanctions + SEPA + VoP + risk score (paid via x402)
  name: IBANforge Compliance API
  phrasing_intents:
  - id: complianceCheck
    intent: Run a pre-payment compliance check on an IBAN
    question: Is the bank behind this IBAN on an OFAC, EU or UN sanctions list?
  phrasing_ops: 1
  slug: ibanforge-compliance-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Prepaid credit bundles — pay once in USDC (x402), get an API key with N credits; batch validation debits 1 credit per IBAN
  name: IBANforge Credits API
  phrasing_intents:
  - id: getCreditBalance
    intent: Check the prepaid credit balance of a key
    question: How many prepaid credits are left on my key?
  - id: listCreditBundles
    intent: List prepaid credit bundles and prices
    question: What prepaid credit bundles are available and what do they cost?
  - id: buyCreditBundle
    intent: Buy a prepaid credit bundle with USDC
    question: Can I pay with USDC on Base to add credits to the key I already have?
  phrasing_ops: 3
  slug: ibanforge-credits-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Free endpoints — no payment required
  name: IBANforge Free API
  phrasing_intents:
  - id: formatCheckIBAN
    intent: Check an IBAN's format and checksum for free
    question: Is there a free way to check an IBAN's mod-97 checksum and length?
  - id: checkSwissQrBill
    intent: Check a Swiss QR-bill payload
    question: Does my Swiss QR-bill still use a combined (type K) address?
  - id: checkPostalAddress
    intent: Check a postal address against ISO 20022 rules
    question: Is my structured postal address ready for the November 2026 ISO 20022 deadline?
  - id: validatePaymentReference
    intent: Validate a structured payment reference
    question: Is this RF creditor reference checksum correct?
  - id: validatePaymentReferencePost
    intent: Validate a payment reference sent as JSON
    question: Can I send a payment reference in a JSON body instead of the query string?
  - id: listIBANStructures
    intent: List all supported IBAN countries
    question: Which countries use IBANs, and how long is each one?
  - id: getIBANStructure
    intent: Get the IBAN format template for a country
    question: Where does the bank code sit inside a country's IBAN?
  - id: submitFeedback
    intent: Report wrong data or claim an x402 refund
    question: How do I report a wrong or stale BIC answer?
  phrasing_ops: 12
  slug: ibanforge-free-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: IBAN validation endpoints (paid via x402)
  name: IBANforge IBAN API
  phrasing_intents:
  - id: validateIBAN
    intent: Validate a single IBAN
    question: Is this IBAN valid, and which bank and BIC does it map to?
  - id: batchValidateIBAN
    intent: Validate up to 100 IBANs at once
    question: Can I validate a whole list of IBANs in one request?
  phrasing_ops: 2
  slug: ibanforge-iban-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Model Context Protocol endpoint for AI agents (Streamable HTTP)
  name: IBANforge MCP API
  phrasing_intents:
  - id: mcpStreamableHttp
    intent: Call IBANforge tools over MCP
    question: Can an AI agent validate IBANs through an MCP server?
  phrasing_ops: 1
  slug: ibanforge-mcp-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Swiss BC-Nummer / IID clearing lookup (paid via x402)
  name: IBANforge Swiss Clearing API
  phrasing_intents:
  - id: lookupChClearing
    intent: Look up a Swiss bank by clearing number
    question: Which Swiss bank has a given BC-Nummer?
  phrasing_ops: 1
  slug: ibanforge-swiss-clearing-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: 'The account page, https://ibanforge.com/account, for a person in a browser: a 6-digit code mailed to the address of the keys, then a read-only session cookie that shows every key of that address. Rota'
  name: IBANforge Account API
  phrasing_intents:
  - id: requestAccountSignInCode
    intent: Email a sign-in code for the account page
    question: How do I sign in to the IBANforge account page without a password?
  - id: openAccountSession
    intent: Exchange a sign-in code for an account session
    question: What happens after I enter the 6-digit code I received by email?
  - id: getAccountOverview
    intent: List every active key of the signed-in address
    question: Which API keys are attached to the email I signed in with?
  - id: getAccountKeyReport
    intent: Read the activity report of one account key
    question: Can I see the traffic and errors of one of my keys from the account page, by its prefix?
  - id: closeAccountSession
    intent: Sign out of the account page
    question: How do I log out of the IBANforge account page?
  phrasing_ops: 5
  slug: ibanforge-account-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ibanforge API Keys API
  slug: open-ibanforge-api-keys-api
- collection_type: open
  name: Ibanforge BIC API
  slug: open-ibanforge-bic-api
- collection_type: open
  name: Ibanforge Compliance API
  slug: open-ibanforge-compliance-api
- collection_type: open
  name: Ibanforge Credits API
  slug: open-ibanforge-credits-api
- collection_type: open
  name: Ibanforge Free API
  slug: open-ibanforge-free-api
- collection_type: open
  name: Ibanforge IBAN API
  slug: open-ibanforge-iban-api
- collection_type: open
  name: Ibanforge MCP API
  slug: open-ibanforge-mcp-api
- collection_type: open
  name: Ibanforge Swiss Clearing API
  slug: open-ibanforge-swiss-clearing-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/overlays/ibanforge-account-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ibanforge-account-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/well-known/ibanforge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ibanforge-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/well-known/ibanforge-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ibanforge-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/well-known/ibanforge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ibanforge-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/agentic-access/ibanforge-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ibanforge-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/rate-limits/ibanforge-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ibanforge-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/plans/ibanforge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ibanforge-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/rules/ibanforge-rules.yml
  title: ''
  type: Spectral
  url: rules/ibanforge-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/json-ld/ibanforge-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ibanforge-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/vocabulary/ibanforge-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ibanforge-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/data-model/ibanforge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ibanforge-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/changelog/ibanforge-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ibanforge-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/conventions/ibanforge-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ibanforge-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/conventions/ibanforge-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ibanforge-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/sandbox/ibanforge-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ibanforge-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/security/ibanforge-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ibanforge-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/cammac-creator/ibanforge/blob/main/CHANGELOG.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/lifecycle/ibanforge-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ibanforge-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/errors/ibanforge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ibanforge-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/conformance/ibanforge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ibanforge-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/llms/ibanforge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ibanforge-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/mcp/ibanforge-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ibanforge-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/hosts/ibanforge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ibanforge-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/vendors/ibanforge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ibanforge-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/packages/ibanforge-packages.yml
  title: ''
  type: Packages
  url: packages/ibanforge-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://ibanforge.com/playground
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@ibanforge/sdk
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/authentication/ibanforge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ibanforge-authentication.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/capabilities/ibanforge-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ibanforge-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/security/ibanforge-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibanforge-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/security/ibanforge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ibanforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ibanforge.com
- group: docs
  title: ''
  type: Documentation
  url: https://ibanforge.com/docs
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/mcp/ibanforge-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ibanforge-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/a2a/ibanforge-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ibanforge-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/well-known/ibanforge-well-known.yml
  title: ''
  type: APICatalog
  url: well-known/ibanforge-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/llms/ibanforge-llms.txt
  title: ''
  type: LlmsText
  url: llms/ibanforge-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://api.ibanforge.com/.well-known/security.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://ibanforge.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ibanforge.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ibanforge.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ibanforge.com/pricing
- group: other
  title: ''
  type: x402
  url: https://api.ibanforge.com/.well-known/x402
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://ibanforge.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@ibanforge.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://ibanforge.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cammac-creator/ibanforge
- group: build
  title: ''
  type: Postman
  url: https://ibanforge.com/ibanforge-postman.json
- group: docs
  title: ''
  type: APIReference
  url: https://ibanforge.com/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://ibanforge.com/docs/onboarding
- group: start
  title: ''
  type: Login
  url: https://ibanforge.com/account
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://ibanforge.com/legal/sla
created: '2026-05-28'
description: Pre-payout IBAN screening for developers and AI agents — validation, issuing-bank identification against national bank registers, Swiss clearing including QR-IID, bank-level sanctions, SEPA and VoP reachability, and risk scoring across 89 IBAN countries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibanforge.png
json_schemas:
- name: AccountOverview
  property_count: 7
  slug: ibanforge-account-overview
- name: BicComplianceResponse
  property_count: 10
  slug: ibanforge-bic-compliance-response
- name: BICLookupResult
  property_count: 26
  slug: ibanforge-biclookup-result
- name: ChClearingResult
  property_count: 14
  slug: ibanforge-ch-clearing-result
- name: ComplianceResult
  property_count: 6
  slug: ibanforge-compliance-result
- name: HealthResponse
  property_count: 8
  slug: ibanforge-health-response
- name: IBANFormatResult
  property_count: 9
  slug: ibanforge-ibanformat-result
- name: IBANValidationResult
  property_count: 26
  slug: ibanforge-ibanvalidation-result
- name: PaymentReferenceResult
  property_count: 10
  slug: ibanforge-payment-reference-result
- name: StatsOverview
  property_count: 7
  slug: ibanforge-stats-overview
jsonld:
- class_count: 13
  name: Ibanforge Context
  property_count: 104
  slug: ibanforge-context
layout: provider
mcp_servers:
- description: 'IBANforge operates an official remote MCP server over Streamable HTTP at https://api.ibanforge.com/mcp, plus a stdio server published to npm as `ibanforge-mcp`. The server card states: "No key at all:'
  name: IBANforge MCP Server
  slug: ibanforge
modified: '2026-09-25'
name: IBANforge
nav: Providers
network: true
overview: 'IBANforge publishes 9 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, BIC API, Compliance API, and 6 more. Tagged areas include Finance, Banking, Compliance, MCP, and A2A.


  The IBANforge catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  IBANforge''s developer surface includes changelog, sandbox, authentication, documentation, pricing, engineering blog, support, and 47 more developer resources.'
plans:
- name: Ibanforge Plans Pricing
  plan_count: 6
  slug: ibanforge-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Ibanforge Rate Limits
  slug: ibanforge-rate-limits
rules:
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: IBANforge API Rules
  rule_count: 3
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 0
  slug: ibanforge-provider-spectral
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: IBANforge API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: ibanforge-rules
score:
  band: exemplar
  composite: 74.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 98.5
    catalog_earned_first_party: 24.0
    catalog_gap: 16.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 41.3
  facets:
    access_clarity: 76.3
    contract_governance: 71.1
    contract_quality: 64.8
    developer_ergonomics: 68.5
    discoverability: 91.7
    operational_transparency: 86.8
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/screenshots/ibanforge-2026-06-20T183111.png
security:
- kind: authentication
  name: Ibanforge Authentication
  slug: ibanforge-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Ibanforge Domain Security
  slug: ibanforge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ibanforge Vulnerability Disclosure
  slug: ibanforge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ibanforge
tags:
- Finance
- Banking
- Compliance
- MCP
- A2A
website: https://ibanforge.com
---
