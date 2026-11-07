---
access_model:
  confidence: high
  label: Enterprise - public contracts, gated credentials
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://tech.sofi.com/lp/request-access/
  - plans/sofi-technologies-plans-pricing.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 169
  human_in_the_loop: 8
  name: Sofi Technologies Agentic Access
  operation_count: 258
  slug: sofi-technologies-agentic-access
  summary_line: 258 operations · 169 acting · 8 human-in-the-loop
api_count: 11
apis:
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Account Events Webhook API from SoFi Technologies — 1 operation(s) for account events webhook.
  name: SoFi Technologies Account Events Webhook API
  slug: sofi-technologies-account-events-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Account-Level Controls API from SoFi Technologies — 9 operation(s) for account-level controls.
  name: SoFi Technologies Account-Level Controls API
  slug: sofi-technologies-account-level-controls-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Accounts and Cards API from SoFi Technologies — 47 operation(s) for accounts and cards.
  name: SoFi Technologies Accounts and Cards API
  slug: sofi-technologies-accounts-and-cards-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The ACH Debit Webhook API from SoFi Technologies — 1 operation(s) for ach debit webhook.
  name: SoFi Technologies ACH Debit Webhook API
  slug: sofi-technologies-ach-debit-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Alerts API from SoFi Technologies — 7 operation(s) for alerts.
  name: SoFi Technologies Alerts API
  slug: sofi-technologies-alerts-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Attachments API from SoFi Technologies — 1 operation(s) for attachments.
  name: SoFi Technologies Attachments API
  slug: sofi-technologies-attachments-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Auth API Webhook API from SoFi Technologies — 2 operation(s) for auth api webhook.
  name: SoFi Technologies Auth API Webhook API
  slug: sofi-technologies-auth-api-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Authorization Events Webhook API from SoFi Technologies — 1 operation(s) for authorization events webhook.
  name: SoFi Technologies Authorization Events Webhook API
  slug: sofi-technologies-authorization-events-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Billpay Webhook API from SoFi Technologies — 1 operation(s) for billpay webhook.
  name: SoFi Technologies Billpay Webhook API
  slug: sofi-technologies-billpay-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Claim API from SoFi Technologies — 4 operation(s) for claim.
  name: SoFi Technologies Claim API
  slug: sofi-technologies-claim-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Configuration API from SoFi Technologies — 1 operation(s) for configuration.
  name: SoFi Technologies Configuration API
  slug: sofi-technologies-configuration-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Corporate Credit and RTF API from SoFi Technologies — 8 operation(s) for corporate credit and rtf.
  name: SoFi Technologies Corporate Credit and RTF API
  slug: sofi-technologies-corporate-credit-and-rtf-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Corporate Hierarchy API from SoFi Technologies — 9 operation(s) for corporate hierarchy.
  name: SoFi Technologies Corporate Hierarchy API
  slug: sofi-technologies-corporate-hierarchy-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Credit API from SoFi Technologies — 8 operation(s) for credit.
  name: SoFi Technologies Credit API
  slug: sofi-technologies-credit-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Dispute Management API from SoFi Technologies — 7 operation(s) for dispute management.
  name: SoFi Technologies Dispute Management API
  slug: sofi-technologies-dispute-management-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Disputed Transactions API from SoFi Technologies — 1 operation(s) for disputed transactions.
  name: SoFi Technologies Disputed Transactions API
  slug: sofi-technologies-disputed-transactions-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Documents API from SoFi Technologies — 2 operation(s) for documents.
  name: SoFi Technologies Documents API
  slug: sofi-technologies-documents-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The External Account Links API from SoFi Technologies — 7 operation(s) for external account links.
  name: SoFi Technologies External Account Links API
  slug: sofi-technologies-external-account-links-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Federal Benefit Enrollment API from SoFi Technologies — 4 operation(s) for federal benefit enrollment.
  name: SoFi Technologies Federal Benefit Enrollment API
  slug: sofi-technologies-federal-benefit-enrollment-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Instant Issue API from SoFi Technologies — 7 operation(s) for instant issue.
  name: SoFi Technologies Instant Issue API
  slug: sofi-technologies-instant-issue-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Intake API from SoFi Technologies — 17 operation(s) for intake.
  name: SoFi Technologies Intake API
  slug: sofi-technologies-intake-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Intake Flow API from SoFi Technologies — 15 operation(s) for intake flow.
  name: SoFi Technologies Intake Flow API
  slug: sofi-technologies-intake-flow-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The IVR API from SoFi Technologies — 3 operation(s) for ivr.
  name: SoFi Technologies IVR API
  slug: sofi-technologies-ivr-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The IVS API from SoFi Technologies — 6 operation(s) for ivs.
  name: SoFi Technologies IVS API
  slug: sofi-technologies-ivs-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: Loan management endpoints.
  name: SoFi Technologies Loan API
  slug: sofi-technologies-loan-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Location Management API from SoFi Technologies — 5 operation(s) for location management.
  name: SoFi Technologies Location Management API
  slug: sofi-technologies-location-management-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Miscellaneous API from SoFi Technologies — 5 operation(s) for miscellaneous.
  name: SoFi Technologies Miscellaneous API
  slug: sofi-technologies-miscellaneous-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Overdraft API from SoFi Technologies — 3 operation(s) for overdraft.
  name: SoFi Technologies Overdraft API
  slug: sofi-technologies-overdraft-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Risk API from SoFi Technologies — 3 operation(s) for risk.
  name: SoFi Technologies Risk API
  slug: sofi-technologies-risk-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Settlement Events Webhook API from SoFi Technologies — 1 operation(s) for settlement events webhook.
  name: SoFi Technologies Settlement Events Webhook API
  slug: sofi-technologies-settlement-events-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Status API from SoFi Technologies — 1 operation(s) for status.
  name: SoFi Technologies Status API
  slug: sofi-technologies-status-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Tasks API from SoFi Technologies — 4 operation(s) for tasks.
  name: SoFi Technologies Tasks API
  slug: sofi-technologies-tasks-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Transaction Events Webhook API from SoFi Technologies — 1 operation(s) for transaction events webhook.
  name: SoFi Technologies Transaction Events Webhook API
  slug: sofi-technologies-transaction-events-webhook-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Transaction Simulation API from SoFi Technologies — 6 operation(s) for transaction simulation.
  name: SoFi Technologies Transaction Simulation API
  slug: sofi-technologies-transaction-simulation-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Transactions API from SoFi Technologies — 46 operation(s) for transactions.
  name: SoFi Technologies Transactions API
  slug: sofi-technologies-transactions-api
