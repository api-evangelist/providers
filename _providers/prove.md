---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Prove Agentic Access
  operation_count: 26
  slug: prove-agentic-access
  summary_line: 26 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: Phone-based authentication and device binding.
  name: Prove Auth API
  slug: prove-auth-api
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: OAuth 2.0 token issuance.
  name: Prove Authentication API
  slug: prove-authentication-api
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: Cross-domain linking of identity scopes.
  name: Prove Domain API
  slug: prove-domain-api
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: Persistent identity lifecycle management.
  name: Prove Identity API
  slug: prove-identity-api
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: Ordered Pre-Fill verification flow - start, validate, challenge, complete.
  name: Prove Identity Verification API
  slug: prove-identity-verification-api
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: Identity discovery and verified attribute retrieval.
  name: Prove Pre-Fill API
  slug: prove-pre-fill-api
- baseURL: https://platform.proveapis.com/v3
  baseurl_source: declared
  description: Unified Authentication possession and trust evaluation.
  name: Prove Trust Score API
  slug: prove-trust-score-api
artifact_total: 50
collections:
- collection_type: open
  name: Prove Auth API
  slug: open-prove-auth-api
- collection_type: open
  name: Prove Auth Authentication API
  slug: open-prove-authentication-api
- collection_type: open
  name: Prove Auth Domain API
  slug: open-prove-domain-api
- collection_type: open
  name: Prove Auth Identity API
  slug: open-prove-identity-api
- collection_type: open
  name: Prove Auth Identity Verification API
  slug: open-prove-identity-verification-api
- collection_type: open
  name: Prove Auth Pre-Fill API
  slug: open-prove-pre-fill-api
- collection_type: open
  name: Prove Auth Trust Score API
  slug: open-prove-trust-score-api
- collection_type: open
  name: Prove API
  slug: open-prove
common:
- group: auth
  href: https://artifacts.apis.io/prove/scopes/prove-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/prove-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/prove/plans/prove-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prove-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/prove/rate-limits/prove-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prove-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/prove/well-known/prove-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prove-status-security.txt
- group: design
  href: https://artifacts.apis.io/prove/rules/prove-rules.yml
  title: ''
  type: Spectral
  url: rules/prove-rules.yml
- group: design
  href: https://artifacts.apis.io/prove/json-ld/prove-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prove-context.jsonld
- group: design
  href: https://artifacts.apis.io/prove/vocabulary/prove-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prove-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/prove/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/prove/data-model/prove-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prove-data-model.yml
- group: design
  href: https://artifacts.apis.io/prove/conventions/prove-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prove-conventions.yml
- group: start
  href: https://artifacts.apis.io/prove/sandbox/prove-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/prove-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/prove/security/prove-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/prove-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prove.com/
- group: design
  href: https://artifacts.apis.io/prove/lifecycle/prove-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/prove-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/prove/errors/prove-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prove-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prove/conformance/prove-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prove-conformance.yml
- group: other
  href: https://artifacts.apis.io/prove/overlays/prove-auth-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/prove-auth-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/prove/llms/prove-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prove-llms.txt
- group: build
  href: https://artifacts.apis.io/prove/mcp/prove-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/prove-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/prove/mcp/prove-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prove-mcp.yml
- group: agent
  href: https://artifacts.apis.io/prove/well-known/prove-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prove-well-known.yml
- group: other
  href: https://artifacts.apis.io/prove/hosts/prove-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prove-hosts.yml
- group: other
  href: https://artifacts.apis.io/prove/vendors/prove-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prove-vendors.yml
- group: build
  href: https://artifacts.apis.io/prove/packages/prove-packages.yml
  title: ''
  type: SDKs
  url: packages/prove-packages.yml
- group: build
  href: https://artifacts.apis.io/prove/packages/prove-packages.yml
  title: ''
  type: Packages
  url: packages/prove-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.prove.com/leadership
- group: other
  href: https://artifacts.apis.io/prove/capabilities/prove-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/prove-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/prove/agentic-access/prove-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prove-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/prove/security/prove-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prove-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/prove/authentication/prove-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prove-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prove-identity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proveidentity
- group: company
  title: ''
  type: Website
  url: https://www.prove.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.prove.com
- group: commercial
  href: https://artifacts.apis.io/prove/finops/prove-finops.yml
  title: ''
  type: FinOps
  url: finops/prove-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.prove.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.prove.com
- group: operate
  title: ''
  type: Support
  url: https://support.prove.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prove.com/legal/prove-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prove.com/legal/overview
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/prove-eng/prove-link-api-testing/collection/93r30p4/prove-api
- group: start
  title: ''
  type: SignUp
  url: https://portal.prove.com/en/signup
