---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cognizant Technology Agentic Access
  operation_count: 4
  slug: cognizant-technology-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: '{scheme}://{host}:{port}/api/v1'
  baseurl_source: declared
  description: The service comprises all the exchanges to the backend in support of a single agent's services. Routing is done by way of agent name on the grpc service hosting the agent, so as to keep info about whi
  name: Cognizant Technology Solutions Agent Service API
  slug: cognizant-technology-agentservice-api
- baseURL: '{scheme}://{host}:{port}/api/v1'
  baseurl_source: declared
  description: The service provides system-wide information about resources available in current instance of neuro-san.
  name: Cognizant Technology Solutions Concierge Service API
  slug: cognizant-technology-conciergeservice-api
artifact_total: 19
common:
- group: start
  title: ''
  type: Login
  url: https://www.cognizant.com/us/en/ocm/demo/login
- group: operate
  href: https://artifacts.apis.io/cognizant-technology/lifecycle/cognizant-technology-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cognizant-technology-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/cognizant-technology/agentic-access/cognizant-technology-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cognizant-technology-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cognizant-technology/finops/cognizant-technology-finops.yml
  title: ''
  type: FinOps
  url: finops/cognizant-technology-finops.yml
- group: design
  href: https://artifacts.apis.io/cognizant-technology/rules/cognizant-technology-rules.yml
  title: ''
  type: Spectral
  url: rules/cognizant-technology-rules.yml
- group: design
  href: https://artifacts.apis.io/cognizant-technology/json-ld/cognizant-technology-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cognizant-technology-context.jsonld
- group: design
  href: https://artifacts.apis.io/cognizant-technology/vocabulary/cognizant-technology-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cognizant-technology-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/cognizant-technology/hosts/cognizant-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognizant-technology-hosts.yml
- group: build
  href: https://artifacts.apis.io/cognizant-technology/integrations/cognizant-technology-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cognizant-technology-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/cognizant-technology/vendors/cognizant-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognizant-technology-vendors.yml
- group: other
  href: https://artifacts.apis.io/cognizant-technology/overlays/cognizant-technology-neuro-san-agent-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cognizant-technology-neuro-san-agent-service-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cognizant-technology/mcp/cognizant-technology-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cognizant-technology-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cognizant-technology/security/cognizant-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognizant-technology-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognizant
- group: company
  title: ''
  type: Website
  url: https://www.cognizant.com/
- group: other
  title: ''
  type: AI Lab
  url: https://www.cognizant.com/us/en/ai-lab
- group: other
  title: ''
  type: Platforms
  url: https://www.cognizant.com/us/en/services/cognizant-platforms
- group: other
  title: ''
  type: Neuro AI Decisioning
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-generative-ai-adoption
- group: other
  title: ''
  type: Neuro AI Enterprise Core
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-ai-enterprise-core
- group: other
  title: ''
  type: Neuro AI Engineering
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-ai-engineering
- group: other
  title: ''
  type: Neuro AI for IT Operations
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-ai-it-operations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cognizant-ai-lab
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cognizant-ai-lab/neuro-san-studio
- group: company
  title: ''
  type: News
  url: https://news.cognizant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cognizant.com/us/en/about-cognizant/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cognizant.com/us/en/about-cognizant/terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.cognizant.com/us/en/insights/insights-blog
- group: build
  href: https://artifacts.apis.io/cognizant-technology/packages/cognizant-technology-packages.yml
  title: ''
  type: Packages
  url: packages/cognizant-technology-packages.yml
- group: build
  href: https://artifacts.apis.io/cognizant-technology/packages/cognizant-technology-packages.yml
  title: ''
  type: SDKs
  url: packages/cognizant-technology-packages.yml
- group: build
  href: https://artifacts.apis.io/cognizant-technology/cli/cognizant-technology-cli.yml
  title: ''
  type: CLI
  url: cli/cognizant-technology-cli.yml
- group: design
  href: https://artifacts.apis.io/cognizant-technology/components/cognizant-technology-components.yml
  title: ''
  type: Components
  url: components/cognizant-technology-components.yml
- group: agent
  href: https://artifacts.apis.io/cognizant-technology/llms/cognizant-technology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognizant-technology-llms.txt
- group: design
  href: https://artifacts.apis.io/cognizant-technology/conformance/cognizant-technology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cognizant-technology-conformance.yml
- group: design
  href: https://artifacts.apis.io/cognizant-technology/lifecycle/cognizant-technology-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cognizant-technology-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cognizant-technology/changelog/cognizant-technology-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cognizant-technology-changelog.yml
- group: auth
  href: https://artifacts.apis.io/cognizant-technology/security/cognizant-technology-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognizant-technology-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cognizant-technology/security/cognizant-technology-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cognizant-technology-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/cognizant-technology/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/cognizant-technology/plans/cognizant-technology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cognizant-technology-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cognizant-technology/rate-limits/cognizant-technology-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cognizant-technology-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cognizant-ai-lab/neuro-san/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cognizant-ai-lab/neuro-san/tree/main/quick-start
