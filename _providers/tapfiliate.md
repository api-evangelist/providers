---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Tapfiliate Agentic Access
  operation_count: 77
  slug: tapfiliate-agentic-access
  summary_line: 77 operations · 41 acting
api_count: 1
apis:
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage affiliate groups
  name: Tapfiliate Affiliate Groups API
  phrasing_intents:
  - id: listAffiliateGroups
    intent: List affiliate groups
    question: Which affiliate groups have I set up in Tapfiliate?
  - id: createAffiliateGroup
    intent: Create an affiliate group
    question: How do I create a new group to organize my affiliates?
  - id: updateAffiliateGroup
    intent: Rename an affiliate group
    question: Can I rename an affiliate group that already exists?
  phrasing_ops: 3
  slug: tapfiliate-affiliate-groups-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage affiliate prospects (pending applicants)
  name: Tapfiliate Affiliate Prospects API
  phrasing_intents:
  - id: listAffiliateProspects
    intent: List affiliate prospects
    question: Who has applied to become an affiliate but isn't one yet?
  - id: createAffiliateProspect
    intent: Add an affiliate prospect
    question: How do I record someone as a prospective affiliate before they join?
  - id: getAffiliateProspect
    intent: Look up an affiliate prospect
    question: Can I see the details of one specific affiliate prospect?
  - id: deleteAffiliateProspect
    intent: Delete an affiliate prospect
    question: Can I remove a prospect application I don't want to pursue?
  phrasing_ops: 4
  slug: tapfiliate-affiliate-prospects-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage affiliates, their groups, notes, and payout methods
  name: Tapfiliate Affiliates API
  phrasing_intents:
  - id: getAffiliate
    intent: Retrieve an affiliate
    question: Can I pull up one affiliate's profile by their ID?
  - id: deleteAffiliate
    intent: Delete an affiliate
    question: How do I permanently delete an affiliate from my account?
  - id: listAffiliates
    intent: List affiliates
    question: Which affiliates belong to a particular affiliate group?
  - id: createAffiliate
    intent: Create an affiliate
    question: How do I sign up a new affiliate directly through the API?
  - id: setAffiliateGroup
    intent: Assign an affiliate to a group
    question: Can I move an affiliate into one of my affiliate groups?
  - id: removeAffiliateGroup
    intent: Remove an affiliate from their group
    question: Can I take an affiliate out of their group without deleting them?
  - id: updateAffiliateNote
    intent: Edit a note on an affiliate
    question: Can I edit the text of a note I already added to an affiliate?
  - id: deleteAffiliateNote
    intent: Delete a note on an affiliate
    question: Can I delete a note I left on an affiliate?
  phrasing_ops: 24
  slug: tapfiliate-affiliates-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: View affiliate balances
  name: Tapfiliate Balances API
  phrasing_intents:
  - id: listAllBalances
    intent: List all affiliate balances
    question: How much do I owe all my affiliates across every program?
  phrasing_ops: 1
  slug: tapfiliate-balances-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Track and manage clicks
  name: Tapfiliate Clicks API
  phrasing_intents:
  - id: listClicks
    intent: List affiliate clicks
    question: Which referral clicks came in during a given date range?
  - id: createClick
    intent: Record a referral click
    question: How do I track a click on an affiliate's referral link from my server?
  - id: getClick
    intent: Get details of a click
    question: What details are recorded for a single click?
  phrasing_ops: 3
  slug: tapfiliate-clicks-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage individual commissions
  name: Tapfiliate Commissions API
  phrasing_intents:
  - id: getCommission
    intent: Retrieve a commission
    question: Can I look up one commission by its ID?
  - id: updateCommission
    intent: Change a commission amount
    question: Can I adjust the amount of a commission after it was created?
  - id: listCommissions
    intent: List commissions
    question: Which commissions are still waiting for approval?
  - id: approveCommission
    intent: Approve a commission
    question: How do I approve a pending commission so it can be paid out?
  - id: disapproveCommission
    intent: Disapprove a commission
    question: Can I revoke approval on a commission I already approved?
  phrasing_ops: 5
  slug: tapfiliate-commissions-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Track and manage conversions and commissions
  name: Tapfiliate Conversions API
  phrasing_intents:
  - id: getConversion
    intent: Retrieve a conversion
    question: Can I look up one conversion by its ID?
  - id: updateConversion
    intent: Update a conversion
    question: Can I change the amount on a conversion after it was tracked?
  - id: deleteConversion
    intent: Delete a conversion
    question: How do I delete a conversion that was recorded by mistake?
  - id: listConversions
    intent: List conversions
    question: Which conversions happened between two dates?
  - id: createConversion
    intent: Record a conversion
    question: How do I track a sale and credit it to an affiliate?
  - id: addCommissionsToConversion
    intent: Add commissions to a conversion
    question: Can I add extra commission entries to a conversion that already exists?
  - id: getConversionMetaData
    intent: Get all metadata for a conversion
    question: What custom metadata is stored on a conversion?
  - id: replaceConversionMetaData
    intent: Replace a conversion's metadata
    question: Can I overwrite a conversion's whole metadata object in one go?
  phrasing_ops: 11
  slug: tapfiliate-conversions-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage customers and their metadata
  name: Tapfiliate Customers API
  phrasing_intents:
  - id: getCustomer
    intent: Retrieve a customer
    question: Can I look up one referred customer by their ID?
  - id: updateCustomer
    intent: Update a customer
    question: Can I change the external identifier on an existing customer?
  - id: deleteCustomer
    intent: Delete a customer
    question: How do I delete a customer record completely?
  - id: listCustomers
    intent: List customers
    question: Which customers have been referred by my affiliates?
  - id: createCustomer
    intent: Create a customer
    question: How do I register a referred customer, for example on a trial signup?
  - id: cancelCustomer
    intent: Cancel or reactivate a customer
    question: How do I mark a customer as cancelled when they churn?
  - id: getCustomerMetaData
    intent: Get all metadata for a customer
    question: What custom metadata is stored on a customer?
  - id: replaceCustomerMetaData
    intent: Replace a customer's metadata
    question: Can I overwrite a customer's whole metadata object in one call?
  phrasing_ops: 11
  slug: tapfiliate-customers-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage affiliate payments
  name: Tapfiliate Payments API
  phrasing_intents:
  - id: getPayment
    intent: Retrieve an affiliate payment
    question: Can I look up a single affiliate payment by its ID?
  - id: cancelPayment
    intent: Cancel a pending payment
    question: How do I cancel an affiliate payment that hasn't gone out yet?
  - id: listPayments
    intent: List affiliate payments
    question: Which affiliate payments were paid out during a given period?
  - id: createPayment
    intent: Create an affiliate payment batch
    question: How do I pay out several affiliates in one batch?
  phrasing_ops: 4
  slug: tapfiliate-payments-api
