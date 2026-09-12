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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Docontrol Agentic Access
  operation_count: 2
  slug: docontrol-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: DoControl is a SaaS data security platform providing automated data access governance, DLP, and insider threat prevention for cloud applications.
  name: DoControl
  slug: docontrol
- baseURL: https://auth.prod.docontrol.io
  baseurl_source: declared
  description: The Authentication API from DoControl — 1 operation(s) for authentication.
  name: DoControl Authentication API
  slug: docontrol-authentication-api
- baseURL: https://apollo-gateway-v4-api.prod.docontrol.io
  baseurl_source: declared
  description: The GraphQL API from DoControl — 1 operation(s) for graphql.
  name: DoControl GraphQL API
  slug: docontrol-graphql-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DoControl Authentication API
  slug: open-docontrol-authentication-api
- collection_type: open
  name: DoControl Authentication GraphQL API
  slug: open-docontrol-graphql-api
- collection_type: open
  name: DoControl API
  slug: open-docontrol
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docontrol-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/docontrol-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docontrol-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docontrol-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docontrol-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/do-control
- group: company
  title: ''
  type: Website
  url: https://www.docontrol.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docontrol.io/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/docontrol-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/docontrol-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docontrol-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/docontrol-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/docontrol-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/docontrol-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/docontrol-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/docontrol-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docontrol-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docontrol.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/docontrol-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/docontrol-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/docontrol-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/docontrol-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docontrol-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: security/docontrol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/docontrol-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.docontrol.io/docontrol-user-guide/system-management/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.docontrol.io/docontrol-user-guide/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.docontrol.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.docontrol.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docontrol.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docontrol.io/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://app.docontrol.io
created: '2026-03-27'
description: DoControl is a SaaS data security platform providing automated data access governance, data loss prevention, insider risk management, shadow-app discovery and misconfiguration management across connected cloud applications including Google Workspace, Microsoft 365, Salesforce, Slack, Box, Dropbox, Zoom, Jira and GitHub. Its public programmable surface is a single Apollo GraphQL gateway at apollo-gateway-v4-api.prod.docontrol.io, reached with a five-minute bearer token exchanged from a console-issued API key at auth.prod.docontrol.io, and DoControl ships a first-party MCP server (dc-mcp-server) that exposes that graph to agents over stdio. Spin.AI announced its acquisition of DoControl on 2026-09-01, stating that the DoControl product, site, contracts and support are unchanged and that the brands operate independently.
finops:
- name: Docontrol Finops
  service_category: API
  slug: docontrol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docontrol.png
layout: provider
mcp_servers:
- description: DoControl publishes a first-party MCP server, dc-mcp-server, from its own GitHub organization. It is a DoControl-maintained fork of apollographql/apollo-mcp-server (109 commits ahead of upstream at ti
  name: DoControl MCP Server
  slug: docontrol-mcp-server
modified: '2026-09-06'
name: DoControl
nav: Providers
network: true
overview: 'DoControl publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and GraphQL API. Tagged areas include Data Security, SaaS Security, Data Access Governance, Data Loss Prevention, and Insider Risk Management.


  DoControl''s developer surface includes authentication, documentation, changelog, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Docontrol Plans Pricing
  plan_count: 0
  slug: docontrol-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Docontrol Rate Limits
  slug: docontrol-rate-limits
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 51.3
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/docontrol/refs/heads/main/screenshots/docontrol-2026-06-20T180108.png
security:
- kind: authentication
  name: Docontrol Authentication
  slug: docontrol-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Docontrol Domain Security
  slug: docontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docontrol Vulnerability Disclosure
  slug: docontrol-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Docontrol Trust Center
  slug: docontrol-trust-center
  summary_line: ISO 27001, SOC 2 Type II, HIPAA, GDPR
slug: docontrol
tags:
- Data Security
- SaaS Security
- Data Access Governance
- Data Loss Prevention
- Insider Risk Management
- SSPM
- GraphQL
- MCP
website: https://www.docontrol.io
---
