---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Plesk simplifies the lives of web developers thanks to its integrated platform with full development and deployment capabilities.
  name: Plesk Developer API
  slug: plesk-developer-api
- baseURL: https://autoinstall.plesk.com
  baseurl_source: declared
  description: 'Plesk API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Plesk API
  slug: plesk-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/plesk/plans/plesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plesk-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/plesk/rules/plesk-rules.yml
  title: ''
  type: Spectral
  url: rules/plesk-rules.yml
- group: design
  href: https://artifacts.apis.io/plesk/json-ld/plesk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/plesk-context.jsonld
- group: design
  href: https://artifacts.apis.io/plesk/vocabulary/plesk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/plesk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/plesk/data-model/plesk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plesk-data-model.yml
- group: operate
  href: https://artifacts.apis.io/plesk/changelog/plesk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plesk-changelog.yml
- group: auth
  href: https://artifacts.apis.io/plesk/security/plesk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/plesk-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/plesk/conformance/plesk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plesk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/plesk/llms/plesk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plesk-llms.txt
- group: other
  href: https://artifacts.apis.io/plesk/hosts/plesk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plesk-hosts.yml
- group: other
  href: https://artifacts.apis.io/plesk/vendors/plesk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plesk-vendors.yml
- group: build
  href: https://artifacts.apis.io/plesk/packages/plesk-packages.yml
  title: ''
  type: SDKs
  url: packages/plesk-packages.yml
- group: build
  href: https://artifacts.apis.io/plesk/packages/plesk-packages.yml
  title: ''
  type: Packages
  url: packages/plesk-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.plesk.com/hc/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.plesk.com/release-notes/obsidian/change-log/
- group: auth
  href: https://artifacts.apis.io/plesk/security/plesk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/plesk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/plesk/security/plesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plesk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.plesk.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plesk.com/en-US/obsidian/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.plesk.com/en-US/obsidian/api-rpc/introduction.79358/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plesk.com/en-US/obsidian/
- group: company
  title: ''
  type: Blog
  url: https://www.plesk.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plesk
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plesk.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plesk.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plesk.com/legal/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec is published; attempts to fetch common spec URLs returned 404 or HTML pages.
  evidence:
  - status: 404
    url: https://plesk.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Plesk is a web hosting and server management platform that helps you manage websites, servers, security, and WordPress from one dashboard. It offers a WebOps platform for app, site and hosting management, providing tools for automation, scaling, and integration with cloud services. Plesk supports multiple operating systems and control panels, enabling hosting providers and developers to streamline deployments, manage DNS, email, and databases, and secure environments with built-in security features.
image: https://www.plesk.com/wp-content/uploads/2026/02/Plesk-screenshot_360.png
json_schemas:
- name: GetApiV2AuthKeysResponse
  property_count: 1
  slug: plesk-get-api-v2-auth-keys-response
- name: GetIdKeysResponse
  property_count: 3
  slug: plesk-get-id-keys-response
- name: PostApiV2ClientsRequest
  property_count: 6
  slug: plesk-post-api-v2-clients-request
jsonld:
- class_count: 3
  name: Plesk Context
  property_count: 10
  slug: plesk-context
layout: provider
modified: '2026-10-28'
name: Plesk
nav: Providers
network: true
overview: 'Plesk is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Hosting, Server Management, Control Panel, and Automation.


  The Plesk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Plesk''s developer surface includes changelog, support, documentation, API reference, getting-started guide, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Plesk Plans Pricing
  plan_count: 3
  slug: plesk-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Plesk Rate Limits
  slug: plesk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Plesk API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: plesk-rules
scopes:
- name: Plesk Scopes
  scope_count: 0
  slug: plesk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Plesk Authentication
  slug: plesk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Plesk Domain Security
  slug: plesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plesk Vulnerability Disclosure
  slug: plesk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: plesk
tags:
- Company
- Web Hosting
- Server Management
- Control Panel
- Automation
- WordPress
website: https://plesk.com/
---
