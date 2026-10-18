---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 60
  human_in_the_loop: 2
  name: Gmi Cloud Agentic Access
  operation_count: 95
  slug: gmi-cloud-agentic-access
  summary_line: 95 operations · 60 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: OpenAI-compatible inference endpoints (GET /v1/models, POST /v1/chat/completions) plus video inference; no machine-readable contract published.
  name: GMI Cloud Inference Engine API
  slug: inference-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: GMI Bare metal management APIs for provisioning, configuring, and controlling physical server nodes. Handles server lifecycle management, hardware inventory, and status monitoring.
  name: GMI Cloud Baremetals API
  slug: gmi-cloud-baremetals-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: GMI Container management APIs for creating, managing, and monitoring containerized applications.
  name: GMI Cloud Containers API
  slug: gmi-cloud-containers-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: GMI Elastic IP address management APIs for allocating, associating, and managing public IP addresses.
  name: GMI Cloud Elastic Ips API
  slug: gmi-cloud-elastic-ips-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The firewalls API from GMI Cloud — 4 operation(s) for firewalls.
  name: GMI Cloud Firewalls API
  slug: gmi-cloud-firewalls-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The idcs API from GMI Cloud — 1 operation(s) for idcs.
  name: GMI Cloud Idcs API
  slug: gmi-cloud-idcs-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: GMI Image management APIs for query OS images.
  name: GMI Cloud Images API
  slug: gmi-cloud-images-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The invitations API from GMI Cloud — 1 operation(s) for invitations.
  name: GMI Cloud Invitations API
  slug: gmi-cloud-invitations-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The logs API from GMI Cloud — 1 operation(s) for logs.
  name: GMI Cloud Logs API
  slug: gmi-cloud-logs-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The me API from GMI Cloud — 9 operation(s) for me.
  name: GMI Cloud Me API
  slug: gmi-cloud-me-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The oauth API from GMI Cloud — 1 operation(s) for oauth.
  name: GMI Cloud OAuth API
  slug: gmi-cloud-oauth-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The organizations API from GMI Cloud — 8 operation(s) for organizations.
  name: GMI Cloud Organizations API
  slug: gmi-cloud-organizations-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: Sandbox instance lifecycle management (Sandbox v2, /api/v2/sandboxes)
  name: GMI Cloud Sandbox API
  slug: gmi-cloud-sandbox-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: Sandbox execution data plane (accessed via the sandbox host and sandbox access token). These endpoints are not under the control plane's `/api/v2` path; clients connect directly to `https://{sandbox_k
  name: GMI Cloud Sandbox Exec API
  slug: gmi-cloud-sandbox-exec-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: 'Sandbox file data plane (`/files`). **These endpoints are not under `/api/v2`** and do not use `Authorization: Bearer`: they are served by the sandbox''s own data-plane entry point — clients connect di'
  name: GMI Cloud Sandbox Files API
  slug: gmi-cloud-sandbox-files-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: Sandbox template management (Sandbox v2, `/api/v2/templates`)
  name: GMI Cloud Sandbox Template API
  slug: gmi-cloud-sandboxtemplate-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: GMI template management APIs for creating and managing reusable container template.
  name: GMI Cloud Templates API
  slug: gmi-cloud-templates-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The users API from GMI Cloud — 4 operation(s) for users.
  name: GMI Cloud Users API
  slug: gmi-cloud-users-api
- baseURL: https://console.gmicloud.ai/api
  baseurl_source: declared
  description: The vpcs API from GMI Cloud — 2 operation(s) for vpcs.
  name: GMI Cloud Vpcs API
  slug: gmi-cloud-vpcs-api
