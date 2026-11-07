---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Didlogic Com Agentic Access
  operation_count: 53
  slug: didlogic-com-agentic-access
  summary_line: 53 operations · 21 acting
api_count: 1
apis:
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Account Balance API from DID Logic — 1 operation(s) for account balance.
  name: DID Logic Account Balance API
  slug: didlogic-com-account-balance-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The API Access API from DID Logic — 1 operation(s) for api access.
  name: DID Logic API Access API
  slug: didlogic-com-api-access-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Calls API from DID Logic — 4 operation(s) for calls.
  name: DID Logic Calls API
  slug: didlogic-com-calls-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Click2Call API from DID Logic — 3 operation(s) for click2call.
  name: DID Logic Click2 Call API
  slug: didlogic-com-click2call-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The HLR Lookups API from DID Logic — 2 operation(s) for hlr lookups.
  name: DID Logic HLR Lookups API
  slug: didlogic-com-hlr-lookups-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Identities API from DID Logic — 2 operation(s) for identities.
  name: DID Logic Identities API
  slug: didlogic-com-identities-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Inbound Destinations API from DID Logic — 2 operation(s) for inbound destinations.
  name: DID Logic Inbound Destinations API
  slug: didlogic-com-inbound-destinations-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The KYC Documents API from DID Logic — 4 operation(s) for kyc documents.
  name: DID Logic KYC Documents API
  slug: didlogic-com-kyc-documents-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Numbers & Inventory API from DID Logic — 8 operation(s) for numbers & inventory.
  name: DID Logic Numbers & Inventory API
  slug: didlogic-com-numbers-inventory-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Purchases API from DID Logic — 1 operation(s) for purchases.
  name: DID Logic Purchases API
  slug: didlogic-com-purchases-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Reports API from DID Logic — 2 operation(s) for reports.
  name: DID Logic Reports API
  slug: didlogic-com-reports-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The Risk Checks API from DID Logic — 2 operation(s) for risk checks.
  name: DID Logic Risk Checks API
  slug: didlogic-com-risk-checks-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The SIP Accounts API from DID Logic — 3 operation(s) for sip accounts.
  name: DID Logic SIP Accounts API
  slug: didlogic-com-sip-accounts-api
- baseURL: https://app.didlogic.com
  baseurl_source: declared
  description: The SMS API from DID Logic — 2 operation(s) for sms.
  name: DID Logic SMS API
  slug: didlogic-com-sms-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/didlogic-com/agentic-access/didlogic-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/didlogic-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/didlogic-com/rate-limits/didlogic-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/didlogic-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/didlogic-com/plans/didlogic-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/didlogic-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/rules/didlogic-com-rules.yml
  title: ''
  type: Spectral
  url: rules/didlogic-com-rules.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/json-ld/didlogic-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/didlogic-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/didlogic-com/vocabulary/didlogic-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/didlogic-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/didlogic-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/data-model/didlogic-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/didlogic-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/components/didlogic-com-components.yml
  title: ''
  type: Components
  url: components/didlogic-com-components.yml
- group: operate
  href: https://artifacts.apis.io/didlogic-com/changelog/didlogic-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/didlogic-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/conventions/didlogic-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/didlogic-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/conventions/didlogic-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/didlogic-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/didlogic-com/sandbox/didlogic-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/didlogic-com-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://didlogic.com/security/
- group: design
  href: https://artifacts.apis.io/didlogic-com/lifecycle/didlogic-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/didlogic-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/errors/didlogic-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/didlogic-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/didlogic-com/conformance/didlogic-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/didlogic-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/didlogic-com/overlays/didlogic-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/didlogic-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/didlogic-com/llms/didlogic-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/didlogic-com-llms.txt
- group: build
  href: https://artifacts.apis.io/didlogic-com/mcp/didlogic-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/didlogic-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/didlogic-com/mcp/didlogic-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/didlogic-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/didlogic-com/well-known/didlogic-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/didlogic-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/didlogic-com/hosts/didlogic-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/didlogic-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/didlogic-com/integrations/didlogic-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/didlogic-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/didlogic-com/vendors/didlogic-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/didlogic-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/didlogic-com/packages/didlogic-com-packages.yml
  title: ''
  type: SDKs
  url: packages/didlogic-com-packages.yml