created: '2026-06-21'
description: Prove is a phone-centric digital identity verification and authentication platform. The Prove API (v3) uses the consumer's mobile phone number and cryptographic possession signals to power Pre-Fill identity prefill, passive Trust Score verification, Unified Authentication, phone-based Auth and a persistent Identity Manager - all behind an OAuth 2.0 client-credentials REST interface served from regional hosts (https://platform.proveapis.com/v3 for the US, https://platform.eu.proveapis.com/v3 for the EU, with UAT sandboxes for each). Official server SDKs ship for TypeScript, Go, Java and .NET, plus web and mobile Auth client SDKs and a public Postman workspace.
finops:
- has_sources: true
  method: generated
  name: Prove Finops
  primary_unit: ''
  service_category: Identity and Security
  slug: prove-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prove.png
json_schemas:
- name: AuthContinueRequest
  property_count: 1
  slug: prove-auth-continue-request
- name: AuthResponse
  property_count: 4
  slug: prove-auth-response
- name: AuthStartRequest
  property_count: 3
  slug: prove-auth-start-request
- name: DeviceRevokeRequest
  property_count: 3
  slug: prove-device-revoke-request
- name: DiscoverResponse
  property_count: 2
  slug: prove-discover-response
- name: EnrollIdentityRequest
  property_count: 6
  slug: prove-enroll-identity-request
- name: FetchResponse
  property_count: 2
  slug: prove-fetch-response
- name: IdentityListResponse
  property_count: 2
  slug: prove-identity-list-response
- name: Identity
  property_count: 5
  slug: prove-identity
- name: SuccessResponse
  property_count: 1
  slug: prove-success-response
- name: TokenRequest
  property_count: 3
  slug: prove-token-request
- name: TokenResponse
  property_count: 5
  slug: prove-token-response
- name: V3ChallengeRequest
  property_count: 3
  slug: prove-v3-challenge-request
- name: V3CompleteRequest
  property_count: 2
  slug: prove-v3-complete-request
- name: V3CompleteResponse
  property_count: 5
  slug: prove-v3-complete-response
- name: V3CorrelationRequest
  property_count: 1
  slug: prove-v3-correlation-request
- name: V3FlowResponse
  property_count: 3
  slug: prove-v3-flow-response
- name: V3StartRequest
  property_count: 9
  slug: prove-v3-start-request
- name: V3StartResponse
  property_count: 4
  slug: prove-v3-start-response
- name: V3UnifyRequest
  property_count: 14
  slug: prove-v3-unify-request
- name: V3UnifyStatusResponse
  property_count: 5
  slug: prove-v3-unify-status-response
jsonld:
- class_count: 25
  name: Prove Context
  property_count: 51
  slug: prove-context
layout: provider
mcp_servers:
- description: A remote MCP server answers at https://developer.prove.com/mcp, the Mintlify-hosted documentation host (CNAME cname.mintlify.builders). An anonymous JSON-RPC tools/list on 2026-10-08 returned three DO
  name: Prove MCP Server
  slug: prove-docs
modified: '2026-10-08'
name: Prove
nav: Providers
network: true
overview: 'Prove publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Authentication API, Domain API, and 4 more. Tagged areas include Identity Verification, Authentication, Phone Intelligence, KYC, and Fraud Prevention.


  The Prove catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Prove''s developer surface includes sandbox, authentication, documentation, engineering blog, support, signup flow, and 36 more developer resources.'
plans:
- name: Prove Plans Pricing
  plan_count: 0
  slug: prove-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Prove Rate Limits
  slug: prove-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Prove API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: prove-rules
scopes:
- name: Prove Scopes
  scope_count: 0
  slug: prove-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 25.0
    contract_governance: 22.0
    contract_quality: 62.7
    developer_ergonomics: 48.2
    discoverability: 75.8
    operational_transparency: 21.1
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/prove/prove-2026-09-02T152234.png
security:
- kind: authentication
  name: Prove Authentication
  slug: prove-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Prove Domain Security
  slug: prove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Prove Trust Center
  slug: prove-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: prove-identity-manager-enroll
  slug: prove-identity-manager-enroll
- name: prove-prefill-verify-identity
  slug: prove-prefill-verify-identity
- name: prove-unified-authentication
  slug: prove-unified-authentication
slug: prove
tags:
- Identity Verification
- Authentication
- Phone Intelligence
- KYC
- Fraud Prevention
website: https://www.prove.com
---
