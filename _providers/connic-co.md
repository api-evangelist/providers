---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: derived
    mcp_server: false
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
  score: 43.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST API for Connic AI agent platform
  name: Connic API
  slug: connic-api
- baseURL: https://api.connic.co
  baseurl_source: declared
  description: 'Public API for connic. Authenticate using an API key in the `Authorization: Bearer ` header. You can create and manage API keys in your [Project Settings](https://connic.co/projects?to=settings/cli).'
  name: connic API Public API
  slug: connic-api-public-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/connic-co/rules/connic-co-rules.yml
  title: ''
  type: Spectral
  url: rules/connic-co-rules.yml
- group: design
  href: https://artifacts.apis.io/connic-co/json-ld/connic-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/connic-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/connic-co/vocabulary/connic-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/connic-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/connic-co/conventions/connic-co-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/connic-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/connic-co/conventions/connic-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/connic-co-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/connic-co/plans/connic-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/connic-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/connic-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/connic-co/data-model/connic-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/connic-co-data-model.yml
- group: build
  href: https://artifacts.apis.io/connic-co/cli/connic-co-cli.yml
  title: ''
  type: CLI
  url: cli/connic-co-cli.yml
- group: auth
  href: https://artifacts.apis.io/connic-co/authentication/connic-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/connic-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/connic-co/errors/connic-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/connic-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/connic-co/conformance/connic-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/connic-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/connic-co/llms/connic-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connic-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/connic-co/well-known/connic-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connic-co-security.txt
- group: auth
  href: https://artifacts.apis.io/connic-co/well-known/connic-co-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connic-co-api-security.txt
- group: agent
  href: https://artifacts.apis.io/connic-co/well-known/connic-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connic-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/connic-co/hosts/connic-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connic-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/connic-co/vendors/connic-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connic-co-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://connic.co/marketplace/connectors/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connic.co/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.connic.co
- group: auth
  title: ''
  type: Security
  url: https://connic.co/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://connic.co/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/connic-org
- group: auth
  href: https://artifacts.apis.io/connic-co/security/connic-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/connic-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/connic-co/security/connic-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connic-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connic.co/
- group: docs
  title: ''
  type: Documentation
  url: https://connic.co/docs/v1
- group: docs
  title: ''
  type: APIReference
  url: https://connic.co/docs/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://connic.co/docs/v1/quickstart
- group: company
  title: ''
  type: Blog
  url: https://connic.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://connic.co/pricing
- group: operate
  title: ''
  type: Support
  url: https://connic.co/contact
created: '2026-11-04'
description: Connic is an AI agent platform that deploys, runs, and governs production agents written in YAML and Python. Based in Munich, it provides infrastructure for software teams to automate operational steps with AI agents, offering features like managed runtime, connectors, retrieval, models, and compliance tools. The platform includes a marketplace, documentation, pricing, and a blog, targeting enterprises seeking scalable AI agent solutions.
image: https://connic.co/og.png
json_schemas:
- name: ABTestResponse
  property_count: 38
  slug: connic-co-abtest-response
- name: AgentRunWithTraces
  property_count: 27
  slug: connic-co-agent-run-with-traces
- name: ComplianceIncidentResponse
  property_count: 28
  slug: connic-co-compliance-incident-response
- name: ComplianceTransparencyApplicationResponse
  property_count: 27
  slug: connic-co-compliance-transparency-application-response
- name: DeploymentListItemResponse
  property_count: 27
  slug: connic-co-deployment-list-item-response
- name: DeploymentResponse
  property_count: 26
  slug: connic-co-deployment-response
jsonld:
- class_count: 120
  name: Connic Co Context
  property_count: 377
  slug: connic-co-context
layout: provider
modified: '2026-11-04'
name: Connic
nav: Providers
network: true
overview: 'Connic publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Public API, and 1 more. Tagged areas include Company, Artificial Intelligence, Platform, Munich, and Automation.


  The Connic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Connic''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Connic Co Plans Pricing
  plan_count: 4
  slug: connic-co-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Connic API Rules
  rule_count: 64
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 13
  slug: connic-co-rules
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 49.4
    developer_ergonomics: 61.2
    discoverability: 66.1
    operational_transparency: 39.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Connic Co Authentication
  slug: connic-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Connic Co Domain Security
  slug: connic-co-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Connic Co Vulnerability Disclosure
  slug: connic-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: connic-co
tags:
- Company
- Artificial Intelligence
- Platform
- Munich
- Automation
website: https://connic.co/
---