- group: operate
  title: ''
  type: Support
  url: https://github.com/cognizant-ai-lab/neuro-san/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cognizant-ai-lab/neuro-san/releases
created: '2025-03-21'
description: 'Cognizant Technology Solutions is a multinational information technology services and consulting company that provides digital, technology, consulting, and operations services to clients worldwide. Cognizant publishes no hosted, general-purpose commercial API and operates no developer portal - developer.cognizant.com and api.cognizant.com do not resolve. It does, however, publish a real machine-readable API contract: Cognizant AI Lab releases Neuro SAN (Neuro AI System of Agent Networks), an Apache-2.0 multi-agent orchestration framework whose agent service ships four .proto files defining two gRPC services, a generated OpenAPI 3.0.3 document the running server publishes at /api/v1/docs, and an MCP 2025-06-18 endpoint that exposes each public agent network as a callable tool. The framework is self-hosted - Cognizant ships the software and the operator runs the server - so there is no Cognizant-operated endpoint, no pricing, and no rate limit to publish. Six first-party Python
  packages are on PyPI, led by neuro-san (0.7.18 on 2026-11-03, 167 releases, actively developed). The commercial Neuro AI platform family (Neuro AI Decisioning, Neuro AI Enterprise Core, Neuro AI Engineering, Neuro AI for IT Operations) and other delivered platforms are engaged through consulting rather than self-service APIs.'
finops:
- has_sources: true
  method: derived
  name: Cognizant Technology Finops
  primary_unit: ''
  service_category: ''
  slug: cognizant-technology-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognizant-technology.png
json_schemas:
- name: ChatRequest
  property_count: 4
  slug: cognizant-technology-chat-request
- name: ChatResponse
  property_count: 2
  slug: cognizant-technology-chat-response
- name: ConciergeResponse
  property_count: 1
  slug: cognizant-technology-concierge-response
- name: ConnectivityResponse
  property_count: 2
  slug: cognizant-technology-connectivity-response
- name: FunctionResponse
  property_count: 1
  slug: cognizant-technology-function-response
jsonld:
- class_count: 17
  name: Cognizant Technology Context
  property_count: 37
  slug: cognizant-technology-context
layout: provider
mcp_servers:
- description: ''
  name: Neuro SAN MCP service
  slug: neuro-san-mcp-service
modified: '2026-11-04'
name: Cognizant Technology Solutions
nav: Providers
network: true
overview: 'Cognizant Technology Solutions publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent Service API and Concierge Service API. Tagged areas include AI Platform, Consulting, Digital Transformation, IT Services, and Multi-Agent.


  The Cognizant Technology Solutions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cognizant Technology Solutions'' developer surface includes product news, engineering blog, CLI, changelog, documentation, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Cognizant Technology Plans Pricing
  plan_count: 0
  slug: cognizant-technology-plans-pricing
press:
- date: ''
  title: Cognizant and OpenAI Partner to Reshape Enterprise ...
  url: https://www.prnewswire.com/news-releases/cognizant-and-openai-partner-to-reshape-enterprise-software-engineering-with-codex-302748608.html
- date: ''
  title: Cognizant Press Releases, Company News
  url: https://news.cognizant.com/newsannouncements
- date: ''
  title: Investor Relations | Cognizant
  url: https://investors.cognizant.com/home/default.aspx
- date: ''
  title: Cognizant News & Events | Cognizant Press Releases ...
  url: https://news.cognizant.com/
- date: ''
  title: Cognizant Named Aston Martin Aramco Formula One™ ...
  url: https://www.prnewswire.com/news-releases/cognizant-named-aston-martin-aramco-formula-one-team-global-ai-services-partner-302755751.html
random_paper: 14
rate_limits:
- limit_count: 0
  name: Cognizant Technology Rate Limits
  slug: cognizant-technology-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Cognizant Technology Solutions API Rules
  rule_count: 42
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 1
  slug: cognizant-technology-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.9
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 50.6
    developer_ergonomics: 51.8
    discoverability: 72.5
    operational_transparency: 39.5
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cognizant-technology/cognizant-technology-2026-06-20T174719.png
security:
- kind: authentication
  name: Cognizant Technology Authentication
  slug: cognizant-technology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cognizant Technology Domain Security
  slug: cognizant-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognizant Technology Vulnerability Disclosure
  slug: cognizant-technology-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 2
skills:
- name: cognizant-technology-converse-with-an-agent-network
  slug: cognizant-technology-converse-with-an-agent-network
- name: cognizant-technology-discover-agent-networks
  slug: cognizant-technology-discover-agent-networks
slug: cognizant-technology
tags:
- AI Platform
- Consulting
- Digital Transformation
- IT Services
- Multi-Agent
- Neuro AI
- Fortune 500
website: https://www.cognizant.com/
---
