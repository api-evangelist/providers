---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Cirra AI provides a Salesforce Admin Model Context Protocol (MCP) server accessible via its documentation site.
  name: Cirra AI API
  slug: cirra-ai-api-2
- baseURL: https://mcp.cirra.ai
  baseurl_source: declared
  description: 'Cirra AI API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cirra AI API
  slug: cirra-ai-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/cirra-ai/plans/cirra-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cirra-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cirra-ai/rules/cirra-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/cirra-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/cirra-ai/json-ld/cirra-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cirra-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/cirra-ai/vocabulary/cirra-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cirra-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cirra-ai/data-model/cirra-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cirra-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cirra-ai/changelog/cirra-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cirra-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cirra.ai/
- group: auth
  href: https://artifacts.apis.io/cirra-ai/security/cirra-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cirra-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/cirra-ai/conformance/cirra-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cirra-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cirra-ai/llms/cirra-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cirra-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/cirra-ai/well-known/cirra-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cirra-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/cirra-ai/well-known/cirra-ai-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cirra-ai-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/cirra-ai/well-known/cirra-ai-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cirra-ai-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/cirra-ai/well-known/cirra-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cirra-ai-app-security.txt
- group: auth
  href: https://artifacts.apis.io/cirra-ai/well-known/cirra-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cirra-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/cirra-ai/well-known/cirra-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cirra-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cirra-ai/hosts/cirra-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cirra-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cirra-ai/vendors/cirra-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cirra-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cirra.ai/legal/tos/
- group: start
  title: ''
  type: SignUp
  url: https://cirra.ai/sign-up/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cirra.ai/legal/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cirra.ai/mcp-server/setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cirra.ai/
- group: auth
  href: https://artifacts.apis.io/cirra-ai/security/cirra-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cirra-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cirra-ai/security/cirra-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cirra-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cirra-ai/security/cirra-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cirra-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cirra.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://cirra.ai/pricing/
- group: company
  title: ''
  type: About
  url: https://cirra.ai/about/
- group: company
  title: ''
  type: Blog
  url: https://cirra.ai/blog/
coverage:
  checked: '2026-11-04'
  detail: Documentation is served at https://docs.cirra.ai/ but is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.cirra.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Cirra AI provides the first commercial Salesforce Admin Model Context Protocol (MCP) server, enabling AI assistants like Claude, ChatGPT, and other MCP‑compatible tools to configure and manage Salesforce orgs through natural language conversation. It connects via Salesforce OAuth, supports read and write operations, offers guardrails, credit‑based usage, team plans, and integrates with tools such as Jira, all while providing audit trails and security controls for admins.
image: https://cirra.ai/images/og-image.png
json_schemas:
- name: PostRegisterRequest
  property_count: 5
  slug: cirra-ai-post-register-request
jsonld:
- class_count: 1
  name: Cirra Ai Context
  property_count: 5
  slug: cirra-ai-context
layout: provider
modified: '2026-11-03'
name: Cirra AI
nav: Providers
network: true
overview: 'Cirra AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Salesforce, MCP, and Admin.


  The Cirra AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cirra AI''s developer surface includes changelog, signup flow, getting-started guide, documentation, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Cirra Ai Plans Pricing
  plan_count: 3
  slug: cirra-ai-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Cirra AI API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: cirra-ai-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cirra Ai Domain Security
  slug: cirra-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cirra Ai Vulnerability Disclosure
  slug: cirra-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cirra Ai Trust Center
  slug: cirra-ai-trust-center
  summary_line: SOC 2
slug: cirra-ai
tags:
- Company
- Artificial Intelligence
- Salesforce
- MCP
- Admin
- Software-as-a-Service
website: https://cirra.ai/
---
