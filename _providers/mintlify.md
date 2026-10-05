---
access_model:
  confidence: medium
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
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Mintlify Agentic Access
  operation_count: 8
  slug: mintlify-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: Mintlify is a developer documentation platform that helps product and engineering teams create, maintain, and host modern docs. It uses a docs‑as‑code workflow (Markdown in your repo) with a rich comp
  name: Mintlify
  slug: mintlify
- baseURL: https://api.mintlify.com
  baseurl_source: spec
  description: Programmatic documentation editing via AI agent jobs.
  name: Mintlify Agent API
  slug: mintlify-agent-api
- baseURL: https://api.mintlify.com
  baseurl_source: spec
  description: Export user feedback, conversations, and usage analytics.
  name: Mintlify Analytics API
  slug: mintlify-analytics-api
- baseURL: https://api.mintlify.com
  baseurl_source: spec
  description: Embeddable AI chat experience grounded in your documentation.
  name: Mintlify Assistant API
  slug: mintlify-assistant-api
- baseURL: https://api.mintlify.com
  baseurl_source: spec
  description: Trigger and monitor documentation deployment updates.
  name: Mintlify Update API
  slug: mintlify-update-api
artifact_total: 40
collections:
- collection_type: postman
  name: Mintlify Agent API
  slug: postman-mintlify-agent-api
- collection_type: postman
  name: Mintlify Agent Analytics API
  slug: postman-mintlify-analytics-api
- collection_type: postman
  name: Mintlify Agent Assistant API
  slug: postman-mintlify-assistant-api
- collection_type: postman
  name: Mintlify Agent Update API
  slug: postman-mintlify-update-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mintlify Agent API
  slug: open-mintlify-agent-api
- collection_type: open
  name: Mintlify Agent Analytics API
  slug: open-mintlify-analytics-api
- collection_type: open
  name: Mintlify Agent Assistant API
  slug: open-mintlify-assistant-api
- collection_type: open
  name: Mintlify Agent Update API
  slug: open-mintlify-update-api
- collection_type: open
  name: Mintlify API
  slug: open-mintlify
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/finops/mintlify-finops.yml
  title: ''
  type: FinOps
  url: finops/mintlify-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/rate-limits/mintlify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mintlify-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/plans/mintlify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mintlify-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/rules/mintlify-rules.yml
  title: ''
  type: Spectral
  url: rules/mintlify-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/rules/mintlify-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/mintlify-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/json-ld/mintlify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mintlify-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/vocabulary/mintlify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mintlify-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/data-model/mintlify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mintlify-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/cli/mintlify-cli.yml
  title: ''
  type: CLI
  url: cli/mintlify-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/changelog/mintlify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mintlify-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.mintlify.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/conformance/mintlify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mintlify-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/llms/mintlify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mintlify-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/a2a/mintlify-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mintlify-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/mcp/mintlify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mintlify-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/well-known/mintlify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mintlify-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/hosts/mintlify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mintlify-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/vendors/mintlify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mintlify-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.mintlify.com/roadmap
- group: docs
  title: ''
  type: APIReference
  url: https://www.mintlify.com/docs/reference/concepts
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/vendor-facets/mintlify-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/mintlify-vendor-facets.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mintlify/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/agentic-access/mintlify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mintlify-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/security/mintlify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mintlify-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/security/mintlify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mintlify-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/security/mintlify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mintlify-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/authentication/mintlify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mintlify-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://www.mintlify.com/blog/skill-md
- group: company
  title: ''
  type: Website
  url: https://www.mintlify.com/
- group: other
  title: ''
  type: Customers
  url: https://www.mintlify.com/customers
- group: company
  title: ''
  type: Blog
  url: https://www.mintlify.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mintlify.com/pricing
- group: docs
  title: ''
  type: Guide
  url: https://www.mintlify.com/guides/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://www.mintlify.com/docs/api/introduction
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mintlify.com/docs/changelog
- group: start
  title: ''
  type: Signup
  url: https://dashboard.mintlify.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.mintlify.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mintlify.com/docs/quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mintlify.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mintlify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mintlify/posts
