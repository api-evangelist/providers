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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 2
  name: Capgo App Agentic Access
  operation_count: 30
  slug: capgo-app-agentic-access
  summary_line: 30 operations · 18 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Capgo API key management.
  name: Capgo API Keys API
  slug: capgo-app-api-keys-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Application inventory and settings.
  name: Capgo Apps API
  slug: capgo-app-apps-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Live update bundle registration, metadata, and channel assignment.
  name: Capgo Bundles API
  slug: capgo-app-bundles-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Live update rollout channels.
  name: Capgo Channels API
  slug: capgo-app-channels-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Device overrides and device inventory.
  name: Capgo Devices API
  slug: capgo-app-devices-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Organization member invitations, roles, and removals.
  name: Capgo Members API
  slug: capgo-app-members-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: Organization CRUD and metadata.
  name: Capgo Organizations API
  slug: capgo-app-organizations-api
- baseURL: https://api.capgo.app
  baseurl_source: declared
  description: App, organization, user, and bundle usage analytics.
  name: Capgo Statistics API
  slug: capgo-app-statistics-api
artifact_total: 24
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://capgo.app/docs/getting-started/quickstart
- group: agent
  href: https://artifacts.apis.io/capgo-app/agentic-access/capgo-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/capgo-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/capgo-app/plans/capgo-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capgo-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/capgo-app/rules/capgo-app-rules.yml
  title: ''
  type: Spectral
  url: rules/capgo-app-rules.yml
- group: design
  href: https://artifacts.apis.io/capgo-app/json-ld/capgo-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capgo-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/capgo-app/vocabulary/capgo-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capgo-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/capgo-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/capgo-app/data-model/capgo-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capgo-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/capgo-app/cli/capgo-app-cli.yml
  title: ''
  type: CLI
  url: cli/capgo-app-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.capgo.app/
- group: design
  href: https://artifacts.apis.io/capgo-app/errors/capgo-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/capgo-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/capgo-app/conformance/capgo-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capgo-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capgo-app/llms/capgo-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capgo-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/capgo-app/well-known/capgo-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capgo-app-security.txt
- group: agent
  href: https://artifacts.apis.io/capgo-app/well-known/capgo-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capgo-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/capgo-app/hosts/capgo-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capgo-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/capgo-app/vendors/capgo-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capgo-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capgo.app/tos/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.capgo.app/
- group: auth
  title: ''
  type: Security
  url: https://capgo.app/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capgo.app/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://capgo.app/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://capgo.app/articles/category/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cap-go
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Cap-go/capgo.app/releases/tag/cli-8.99.1
- group: start
  title: ''
  type: SignUp
  url: https://capgo.app/register
- group: auth
  href: https://artifacts.apis.io/capgo-app/scopes/capgo-app-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/capgo-app-scopes.yml
- group: auth
  href: https://artifacts.apis.io/capgo-app/authentication/capgo-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capgo-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/capgo-app/security/capgo-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/capgo-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/capgo-app/security/capgo-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/capgo-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/capgo-app/security/capgo-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capgo-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capgo.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://capgo.app/tools/
- group: docs
  title: ''
  type: Documentation
  url: https://capgo.app/docs/public-api/
- group: docs
  title: ''
  type: APIReference
  url: https://capgo.app/.well-known/capgo-public-api-openapi.json
- group: operate
  title: ''
  type: Support
  url: https://capgo.app/contact
- group: company
  title: ''
  type: Blog
  url: https://capgo.app/blog
created: '2026-11-04'
description: Capgo provides a platform to build Capacitor and Ionic apps using AI agents, offering features such as native iOS and Android builds, store publishing, live updates, and integration with MCP skills. The service enables developers to streamline app development and deployment with AI-powered assistance, targeting modern mobile app workflows.
image: https://capgo.app/capgo_social.png
json_schemas:
- name: ApiKeyCreate
  property_count: 6
  slug: capgo-app-api-key-create
- name: BundleCreate
  property_count: 4
  slug: capgo-app-bundle-create
- name: Bundle
  property_count: 10
  slug: capgo-app-bundle
- name: ChannelSet
  property_count: 12
  slug: capgo-app-channel-set
- name: MemberCreate
  property_count: 3
  slug: capgo-app-member-create
- name: OrganizationUpdate
  property_count: 4
  slug: capgo-app-organization-update
jsonld:
- class_count: 38
  name: Capgo App Context
  property_count: 71
  slug: capgo-app-context
layout: provider
modified: '2026-11-04'
name: Capgo
nav: Providers
network: true
overview: 'Capgo publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, Bundles API, and 5 more. Tagged areas include Company, Artificial Intelligence, Mobile, Development, and Capacitor.


  The Capgo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capgo''s developer surface includes getting-started guide, CLI, pricing, changelog, signup flow, authentication, documentation, and 30 more developer resources.'
plans:
- name: Capgo App Plans Pricing
  plan_count: 8
  slug: capgo-app-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Capgo API Rules
  rule_count: 66
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 5
  slug: capgo-app-rules
scopes:
- name: Capgo App Scopes
  scope_count: 1
  slug: capgo-app-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 43.5
    discoverability: 67.0
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Capgo App Authentication
  slug: capgo-app-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Capgo App Domain Security
  slug: capgo-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Capgo App Vulnerability Disclosure
  slug: capgo-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Capgo App Trust Center
  slug: capgo-app-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: get-organizations
  slug: capgo-app-get-orgs
slug: capgo-app
tags:
- Company
- Artificial Intelligence
- Mobile
- Development
- Capacitor
website: https://capgo.app/
---
