---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Rdapapi Io Agentic Access
  operation_count: 9
  slug: rdapapi-io-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Look up an Autonomous System Number.
  name: rdapapi-io ASN API
  slug: rdapapi-io-asn-api
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Look up one domain, or up to 10 in a single call with the bulk endpoint.
  name: rdapapi-io Domain API
  slug: rdapapi-io-domain-api
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Look up a contact or organization by RDAP handle.
  name: rdapapi-io Entity API
  slug: rdapapi-io-entity-api
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Uptime checks.
  name: rdapapi-io Health API
  slug: rdapapi-io-health-api
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Look up an IP address or CIDR block.
  name: rdapapi-io IP API
  slug: rdapapi-io-ip-api
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Look up a nameserver host record, for the registries that publish one.
  name: rdapapi-io Nameserver API
  slug: rdapapi-io-nameserver-api
- baseURL: https://rdapapi.io/api/v1
  baseurl_source: declared
  description: Check which TLDs are supported, in bulk or one at a time.
  name: rdapapi-io TLDs API
  slug: rdapapi-io-tlds-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/rdapapi-io/agentic-access/rdapapi-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rdapapi-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/rdapapi-io/rate-limits/rdapapi-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rdapapi-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rdapapi-io/plans/rdapapi-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rdapapi-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rdapapi-io/rules/rdapapi-io-rules.yml
  title: ''
  type: Spectral
  url: rules/rdapapi-io-rules.yml
- group: design
  href: https://artifacts.apis.io/rdapapi-io/json-ld/rdapapi-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rdapapi-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/rdapapi-io/vocabulary/rdapapi-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rdapapi-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rdapapi-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rdapapi-io/data-model/rdapapi-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rdapapi-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/rdapapi-io/changelog/rdapapi-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rdapapi-io-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://rdapapi.io/toms
- group: auth
  href: https://artifacts.apis.io/rdapapi-io/authentication/rdapapi-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rdapapi-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/rdapapi-io/lifecycle/rdapapi-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rdapapi-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rdapapi-io/errors/rdapapi-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rdapapi-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rdapapi-io/conformance/rdapapi-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rdapapi-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rdapapi-io/llms/rdapapi-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rdapapi-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/rdapapi-io/well-known/rdapapi-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rdapapi-io-security.txt
- group: agent
  href: https://artifacts.apis.io/rdapapi-io/well-known/rdapapi-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rdapapi-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/rdapapi-io/hosts/rdapapi-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rdapapi-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/rdapapi-io/vendors/rdapapi-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rdapapi-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/rdapapi-io/packages/rdapapi-io-packages.yml
  title: ''
  type: Packages
  url: packages/rdapapi-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rdapapi.io
- group: build
  title: ''
  type: SDKs
  url: https://rdapapi.io/sdks
- group: auth
  href: https://artifacts.apis.io/rdapapi-io/security/rdapapi-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rdapapi-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rdapapi-io/security/rdapapi-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rdapapi-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rdapapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://rdapapi.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rdapapi.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://rdapapi.io/docs
- group: operate
  title: ''
  type: Support
  url: https://rdapapi.io/contact
- group: company
  title: ''
  type: Blog
  url: https://rdapapi.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://rdapapi.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rdapapi.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rdapapi.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://rdapapi.io/register
created: '2026-10-31'
description: RDAP API provides developers with a modern, JSON-native WHOIS replacement, delivering normalized domain registration data across over 1,200 top-level domains. It offers a 7‑day free trial and paid plans starting at $9 per month, enabling easy integration of domain lookup capabilities into applications without parsing raw WHOIS text.
image: https://rdapapi.io/og-image.jpg
json_schemas:
- name: AsnResponse
  property_count: 13
  slug: rdapapi-io-asn-response
- name: DomainResponse
  property_count: 11
  slug: rdapapi-io-domain-response
- name: EntityResponse
  property_count: 19
  slug: rdapapi-io-entity-response
- name: IpResponse
  property_count: 17
  slug: rdapapi-io-ip-response
- name: NameserverResponse
  property_count: 9
  slug: rdapapi-io-nameserver-response
- name: TldEntry
  property_count: 7
  slug: rdapapi-io-tld-entry
jsonld:
- class_count: 21
  name: Rdapapi Io Context
  property_count: 75
  slug: rdapapi-io-context
layout: provider
modified: '2026-10-31'
name: rdapapi-io
nav: Providers
network: true
overview: 'rdapapi-io publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including ASN API, Domain API, Entity API, and 4 more. Tagged areas include Company, RDAP, Domain, API, and Whois.


  The rdapapi-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  rdapapi-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Rdapapi Io Plans Pricing
  plan_count: 3
  slug: rdapapi-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Rdapapi Io Rate Limits
  slug: rdapapi-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: rdapapi-io API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 1
  slug: rdapapi-io-rules
scopes:
- name: Rdapapi Io Scopes
  scope_count: 0
  slug: rdapapi-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 65.4
    developer_ergonomics: 61.2
    discoverability: 66.1
    operational_transparency: 70.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rdapapi Io Authentication
  slug: rdapapi-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Rdapapi Io Domain Security
  slug: rdapapi-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Rdapapi Io Vulnerability Disclosure
  slug: rdapapi-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: rdapapi-io-main
  slug: rdapapi-io-main
slug: rdapapi-io
tags:
- Company
- RDAP
- Domain
- API
- Whois
website: https://rdapapi.io/
---
