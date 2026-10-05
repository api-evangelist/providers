---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-10-04'
api_count: 6
apis:
- description: VS Code, JetBrains (IntelliJ, PhpStorm, etc.), and Eclipse plugins surfacing autocomplete, chat, and agentic workflows. Communicates with Tabnine's hosted or self-hosted backend over a proprietary pro
  name: Tabnine IDE Plugins
  slug: plugins
- description: Enterprise SKU with admin console (data analytics, model provisioning, context permissions, SSO), Enterprise Context Engine (codebase indexing), and flexible deployment (SaaS / VPC / Local / Air-Gappe
  name: Tabnine Enterprise (Admin Suite + Context Engine)
  slug: enterprise
- description: The Groups API from Tabnine — 2 operation(s) for groups.
  name: Tabnine Groups API
  slug: tabnine-groups-api
- description: The Main API from Tabnine — 12 operation(s) for main.
  name: Tabnine Main API
  slug: tabnine-main-api
- description: The Schemas API from Tabnine — 1 operation(s) for schemas.
  name: Tabnine Schemas API
  slug: tabnine-schemas-api
- description: The Users API from Tabnine — 2 operation(s) for users.
  name: Tabnine Users API
  slug: tabnine-users-api
artifact_total: 21
asyncapis:
- description: ''
  name: Tabnine Webhooks
  slug: tabnine-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/llms/tabnine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tabnine-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/well-known/tabnine-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tabnine-status-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/rules/tabnine-rules.yml
  title: ''
  type: Spectral
  url: rules/tabnine-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/json-ld/tabnine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tabnine-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/vocabulary/tabnine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tabnine-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/asyncapi/tabnine-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tabnine-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/data-model/tabnine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tabnine-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/changelog/tabnine-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tabnine-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tabnine.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/authentication/tabnine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tabnine-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/conformance/tabnine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tabnine-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/well-known/tabnine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tabnine-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/hosts/tabnine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tabnine-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/vendors/tabnine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tabnine-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tricentis.com/resources/tosca-cloud-ata-demo
- group: operate
  title: ''
  type: Support
  url: https://support.tabnine.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tabnine.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.tabnine.com/main/welcome/readme/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.tricentis.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.tricentis.com/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tabnine.com/main/administering-tabnine/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tabnine.com/main/getting-started/install
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/security/tabnine-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tabnine-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/security/tabnine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tabnine-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codota
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tabnine
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabnine.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/plans/tabnine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tabnine-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/rate-limits/tabnine-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tabnine-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/finops/tabnine-finops.yml
  title: ''
  type: FinOps
  url: finops/tabnine-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tabnine.com/blog/feed/
- group: company
  title: ''
  type: Website
  url: https://www.tabnine.com/
coverage:
  checked: '2026-10-04'
  detail: Documentation is served via Gitbook with no machine‑readable OpenAPI/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.tabnine.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-05-08'
description: Tabnine provides AI code completion, chat, and agentic workflows across IDEs and CLI, with strong support for SaaS, VPC, and air-gapped on-prem deployments. The Enterprise Context Engine indexes a customer's codebase, dependencies, and architecture. Tabnine's consumer surface is via IDE plugins (VS Code, JetBrains, Eclipse) and the Tabnine CLI; there is no general-purpose public REST inference API for end-developers.
finops:
- name: Tabnine Finops
  service_category: AI
  slug: tabnine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tabnine.png
json_schemas:
- name: GetGroupsIdResponse
  property_count: 2
  slug: tabnine-get-groups-id-response
- name: GetGroupsResponse
  property_count: 2
  slug: tabnine-get-groups-response
- name: GetUsersIdResponse
  property_count: 3
  slug: tabnine-get-users-id-response
- name: GetUsersResponse
  property_count: 3
  slug: tabnine-get-users-response
- name: PostGroupsResponse
  property_count: 2
  slug: tabnine-post-groups-response
- name: PostUsersResponse
  property_count: 4
  slug: tabnine-post-users-response
jsonld:
- class_count: 14
  name: Tabnine Context
  property_count: 4
  slug: tabnine-context
layout: provider
modified: '2026-05-08'
name: Tabnine
nav: Providers
network: true
overview: 'Tabnine publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Groups API, Main API, Schemas API, and 3 more. Tagged areas include Artificial Intelligence, Developer Tools, Code Completion, Self-Hosted, and Enterprise.


  The Tabnine catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Tabnine''s developer surface includes changelog, authentication, support, getting-started guide, documentation, engineering blog, and 26 more developer resources.'
plans:
- name: Tabnine Plans Pricing
  plan_count: 1
  slug: tabnine-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Tabnine Rate Limits
  slug: tabnine-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Tabnine API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: tabnine-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.8
    catalog_earned_first_party: 0.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 28.3
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 30.0
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 14.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/screenshots/tabnine-2026-06-20T194849.png
security:
- kind: authentication
  name: Tabnine Authentication
  slug: tabnine-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tabnine Domain Security
  slug: tabnine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tabnine Trust Center
  slug: tabnine-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tabnine
tags:
- Artificial Intelligence
- Developer Tools
- Code Completion
- Self-Hosted
- Enterprise
- Privacy
website: https://www.tabnine.com/
---
