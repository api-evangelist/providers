---
agent_readiness:
  band: agent-ready
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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Wholechain Agentic Access
  operation_count: 34
  slug: wholechain-agentic-access
  summary_line: 34 operations · 19 acting
api_count: 2
apis:
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The Connect API from Wholechain — 19 operation(s) for connect.
  name: Wholechain Connect API
  slug: wholechain-connect-api
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The Edi API from Wholechain — 1 operation(s) for edi.
  name: Wholechain Edi API
  slug: wholechain-edi-api
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The EPCIS Interface API from Wholechain — 5 operation(s) for epcis interface.
  name: Wholechain EPCIS Interface API
  slug: wholechain-epcis-interface-api
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The EPCIS Legacy Interface API from Wholechain — 1 operation(s) for epcis legacy interface.
  name: Wholechain EPCIS Legacy Interface API
  slug: wholechain-epcis-legacy-interface-api
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The Events API from Wholechain — 1 operation(s) for events.
  name: Wholechain Events API
  slug: wholechain-events-api
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The ExternalOAuth API from Wholechain — 2 operation(s) for externaloauth.
  name: Wholechain External O Auth API
  slug: wholechain-externaloauth-api
- baseURL: https://connect.wholechain.com
  baseurl_source: declared
  description: The Health API from Wholechain — 1 operation(s) for health.
  name: Wholechain Health API
  slug: wholechain-health-api
artifact_total: 24
common:
- group: build
  href: https://artifacts.apis.io/wholechain/integrations/wholechain-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/wholechain-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/wholechain/agentic-access/wholechain-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wholechain-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/wholechain/rate-limits/wholechain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wholechain-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wholechain/plans/wholechain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wholechain-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wholechain/rules/wholechain-rules.yml
  title: ''
  type: Spectral
  url: rules/wholechain-rules.yml
- group: design
  href: https://artifacts.apis.io/wholechain/json-ld/wholechain-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wholechain-context.jsonld
- group: design
  href: https://artifacts.apis.io/wholechain/vocabulary/wholechain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wholechain-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/wholechain/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/wholechain/data-model/wholechain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wholechain-data-model.yml
- group: design
  href: https://artifacts.apis.io/wholechain/conventions/wholechain-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wholechain-conventions.yml
- group: start
  href: https://artifacts.apis.io/wholechain/sandbox/wholechain-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/wholechain-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/wholechain/authentication/wholechain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wholechain-authentication.yml
- group: design
  href: https://artifacts.apis.io/wholechain/lifecycle/wholechain-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wholechain-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wholechain/errors/wholechain-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wholechain-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wholechain/conformance/wholechain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wholechain-conformance.yml
- group: other
  href: https://artifacts.apis.io/wholechain/overlays/wholechain-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wholechain-connect-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/wholechain/llms/wholechain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wholechain-llms.txt
- group: other
  href: https://artifacts.apis.io/wholechain/hosts/wholechain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wholechain-hosts.yml
- group: other
  href: https://artifacts.apis.io/wholechain/vendors/wholechain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wholechain-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wholechain/security/wholechain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wholechain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wholechain.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wholechain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.wholechain.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.wholechain.com/GettingStarted/Introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.wholechain.com/GettingStarted/Swagger/
- group: operate
  title: ''
  type: Support
  url: https://support.wholechain.com/
- group: company
  title: ''
  type: Blog
  url: https://wholechain.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wholechain
- group: commercial
  title: ''
  type: Pricing
  url: https://wholechain.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.wholechain.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wholechain.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.wholechain.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wholechain.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wholechain.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wholechain/
- group: other
  title: ''
  type: X
  url: https://x.com/wholechain
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Wholechain
created: '2026-10-18'
description: Wholechain (Wholechain, Inc.) is a blockchain-based supply chain traceability platform built to enable trust, coordination, and transparency in fragmented supply chains. It helps businesses map and capture supply chain events from origin to final delivery on mobile, tablet or desktop, share interoperable traceability records with partners using global data standards such as GS1 and GDST, verify origins down to the farm, fishery or vessel, reduce compliance burdens, and integrate with ERP and warehouse systems through a developer API documented at developers.wholechain.com.
image: https://framerusercontent.com/assets/wfr5sT20U5Yirjy282MquYYPSOw.jpg
json_schemas:
- name: Wholechain.API.Contracts.Connect.Events.Requests.V2.ConnectPurchaseOrder
  property_count: 19
  slug: wholechain-wholechain-api-contracts-connect-events-requests-v2-connect-purchase-order
- name: Wholechain.API.Contracts.Connect.Integration.ProcessEvents.ProcessEventsResponse
  property_count: 6
  slug: wholechain-wholechain-api-contracts-connect-integration-process-events-process-events-response
- name: Wholechain.API.Contracts.Events.Responses.PaginatedEventDetailsResponse
  property_count: 7
  slug: wholechain-wholechain-api-contracts-events-responses-paginated-event-details-response
- name: Wholechain.API.Contracts.Jobs.Responses.GetPaginatedJobsResponse
  property_count: 7
  slug: wholechain-wholechain-api-contracts-jobs-responses-get-paginated-jobs-response
- name: Wholechain.API.Contracts.Products.Responses.PaginatedProductsResponse
  property_count: 8
  slug: wholechain-wholechain-api-contracts-products-responses-paginated-products-response
- name: Wholechain.Connect.Application.Services.FileService.FileUploadEvent
  property_count: 28
  slug: wholechain-wholechain-connect-application-services-file-service-file-upload-event
jsonld:
- class_count: 120
  name: Wholechain Context
  property_count: 392
  slug: wholechain-context
layout: provider
modified: '2026-10-18'
name: Wholechain
nav: Providers
network: true
overview: 'Wholechain publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connect API, Edi API, EPCIS Interface API, and 4 more. Tagged areas include Company, Supply Chain, Traceability, Blockchain, and Food Safety.


  The Wholechain catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wholechain''s developer surface includes sandbox, authentication, documentation, getting-started guide, API reference, support, engineering blog, and 30 more developer resources.'
plans:
- name: Wholechain Plans Pricing
  plan_count: 4
  slug: wholechain-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Wholechain Rate Limits
  slug: wholechain-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Wholechain API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: wholechain-rules
scopes:
- name: Wholechain Scopes
  scope_count: 0
  slug: wholechain-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.0
    catalog_earned_first_party: 24.0
    catalog_gap: 29.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 33.3
    contract_quality: 50.9
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wholechain Authentication
  slug: wholechain-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wholechain Domain Security
  slug: wholechain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: wholechain-manage-master-data
  slug: wholechain-manage-master-data
- name: wholechain-record-traceability-events
  slug: wholechain-record-traceability-events
- name: wholechain-trace-and-epcis
  slug: wholechain-trace-and-epcis
slug: wholechain
tags:
- Company
- Supply Chain
- Traceability
- Blockchain
- Food Safety
- Compliance
- GS1
- Logistics
website: https://wholechain.com
---
