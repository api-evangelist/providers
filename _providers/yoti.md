---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: Yoti Age Verification API provides endpoints to verify a user's age and identity.
  name: Age Verification API
  slug: age-verification-api
- baseURL: https://auth.api.yoti.com
  baseurl_source: declared
  description: The Accounts API from Yoti — 1 operation(s) for accounts.
  name: Yoti Accounts API
  slug: yoti-accounts-api
- baseURL: https://auth.api.yoti.com
  baseurl_source: declared
  description: The Ai API from Yoti — 1 operation(s) for ai.
  name: Yoti AI API
  slug: yoti-ai-api
- baseURL: https://auth.api.yoti.com
  baseurl_source: declared
  description: The Oauth API from Yoti — 1 operation(s) for oauth.
  name: Yoti OAuth API
  slug: yoti-oauth-api
- baseURL: https://auth.api.yoti.com
  baseurl_source: declared
  description: The Path API from Yoti — 1 operation(s) for path.
  name: Yoti Path API
  slug: yoti-path-api
- baseURL: https://auth.api.yoti.com
  baseurl_source: declared
  description: The Poa API from Yoti — 1 operation(s) for poa.
  name: Yoti Poa API
  slug: yoti-poa-api
- baseURL: https://auth.api.yoti.com
  baseurl_source: declared
  description: The Sessions API from Yoti — 2 operation(s) for sessions.
  name: Yoti Sessions API
  slug: yoti-sessions-api
artifact_total: 20
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/rules/yoti-rules.yml
  title: ''
  type: Spectral
  url: rules/yoti-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/json-ld/yoti-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yoti-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/vocabulary/yoti-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yoti-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/data-model/yoti-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yoti-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/sandbox/yoti-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/yoti-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.yoti.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/authentication/yoti-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yoti-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/conformance/yoti-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yoti-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/llms/yoti-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yoti-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/mcp/yoti-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yoti-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/well-known/yoti-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yoti-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/well-known/yoti-backstage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yoti-backstage-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/well-known/yoti-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yoti-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/hosts/yoti-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yoti-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/vendors/yoti-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yoti-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/packages/yoti-packages.yml
  title: ''
  type: SDKs
  url: packages/yoti-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/packages/yoti-packages.yml
  title: ''
  type: Packages
  url: packages/yoti-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yoti.com/
- group: auth
  title: ''
  type: Security
  url: https://www.yoti.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.yoti.com/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/scopes/yoti-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/yoti-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/security/yoti-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/yoti-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yoti/refs/heads/main/security/yoti-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yoti-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yoti.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yoti.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.yoti.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.yoti.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.yoti.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.yoti.com/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://www.yoti.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.yoti.com/contact/business/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yoti.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yoti.com/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developers.yoti.com/mcp
  - status: 403
    url: https://cdn.aws.yoti.com/mcp
  - status: 200
    url: https://www.yoti.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Yoti provides a digital identity platform that enables businesses to verify users, issue digital ID wallets, and comply with age verification, KYC, and AML regulations. Their APIs cover identity verification, age checks, digital signatures, and trust services, supporting web, mobile, and in‑branch integrations across multiple languages and SDKs.
image: https://cdn.aws.yoti.com/wp-content/uploads/Yoti-site-image_1200x675.jpg
json_schemas:
- name: PostAccountsAccountidModerationsRequest
  property_count: 15
  slug: yoti-post-accounts-accountid-moderations-request
- name: PostAiV1V1IdRequest
  property_count: 4
  slug: yoti-post-ai-v1-v1-id-request
- name: PostApiV1SessionsRequest
  property_count: 1
  slug: yoti-post-api-v1-sessions-request
- name: PostApiV1SessionsResponse
  property_count: 4
  slug: yoti-post-api-v1-sessions-response
- name: PostPoaV1VerifyRequest
  property_count: 6
  slug: yoti-post-poa-v1-verify-request
- name: PostPoaV1VerifyResponse
  property_count: 5
  slug: yoti-post-poa-v1-verify-response
jsonld:
- class_count: 9
  name: Yoti Context
  property_count: 31
  slug: yoti-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.yoti.com.
  name: Yoti MCP Server
  slug: yoti-mcp-yml
modified: '2026-10-14'
name: Yoti
nav: Providers
network: true
overview: 'Yoti is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AI API, OAuth API, and 4 more. Tagged areas include Company, Identity, Verification, DigitalID, and SDK.


  The Yoti catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yoti''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Yoti API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: yoti-rules
scopes:
- name: Yoti Scopes
  scope_count: 2
  slug: yoti-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 25.7
    developer_ergonomics: 71.4
    discoverability: 73.3
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Yoti Authentication
  slug: yoti-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Yoti Domain Security
  slug: yoti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yoti Trust Center
  slug: yoti-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: yoti
tags:
- Company
- Identity
- Verification
- DigitalID
- SDK
website: https://www.yoti.com
---
