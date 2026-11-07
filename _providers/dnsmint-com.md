---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DNSMint turns an IP address into a stable hostname on a domain we operate, served by our authoritative DNS.
  name: DNSMint API
  slug: dnsmint-api
- baseURL: https://dnsmint.com/api
  baseurl_source: declared
  description: DNSMint turns an IP address into a stable hostname on a domain we operate, served by our authoritative DNS. Register an IP with one call, point your ACME client at the hostname, and update the IP when
  name: DNSMint API API
  slug: dnsmint-api-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/dnsmint-com/rules/dnsmint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dnsmint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dnsmint-com/json-ld/dnsmint-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dnsmint-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dnsmint-com/vocabulary/dnsmint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dnsmint-com-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/dnsmint-com/plans/dnsmint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dnsmint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dnsmint-com/data-model/dnsmint-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dnsmint-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dnsmint-com/changelog/dnsmint-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dnsmint-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dnsmint-com/authentication/dnsmint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dnsmint-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dnsmint-com/lifecycle/dnsmint-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dnsmint-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dnsmint-com/errors/dnsmint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dnsmint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dnsmint-com/conformance/dnsmint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dnsmint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dnsmint-com/llms/dnsmint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dnsmint-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dnsmint-com/mcp/dnsmint-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dnsmint-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dnsmint-com/well-known/dnsmint-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dnsmint-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dnsmint-com/well-known/dnsmint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dnsmint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dnsmint-com/hosts/dnsmint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dnsmint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dnsmint-com/vendors/dnsmint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dnsmint-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dnsmint.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://dnsmint.com/status
- group: auth
  title: ''
  type: Security
  url: https://dnsmint.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dnsmint.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dnsmint.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dnsmint.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dnsmint
- group: operate
  title: ''
  type: ChangeLog
  url: https://dnsmint.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://dnsmint.com/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://dnsmint.com/api-reference
- group: auth
  href: https://artifacts.apis.io/dnsmint-com/security/dnsmint-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dnsmint-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dnsmint-com/security/dnsmint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dnsmint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dnsmint.com/
created: '2026-11-05'
description: DNSMint provides programmable DNS identities for machines, agents, and infrastructure. Your agent mints its own HTTPS endpoint on a dedicated domain with a single API call, eliminating the need for a registrar, zone configuration, or human intervention. This service enables automated, secure, and scalable DNS management for cloud-native applications and IoT devices, simplifying network operations and enhancing reliability.
image: https://dnsmint.com/og.png
json_schemas:
- name: CreateHostnameRequest
  property_count: 6
  slug: dnsmint-com-create-hostname-request
- name: CreateRecordRequest
  property_count: 17
  slug: dnsmint-com-create-record-request
- name: HostView
  property_count: 5
  slug: dnsmint-com-host-view
- name: ManagedCertificate
  property_count: 9
  slug: dnsmint-com-managed-certificate
- name: ProvisioningStatus
  property_count: 5
  slug: dnsmint-com-provisioning-status
- name: RegisterIpRequest
  property_count: 2
  slug: dnsmint-com-register-ip-request
jsonld:
- class_count: 23
  name: Dnsmint Com Context
  property_count: 79
  slug: dnsmint-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at dnsmint.com.
  name: DNSMint MCP Server
  slug: dnsmint-com-mcp-yml
modified: '2026-11-05'
name: DNSMint
nav: Providers
network: true
overview: 'DNSMint publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include DNS, Automation, Infrastructure, and Cloud.


  The DNSMint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DNSMint''s developer surface includes changelog, authentication, pricing, getting-started guide, API reference, and 24 more developer resources.'
plans:
- name: Dnsmint Com Plans Pricing
  plan_count: 2
  slug: dnsmint-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: DNSMint API Rules
  rule_count: 57
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 7
  slug: dnsmint-com-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 50.7
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dnsmint Com Authentication
  slug: dnsmint-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dnsmint Com Domain Security
  slug: dnsmint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dnsmint Com Vulnerability Disclosure
  slug: dnsmint-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dnsmint-com
tags:
- DNS
- Automation
- Infrastructure
- Cloud
website: https://dnsmint.com/
---
