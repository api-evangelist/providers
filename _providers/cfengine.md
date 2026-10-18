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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-17'
api_count: 10
apis:
- description: API reference for Cfengine automation platform
  name: Cfengine API
  slug: cfengine-api-2
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Ai API from Cfengine — 1 operation(s) for ai.
  name: Cfengine AI API
  slug: cfengine-ai-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Build API from Cfengine — 9 operation(s) for build.
  name: Cfengine Build API
  slug: cfengine-build-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Cfengine API API from Cfengine — 1 operation(s) for cfengine api.
  name: Cfengine Cfengine API
  slug: cfengine-cfengine-api-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Cmdb API from Cfengine — 3 operation(s) for cmdb.
  name: Cfengine Cmdb API
  slug: cfengine-cmdb-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Hosts API from Cfengine — 6 operation(s) for hosts.
  name: Cfengine Hosts API
  slug: cfengine-hosts-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Inventory API from Cfengine — 2 operation(s) for inventory.
  name: Cfengine Inventory API
  slug: cfengine-inventory-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Rbac API from Cfengine — 1 operation(s) for rbac.
  name: Cfengine Rbac API
  slug: cfengine-rbac-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The Role API from Cfengine — 2 operation(s) for role.
  name: Cfengine Role API
  slug: cfengine-role-api
- baseURL: https://hub.cfengine.com
  baseurl_source: declared
  description: The User API from Cfengine — 2 operation(s) for user.
  name: Cfengine User API
  slug: cfengine-user-api
artifact_total: 22
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/rules/cfengine-rules.yml
  title: ''
  type: Spectral
  url: rules/cfengine-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/json-ld/cfengine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cfengine-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/vocabulary/cfengine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cfengine-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/data-model/cfengine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cfengine-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/cli/cfengine-cli.yml
  title: ''
  type: CLI
  url: cli/cfengine-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/changelog/cfengine-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cfengine-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cfengine.com/solutions/security-automation/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/authentication/cfengine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cfengine-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/conformance/cfengine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cfengine-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/well-known/cfengine-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cfengine-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/well-known/cfengine-northerntech-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cfengine-northerntech-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/well-known/cfengine-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cfengine-docs-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/well-known/cfengine-build-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cfengine-build-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/well-known/cfengine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cfengine-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/hosts/cfengine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfengine-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://cfengine.com/tags/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cfengine
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cfengine.com/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cfengine.com/docs/lts/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cfengine.com/docs/lts/reference/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/security/cfengine-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cfengine-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/security/cfengine-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cfengine-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfengine/refs/heads/main/security/cfengine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfengine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cfengine.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cfengine.com
- group: company
  title: ''
  type: Blog
  url: https://cfengine.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cfengine.com/docs/lts/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://cfengine.com/contact
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI or other machine‑readable contract was found on the API host or documentation site.
  evidence:
  - status: 0
    url: https://api.cfengine.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cfengine provides infrastructure automation, security, and compliance solutions for large-scale environments. Offering both open source and commercial editions, it enables configuration management, CI/CD integration, and policy compliance across Linux and Windows systems. The platform includes AI‑assisted insights, extensive policy libraries, and a web UI for monitoring and reporting, serving enterprises worldwide.
image: https://cfengine.com/images/previews/logo_wide_opengraph.png
json_schemas:
- name: DeleteApiBuildProjects1ModulesAutorunResponse
  property_count: 17
  slug: cfengine-delete-api-build-projects1-modules-autorun-response
- name: GetApiBuildBuildidResponse
  property_count: 17
  slug: cfengine-get-api-build-buildid-response
- name: GetApiBuildModulesAutorunResponse
  property_count: 16
  slug: cfengine-get-api-build-modules-autorun-response
- name: GetApiBuildModulesAutorun100Response
  property_count: 16
  slug: cfengine-get-api-build-modules-autorun100-response
- name: PatchApiBuildProjects1ModulesAutorunResponse
  property_count: 17
  slug: cfengine-patch-api-build-projects1-modules-autorun-response
- name: PostApiBuildProjects1ModulesAutorunResponse
  property_count: 17
  slug: cfengine-post-api-build-projects1-modules-autorun-response
jsonld:
- class_count: 45
  name: Cfengine Context
  property_count: 68
  slug: cfengine-context
layout: provider
modified: '2026-10-07'
name: Cfengine
nav: Providers
network: true
overview: 'Cfengine is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including AI API, Build API, Cfengine API, and 7 more. Tagged areas include Company, Automation, Infrastructure, Security, and Compliance.


  The Cfengine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cfengine''s developer surface includes CLI, changelog, authentication, API reference, documentation, engineering blog, getting-started guide, and 21 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cfengine API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: cfengine-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 64.3
    discoverability: 62.5
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cfengine Authentication
  slug: cfengine-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cfengine Domain Security
  slug: cfengine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cfengine Vulnerability Disclosure
  slug: cfengine-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cfengine Trust Center
  slug: cfengine-trust-center
  summary_line: HIPAA, GDPR
slug: cfengine
tags:
- Company
- Automation
- Infrastructure
- Security
- Compliance
website: https://cfengine.com
---
