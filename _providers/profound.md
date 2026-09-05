---
access_model:
  confidence: high
  label: Enterprise, on request
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.tryprofound.com/pricing
  - https://docs.tryprofound.com/rest-api/introduction
  trial: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Profound Agentic Access
  operation_count: 125
  slug: profound-agentic-access
  summary_line: 125 operations · 90 acting
api_count: 2
apis:
- description: The inbound log-ingestion endpoint for Profound Agent Analytics. Customers POST batches of up to 1,000 web-request log entries as JSON (timestamp, method, host, path, status_code, ip, user_agent, plus
  name: Profound Agent Analytics Ingestion API
  slug: profound-agent-analytics-ingestion-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Agents API from Profound — 8 operation(s) for agents.
  name: Profound Agents API
  slug: profound-agents-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The beta API from Profound — 2 operation(s) for beta.
  name: Profound Beta API
  slug: profound-beta-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Bot Traffic Reports API from Profound — 2 operation(s) for bot traffic reports.
  name: Profound Bot Traffic Reports API
  slug: profound-bot-traffic-reports-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Categories API from Profound — 10 operation(s) for categories.
  name: Profound Categories API
  slug: profound-categories-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Content API from Profound — 2 operation(s) for content.
  name: Profound Content API
  slug: profound-content-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Content optimization API from Profound — 2 operation(s) for content optimization.
  name: Profound Content optimization API
  slug: profound-content-optimization-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Documents API from Profound — 3 operation(s) for documents.
  name: Profound Documents API
  slug: profound-documents-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Human Referrals API from Profound — 2 operation(s) for human referrals.
  name: Profound Human Referrals API
  slug: profound-human-referrals-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Integrations API from Profound — 1 operation(s) for integrations.
  name: Profound Integrations API
  slug: profound-integrations-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Knowledge bases API from Profound — 4 operation(s) for knowledge bases.
  name: Profound Knowledge bases API
  slug: profound-knowledge-bases-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The OpenAI Ads API from Profound — 1 operation(s) for openai ads.
  name: Profound OpenAI Ads API
  slug: profound-openai-ads-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Organization API from Profound — 16 operation(s) for organization.
  name: Profound Organization API
  slug: profound-organization-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Projects API from Profound — 10 operation(s) for projects.
  name: Profound Projects API
  slug: profound-projects-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Prompts API from Profound — 3 operation(s) for prompts.
  name: Profound Prompts API
  slug: profound-prompts-api
- baseURL: https://api.tryprofound.com
  baseurl_source: declared
  description: The Reports API from Profound — 62 operation(s) for reports.
  name: Profound Reports API
  slug: profound-reports-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/profound-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryprofound.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryprofound.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryprofound.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryprofound.com/api-reference/organization/get-categories
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryprofound.com/rest-api/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.tryprofound.com
- group: company
  title: ''
  type: Blog
  url: https://www.tryprofound.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cooper-square-technologies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryprofound.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tryprofound.com/rest-api/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryprofound.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.tryprofound.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.tryprofound.com/welcome
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tryprofound.com/legal/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/profound-external-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/profound-external-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/profound-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/profound-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/profound/
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@profoundai/client
- group: agent
  title: ''
  type: MCPServer
  url: mcp/profound-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/profound-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/profound-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/profound-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/profound-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/profound-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/profound-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/profound-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/profound-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/profound-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/profound-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/profound-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/profound-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profound-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/profound-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/profound-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profound-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/profound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tryprofound.com/vulnerability-reporting
- group: auth
  title: ''
  type: TrustCenter
  url: security/profound-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tryprofound.com
created: '2026-07-17'
description: Profound is a marketing platform for the AI era and a leading platform for Answer Engine Optimization (AEO). Operated by Cooper Square Technologies Inc. (dba Profound) in New York, it helps brands measure and improve how they are represented across AI answer engines and assistants — ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews and AI Mode, Copilot, and Grok — through answer-engine insights, agent analytics, prompt volumes, shopping visibility, and content optimization. Profound publishes a 125-operation OpenAPI 3.1 for its External API at api.tryprofound.com, runs a separate Agent Analytics Ingestion API, ships official Python and TypeScript SDKs, and operates a hosted remote MCP server at mcp.tryprofound.com with OAuth 2.1 and a conformant A2A agent card. API access is included on the Enterprise plan on request. Profound is SOC 2 and HIPAA aligned and publishes a responsible-disclosure policy. Backed by Kleiner Perkins.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/profound.png
layout: provider
mcp_servers:
- description: ''
  name: Profound MCP Server
  slug: profound-mcp-server
modified: '2026-08-13'
name: Profound
nav: Providers
network: true
overview: 'Profound publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Beta API, Bot Traffic Reports API, and 12 more. Tagged areas include Company, Artificial Intelligence, Answer Engine Optimization, AEO, and AI Search.


  Profound''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Profound Plans Pricing
  plan_count: 3
  slug: profound-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Profound Rate Limits
  slug: profound-rate-limits
scopes:
- name: Profound Scopes
  scope_count: 4
  slug: profound-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 4.5
    contract_quality: 54.7
    developer_ergonomics: 81.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/screenshots/profound-2026-08-17T080414.png
security:
- kind: authentication
  name: Profound Authentication
  slug: profound-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Profound Domain Security
  slug: profound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Profound Vulnerability Disclosure
  slug: profound-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Profound Trust Center
  slug: profound-trust-center
  summary_line: SOC 2, HIPAA
slug: profound
tags:
- Company
- Artificial Intelligence
- Answer Engine Optimization
- AEO
- AI Search
- Generative Engine Optimization
- Marketing
- Analytics
- Agent Analytics
- Brand Visibility
- Citations
- MCP
website: https://www.tryprofound.com
---
