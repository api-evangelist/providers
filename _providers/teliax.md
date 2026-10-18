---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 240
  human_in_the_loop: 9
  name: Teliax Agentic Access
  operation_count: 467
  slug: teliax-agentic-access
  summary_line: 467 operations · 240 acting · 9 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Tenant-wide activity journal (read-only)
  name: Teliax Activity Journal API
  slug: teliax-activity-journal-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Submit and track bulk inventory operations (metadata, PIN, CNAM) with order references.
  name: Teliax Bulk Operations API
  slug: teliax-bulk-operations-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Bulk port project management
  name: Teliax Bulk Port API
  slug: teliax-bulk-port-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Background job monitoring and management
  name: Teliax Bulk Port Jobs API
  slug: teliax-bulk-port-jobs-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Carrier coordination email (#336)
  name: Teliax Carrier Email API
  slug: teliax-carrier-email-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Authenticated NANPA FGD assignment reference data; not carrier routing configuration
  name: Teliax CIC Reference Data API
  slug: teliax-cic-reference-data-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Caller Name lookups and Robocall Mitigation scoring via TransUnion TruContact.
  name: Teliax CNAM API
  slug: teliax-cnam-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Account API from Teliax — 4 operation(s) for customer/account.
  name: Teliax Customer/Account API
  slug: teliax-customer-account-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Analytics API from Teliax — 5 operation(s) for customer/analytics.
  name: Teliax Customer/Analytics API
  slug: teliax-customer-analytics-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/ApiKeys API from Teliax — 4 operation(s) for customer/apikeys.
  name: Teliax Customer/Api Keys API
  slug: teliax-customer-apikeys-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Billing API from Teliax — 7 operation(s) for customer/billing.
  name: Teliax Customer/Billing API
  slug: teliax-customer-billing-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Messaging API from Teliax — 25 operation(s) for customer/messaging.
  name: Teliax Customer/Messaging API
  slug: teliax-customer-messaging-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Network API from Teliax — 2 operation(s) for customer/network.
  name: Teliax Customer/Network API
  slug: teliax-customer-network-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Numbers API from Teliax — 21 operation(s) for customer/numbers.
  name: Teliax Customer/Numbers API
  slug: teliax-customer-numbers-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Porting API from Teliax — 30 operation(s) for customer/porting.
  name: Teliax Customer/Porting API
  slug: teliax-customer-porting-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Team API from Teliax — 9 operation(s) for customer/team.
  name: Teliax Customer/Team API
  slug: teliax-customer-team-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The Customer/Trunks API from Teliax — 14 operation(s) for customer/trunks.
  name: Teliax Customer/Trunks API
  slug: teliax-customer-trunks-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Do Not Originate checks — determine whether a phone number is flagged as one that should never appear as a caller ID.
  name: Teliax DNO API
  slug: teliax-dno-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Geographic inventory visualization data
  name: Teliax Inventory Map API
  slug: teliax-inventory-map-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Generate and download inventory reports
  name: Teliax Inventory Reports API
  slug: teliax-inventory-reports-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Operator-facing job run lifecycle (sync history, attempts, warnings)
  name: Teliax Job Runs API
  slug: teliax-job-runs-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: LERG telecom routing data — table metadata, NPA-NXX lookups, switch data, tandem relationships, and complex cross-table queries.
  name: Teliax LERG API
  slug: teliax-lerg-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: GraphQL interface for flexible LERG data queries with field selection, filtering, pagination, nested relationships, and dynamic joins.
  name: Teliax LERG GraphQL API
  slug: teliax-lerg-graphql-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Local Routing Number lookups — resolve a phone number to the switch that currently serves it, with porting metadata.
  name: Teliax LRN API
  slug: teliax-lrn-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: LSMS database queries — relationship lookups across phone numbers, LRNs, SPIDs, and service providers via REST or GraphQL.
  name: Teliax LSMS API
  slug: teliax-lsms-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Customer-safe TNIQ-managed carrier and NPAC processing
  name: Teliax Managed Port Processing API
  slug: teliax-managed-port-processing-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: 10DLC brand registration and management
  name: Teliax Messaging Brands API
  slug: teliax-messaging-brands-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: 10DLC campaign management and phone number assignment
  name: Teliax Messaging Campaigns API
  slug: teliax-messaging-campaigns-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: 'TCR reference data: use cases, verticals, entity types'
  name: Teliax Messaging Enums API
  slug: teliax-messaging-enums-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Per-SPID NNID hold policy, collision-safe backfill, and overwrite findings (#245)
  name: Teliax Messaging NNID Hold API
  slug: teliax-messaging-nnid-hold-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: 'nnSR overwrite-request approval queue: list, approve, reject, LOA attach (#245 W3)'
  name: Teliax Messaging NNID Overwrite Requests API
  slug: teliax-messaging-nnid-overwrite-requests-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: NetNumber ID management for SMS provisioning
  name: Teliax Messaging NNIDs API
  slug: teliax-messaging-nnids-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Assign or remove NNIDs on phone numbers (nnSR push)
  name: Teliax Messaging Number NNID API
  slug: teliax-messaging-number-nnid-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Search and query number inventory
  name: Teliax Number Inventory API
  slug: teliax-number-inventory-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Three-phase inventory audit operations
  name: Teliax Number Inventory Audit API
  slug: teliax-number-inventory-audit-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Query-based inventory search with powerful filter language
  name: Teliax Number Inventory Query API
  slug: teliax-number-inventory-query-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Port-out release project management for NPAC releases
  name: Teliax Port-Out Release API
  slug: teliax-port-out-release-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Supporting documents (LOA/BILL/CSR/OTHER) for LNP port-in projects
  name: Teliax Port Project Documents API
  slug: teliax-port-project-documents-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The port-protection-rule-controller API from Teliax — 3 operation(s) for port-protection-rule-controller.
  name: Teliax Port Protection Rule Controller API
  slug: teliax-port-protection-rule-controller-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Queue async reports that are emailed to the requesting user as CSV/XLSX attachments.
  name: Teliax Reports API
  slug: teliax-reports-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Resp Org Change workflow management
  name: Teliax ROC API
  slug: teliax-roc-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Toll-free number routing — CIC lookups, ROR lookups, and CPR inspection.
  name: Teliax Route Link API
  slug: teliax-routelink-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Service Order Administration endpoints for Local Number Portability
  name: Teliax SOA Operations API
  slug: teliax-soa-operations-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: TCR webhook event receiver and event history
  name: Teliax TCR Webhooks API
  slug: teliax-tcr-webhooks-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Authenticated read-only CIC, NNID, Resp Org, and NPAC SPID reference directories
  name: Teliax Telecom Reference Data API
  slug: teliax-telecom-reference-data-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Toll-free number management via Somos TFN Registry
  name: Teliax Toll Free API
  slug: teliax-toll-free-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: Toll-free number inventory synchronization
  name: Teliax Toll-Free Sync API
  slug: teliax-toll-free-sync-api
- baseURL: https://api.telique.ringer.tel
  baseurl_source: declared
  description: The trans-union-cnam-controller API from Teliax — 3 operation(s) for trans-union-cnam-controller.
  name: Teliax Trans Union Cnam Controller API
  slug: teliax-trans-union-cnam-controller-api
artifact_total: 76
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/agentic-access/teliax-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/teliax-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/rate-limits/teliax-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/teliax-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/plans/teliax-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/teliax-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/rules/teliax-rules.yml
  title: ''
  type: Spectral
  url: rules/teliax-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/rules/teliax-ringer-oapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/teliax-ringer-oapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/json-ld/teliax-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teliax-context.jsonld
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/conventions/teliax-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/teliax-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/conventions/teliax-conventions.yml
  title: ''
  type: Conventions
  url: conventions/teliax-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/scopes/teliax-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/teliax-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/lifecycle/teliax-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/teliax-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/lifecycle/teliax-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/teliax-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/errors/teliax-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/teliax-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/conformance/teliax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teliax-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/overlays/teliax-telique-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/teliax-telique-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/mcp/teliax-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/teliax-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/mcp/teliax-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/teliax-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/well-known/teliax-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teliax-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/hosts/teliax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teliax-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/vendors/teliax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teliax-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/packages/teliax-packages.yml
  title: ''
  type: SDKs
  url: packages/teliax-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/packages/teliax-packages.yml
  title: ''
  type: Packages
  url: packages/teliax-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/authentication/teliax-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teliax-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/security/teliax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teliax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teliax.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/teliax/ringer-oapi/blob/5ba0143e6b8246571905b37f17b8719a6e8ceaf2/.spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ringer.tel/
- group: company
  title: ''
  type: Blog
  url: https://ringer.tel/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ringer.tel/ringer-business/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.teliax.com/support/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ringer.tel/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ringer.tel/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teliax
created: '2026-10-09'
description: 'Teliax is a wholesale and carrier-grade telecommunications provider that now operates as Ringer Network Solutions: www.teliax.com redirects to ringer.tel, whose homepage lists ''Ringer Network Solutions (formerly Teliax) - Wholesale and carrier-grade services'' alongside Ringer Business (formerly Leap Telecom) and Ringer Mobile. Products include SIP trunking, wholesale voice, toll-free services, access homing tandem, hosted PBX, MS Teams integration, private-label CPaaS and TeliQue telecom data services, with developer documentation for Ringer APIs (TeliQue, TNIQ, WARP) at docs.ringer.tel and the ringer-oapi repository in the Teliax Inc. GitHub organization.'
image: https://ringer.tel/hs-fs/hubfs/Ringer_Primary-Color.png
json_schemas:
- name: AutoActivationSettingsResponse
  property_count: 9
  slug: teliax-auto-activation-settings-response
- name: ComplexQueryRequest
  property_count: 6
  slug: teliax-complex-query-request
- name: CprDumpResponse
  property_count: 6
  slug: teliax-cpr-dump-response
- name: DnoLookupResponse
  property_count: 7
  slug: teliax-dno-lookup-response
- name: github_com_ringer-warp_api-gateway_internal_models.Assignment
  property_count: 30
  slug: teliax-github-com-ringer-warp-api-gateway-internal-models-assignment
- name: github_com_ringer-warp_api-gateway_internal_models.AssignmentWithUsages
  property_count: 32
  slug: teliax-github-com-ringer-warp-api-gateway-internal-models-assignment-with-usages
- name: github_com_ringer-warp_api-gateway_internal_models.TrunkGroup
  property_count: 22
  slug: teliax-github-com-ringer-warp-api-gateway-internal-models-trunk-group
- name: github_com_ringer-warp_api-gateway_internal_models.TrunkGroupWithIPs
  property_count: 23
  slug: teliax-github-com-ringer-warp-api-gateway-internal-models-trunk-group-with-ips
- name: IdentityRequest
  property_count: 8
  slug: teliax-identity-request
- name: internal_handlers.BulkAssignRequest
  property_count: 12
  slug: teliax-internal-handlers-bulk-assign-request
- name: internal_handlers.TrunkUpdateResult
  property_count: 23
  slug: teliax-internal-handlers-trunk-update-result
- name: PortProjectDetailResponse
  property_count: 45
  slug: teliax-port-project-detail-response
- name: PortProjectDetail
  property_count: 78
  slug: teliax-port-project-detail
- name: PortProjectResponse
  property_count: 51
  slug: teliax-port-project-response
- name: QueryResponse
  property_count: 7
  slug: teliax-query-response
- name: SoaQueryResponse
  property_count: 17
  slug: teliax-soa-query-response
- name: TandemQueryResponse
  property_count: 3
  slug: teliax-tandem-query-response
- name: TollFreePtrOperationDto
  property_count: 27
  slug: teliax-toll-free-ptr-operation-dto
jsonld:
- class_count: 120
  name: Teliax Context
  property_count: 593
  slug: teliax-context
layout: provider
mcp_servers:
- description: 'Ringer''s (formerly Teliax) official MCP server for Telique telecom data (LRN, CNAM, DNO, LERG, RouteLink toll-free, LSMS/LERG GraphQL). It ships two ways: a hosted OAuth-protected remote endpoint and '
  name: Telique MCP Server
  slug: telique
modified: '2026-10-09'
name: Teliax
nav: Providers
network: true
overview: 'Teliax publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity Journal API, Bulk Operations API, Bulk Port API, and 45 more. Tagged areas include Company, Telecommunications, Voice, SIP Trunking, and Toll-Free.


  The Teliax catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Teliax''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 28 more developer resources.'
plans:
- name: Teliax Plans Pricing
  plan_count: 2
  slug: teliax-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Teliax Rate Limits
  slug: teliax-rate-limits
rules:
- authorship: provider
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Teliax — ringer oapi rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: teliax-ringer-oapi-spectral-rules
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Teliax API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 3
  slug: teliax-rules
scopes:
- name: Teliax Scopes
  scope_count: 22
  slug: teliax-scopes
  summary_line: 22 scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 94.0
    catalog_earned_first_party: 34.0
    catalog_gap: 21.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 52.6
    contract_governance: 72.7
    contract_quality: 60.1
    developer_ergonomics: 37.5
    discoverability: 73.3
    operational_transparency: 34.2
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/teliax/refs/heads/main/screenshots/teliax-2026-10-11T130732.png
security:
- kind: authentication
  name: Teliax Authentication
  slug: teliax-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Teliax Domain Security
  slug: teliax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teliax
tags:
- Company
- Telecommunications
- Voice
- SIP Trunking
- Toll-Free
- Wholesale Carrier
- CPaaS
website: https://www.teliax.com/
---
