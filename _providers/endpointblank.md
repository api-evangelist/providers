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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-10-17'
api_count: 11
apis:
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Agent Oauth API from Bengal Technologies — 2 operation(s) for agent oauth.
  name: Bengal Technologies Agent Oauth API
  slug: endpointblank-agent-oauth-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Api Packages API from Bengal Technologies — 4 operation(s) for api packages.
  name: Bengal Technologies Api Packages API
  slug: endpointblank-api-packages-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Applications API from Bengal Technologies — 4 operation(s) for applications.
  name: Bengal Technologies Applications API
  slug: endpointblank-applications-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Authorize API from Bengal Technologies — 1 operation(s) for authorize.
  name: Bengal Technologies Authorize API
  slug: endpointblank-authorize-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Callback API from Bengal Technologies — 1 operation(s) for callback.
  name: Bengal Technologies Callback API
  slug: endpointblank-callback-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Clients API from Bengal Technologies — 11 operation(s) for clients.
  name: Bengal Technologies Clients API
  slug: endpointblank-clients-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Credentials API from Bengal Technologies — 1 operation(s) for credentials.
  name: Bengal Technologies Credentials API
  slug: endpointblank-credentials-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Endpoints API from Bengal Technologies — 1 operation(s) for endpoints.
  name: Bengal Technologies Endpoints API
  slug: endpointblank-endpoints-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Environments API from Bengal Technologies — 2 operation(s) for environments.
  name: Bengal Technologies Environments API
  slug: endpointblank-environments-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The Organization API from Bengal Technologies — 2 operation(s) for organization.
  name: Bengal Technologies Organization API
  slug: endpointblank-organization-api
- baseURL: https://app.endpointblank.com/api/v1
  baseurl_source: declared
  description: The .well Known API from Bengal Technologies — 1 operation(s) for .well known.
  name: Bengal Technologies .well Known API
  slug: endpointblank-well-known-api
artifact_total: 23
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/plans/endpointblank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/endpointblank-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/rules/endpointblank-rules.yml
  title: ''
  type: Spectral
  url: rules/endpointblank-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/json-ld/endpointblank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/endpointblank-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/vocabulary/endpointblank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/endpointblank-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/data-model/endpointblank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/endpointblank-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/conventions/endpointblank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/endpointblank-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/conventions/endpointblank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/endpointblank-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/authentication/endpointblank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/endpointblank-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/conformance/endpointblank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/endpointblank-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/well-known/endpointblank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/endpointblank-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/hosts/endpointblank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/endpointblank-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/packages/endpointblank-packages.yml
  title: ''
  type: SDKs
  url: packages/endpointblank-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/packages/endpointblank-packages.yml
  title: ''
  type: Packages
  url: packages/endpointblank-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://endpointblank.com/docs/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/scopes/endpointblank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/endpointblank-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/endpointblank/refs/heads/main/security/endpointblank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endpointblank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://endpointblank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://endpointblank.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://endpointblank.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://endpointblank.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://endpointblank.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://endpointblank.com/users/register
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://endpointblank.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Bengal Technologies provides a platform for API lifecycle management, enabling versioning, deprecation scheduling, and machine‑to‑machine authentication. Their portal lets developers register applications, obtain scoped credentials, and monitor usage across multiple API versions, with built‑in logging, alerts, and SDKs for popular languages. The service aims to simplify API governance without breaking existing clients.
image: https://endpointblank.com/images/og-default.png
json_schemas:
- name: DeleteClientsClientidEnvironmentsIdResponse
  property_count: 6
  slug: endpointblank-delete-clients-clientid-environments-id-response
- name: PostAgentOauthAgentoauthidRequest
  property_count: 4
  slug: endpointblank-post-agent-oauth-agentoauthid-request
- name: PostApiPackagesIdEndpointsResponse
  property_count: 6
  slug: endpointblank-post-api-packages-id-endpoints-response
- name: PostApplicationsApplicationidEnvironmentsResponse
  property_count: 6
  slug: endpointblank-post-applications-applicationid-environments-response
- name: PostClientsClientidCredentialsIdRotateResponse
  property_count: 8
  slug: endpointblank-post-clients-clientid-credentials-id-rotate-response
- name: PostClientsResponse
  property_count: 8
  slug: endpointblank-post-clients-response
jsonld:
- class_count: 48
  name: Endpointblank Context
  property_count: 24
  slug: endpointblank-context
layout: provider
modified: '2026-10-16'
name: Bengal Technologies
nav: Providers
network: true
overview: 'Bengal Technologies is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Agent Oauth API, Api Packages API, Applications API, and 8 more. Tagged areas include Company, API Management, Versioning, Authentication, and Monitoring.


  The Bengal Technologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bengal Technologies'' developer surface includes authentication, getting-started guide, documentation, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Endpointblank Plans Pricing
  plan_count: 5
  slug: endpointblank-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bengal Technologies API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: endpointblank-rules
scopes:
- name: Endpointblank Scopes
  scope_count: 0
  slug: endpointblank-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 28.5
    developer_ergonomics: 40.5
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Endpointblank Authentication
  slug: endpointblank-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Endpointblank Domain Security
  slug: endpointblank-domain-security
  summary_line: TLSv1.3 · HSTS
slug: endpointblank
tags:
- Company
- API Management
- Versioning
- Authentication
- Monitoring
website: https://endpointblank.com/
---
