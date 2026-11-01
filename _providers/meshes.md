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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Meshes API provides endpoints for managing integrations, workspaces, and webhook deliveries.
  name: Meshes API
  slug: meshes-api-2
- baseURL: https://events.meshes.io
  baseurl_source: declared
  description: 'Meshes API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Meshes API
  slug: meshes-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/meshes/plans/meshes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meshes-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/meshes/rules/meshes-rules.yml
  title: ''
  type: Spectral
  url: rules/meshes-rules.yml
- group: design
  href: https://artifacts.apis.io/meshes/json-ld/meshes-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meshes-context.jsonld
- group: design
  href: https://artifacts.apis.io/meshes/vocabulary/meshes-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meshes-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/meshes/data-model/meshes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meshes-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://meshes.io/security
- group: auth
  href: https://artifacts.apis.io/meshes/authentication/meshes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meshes-authentication.yml
- group: design
  href: https://artifacts.apis.io/meshes/conformance/meshes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meshes-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meshes/llms/meshes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meshes-llms.txt
- group: auth
  href: https://artifacts.apis.io/meshes/well-known/meshes-meshes-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/meshes-meshes-security.txt
- group: agent
  href: https://artifacts.apis.io/meshes/well-known/meshes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meshes-well-known.yml
- group: other
  href: https://artifacts.apis.io/meshes/hosts/meshes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meshes-hosts.yml
- group: other
  href: https://artifacts.apis.io/meshes/vendors/meshes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meshes-vendors.yml
- group: build
  href: https://artifacts.apis.io/meshes/packages/meshes-packages.yml
  title: ''
  type: SDKs
  url: packages/meshes-packages.yml
- group: build
  href: https://artifacts.apis.io/meshes/packages/meshes-packages.yml
  title: ''
  type: Packages
  url: packages/meshes-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://meshes.io/integrations/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://meshes.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://meshes.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://meshes.io/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meshes.dev/openapi
- group: auth
  href: https://artifacts.apis.io/meshes/security/meshes-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/meshes-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/meshes/security/meshes-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meshes-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/meshes/security/meshes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meshes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meshes.io/
- group: docs
  title: ''
  type: Documentation
  url: https://meshes.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://meshes.io/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://meshes.io/docs/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://meshes.io/contact
- group: company
  title: ''
  type: Blog
  url: https://meshes.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mesheshq
- group: commercial
  title: ''
  type: Pricing
  url: https://meshes.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://meshes.io/auth/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meshes.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meshes.io/privacy-policy
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on api.meshes.io or meshes.io.
  evidence:
  - status: 404
    url: https://api.meshes.io/openapi.json
  - status: 404
    url: https://api.meshes.io/openapi.yaml
  - status: 404
    url: https://api.meshes.io/swagger.json
  - status: 404
    url: https://meshes.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Meshes provides an embedded integration platform as a service (iPaaS) enabling SaaS applications to easily connect, route, and manage outbound integrations. The platform offers features such as multi‑tenant workspaces, fan‑out routing, retry handling, webhook support, and detailed delivery history. Meshes targets product teams building customer‑facing SaaS solutions that need to integrate with services like CRM, Slack, payment processors, and more, reducing the complexity of building and maintaining custom integration code. The service includes a developer portal, comprehensive documentation, API reference, pricing details, and support resources, positioning Meshes as a modern alternative to traditional integration tools.
image: https://meshes.io/images/meshes-social-image.png
json_schemas:
- name: GetApiV1SessionsResponse
  property_count: 2
  slug: meshes-get-api-v1-sessions-response
- name: PostApiV1RulesRequest
  property_count: 4
  slug: meshes-post-api-v1-rules-request
- name: PostApiV1SessionsRequest
  property_count: 11
  slug: meshes-post-api-v1-sessions-request
- name: PostApiV1SessionsResponse
  property_count: 9
  slug: meshes-post-api-v1-sessions-response
- name: PostApiV1SessionsSessionidRefreshResponse
  property_count: 5
  slug: meshes-post-api-v1-sessions-sessionid-refresh-response
jsonld:
- class_count: 5
  name: Meshes Context
  property_count: 21
  slug: meshes-context
layout: provider
modified: '2026-10-18'
name: Meshes
nav: Providers
network: true
overview: 'Meshes is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, iPaaS, Software-as-a-Service, and Integration.


  The Meshes catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meshes'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Meshes Plans Pricing
  plan_count: 5
  slug: meshes-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Meshes API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: meshes-rules
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 64.3
    discoverability: 57.1
    operational_transparency: 55.3
  previous_composite: 57.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Meshes Authentication
  slug: meshes-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Meshes Domain Security
  slug: meshes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Meshes Vulnerability Disclosure
  slug: meshes-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Meshes Trust Center
  slug: meshes-trust-center
  summary_line: SOC 2, GDPR
slug: meshes
tags:
- Company
- iPaaS
- Software-as-a-Service
- Integration
website: https://meshes.io/
---