- group: company
  title: ''
  type: Twitter
  url: https://x.com/mintlify
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mintlify.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mintlify.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://security.mintlify.com
- group: operate
  title: ''
  type: Support
  url: https://www.mintlify.com/docs/contact-support
- group: other
  title: ''
  type: Enterprise
  url: https://www.mintlify.com/enterprise
- group: other
  title: ''
  type: Startups
  url: https://www.mintlify.com/startups
- group: other
  title: ''
  type: OpenSource
  url: https://www.mintlify.com/oss-program
- group: operate
  title: ''
  type: SalesContact
  url: https://www.mintlify.com/contact/sales
- group: company
  title: ''
  type: Careers
  url: https://www.mintlify.com/careers
- group: other
  title: ''
  type: Testimonials
  url: https://www.mintlify.com/wall-of-love
- group: operate
  title: ''
  type: Migration
  url: https://www.mintlify.com/switch
- group: auth
  title: ''
  type: ResponsibleDisclosure
  url: https://www.mintlify.com/security/responsible-disclosure
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@GetMintlify/videos
- group: agent
  title: ''
  type: LlmsText
  url: https://www.mintlify.com/docs/llms.txt
created: '2026-01-05'
description: Mintlify is an AI-native intelligent documentation platform designed for the next generation of technical documentation, combining beautiful out-of-the-box design with advanced collaboration and AI capabilities.
finops:
- name: Mintlify Finops
  service_category: Documentation / Developer Tools
  slug: mintlify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mintlify.png
json_schemas:
- name: AgentJobRequest
  property_count: 4
  slug: mintlify-agent-job-request
- name: AgentJob
  property_count: 7
  slug: mintlify-agent-job
- name: AgentJob
  property_count: 7
  slug: mintlify-agentjob
- name: AgentJobRequest
  property_count: 4
  slug: mintlify-agentjobrequest
- name: AssistantMessageRequest
  property_count: 4
  slug: mintlify-assistant-message-request
- name: AssistantMessageRequest
  property_count: 4
  slug: mintlify-assistantmessagerequest
- name: SearchRequest
  property_count: 4
  slug: mintlify-search-request
- name: SearchResult
  property_count: 3
  slug: mintlify-search-result
- name: SearchRequest
  property_count: 4
  slug: mintlify-searchrequest
- name: SearchResult
  property_count: 3
  slug: mintlify-searchresult
- name: UpdateStatus
  property_count: 8
  slug: mintlify-update-status
- name: UpdateStatus
  property_count: 8
  slug: mintlify-updatestatus
json_structures:
- name: Mintlify Structure
  property_count: 0
  slug: mintlify-structure
jsonld:
- class_count: 6
  name: Mintlify Context
  property_count: 26
  slug: mintlify-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mintlify.com over HTTP.
  name: Mintlify MCP Server
  slug: mintlify
modified: '2026-05-30'
name: Mintlify
nav: Providers
network: true
overview: 'Mintlify publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Analytics API, Assistant API, and 2 more. Tagged areas include Documentation, API Documentation, Developer Portal, MCP, and AI Assistant.


  The Mintlify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mintlify''s developer surface includes CLI, changelog, API reference, authentication, engineering blog, pricing, documentation, and 50 more developer resources.'
plans:
- name: Mintlify Plans Pricing
  plan_count: 4
  slug: mintlify-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Mintlify Rate Limits
  slug: mintlify-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Mintlify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mintlify-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Mintlify API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: mintlify-rules
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 70.0
    catalog_earned_first_party: 0.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.7
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 57.7
    developer_ergonomics: 57.7
    discoverability: 66.7
    operational_transparency: 60.5
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/screenshots/mintlify-2026-06-20T185606.png
security:
- kind: authentication
  name: Mintlify Authentication
  slug: mintlify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mintlify Domain Security
  slug: mintlify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mintlify Vulnerability Disclosure
  slug: mintlify-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Mintlify Trust Center
  slug: mintlify-trust-center
  summary_line: SOC 2, ISO 27001
slug: mintlify
tags:
- Documentation
- API Documentation
- Developer Portal
- MCP
- AI Assistant
- Docs as Code
website: https://www.mintlify.com/
---
