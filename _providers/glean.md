---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Glean Agentic Access
  operation_count: 61
  slug: glean-agentic-access
  summary_line: 61 operations · 35 acting
api_count: 1
apis:
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: Read and submit activity signals (views, clicks, edits) that improve personalization and ranking across the Glean instance.
  name: Glean Activity API
  slug: glean-activity-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: Build and invoke autonomous agents that reason over enterprise data and perform multi-step workflows on behalf of users.
  name: Glean Agents API
  slug: glean-agents-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The announcements API from Glean — 3 operation(s) for announcements.
  name: Glean Announcements API
  slug: glean-announcements-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The answers API from Glean — 5 operation(s) for answers.
  name: Glean Answers API
  slug: glean-answers-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: Multi-turn generative chat over enterprise content with grounded answers, citations, and tool use.
  name: Glean Chat API
  slug: glean-chat-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The collections API from Glean — 8 operation(s) for collections.
  name: Glean Collections API
  slug: glean-collections-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The documents API from Glean — 3 operation(s) for documents.
  name: Glean Documents API
  slug: glean-documents-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: Administer governance policies, data classification, and access controls across the Glean instance.
  name: Glean Governance API
  slug: glean-governance-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The insights API from Glean — 1 operation(s) for insights.
  name: Glean Insights API
  slug: glean-insights-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: Look up people in the enterprise knowledge graph including profile, expertise, org chart relationships, and activity.
  name: Glean People API
  slug: glean-people-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The pins API from Glean — 5 operation(s) for pins.
  name: Glean Pins API
  slug: glean-pins-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: Run unified semantic and keyword search across all connected enterprise content with permission-aware results, filters, and facets.
  name: Glean Search API
  slug: glean-search-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The shortcuts API from Glean — 5 operation(s) for shortcuts.
  name: Glean Shortcuts API
  slug: glean-shortcuts-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The summarize API from Glean — 1 operation(s) for summarize.
  name: Glean Summarize API
  slug: glean-summarize-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The tools API from Glean — 2 operation(s) for tools.
  name: Glean Tools API
  slug: glean-tools-api
- baseURL: https://{instance}-be.glean.com/rest/api/v1
  baseurl_source: declared
  description: The verification API from Glean — 3 operation(s) for verification.
  name: Glean Verification API
  slug: glean-verification-api
artifact_total: 44
collections:
- collection_type: open
  name: Glean Client REST activity API
  slug: open-glean-activity-api
- collection_type: open
  name: Glean Client REST activity agents API
  slug: open-glean-agents-api
- collection_type: open
  name: Glean Client REST activity announcements API
  slug: open-glean-announcements-api
- collection_type: open
  name: Glean Client REST activity answers API
  slug: open-glean-answers-api
- collection_type: open
  name: Glean Client REST activity chat API
  slug: open-glean-chat-api
- collection_type: open
  name: Glean Client REST activity collections API
  slug: open-glean-collections-api
- collection_type: open
  name: Glean Client REST activity documents API
  slug: open-glean-documents-api
- collection_type: open
  name: Glean Client REST activity governance API
  slug: open-glean-governance-api
- collection_type: open
  name: Glean Client REST activity insights API
  slug: open-glean-insights-api
- collection_type: open
  name: Glean Client REST activity people API
  slug: open-glean-people-api
- collection_type: open
  name: Glean Client REST activity pins API
  slug: open-glean-pins-api
- collection_type: open
  name: Glean Client REST activity search API
  slug: open-glean-search-api
- collection_type: open
  name: Glean Client REST activity shortcuts API
  slug: open-glean-shortcuts-api
- collection_type: open
  name: Glean Client REST activity summarize API
  slug: open-glean-summarize-api
- collection_type: open
  name: Glean Client REST activity tools API
  slug: open-glean-tools-api
- collection_type: open
  name: Glean Client REST activity verification API
  slug: open-glean-verification-api
- collection_type: open
  name: Glean Client REST API
  slug: open-glean
common:
- group: operate
  href: https://artifacts.apis.io/glean/rate-limits/glean-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/glean-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/glean/finops/glean-finops.yml
  title: ''
  type: FinOps
  url: finops/glean-finops.yml
- group: commercial
  href: https://artifacts.apis.io/glean/plans/glean-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glean-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/glean/capabilities/glean-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/glean-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/glean/agentic-access/glean-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/glean-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/glean/security/glean-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/glean-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/glean/security/glean-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/glean-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/glean/security/glean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glean-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/glean/authentication/glean-authentication.yml
  title: ''
  type: Authentication
  url: authentication/glean-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.glean.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.glean.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.glean.com/api-info/client/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://developers.glean.com/sdks
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gleanwork
- group: company
  title: ''
  type: Blog
  url: https://www.glean.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.glean.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.glean.com/
- group: operate
  title: ''
  type: Support
  url: https://help.glean.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glean.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glean.com/legal/customer-terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glean-technologies/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.glean.com/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.glean.com/llms.txt
created: '2026-05-23'
description: Glean is an AI-powered work assistant and enterprise search platform that connects to a company's apps and data sources to provide unified search, generative answers, and autonomous agents grounded in enterprise knowledge. Glean exposes a Client API for end-user features (search, chat, agents, answers), an Indexing API for ingesting custom data sources, and Admin and Activity APIs for governance and observability.
finops:
- has_sources: false
  method: generated
  name: Glean Finops
  primary_unit: ''
  service_category: API
  slug: glean-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glean.png
layout: provider
mcp_servers:
- description: Remote MCP server at developers.glean.com over HTTP.
  name: Glean MCP Server
  slug: glean
- description: Remote MCP server at docs.glean.com over HTTP.
  name: Glean MCP Server
  slug: glean-2
modified: '2026-05-23'
name: Glean
nav: Providers
network: true
overview: 'Glean publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Agents API, Announcements API, and 13 more. Tagged areas include Agents, Artificial Intelligence, Answers, Chat, and Connectors.


  The Glean catalog on APIs.io includes 1 Spectral governance ruleset.


  Glean''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, support, changelog, and 16 more developer resources.'
plans:
- name: Glean Plans Pricing
  plan_count: 0
  slug: glean-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Glean Rate Limits
  slug: glean-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Glean API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: glean-rules
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.5
    catalog_earned_first_party: 0.0
    catalog_gap: 71.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 24.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/glean/glean-2026-06-20T181906.png
security:
- kind: authentication
  name: Glean Authentication
  slug: glean-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glean Domain Security
  slug: glean-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Glean Vulnerability Disclosure
  slug: glean-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Glean Trust Center
  slug: glean-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: glean
tags:
- Agents
- Artificial Intelligence
- Answers
- Chat
- Connectors
- Enterprise Search
- Generative AI
- Indexing
- Knowledge
- RAG
- Search
- Work Assistant
- Knowledge Management
website: https://www.glean.com/
---
