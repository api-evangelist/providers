---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Agents API from DialNexa — 2 operation(s) for agents.
  name: DialNexa Agents API
  slug: dialnexa-agents-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Batch Calls API from DialNexa — 3 operation(s) for batch calls.
  name: DialNexa Batch Calls API
  slug: dialnexa-batch-calls-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Calls API from DialNexa — 2 operation(s) for calls.
  name: DialNexa Calls API
  slug: dialnexa-calls-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Knowledge Base API from DialNexa — 2 operation(s) for knowledge base.
  name: DialNexa Knowledge Base API
  slug: dialnexa-knowledge-base-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Languages API from DialNexa — 2 operation(s) for languages.
  name: DialNexa Languages API
  slug: dialnexa-languages-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The LLMs API from DialNexa — 3 operation(s) for llms.
  name: DialNexa LL Ms API
  slug: dialnexa-llms-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Organization Folders API from DialNexa — 2 operation(s) for organization folders.
  name: DialNexa Organization Folders API
  slug: dialnexa-organization-folders-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Phone Numbers API from DialNexa — 8 operation(s) for phone numbers.
  name: DialNexa Phone Numbers API
  slug: dialnexa-phone-numbers-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Transcribers API from DialNexa — 3 operation(s) for transcribers.
  name: DialNexa Transcribers API
  slug: dialnexa-transcribers-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Voices API from DialNexa — 5 operation(s) for voices.
  name: DialNexa Voices API
  slug: dialnexa-voices-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Webhooks API from DialNexa — 2 operation(s) for webhooks.
  name: DialNexa Webhooks API
  slug: dialnexa-webhooks-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Workflow Leads API from DialNexa — 4 operation(s) for workflow leads.
  name: DialNexa Workflow Leads API
  slug: dialnexa-workflow-leads-api
- baseURL: https://api.dialnexa.com
  baseurl_source: declared
  description: The Workflows API from DialNexa — 3 operation(s) for workflows.
  name: DialNexa Workflows API
  slug: dialnexa-workflows-api
artifact_total: 20
asyncapis:
- description: ''
  name: Dialnexa Webhooks
  slug: dialnexa-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dialnexa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dialnexa-authentication.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/dialnexa-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dialnexa-llms.txt
- group: company
  title: ''
  type: Website
  url: https://dialnexa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dialnexa.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/dialnexa-plans-pricing.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dialnexa-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dialnexa-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dialnexa-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dialnexa-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dialnexa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dialnexa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dialnexa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/dialnexa-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dialnexa-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dialnexa-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dialnexa-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/dialnexa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dialnexa-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dialnexa-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dialnexa-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dialnexa-api-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://dialnexa.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dialnexa.com/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://dialnexa.com/docs/api-reference/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dialnexa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dialnexa.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://dialnexa.com/blogs/
- group: start
  title: ''
  type: SignUp
  url: https://app.dialnexa.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dialnexa
- group: operate
  title: ''
  type: Support
  url: https://dialnexa.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://dialnexa.com/pricing
created: '2026-08-21'
description: DialNexa is a Voice AI agents platform for sales calls, lead qualification, follow-ups, meeting booking, collections and support workflows, with a strong focus on Indian-market multilingual calling (English, Hindi, Hinglish, Marathi, Kannada, Gujarati, Tamil, Telugu, Bengali and mixed-language calls). The public contract is an OpenAPI 3.0 document of 43 paths and 56 operations served from api.dialnexa.com with bearer authentication. DialNexa publishes an RFC 9727 api-catalog as a proper application/linkset+json document, two llms.txt files (a site index and a 90KB documentation index), an auth.md written explicitly for AI agents and automation systems describing how API keys are provisioned, an official remote MCP server at api.dialnexa.com/v1/mcp (OAuth 2.1 with PKCE, 97 documented tools), and a provider-published Agent Skill served from /.well-known/agent-skills/.
layout: provider
mcp_servers:
- description: Official hosted remote MCP server for the DialNexa Voice AI platform. Implements stateless MCP Streamable HTTP at https://api.dialnexa.com/v1/mcp with OAuth 2.1 (authorization-code + PKCE, workspace s
  name: DialNexa MCP Server
  slug: dialnexa-mcp-server
modified: '2026-09-03'
name: DialNexa
nav: Providers
network: true
overview: 'DialNexa publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Batch Calls API, Calls API, and 10 more. Tagged areas include Voice AI, AI Agents, Telephony, Lead Qualification, and Multilingual.


  The DialNexa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DialNexa''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, engineering blog, signup flow, and 27 more developer resources.'
plans:
- name: Dialnexa Plans Pricing
  plan_count: 3
  slug: dialnexa-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Dialnexa Rate Limits
  slug: dialnexa-rate-limits
scopes:
- name: Dialnexa Scopes
  scope_count: 0
  slug: dialnexa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 66.6
    developer_ergonomics: 78.6
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 62.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dialnexa/refs/heads/main/screenshots/dialnexa-2026-09-02T145252.png
security:
- kind: authentication
  name: Dialnexa Authentication
  slug: dialnexa-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dialnexa Domain Security
  slug: dialnexa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dialnexa
tags:
- Voice AI
- AI Agents
- Telephony
- Lead Qualification
- Multilingual
website: https://dialnexa.com
---