- baseURL: https://api.tapfiliate.com/1.6/
  baseurl_source: declared
  description: Manage affiliate programs and program affiliates
  name: Tapfiliate Programs API
  phrasing_intents:
  - id: getProgram
    intent: Retrieve an affiliate program
    question: Can I look up the settings of one affiliate program?
  - id: listPrograms
    intent: List affiliate programs
    question: Which affiliate programs do I run in Tapfiliate?
  - id: listProgramAffiliates
    intent: List affiliates in a program
    question: Who is enrolled in a particular affiliate program?
  - id: addAffiliatToProgram
    intent: Enroll an affiliate in a program
    question: How do I add an existing affiliate to another program?
  - id: getProgramAffiliate
    intent: Get an affiliate's program enrollment
    question: What are an affiliate's coupon and referral link in a given program?
  - id: updateProgramAffiliate
    intent: Update an affiliate's program enrollment
    question: Can I assign a coupon code to an affiliate within a program?
  - id: approveAffiliate
    intent: Approve an affiliate in a program
    question: How do I approve an affiliate who applied to my program?
  - id: disapproveAffiliate
    intent: Disapprove an affiliate in a program
    question: Can I reject or revoke an affiliate's place in a program?
  phrasing_ops: 11
  slug: tapfiliate-programs-api
- description: Official remote Model Context Protocol server for Tapfiliate, announced 2026-08-07. A read-only analytics surface over live account data — clicks, conversions, customers, revenue, commissions, payouts
  name: Tapfiliate MCP Server
  slug: tapfiliate-mcp-server
artifact_total: 40
asyncapis:
- description: ''
  name: Tapfiliate Webhooks
  slug: tapfiliate-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tapfiliate REST Affiliate Groups API
  slug: open-tapfiliate-affiliate-groups-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Affiliate Prospects API
  slug: open-tapfiliate-affiliate-prospects-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Affiliates API
  slug: open-tapfiliate-affiliates-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Balances API
  slug: open-tapfiliate-balances-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Clicks API
  slug: open-tapfiliate-clicks-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Commissions API
  slug: open-tapfiliate-commissions-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Conversions API
  slug: open-tapfiliate-conversions-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Customers API
  slug: open-tapfiliate-customers-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Payments API
  slug: open-tapfiliate-payments-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Programs API
  slug: open-tapfiliate-programs-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/capabilities/tapfiliate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tapfiliate-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/agentic-access/tapfiliate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tapfiliate-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/security/tapfiliate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tapfiliate-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/security/tapfiliate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tapfiliate-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/authentication/tapfiliate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tapfiliate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tapfiliate.com
