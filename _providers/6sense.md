---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: 6Sense Agentic Access
  operation_count: 7
  slug: 6sense-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 7
apis:
- baseURL: https://epsilon.6sense.com
  baseurl_source: declared
  description: The Company API from 6sense — 1 operation(s) for company.
  name: 6sense Company API
  slug: 6sense-company-api
- baseURL: https://api.6sense.com
  baseurl_source: declared
  description: The Enrichment API from 6sense — 2 operation(s) for enrichment.
  name: 6sense Enrichment API
  slug: 6sense-enrichment-api
- baseURL: https://api.6sense.com
  baseurl_source: declared
  description: The People API from 6sense — 4 operation(s) for people.
  name: 6sense People API
  slug: 6sense-people-api
- description: Hosted remote Model Context Protocol server at https://api.6sense.com/mcp (beta). Read-only retrieval of Revvy AI-powered 6sense insights — account insights, 6QA trends, keyword performance, ad campai
  name: 6sense MCP Server
  slug: 6sense-mcp
- baseURL: https://epsilon.6sense.com
  baseurl_source: declared
  description: The Scoring API from 6sense — 1 operation(s) for scoring.
  name: 6sense Scoring API
  slug: 6sense-scoring-api
artifact_total: 32
asyncapis:
- description: 'Outbound webhook events emitted by the 6sense AI Email product (formerly Conversational Email, formerly Saleswhale) to a customer-configured Target URL. PROVENANCE: 6sense does not publish an AsyncAPI'
  name: 6sense AI Email Webhooks
  slug: 6sense-ai-email-asyncapi
- description: ''
  name: 6Sense Ai Email Webhooks
  slug: 6sense-ai-email-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 6sense Firmographics Company API
  slug: open-6sense-company-api
- collection_type: open
  name: 6sense Company Firmographics API
  slug: open-6sense-company-firmographics-api
- collection_type: open
  name: 6sense Company Identification API
  slug: open-6sense-company-identification-api
- collection_type: open
  name: 6sense Firmographics Company Enrichment API
  slug: open-6sense-enrichment-api
- collection_type: open
  name: 6sense Lead Scoring API
  slug: open-6sense-lead-scoring-api
- collection_type: open
  name: 6sense Lead Scoring And Firmographics API
  slug: open-6sense-lead-scoring-firmographics-api
- collection_type: open
  name: 6sense Firmographics Company People API
  slug: open-6sense-people-api
- collection_type: open
  name: 6sense People Enrichment API
  slug: open-6sense-people-enrichment-api
- collection_type: open
  name: 6sense People Search API
  slug: open-6sense-people-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/6sense-scribe-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/6sense-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/6sense-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/6sense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/6sense-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://6sense.com
- group: docs
  title: ''
  type: Documentation
  url: https://6sense.com/platform
- group: start
  title: ''
  type: Portal
  url: https://api.6sense.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://support.6sense.com/docs/6sense-api-overview
- group: operate
  title: ''
  type: Support
  url: https://support.6sense.com
- group: other
  title: ''
  type: CaseStudies
  url: https://6sense.com/customers
- group: company
  title: ''
  type: Blog
  url: https://6sense.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/6sense
- group: build
  title: ''
  type: Github
  url: https://github.com/6si
- group: commercial
  title: ''
  type: Pricing
  url: https://6sense.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/6sense-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/6sense-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/6sense-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/6sense-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/6sense-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: mcp/6sense-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/6sense-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/6sense-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/6sense-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/6sense-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/6sense-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/6sense-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/6sense-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.6sense.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://api.6sense.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/6sense-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.6sense.com/docs/product-release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/6sense-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.6sense.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/6sense-ai-email-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/6sense-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/6sense-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/6sense-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.6sense.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.6sense.com/docs/api-credits-api-tokens
- group: commercial
  title: ''
  type: TermsOfService
  url: https://6sense.com/terms-of-use/
- group: start
  title: ''
  type: Login
  url: https://login.6sense.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/6si
created: '2026-05-25'
description: 6sense Insights is a B2B revenue AI platform that identifies in-market accounts from anonymous buying signals and orchestrates marketing and sales against them. Its Signalverse intent graph, Master Company Database of roughly 76 million company accounts and predictive models power account-based marketing, advertising, AI email agents and sales intelligence. For developers, 6sense exposes six HTTP data APIs across three hosts — Company Identification, Company Firmographics, Lead Scoring, Lead Scoring and Firmographics, People Enrichment and People Search — plus the acquired AI Email (Saleswhale) API with a signed webhook surface, and a hosted remote MCP server at api.6sense.com/mcp for agent access. Access is token-based and metered against contract-year credit pools rather than list-priced plans.
finops:
- name: 6Sense Finops
  service_category: Sales and Marketing Technology
  slug: 6sense-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the 6sense Revenue AI Platform, covering account-based marketing (ABM), intent data, predictive scoring, firmographic and technographic enrichme
  name: 6sense GraphQL Schema
  slug: 6sense-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/6sense.png
json_schemas:
- name: 6sense Company
  property_count: 20
  slug: 6sense-company
- name: 6sense Enriched Contact
  property_count: 17
  slug: 6sense-contact
- name: 6sense Product Score
  property_count: 10
  slug: 6sense-score
jsonld:
- class_count: 0
  name: 6Sense Context
  property_count: 4
  slug: 6sense-context
layout: provider
mcp_servers:
- description: ''
  name: 6sense MCP
  slug: 6sense-mcp
modified: '2026-08-13'
name: 6sense
nav: Providers
network: true
overview: '6sense publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Company API, Enrichment API, People API, and 1 more. Tagged areas include Account Based Marketing, Intent Data, B2B, Predictive Analytics, and Revenue.


  The 6sense catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  6sense''s developer surface includes authentication, documentation, developer portal, support, engineering blog, GitHub presence, pricing, and 37 more developer resources.'
plans:
- name: 6Sense Plans Pricing
  plan_count: 4
  slug: 6sense-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: 6Sense Rate Limits
  slug: 6sense-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: 6sense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: 6sense-jsonschema-spectral-rules
scopes:
- name: 6Sense Scopes
  scope_count: 1
  slug: 6sense-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 69.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 90.3
    catalog_earned_first_party: 24.0
    catalog_gap: 24.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 43.2
    contract_quality: 67.7
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 43.2
    operational_transparency: 81.6
  previous_composite: 69.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/6sense/refs/heads/main/screenshots/6sense-2026-06-20T162740.png
security:
- kind: authentication
  name: 6Sense Authentication
  slug: 6sense-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: 6Sense Domain Security
  slug: 6sense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: 6Sense Trust Center
  slug: 6sense-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: 6sense
tags:
- Account Based Marketing
- Intent Data
- B2B
- Predictive Analytics
- Revenue
- Sales Intelligence
- Artificial Intelligence
- Marketing Technology
website: https://6sense.com
---
