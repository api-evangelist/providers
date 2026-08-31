---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Browserbase Agentic Access
  operation_count: 17
  slug: browserbase-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 1
apis:
- description: The Contexts API from Browserbase — 2 operation(s) for contexts.
  name: Browserbase Contexts API
  slug: browserbase-contexts-api
- description: The Extensions API from Browserbase — 2 operation(s) for extensions.
  name: Browserbase Extensions API
  slug: browserbase-extensions-api
- description: The Projects API from Browserbase — 3 operation(s) for projects.
  name: Browserbase Projects API
  slug: browserbase-projects-api
- description: The Sessions API from Browserbase — 6 operation(s) for sessions.
  name: Browserbase Sessions API
  slug: browserbase-sessions-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Browserbase Contexts API
  slug: open-browserbase-contexts-api
- collection_type: open
  name: Browserbase Contexts Extensions API
  slug: open-browserbase-extensions-api
- collection_type: open
  name: Browserbase Contexts Projects API
  slug: open-browserbase-projects-api
- collection_type: open
  name: Browserbase Contexts Sessions API
  slug: open-browserbase-sessions-api
- collection_type: open
  name: Browserbase API
  slug: open-browserbase
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/browserbase/mcp-server-browserbase/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/browserbase/mcp-server-browserbase/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/browserbase/mcp-server-browserbase/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/browserbase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/browserbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/browserbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/browserbase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.browserbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.browserbase.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.browserbase.com/reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.browserbase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/browserbase
- group: commercial
  title: ''
  type: Pricing
  url: https://www.browserbase.com/pricing
- group: other
  title: ''
  type: Enterprise
  url: https://www.browserbase.com/enterprise
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.browserbase.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.browserbase.com
- group: start
  title: ''
  type: Signup
  url: https://www.browserbase.com/sign-up
- group: company
  title: ''
  type: Careers
  url: https://www.browserbase.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.browserbase.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.browserbase.com/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.browserbase.com/llms.txt
created: '2026-05-23'
description: Browserbase is a browser-agent platform that provides managed, headless Chromium browsers and supporting web primitives for AI agents and automation workloads. Customers use a single API key to spin up sessions, fetch and search the web, persist context, route LLM calls, and observe agent behavior across replays and logs. The company maintains the popular open-source Stagehand SDK, a Director UI for agent design, a Browse CLI, and an MCP server. Target customers are AI startups, agent developers, RPA teams, and enterprises running production web automation, with SOC 2 Type II and HIPAA options. Billing is usage-based with a free tier and paid plans on the pricing page.
examples:
- key_count: 2
  name: Browserbase Create Context Example
  slug: browserbase-create-context-example
- key_count: 2
  name: Browserbase Create Session Example
  slug: browserbase-create-session-example
- key_count: 2
  name: Browserbase Get Session Debug Example
  slug: browserbase-get-session-debug-example
- key_count: 2
  name: Browserbase Get Session Example
  slug: browserbase-get-session-example
- key_count: 2
  name: Browserbase List Projects Example
  slug: browserbase-list-projects-example
finops:
- name: Browserbase Finops
  service_category: API
  slug: browserbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/browserbase.png
json_schemas:
- name: Browserbase Context
  property_count: 8
  slug: browserbase-context
- name: Browserbase Project
  property_count: 7
  slug: browserbase-project
- name: Browserbase Session
  property_count: 0
  slug: browserbase-session
json_structures:
- name: Browserbase Context Structure
  property_count: 6
  slug: browserbase-context-structure
- name: Browserbase Project Structure
  property_count: 7
  slug: browserbase-project-structure
- name: Browserbase Session Structure
  property_count: 12
  slug: browserbase-session-structure
jsonld:
- class_count: 0
  name: Browserbase Context
  property_count: 5
  slug: browserbase-context
layout: provider
modified: '2026-05-25'
name: Browserbase
nav: Providers
network: true
overview: 'Browserbase publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contexts API, Extensions API, Projects API, and 1 more. Tagged areas include Headless Browser, Browser Infrastructure, Web Automation, AI Agents, and Web Scraping.


  The Browserbase catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Browserbase''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, changelog, signup flow, and 14 more developer resources.'
plans:
- name: Browserbase Plans Pricing
  plan_count: 1
  slug: browserbase-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Browserbase Rate Limits
  slug: browserbase-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Browserbase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: browserbase-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Browserbase API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 5
  slug: browserbase-rules
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -4.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 28.8
    contract_quality: 57.8
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 55.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/browserbase/refs/heads/main/screenshots/browserbase-2026-06-20T173725.png
security:
- kind: authentication
  name: Browserbase Authentication
  slug: browserbase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Browserbase Domain Security
  slug: browserbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Browserbase Vulnerability Disclosure
  slug: browserbase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: browserbase
tags:
- Headless Browser
- Browser Infrastructure
- Web Automation
- AI Agents
- Web Scraping
- Stagehand
- Playwright
- Puppeteer
- Web Search
- Web Fetch
- Model Gateway
- MCP
- Session Recording
- Agent Identity
website: https://www.browserbase.com
---
