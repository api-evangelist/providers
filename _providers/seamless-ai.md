---
access_model:
  confidence: high
  label: Freemium platform · API gated behind a Public API license
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - https://seamless.ai/pricing
  - https://docs.seamless.ai/api-http-status-codes
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-09-15'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Seamless Ai Agentic Access
  operation_count: 9
  slug: seamless-ai-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 2
apis:
- baseURL: https://api.seamless.ai/api/client/v1
  baseurl_source: declared
  description: The Seamless.AI Public API v1 — nine operations covering contact and company search, asynchronous enrichment (research), result polling, org-data retrieval and the OAuth token exchange. Search and org
  name: Seamless.AI Public API
  slug: seamless-ai-public-api
- baseURL: https://api.seamless.ai/api/client/v1
  baseurl_source: declared
  description: The Mcp API from Seamless.AI — 1 operation(s) for mcp.
  name: Seamless.AI MCP API
  slug: seamless-ai-mcp-api
artifact_total: 28
asyncapis:
- description: ''
  name: Seamless Ai Webhooks
  slug: seamless-ai-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/mcp/seamless-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/seamless-ai-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://seamless.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.seamless.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seamless.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.seamless.ai/searchcontacts
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seamless.ai/authenticate-and-make-your-first-request
- group: other
  title: ''
  type: Overview
  url: https://seamless.ai/products/api
- group: operate
  title: ''
  type: Support
  url: https://seamless.ai/customers/education
- group: company
  title: ''
  type: Blog
  url: https://seamless.ai/customers/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://seamless.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.seamless.ai/register
- group: start
  title: ''
  type: Login
  url: https://login.seamless.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seamless.ai/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seamless.ai/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SeamlessAI
- group: other
  title: ''
  type: Glossary
  url: https://seamless.ai/customers/education/articles/api-terms-glossary
- group: other
  title: ''
  type: Announcement
  url: https://seamless.ai/news/releases/api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seamlessai
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/a2a/seamless-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/seamless-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/llms/seamless-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seamless-ai-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.seamless.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/agentic-access/seamless-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/seamless-ai-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/well-known/seamless-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seamless-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/authentication/seamless-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/seamless-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/scopes/seamless-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/seamless-ai-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/conventions/seamless-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/seamless-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/errors/seamless-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/seamless-ai-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/rate-limits/seamless-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/seamless-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/plans/seamless-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/seamless-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/lifecycle/seamless-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/seamless-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/conformance/seamless-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seamless-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/data-model/seamless-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seamless-ai-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/packages/seamless-ai-packages.yml
  title: ''
  type: Packages
  url: packages/seamless-ai-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/asyncapi/seamless-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/seamless-ai-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/security/seamless-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seamless-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/security/seamless-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/seamless-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.seamless.ai/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-contact-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-contact-search-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-company-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-company-search-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-contact-research-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-contact-research-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-company-research-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-company-research-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-org-contacts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-org-contacts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-org-companies-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-org-companies-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/overlays/seamless-ai-oauth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seamless-ai-oauth-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/json-schema/seamless-ai-contact-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/seamless-ai-contact-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/json-schema/seamless-ai-company-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/seamless-ai-company-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/json-structure/seamless-ai-contact-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/seamless-ai-contact-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/json-structure/seamless-ai-company-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/seamless-ai-company-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/json-ld/seamless-ai-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/seamless-ai-context.jsonld
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/examples/seamless-ai-search-contacts-example.json
  title: ''
  type: Examples
  url: examples/seamless-ai-search-contacts-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/examples/seamless-ai-research-contacts-example.json
  title: ''
  type: Examples
  url: examples/seamless-ai-research-contacts-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/examples/seamless-ai-poll-contacts-research-results-example.json
  title: ''
  type: Examples
  url: examples/seamless-ai-poll-contacts-research-results-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/rules/seamless-ai-rules.yml
  title: ''
  type: SpectralRuleset
  url: rules/seamless-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/vocabulary/seamless-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seamless-ai-vocabulary.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/collections/seamless-ai-contact-search-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/seamless-ai-contact-search-api.postman_collection.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/collections/seamless-ai-company-search-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/seamless-ai-company-search-api.postman_collection.json
