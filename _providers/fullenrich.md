---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fullenrich Agentic Access
  operation_count: 10
  slug: fullenrich-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://app.fullenrich.com/api/v2
  baseurl_source: declared
  description: Submit up to 100 contacts per request for asynchronous waterfall enrichment across 25+ data sources, then collect the most probable work email, personal email and mobile phone by webhook or by polling
  name: FullEnrich Contact Enrichment API
  slug: fullenrich-contact-enrichment-api
- baseURL: https://app.fullenrich.com/api/v2
  baseurl_source: declared
  description: Resolve the person and company behind one or more email addresses in bulk, asynchronously, returning the full profile and employment history.
  name: FullEnrich Reverse Email Lookup API
  slug: fullenrich-reverse-email-lookup-api
- baseURL: https://app.fullenrich.com/api/v2
  baseurl_source: declared
  description: Synchronously search 800M people and 50M companies with structured filters across role, seniority, function, industry, location, company size and more. Values within a field are OR'd; fields are AND'd
  name: FullEnrich Search API
  slug: fullenrich-search-api
- baseURL: https://app.fullenrich.com/api/v2
  baseurl_source: declared
  description: Look up a single best-matching person or company from deterministic identifiers — professional network URL or ID, company domain, or full name plus a company identifier.
  name: FullEnrich Lookup API
  slug: fullenrich-lookup-api
- baseURL: https://app.fullenrich.com/api/v2
  baseurl_source: declared
  description: Check the workspace credit balance before spending, and validate that an API key is active. Both operations are free.
  name: FullEnrich Account API
  slug: fullenrich-account-api
- description: First-party remote Model Context Protocol server exposing 13 tools for B2B contact and company search, waterfall enrichment, and CSV/JSON export. Streamable HTTP transport with browser OAuth against a
  name: FullEnrich MCP Server
  slug: fullenrich-mcp-server
artifact_total: 22
asyncapis:
- description: ''
  name: Fullenrich Webhooks
  slug: fullenrich-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FullEnrich Account API
  slug: open-fullenrich-account-api
- collection_type: open
  name: FullEnrich Account Contact Enrichment API
  slug: open-fullenrich-contact-enrichment-api
- collection_type: open
  name: FullEnrich Account Reverse Email Lookup API
  slug: open-fullenrich-reverse-email-lookup-api
- collection_type: open
  name: FullEnrich API
  slug: open-fullenrich
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/fullenrich-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fullenrich-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fullenrich-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/fullenrich-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fullenrich-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fullenrich-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fullenrich-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fullenrich-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fullenrich-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fullenrich-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fullenrich-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fullenrich-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fullenrich-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fullenrich.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fullenrich-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/fullenrich-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fullenrich-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://fullenrich.com/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/fullenrich-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/FullEnrich/fullenrich-skills/blob/HEAD/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fullenrich-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fullenrich-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fullenrich-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fullenrich-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fullenrich-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fullenrich-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fullenrich.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fullenrich.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fullenrich.com/api/v2/general/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fullenrich.com/api/v2/implement-in-product/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.fullenrich.com
- group: company
  title: ''
  type: Blog
  url: https://fullenrich.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FullEnrich
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fullenrich
- group: company
  title: ''
  type: Website
  url: https://fullenrich.com
- group: commercial
  title: ''
  type: Pricing
  url: https://fullenrich.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fullenrich.com/app/signUp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fullenrich.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fullenrich.com/privacy-policy
created: '2026-07-01'
description: FullEnrich is a B2B contact enrichment platform that finds verified business emails, personal emails and mobile phone numbers by running a waterfall across 25+ data vendors, billing credits only when data is found and passes verification. Its v2 REST API covers four surfaces — asynchronous bulk contact enrichment, bulk reverse email lookup, and synchronous people/company search and lookup across 800M people and 50M companies. Alongside the REST API it operates a first-party remote MCP server with 13 tools, publishes nine MIT-licensed Agent Skills, serves an A2A agent card, and maintains a machine-readable pricing document written for AI agents to read.
finops:
- name: Fullenrich Finops
  service_category: Data and Analytics
  slug: fullenrich-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fullenrich.png
layout: provider
mcp_servers:
- description: FullEnrich operates a first-party remote MCP server that exposes B2B contact and company search, waterfall enrichment, and CSV/JSON export to MCP-capable agents. Transport is Streamable HTTP; authenti
  name: FullEnrich MCP Server
  slug: fullenrich-mcp-server
modified: '2026-08-14'
name: FullEnrich
nav: Providers
network: true
overview: 'FullEnrich publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contact Enrichment API, Reverse Email Lookup API, Search API, and 2 more. Tagged areas include B2B Data, Contact Enrichment, Email Finder, Phone Finder, and Waterfall Enrichment.


  The FullEnrich catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FullEnrich''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Fullenrich Plans Pricing
  plan_count: 3
  slug: fullenrich-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Fullenrich Rate Limits
  slug: fullenrich-rate-limits
scopes:
- name: Fullenrich Scopes
  scope_count: 14
  slug: fullenrich-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 67.1
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fullenrich/refs/heads/main/screenshots/fullenrich-2026-07-25T215257.png
security:
- kind: authentication
  name: Fullenrich Authentication
  slug: fullenrich-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Fullenrich Domain Security
  slug: fullenrich-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fullenrich Vulnerability Disclosure
  slug: fullenrich-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Fullenrich Trust Center
  slug: fullenrich-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: fullenrich
tags:
- B2B Data
- Contact Enrichment
- Email Finder
- Phone Finder
- Waterfall Enrichment
- Sales Intelligence
- People Search
- Company Search
- Reverse Email Lookup
- Agent Ready
website: https://fullenrich.com
---