- baseURL: https://api-{corename}.{env}.gpsrv.com/intserv/4.0/
  baseurl_source: declared
  description: The Transfers API from SoFi Technologies — 4 operation(s) for transfers.
  name: SoFi Technologies Transfers API
  slug: sofi-technologies-transfers-api
artifact_total: 49
asyncapis:
- description: ''
  name: Sofi Technologies Webhooks
  slug: sofi-technologies-webhooks
common:
- group: design
  href: https://artifacts.apis.io/sofi-technologies/rules/sofi-technologies-rules.yml
  title: ''
  type: Spectral
  url: rules/sofi-technologies-rules.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/vocabulary/sofi-technologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sofi-technologies-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/sofi-technologies/hosts/sofi-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sofi-technologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/sofi-technologies/vendors/sofi-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sofi-technologies-vendors.yml
- group: other
  href: https://artifacts.apis.io/sofi-technologies/capabilities/sofi-technologies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sofi-technologies-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/skills/sofi-technologies-open-card-account.md
  title: ''
  type: AgentSkill
  url: skills/sofi-technologies-open-card-account.md
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/skills/sofi-technologies-ach-money-movement.md
  title: ''
  type: AgentSkill
  url: skills/sofi-technologies-ach-money-movement.md
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/skills/sofi-technologies-file-dispute-claim.md
  title: ''
  type: AgentSkill
  url: skills/sofi-technologies-file-dispute-claim.md
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/agentic-access/sofi-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sofi-technologies-agentic-access.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sofi.com/sofi-plus/
- group: operate
  title: ''
  type: StatusPage
  url: https://sofi.statuspage.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/SoFi
- group: design
  href: https://artifacts.apis.io/sofi-technologies/asyncapi/sofi-technologies-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sofi-technologies-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/mcp/sofi-technologies-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sofi-technologies-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/llms/sofi-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sofi-technologies-llms.txt
- group: agent
  href: https://artifacts.apis.io/sofi-technologies/well-known/sofi-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sofi-technologies-well-known.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/conventions/sofi-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sofi-technologies-conventions.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/conventions/sofi-technologies-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sofi-technologies-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sofi-technologies/authentication/sofi-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sofi-technologies-authentication.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/errors/sofi-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sofi-technologies-problem-types.yml
- group: build
  href: https://artifacts.apis.io/sofi-technologies/errors/sofi-technologies-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/sofi-technologies-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/lifecycle/sofi-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sofi-technologies-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sofi-technologies/lifecycle/sofi-technologies-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sofi-technologies-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sofi-technologies/changelog/sofi-technologies-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sofi-technologies-changelog.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/conformance/sofi-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sofi-technologies-conformance.yml
- group: design
  href: https://artifacts.apis.io/sofi-technologies/data-model/sofi-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sofi-technologies-data-model.yml