artifact_total: 44
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/agentic-access/gmi-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gmi-cloud-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/rate-limits/gmi-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gmi-cloud-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/rules/gmi-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/gmi-cloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/json-ld/gmi-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gmi-cloud-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/vocabulary/gmi-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gmi-cloud-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/data-model/gmi-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gmi-cloud-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/conventions/gmi-cloud-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gmi-cloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/conventions/gmi-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gmi-cloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/errors/gmi-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gmi-cloud-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/conformance/gmi-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gmi-cloud-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/llms/gmi-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gmi-cloud-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/a2a/gmi-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gmi-cloud-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/mcp/gmi-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gmi-cloud-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/well-known/gmi-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gmi-cloud-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/hosts/gmi-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gmi-cloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/vendors/gmi-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gmi-cloud-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/packages/gmi-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/gmi-cloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/packages/gmi-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/gmi-cloud-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/authentication/gmi-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gmi-cloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gmi-cloud/refs/heads/main/security/gmi-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gmi-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gmicloud.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.gmicloud.ai/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gmicloud.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gmicloud.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gmicloud.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.gmicloud.ai/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GMISWE
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gmicloud.ai/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gmicloud.ai/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gmicloud.ai/en/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://console.gmicloud.ai/
created: '2026-10-13'
description: GMI Cloud is a GPU cloud and AI inference provider offering the Inference Engine (OpenAI-compatible LLM, image and video model APIs at api.gmi-serving.com), the Cluster Engine for GPU containers, bare-metal and VPC infrastructure, and GMI Sandbox for isolated code execution. Its control-plane APIs are served from console.gmicloud.ai and documented at docs.gmicloud.ai.
image: https://www.gmicloud.ai/_next/static/media/gmi-cloud.0t7b2ghyy4szj.png
json_schemas:
- name: authTokenResponse
  property_count: 2
  slug: gmi-cloud-auth-token-response
- name: BaremetalReq
  property_count: 9
  slug: gmi-cloud-baremetal-req
- name: BaremetalResp
  property_count: 13
  slug: gmi-cloud-baremetal-resp
- name: BuildDefinition
  property_count: 4
  slug: gmi-cloud-build-definition
- name: containerConfig
  property_count: 7
  slug: gmi-cloud-container-config
- name: containersResp
  property_count: 0
  slug: gmi-cloud-containers-resp
- name: createApiKeyRequest
  property_count: 3
  slug: gmi-cloud-create-api-key-request
- name: createOAuthAuthTokenRequest
  property_count: 2
  slug: gmi-cloud-create-oauth-auth-token-request
- name: CreateSandboxControlRequest
  property_count: 5
  slug: gmi-cloud-create-sandbox-control-request
- name: createSessionRequest
  property_count: 2
  slug: gmi-cloud-create-session-request
- name: CreateTemplateRequest
  property_count: 6
  slug: gmi-cloud-create-template-request
- name: elasticIPResp
  property_count: 0
  slug: gmi-cloud-elastic-ipresp
- name: exchangeAuthorizationCodeRequest
  property_count: 2
  slug: gmi-cloud-exchange-authorization-code-request
- name: FirewallResp
  property_count: 0
  slug: gmi-cloud-firewall-resp
- name: SandboxExecResultResponse
  property_count: 11
  slug: gmi-cloud-sandbox-exec-result-response
- name: SetSandboxControlTimeoutResponse
  property_count: 2
  slug: gmi-cloud-set-sandbox-control-timeout-response
- name: updatePasswordRequest
  property_count: 4
  slug: gmi-cloud-update-password-request
- name: UpdateTemplateRequest
  property_count: 3
  slug: gmi-cloud-update-template-request
jsonld:
- class_count: 120
  name: Gmi Cloud Context
  property_count: 155
  slug: gmi-cloud-context
layout: provider
mcp_servers:
- description: GMI Cloud documentation MCP server (Mintlify-hosted on docs.gmicloud.ai) exposing documentation search and retrieval; tools/list answered anonymously with HTTP 200 on 2026-10-13. It is a docs MCP, not
  name: GMI Cloud Documentation
  slug: gmi-cloud-documentation
modified: '2026-10-13'
name: GMI Cloud
nav: Providers
network: true
overview: 'GMI Cloud publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Baremetals API, Containers API, Elastic Ips API, and 16 more. Tagged areas include Company, Artificial Intelligence, Inference, GPU Cloud, and LLM.


  The GMI Cloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GMI Cloud''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 25 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 5
  name: Gmi Cloud Rate Limits
  slug: gmi-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: GMI Cloud API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 4
  slug: gmi-cloud-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 59.5
    discoverability: 80.0
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Gmi Cloud Authentication
  slug: gmi-cloud-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Gmi Cloud Domain Security
  slug: gmi-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gmi-cloud
tags:
- Company
- Artificial Intelligence
- Inference
- GPU Cloud
- LLM
- Model Routing
- Sandbox
- Infrastructure
website: https://www.gmicloud.ai
---