- group: build
  href: https://artifacts.apis.io/didlogic-com/packages/didlogic-com-packages.yml
  title: ''
  type: Packages
  url: packages/didlogic-com-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://didlogic.com/news/did-numbers-in-iceland/
- group: auth
  href: https://artifacts.apis.io/didlogic-com/authentication/didlogic-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/didlogic-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/didlogic-com/security/didlogic-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/didlogic-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/didlogic-com/security/didlogic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/didlogic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://didlogic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://didlogic.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.didlogic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.didlogic.com/docs/api/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.didlogic.com/docs/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.didlogic.com/docs/release-notes
- group: operate
  title: ''
  type: Support
  url: https://support.didlogic.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://didlogic.com/faq/
- group: operate
  title: ''
  type: Contact
  url: https://didlogic.com/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://didlogic.com/setup/customer-service/network-status/
- group: company
  title: ''
  type: Blog
  url: https://didlogic.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://didlogic.com/pricing/phone-numbers/
- group: start
  title: ''
  type: SignUp
  url: https://didlogic.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://app.didlogic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://didlogic.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://didlogic.com/privacy-and-security/
- group: auth
  title: ''
  type: Security
  url: https://didlogic.com/security/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/didlogic/
created: '2026-11-05'
description: DID Logic (didlogic, legal entity DID Logic PTE. LTD.) is a global SIP trunk and DID number provider operating 12 points of presence worldwide, offering direct, low-latency access to regional voice carriers. It sells virtual phone numbers by country, wholesale international voice and SMS, an SMS API, AI voice agent integrations (e.g. Vapi), a Voice SDK and an MCP server, with a developer portal at docs.didlogic.com documenting REST APIs (v1 and v2) for balance, calls, Click2Call, purchases, SIP accounts, SMS, number inventory, HLR lookups and KYC.
image: https://didlogic.com/wp-content/uploads/2024/11/DiDLogic_Featured-image.png
json_schemas:
- name: CdrListResponse
  property_count: 2
  slug: didlogic-com-cdr-list-response
- name: Warning
  property_count: 4
  slug: didlogic-com-warning
jsonld:
- class_count: 5
  name: Didlogic Com Context
  property_count: 20
  slug: didlogic-com-context
layout: provider
mcp_servers:
- description: 'Official hosted didlogic MCP server connecting AI assistants (Claude, ChatGPT, Cursor, VS Code, Claude Code) to a didlogic account. Per the provider docs it supports every operation of the public API '
  name: didlogic MCP Server
  slug: didlogic-mcp-server
modified: '2026-11-05'
name: DID Logic
nav: Providers
network: true
overview: 'DID Logic publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Balance API, API Access API, Calls API, and 11 more. Tagged areas include Company, Telecommunications, VoIP, SIP Trunking, and DID Numbers.


  The DID Logic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DID Logic''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 42 more developer resources.'
plans:
- name: Didlogic Com Plans Pricing
  plan_count: 5
  slug: didlogic-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Didlogic Com Rate Limits
  slug: didlogic-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: DID Logic API Rules
  rule_count: 58
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 12
  slug: didlogic-com-rules
score:
  band: exemplar
  composite: 68.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 63.5
    developer_ergonomics: 73.2
    discoverability: 66.7
    operational_transparency: 63.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Didlogic Com Authentication
  slug: didlogic-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Didlogic Com Domain Security
  slug: didlogic-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Didlogic Com Trust Center
  slug: didlogic-com-trust-center
  summary_line: ISO 27001
skill_count: 5
skills:
- name: didlogic-buy-and-route-number
  slug: didlogic-com-buy-and-route-number
- name: didlogic-click2call
  slug: didlogic-com-click2call
- name: didlogic-hlr-lookup
  slug: didlogic-com-hlr-lookup
- name: didlogic-send-sms
  slug: didlogic-com-send-sms
- name: didlogic-traffic-report
  slug: didlogic-com-traffic-report
slug: didlogic-com
tags:
- Company
- Telecommunications
- VoIP
- SIP Trunking
- DID Numbers
- SMS
- Voice
- MCP
website: https://didlogic.com/
---
