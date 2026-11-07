---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 3
  name: Abm Dev Agentic Access
  operation_count: 70
  slug: abm-dev-agentic-access
  summary_line: 70 operations · 36 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Orchestrate multi-step outreach campaigns that combine people-finding, enrichment, and CRM writeback
  name: abm-dev Campaigns API
  slug: abm-dev-campaigns-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: CRM integration configuration and field mappings
  name: abm-dev CRM API
  slug: abm-dev-crm-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Core enrichment operations - enrich persons and companies with data from multiple sources
  name: abm-dev Enrichment API
  slug: abm-dev-enrichment-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Global enrichment settings — source priority, auto-approval, writeback behavior
  name: abm-dev Enrichment Config API
  slug: abm-dev-enrichment-config-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Configure which enrichment fields are enabled, required, or mapped to CRM properties
  name: abm-dev Field Configuration API
  slug: abm-dev-field-configuration-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: System health monitoring
  name: abm-dev Health API
  slug: abm-dev-health-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Account and workspace management
  name: abm-dev Organization API
  slug: abm-dev-organization-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Find decision-makers at target companies by role — powered by multi-source search and optional enrichment
  name: abm-dev People Finder API
  slug: abm-dev-people-finder-api
- baseURL: https://api.abm.dev
  baseurl_source: declared
  description: Subscribe to real-time event notifications for enrichments, campaigns, and system events
  name: abm-dev Webhooks API
  slug: abm-dev-webhooks-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: Security
  url: https://abm.dev/security
- group: agent
  href: https://artifacts.apis.io/abm-dev/agentic-access/abm-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abm-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/abm-dev/rules/abm-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/abm-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/abm-dev/json-ld/abm-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/abm-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/abm-dev/vocabulary/abm-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abm-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/abm-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/abm-dev/data-model/abm-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abm-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/abm-dev/authentication/abm-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abm-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/abm-dev/errors/abm-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/abm-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/abm-dev/conformance/abm-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abm-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abm-dev/llms/abm-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abm-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/abm-dev/well-known/abm-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abm-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/abm-dev/well-known/abm-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abm-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/abm-dev/hosts/abm-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abm-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/abm-dev/vendors/abm-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abm-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/abm-dev/packages/abm-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/abm-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/abm-dev/packages/abm-dev-packages.yml
  title: ''
  type: Packages
  url: packages/abm-dev-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://abm.dev/sign-up
- group: start
  title: ''
  type: Sandbox
  url: https://abm.dev/dashboard/playground
- group: auth
  href: https://artifacts.apis.io/abm-dev/security/abm-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/abm-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/abm-dev/security/abm-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abm-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abm.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://abm.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://abm.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://abm.dev/docs
- group: operate
  title: ''
  type: Support
  url: https://abm.dev/help
- group: company
  title: ''
  type: Blog
  url: https://abm.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abm-dev-git
- group: commercial
  title: ''
  type: Pricing
  url: https://abm.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abm.dev/privacy
created: '2026-10-30'
description: ABM.dev provides an account‑based marketing API designed for AI agents, delivering searchable, enriched B2B person and company data with source citations and confidence scores. The platform offers a single endpoint to search, enrich, and create outreach actions, supporting streaming results via SSE and integrating with tools like LinkedIn, Hunter, Perplexity, and Tavily. Public beta is available with flexible pricing per enrichment. The service aims to automate personalized marketing at scale for marketers, developers, and autonomous agents.
image: https://abm.dev/logo.png
json_schemas:
- name: ApiKeySummary
  property_count: 14
  slug: abm-dev-api-key-summary
- name: CreateApiKeyResponse
  property_count: 8
  slug: abm-dev-create-api-key-response
- name: EnrichmentConfiguration
  property_count: 6
  slug: abm-dev-enrichment-configuration
- name: PersonFinderCandidate
  property_count: 10
  slug: abm-dev-person-finder-candidate
- name: PersonFinderJob
  property_count: 12
  slug: abm-dev-person-finder-job
- name: SignupOrganizationResponse
  property_count: 8
  slug: abm-dev-signup-organization-response
jsonld:
- class_count: 13
  name: Abm Dev Context
  property_count: 85
  slug: abm-dev-context
layout: provider
modified: '2026-10-30'
name: abm-dev
nav: Providers
network: true
overview: 'abm-dev publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Campaigns API, CRM API, Enrichment API, and 6 more. Tagged areas include Account Based Marketing, AI Agents, Data Enrichment, B2B, and Marketing API.


  The abm-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  abm-dev''s developer surface includes authentication, signup flow, sandbox, documentation, API reference, getting-started guide, support, and 23 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: abm-dev API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: abm-dev-rules
scopes:
- name: Abm Dev Scopes
  scope_count: 0
  slug: abm-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 46.9
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/abm-dev/abm-dev-2026-11-03T120142.png
security:
- kind: authentication
  name: Abm Dev Authentication
  slug: abm-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Abm Dev Domain Security
  slug: abm-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Abm Dev Vulnerability Disclosure
  slug: abm-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enrichment
  slug: abm-dev-enrichment
slug: abm-dev
tags:
- Account Based Marketing
- AI Agents
- Data Enrichment
- B2B
- Marketing API
website: https://abm.dev/
---
