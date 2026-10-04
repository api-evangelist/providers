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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-03'
api_count: 5
apis:
- baseURL: https://app.autify.com
  baseurl_source: declared
  description: The Autify Cli API from Autify — 2 operation(s) for autify cli.
  name: Autify Autify Cli API
  slug: autify-autify-cli-api
- baseURL: https://app.autify.com
  baseurl_source: declared
  description: The ~ API from Autify — 1 operation(s) for ~.
  name: Autify ~ API
  slug: autify-default-api
- baseURL: https://app.autify.com
  baseurl_source: declared
  description: The Payload API from Autify — 1 operation(s) for payload.
  name: Autify Payload API
  slug: autify-payload-api
- baseURL: https://app.autify.com
  baseurl_source: declared
  description: The Projects API from Autify — 3 operation(s) for projects.
  name: Autify Projects API
  slug: autify-projects-api
- baseURL: https://app.autify.com
  baseurl_source: declared
  description: The Workspaces API from Autify — 3 operation(s) for workspaces.
  name: Autify Workspaces API
  slug: autify-workspaces-api
artifact_total: 14
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/plans/autify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autify-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/rules/autify-rules.yml
  title: ''
  type: Spectral
  url: rules/autify-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/json-ld/autify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autify-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/vocabulary/autify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autify-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/data-model/autify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autify-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/cli/autify-cli.yml
  title: ''
  type: CLI
  url: cli/autify-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/changelog/autify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/autify-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/authentication/autify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autify-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/conformance/autify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autify-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/llms/autify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autify-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/well-known/autify-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autify-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/well-known/autify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autify-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/hosts/autify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autify-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/vendors/autify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autify-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autify.com/
- group: company
  title: ''
  type: Newsroom
  url: https://autify.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.autify.com/docs/release-notes
- group: company
  title: ''
  type: Blog
  url: https://autify.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.autify.com/docs/sso-feature
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autify/refs/heads/main/security/autify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.autify.com/v1/en
- group: commercial
  title: ''
  type: Pricing
  url: https://autify.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autify.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autify.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.autify.com/v1/en
coverage:
  checked: 2026-09-26
  detail: Autify's API documentation pages return only HTML/markdown without an OpenAPI or other machine-readable contract.
  evidence:
  - status: 0
    url: https://api.autify.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Autify provides an AI-powered test automation platform that enables teams to create, execute, and maintain automated tests for web, mobile, and desktop applications without code. The solution supports end‑to‑end testing, regression testing, and integrates with CI/CD pipelines, helping enterprises accelerate release cycles while ensuring quality.
image: https://cdn.prod.website-files.com/67220b7ba7c82c886f24b01d/672ca7458bb407b3e0757d2d_Autify%20Open%20Graph%20(1200x630).png
json_schemas:
- name: GetApiWorkspacesResponse
  property_count: 1
  slug: autify-get-api-workspaces-response
- name: GetApiWorkspacesWorkspaceidIdResponse
  property_count: 3
  slug: autify-get-api-workspaces-workspaceid-id-response
- name: PostApiWorkspacesWorkspaceidTestplansTestplanidRunRequest
  property_count: 2
  slug: autify-post-api-workspaces-workspaceid-testplans-testplanid-run-request
- name: PostApiWorkspacesWorkspaceidTestplansTestplanidRunResponse
  property_count: 1
  slug: autify-post-api-workspaces-workspaceid-testplans-testplanid-run-response
jsonld:
- class_count: 4
  name: Autify Context
  property_count: 6
  slug: autify-context
layout: provider
modified: '2026-09-26'
name: Autify
nav: Providers
network: true
overview: 'Autify publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Autify Cli API, ~ API, Payload API, and 2 more. Tagged areas include Company, Artificial Intelligence, Test Automation, No-Code, and Software-as-a-Service.


  The Autify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Autify''s developer surface includes CLI, changelog, authentication, engineering blog, getting-started guide, documentation, pricing, and 19 more developer resources.'
plans:
- name: Autify Plans Pricing
  plan_count: 6
  slug: autify-plans-pricing
random_paper: 20
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Autify API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: autify-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 47.6
    discoverability: 80.4
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Autify Authentication
  slug: autify-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Autify Domain Security
  slug: autify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autify
tags:
- Company
- Artificial Intelligence
- Test Automation
- No-Code
- Software-as-a-Service
website: https://autify.com/
---