created: '2026-05-02'
description: Seamless.AI is a B2B sales intelligence platform that provides real-time contact and company data to help sales teams find and connect with their ideal customers. The platform uses artificial intelligence to continuously verify and update contact information including emails, direct dials and mobile numbers. Its Public API v1 is a three-hop enrichment pipeline — search, research, then collect by polling or webhook — secured with an API key in a Token header or OAuth 2.0, and metered in research credits rather than API calls. Alongside the nine-operation REST API, Seamless.AI operates a hosted Model Context Protocol server exposing 54 tools across search, research, lists, saved searches, campaigns, templates, email, calls, tasks and activity, secured with OAuth 2.1, dynamic client registration and published per-tool risk tiers.
examples:
- key_count: 8
  name: Seamless Ai Get Access Token Example
  slug: seamless-ai-get-access-token-example
- key_count: 8
  name: Seamless Ai Get Companies Example
  slug: seamless-ai-get-companies-example
- key_count: 8
  name: Seamless Ai Get Contacts Example
  slug: seamless-ai-get-contacts-example
- key_count: 8
  name: Seamless Ai Poll Company Research Results Example
  slug: seamless-ai-poll-company-research-results-example
- key_count: 8
  name: Seamless Ai Poll Contacts Research Results Example
  slug: seamless-ai-poll-contacts-research-results-example
- key_count: 8
  name: Seamless Ai Research Companies Example
  slug: seamless-ai-research-companies-example
- key_count: 8
  name: Seamless Ai Research Contacts Example
  slug: seamless-ai-research-contacts-example
- key_count: 8
  name: Seamless Ai Search Companies Example
  slug: seamless-ai-search-companies-example
- key_count: 8
  name: Seamless Ai Search Contacts Example
  slug: seamless-ai-search-contacts-example
finops:
- name: Seamless Ai Finops
  service_category: API
  slug: seamless-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seamless-ai.png
json_schemas:
- name: Seamless.AI Company
  property_count: 51
  slug: seamless-ai-company
- name: Seamless.AI Contact
  property_count: 101
  slug: seamless-ai-contact
json_structures:
- name: Seamless Ai Company Structure
  property_count: 51
  slug: seamless-ai-company-structure
- name: Seamless Ai Contact Structure
  property_count: 101
  slug: seamless-ai-contact-structure
jsonld:
- class_count: 147
  name: Seamless Ai Context
  property_count: 0
  slug: seamless-ai-context
layout: provider
mcp_servers:
- description: ''
  name: Seamless.AI MCP Server
  slug: seamlessai-mcp-server
modified: '2026-08-14'
name: Seamless.AI
nav: Providers
network: true
overview: 'Seamless.AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Public API and MCP API. Tagged areas include B2B, Contact Data, Sales Intelligence, Prospecting, and Lead Generation.


  The Seamless.AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Seamless.AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 50 more developer resources.'
plans:
- name: Seamless Ai Plans Pricing
  plan_count: 3
  slug: seamless-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Seamless Ai Rate Limits
  slug: seamless-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Seamless.AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: seamless-ai-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Seamless.AI API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: seamless-ai-rules
scopes:
- name: Seamless Ai Scopes
  scope_count: 2
  slug: seamless-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.5
    catalog_earned_first_party: 20.0
    catalog_gap: 37.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 33.3
    contract_quality: 71.1
    developer_ergonomics: 65.5
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 66.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/screenshots/seamless-ai-2026-06-20T193614.png
security:
- kind: authentication
  name: Seamless Ai Authentication
  slug: seamless-ai-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Seamless Ai Domain Security
  slug: seamless-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Seamless Ai Trust Center
  slug: seamless-ai-trust-center
  summary_line: trust center published
slug: seamless-ai
tags:
- B2B
- Contact Data
- Sales Intelligence
- Prospecting
- Lead Generation
- CRM Enrichment
- Data Enrichment
- MCP
- Agents
- Sales Automation
website: https://seamless.ai
---
