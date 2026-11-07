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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 6
  name: Bike4Mind Com Agentic Access
  operation_count: 88
  slug: bike4mind-com-agentic-access
  summary_line: 88 operations · 49 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.bike4mind.com/api/v1
  baseurl_source: declared
  description: Programmatic access to the Bike4Mind API
  name: Bike4Mind API
  slug: bike4mind-api
artifact_total: 21
asyncapis:
- description: ''
  name: Bike4Mind Com Webhooks
  slug: bike4mind-com-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bike4mind.com/tags/getting-started
- group: agent
  href: https://artifacts.apis.io/bike4mind-com/agentic-access/bike4mind-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bike4mind-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bike4mind-com/plans/bike4mind-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bike4mind-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bike4mind-com/rules/bike4mind-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bike4mind-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bike4mind-com/json-ld/bike4mind-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bike4mind-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bike4mind-com/vocabulary/bike4mind-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bike4mind-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bike4mind-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bike4mind-com/asyncapi/bike4mind-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bike4mind-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bike4mind-com/data-model/bike4mind-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bike4mind-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bike4mind.com/security
- group: auth
  href: https://artifacts.apis.io/bike4mind-com/authentication/bike4mind-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bike4mind-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bike4mind-com/errors/bike4mind-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bike4mind-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bike4mind-com/conformance/bike4mind-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bike4mind-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bike4mind-com/llms/bike4mind-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bike4mind-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bike4mind-com/a2a/bike4mind-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bike4mind-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/bike4mind-com/mcp/bike4mind-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bike4mind-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bike4mind-com/mcp/bike4mind-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bike4mind-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bike4mind-com/well-known/bike4mind-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bike4mind-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bike4mind-com/well-known/bike4mind-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bike4mind-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bike4mind-com/hosts/bike4mind-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bike4mind-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bike4mind-com/vendors/bike4mind-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bike4mind-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bike4mind.com/tos
- group: start
  title: ''
  type: SignUp
  url: https://app.bike4mind.com/register?utm_source=bike4mind.com&utm_medium=site&utm_campaign=header&utm_content=desktop_signup
- group: auth
  title: ''
  type: Security
  url: https://bike4mind.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bike4mind.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://bike4mind.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bike4mind
- group: operate
  title: ''
  type: ChangeLog
  url: https://bike4mind.com/whats-new
- group: auth
  href: https://artifacts.apis.io/bike4mind-com/security/bike4mind-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bike4mind-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bike4mind-com/security/bike4mind-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bike4mind-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bike4mind-com/security/bike4mind-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bike4mind-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bike4mind.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bike4mind.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.bike4mind.com/api/v1/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://bike4mind.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://bike4mind.com/blog
created: '2026-11-02'
description: Bike4Mind is an open‑core AI workbench that empowers builders, developers, researchers and enterprises to create, deploy and scale AI‑driven agents and applications. The platform offers a suite of models, tools, and integrations, providing a collaborative workspace with generous free credits and self‑hosted options. Its mission is to decentralize AI capabilities, making advanced models accessible without reliance on large hyperscalers, and it operates as a profitable, bootstrapped company with a global distributed team.
image: https://bike4mind.com/assets/images/SCREENSHOT_LATEST.png
json_schemas:
- name: createCompletionRequest
  property_count: 9
  slug: bike4mind-com-create-completion-request
- name: generateImageRequest
  property_count: 26
  slug: bike4mind-com-generate-image-request
- name: getSkillMarketListingResponse200
  property_count: 4
  slug: bike4mind-com-get-skill-market-listing-response200
- name: listModelsResponse200
  property_count: 2
  slug: bike4mind-com-list-models-response200
- name: listMySkillMarketListingsResponse200
  property_count: 2
  slug: bike4mind-com-list-my-skill-market-listings-response200
- name: listSkillMarketReviewQueueResponse200
  property_count: 2
  slug: bike4mind-com-list-skill-market-review-queue-response200
jsonld:
- class_count: 120
  name: Bike4Mind Com Context
  property_count: 221
  slug: bike4mind-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at bike4mind.com.
  name: Bike4Mind MCP Server
  slug: bike4mind-com-mcp-yml
modified: '2026-11-02'
name: Bike4Mind
nav: Providers
network: true
overview: 'Bike4Mind is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Open Source, Platform, and Workbench.


  The Bike4Mind catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bike4Mind''s developer surface includes getting-started guide, authentication, signup flow, changelog, documentation, API reference, pricing, and 29 more developer resources.'
plans:
- name: Bike4Mind Com Plans Pricing
  plan_count: 2
  slug: bike4mind-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Bike4Mind API Rules
  rule_count: 69
  severity_counts:
    error: 53
    hint: 0
    info: 2
    warn: 14
  slug: bike4mind-com-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 67.5
    developer_ergonomics: 29.2
    discoverability: 65.8
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
    skills: derived
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
- kind: authentication
  name: Bike4Mind Com Authentication
  slug: bike4mind-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bike4Mind Com Domain Security
  slug: bike4mind-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bike4Mind Com Vulnerability Disclosure
  slug: bike4mind-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bike4Mind Com Trust Center
  slug: bike4mind-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 4
skills:
- name: bike4mind-com-create-agent-with-avatar
  slug: bike4mind-com-create-agent-with-avatar
- name: bike4mind-com-create-and-retrieve-artifact
  slug: bike4mind-com-create-and-retrieve-artifact
- name: bike4mind-com-manage-projects
  slug: bike4mind-com-manage-projects
- name: bike4mind-com-upload-and-list-files
  slug: bike4mind-com-upload-and-list-files
slug: bike4mind-com
tags:
- Company
- Artificial Intelligence
- Open Source
- Platform
- Workbench
website: https://bike4mind.com/
---