- group: docs
  title: ''
  type: Documentation
  url: https://tapfiliate.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Tapfiliate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tapfiliate/
- group: company
  title: ''
  type: Blog
  url: https://tapfiliate.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tapfiliate.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tapfiliate.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/tapfiliate
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/plans/tapfiliate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tapfiliate-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/rate-limits/tapfiliate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tapfiliate-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/finops/tapfiliate-finops.yml
  title: ''
  type: FinOps
  url: finops/tapfiliate-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/vocabulary/tapfiliate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tapfiliate-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/json-ld/tapfiliate-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/tapfiliate-context.jsonld
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/packages/tapfiliate-packages.yml
  title: ''
  type: Packages
  url: packages/tapfiliate-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/packages/tapfiliate-packages.yml
  title: ''
  type: SDKs
  url: packages/tapfiliate-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/mcp/tapfiliate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tapfiliate-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/mcp/tapfiliate-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tapfiliate-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/scopes/tapfiliate-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tapfiliate-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/well-known/tapfiliate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tapfiliate-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/well-known/tapfiliate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tapfiliate-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/security/tapfiliate-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tapfiliate-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/conventions/tapfiliate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tapfiliate-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/errors/tapfiliate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tapfiliate-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/lifecycle/tapfiliate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tapfiliate-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/conformance/tapfiliate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tapfiliate-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/data-model/tapfiliate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tapfiliate-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/asyncapi/tapfiliate-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tapfiliate-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/sandbox/tapfiliate-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tapfiliate-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/llms/tapfiliate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tapfiliate-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tapfiliate.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://tapfiliate.com/docs/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://tapfiliate.com/docs/integrations/rest-api/
- group: operate
  title: ''
  type: Support
  url: https://support.tapfiliate.com/
- group: start
  title: ''
  type: SignUp
  url: https://tapfiliate.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tapfiliate.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tapfiliate.com/privacy/
created: 2026-06-13
description: Tapfiliate is an affiliate tracking and management platform with a REST API for creating affiliate programs, managing affiliates, tracking conversions, and handling commission payouts. The API is versioned at V1.6 and uses API key authentication via the X-Api-Key header.
examples:
- key_count: 4
  name: Tapfiliate Create Affiliate Example
  slug: tapfiliate-create-affiliate-example
- key_count: 4
  name: Tapfiliate Create Conversion Example
  slug: tapfiliate-create-conversion-example
finops:
- name: Tapfiliate Finops
  service_category: ''
  slug: tapfiliate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tapfiliate.png
json_schemas:
- name: Affiliate
  property_count: 10
  slug: tapfiliate-affiliate
- name: Commission
  property_count: 7
  slug: tapfiliate-commission
- name: Conversion
  property_count: 8
  slug: tapfiliate-conversion
- name: Customer
  property_count: 6
  slug: tapfiliate-customer
jsonld:
- class_count: 54
  name: Tapfiliate Context
  property_count: 0
  slug: tapfiliate-context
layout: provider
mcp_servers:
- description: Tapfiliate operates an official REMOTE MCP server at https://mcp.tapfiliate.com/mcp. It is an OAuth 2.0 protected resource (RFC 9728) — an anonymous tools/list returns HTTP 401 with a WWW-Authenticate
  name: Tapfiliate MCP Server
  slug: tapfiliate
modified: 2026-08-13
name: Tapfiliate
nav: Providers
network: true
overview: 'Tapfiliate publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Affiliate Groups API, Affiliate Prospects API, Affiliates API, and 8 more. Tagged areas include Affiliate Marketing, Affiliate Tracking, Commission Management, Conversion Tracking, and Partner Programs.


  The Tapfiliate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Tapfiliate''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, API reference, getting-started guide, and 35 more developer resources.'
plans:
- name: Tapfiliate Plans Pricing
  plan_count: 3
  slug: tapfiliate-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Tapfiliate Rate Limits
  slug: tapfiliate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tapfiliate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tapfiliate-jsonschema-spectral-rules
scopes:
- name: Tapfiliate Scopes
  scope_count: 4
  slug: tapfiliate-scopes
  summary_line: 4 scopes
score:
  band: exemplar
  composite: 69.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 28.0
    contract_quality: 66.4
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 39.5
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/screenshots/tapfiliate-2026-06-20T194920.png
security:
- kind: authentication
  name: Tapfiliate Authentication
  slug: tapfiliate-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tapfiliate Domain Security
  slug: tapfiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tapfiliate Vulnerability Disclosure
  slug: tapfiliate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tapfiliate
tags:
- Affiliate Marketing
- Affiliate Tracking
- Commission Management
- Conversion Tracking
- Partner Programs
- Referral Programs
- Influencer Marketing
website: https://tapfiliate.com
---
