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
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.avo.app
  baseurl_source: declared
  description: 'Avo API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Avo API
  slug: avo-app-api
artifact_total: 11
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://www.avo.app/docs/index
- group: commercial
  href: https://artifacts.apis.io/avo-app/plans/avo-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avo-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avo-app/rules/avo-app-rules.yml
  title: ''
  type: Spectral
  url: rules/avo-app-rules.yml
- group: design
  href: https://artifacts.apis.io/avo-app/json-ld/avo-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avo-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/avo-app/vocabulary/avo-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avo-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avo-app/data-model/avo-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avo-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/avo-app/cli/avo-app-cli.yml
  title: ''
  type: CLI
  url: cli/avo-app-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.avo.app/security
- group: auth
  href: https://artifacts.apis.io/avo-app/authentication/avo-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avo-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/avo-app/conformance/avo-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avo-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avo-app/llms/avo-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avo-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/avo-app/well-known/avo-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avo-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/avo-app/hosts/avo-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avo-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/avo-app/vendors/avo-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avo-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/avo-app/packages/avo-app-packages.yml
  title: ''
  type: SDKs
  url: packages/avo-app-packages.yml
- group: build
  href: https://artifacts.apis.io/avo-app/packages/avo-app-packages.yml
  title: ''
  type: Packages
  url: packages/avo-app-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avo.app/l/terms
- group: auth
  title: ''
  type: Security
  url: https://www.avo.app/security
- group: start
  title: ''
  type: Sandbox
  url: https://www.avo.app/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avo.app/l/privacy
- group: start
  title: ''
  type: Login
  url: https://www.avo.app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avohq
- group: auth
  href: https://artifacts.apis.io/avo-app/security/avo-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avo-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/avo-app/security/avo-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avo-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avo.app
- group: docs
  title: ''
  type: Documentation
  url: https://www.avo.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avo.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.avo.app/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.avo.app/docs
created: '2026-10-29'
description: Avo provides a data governance platform that helps product teams design, implement, and monitor analytics tracking plans. Their solution enables unified tracking across teams, automated review workflows, and real‑time data quality monitoring, ensuring that every event is defined correctly, implemented accurately, and trusted everywhere. Avo’s AI‑assisted tools simplify schema management, observability, and integration with major analytics stacks, making data governance scalable and reliable for modern product organizations.
image: https://cdn.prod.website-files.com/65b671b80c07b825f14b65c6/693af61123c92524b2dc37fb_UPDATED%20Opengraph%20image.png
json_schemas:
- name: GetWorkspacesWorkspaceidInspectorIssuesIssueidVariationsResp
  property_count: 2
  slug: avo-app-get-workspaces-workspaceid-inspector-issues-issueid-variations-resp
- name: GetWorkspacesWorkspaceidInspectorIssuesV3IssueidResponse
  property_count: 17
  slug: avo-app-get-workspaces-workspaceid-inspector-issues-v3-issueid-response
- name: PostWorkspacesWorkspaceidBranchesMyBranchImportV1Request
  property_count: 1
  slug: avo-app-post-workspaces-workspaceid-branches-my-branch-import-v1-request
- name: PostWorkspacesWorkspaceidBranchesMyBranchImportV1Response
  property_count: 3
  slug: avo-app-post-workspaces-workspaceid-branches-my-branch-import-v1-response
jsonld:
- class_count: 4
  name: Avo App Context
  property_count: 22
  slug: avo-app-context
layout: provider
modified: '2026-10-29'
name: Avo
nav: Providers
network: true
overview: 'Avo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Governance, Analytics, AI, and SaaS.


  The Avo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Avo''s developer surface includes getting-started guide, CLI, authentication, sandbox, documentation, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Avo App Plans Pricing
  plan_count: 3
  slug: avo-app-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Avo API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: avo-app-rules
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 71.0
    catalog_earned_first_party: 12.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 19.7
    contract_quality: 23.6
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avo App Authentication
  slug: avo-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Avo App Domain Security
  slug: avo-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Avo App Trust Center
  slug: avo-app-trust-center
  summary_line: SOC 2, GDPR
slug: avo-app
tags:
- Company
- Data Governance
- Analytics
- AI
- SaaS
website: https://www.avo.app
---