- group: start
  href: https://artifacts.apis.io/sofi-technologies/sandbox/sofi-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sofi-technologies-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/sofi-technologies/plans/sofi-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sofi-technologies-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sofi-technologies/rate-limits/sofi-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sofi-technologies-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sofi-technologies/finops/sofi-technologies-finops.yml
  title: ''
  type: FinOps
  url: finops/sofi-technologies-finops.yml
- group: auth
  href: https://artifacts.apis.io/sofi-technologies/security/sofi-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sofi-technologies-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sofi-technologies/security/sofi-technologies-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sofi-technologies-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/sofi-1
- group: other
  href: https://artifacts.apis.io/sofi-technologies/overlays/sofi-technologies-program-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sofi-technologies-program-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.sofi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tech.sofi.com/pro/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tech.sofi.com/pro/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tech.sofi.com/pro/reference/program-api-intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tech.sofi.com/pro/docs/quickstart
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/galileo-ft/workspace
- group: start
  title: ''
  type: SignUp
  url: https://tech.sofi.com/lp/request-access/
- group: operate
  title: ''
  type: Support
  url: https://tech.sofi.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://tech.sofi.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://tech.sofi.com/news/
- group: company
  title: ''
  type: About
  url: https://tech.sofi.com/about/
- group: company
  title: ''
  type: Careers
  url: https://tech.sofi.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sofi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sofi.com/privacy-policies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sofi-technologies
created: '2026-04-19'
description: 'SoFi Technologies, Inc. (NASDAQ: SOFI) is a US member-centric digital financial services company and federally chartered bank holding company. Alongside its consumer banking, lending and investing business it operates SoFi Tech Solutions - the B2B financial technology platform formed from its acquisitions of Galileo Financial Technologies and Technisys, and rebranded under the SoFi name in 2026. SoFi Tech Solutions is the API business: a card issuer-processor and banking-as-a-service platform whose public developer hub at docs.tech.sofi.com publishes eleven OpenAPI definitions covering 258 operations - the 167-operation Program API for accounts, cards, authorizations, ACH and bill pay, plus Payment Hub, Dispute, Loan, Risk and Public Config APIs and three client-hosted webhook contracts. The platform declares ISO 20022, ISO 8583, Nacha ACH, EMV and 3-D Secure in its own contracts, and discovery runs through a real RFC 9727 api-catalog linkset.'
finops:
- has_sources: true
  method: derived
  name: Sofi Technologies Finops
  primary_unit: ''
  service_category: ''
  slug: sofi-technologies-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sofi-technologies.png
layout: provider
mcp_servers:
- description: A remote Model Context Protocol endpoint is live on the SoFi Tech Solutions developer hub at https://docs.tech.sofi.com/mcp. It answers a JSON-RPC POST with a well-formed MCP error envelope ({"jsonrpc
  name: SoFi Tech Solutions Documentation MCP
  slug: sofi-tech-solutions-documentation-mcp
modified: '2026-09-06'
name: SoFi Technologies
nav: Providers
network: true
overview: 'SoFi Technologies publishes 36 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Events Webhook API, Account-Level Controls API, Accounts and Cards API, and 33 more. Tagged areas include Fintech, Payments, Banking, Card Issuing, and Banking as a Service.


  The SoFi Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SoFi Technologies'' developer surface includes pricing, authentication, changelog, sandbox, documentation, API reference, getting-started guide, and 43 more developer resources.'
plans:
- name: Sofi Technologies Plans Pricing
  plan_count: 0
  slug: sofi-technologies-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Sofi Technologies Rate Limits
  slug: sofi-technologies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: SoFi Technologies API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: sofi-technologies-rules
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.0
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 54.4
    developer_ergonomics: 61.3
    discoverability: 80.8
    operational_transparency: 89.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 90.6
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/sofi-technologies/sofi-technologies-2026-06-20T194126.png
security:
- kind: authentication
  name: Sofi Technologies Authentication
  slug: sofi-technologies-authentication
  summary_line: body-parameter/http-bearer/apiKey · 3 schemes
- kind: domain-security
  name: Sofi Technologies Domain Security
  slug: sofi-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sofi Technologies Vulnerability Disclosure
  slug: sofi-technologies-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 3
skills:
- name: sofi-technologies-ach-money-movement
  slug: sofi-technologies-ach-money-movement
- name: sofi-technologies-file-dispute-claim
  slug: sofi-technologies-file-dispute-claim
- name: sofi-technologies-open-card-account
  slug: sofi-technologies-open-card-account
slug: sofi-technologies
tags:
- Fintech
- Payments
- Banking
- Card Issuing
- Banking as a Service
- Personal Finance
- Lending
- ACH
- ISO 20022
- Disputes
- Identity Verification
- Webhook
- Consumer Banking
website: https://www.sofi.com
---
