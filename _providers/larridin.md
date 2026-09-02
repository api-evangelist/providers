---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Larridin Agentic Access
  operation_count: 41
  slug: larridin-agentic-access
  summary_line: 41 operations
api_count: 1
apis:
- description: Organization- and department-level AI adoption metrics.
  name: Larridin Adoption API
  slug: larridin-adoption-api
- description: AI proficiency scoring, prompt categories, and conversation metrics. Period-based selection.
  name: Larridin Proficiency API
  slug: larridin-proficiency-api
- description: Survey campaigns, questions, options, and responses.
  name: Larridin Surveys API
  slug: larridin-surveys-api
- description: Browser and desktop AI tool adoption, policy enforcement, and unapproved tool discovery.
  name: Larridin Tools API
  slug: larridin-tools-api
- description: Clustered workflow analysis, friction, recommendations, and tool verdicts.
  name: Larridin Workflow Intelligence API
  slug: larridin-workflow-intelligence-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Larridin Scout Adoption API
  slug: open-larridin-adoption-api
- collection_type: open
  name: Larridin Scout Adoption Proficiency API
  slug: open-larridin-proficiency-api
- collection_type: open
  name: Larridin Scout Adoption Surveys API
  slug: open-larridin-surveys-api
- collection_type: open
  name: Larridin Scout Adoption Tools API
  slug: open-larridin-tools-api
- collection_type: open
  name: Larridin Scout Adoption Workflow Intelligence API
  slug: open-larridin-workflow-intelligence-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/larridin-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/larridin-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://larridin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.larridin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.larridin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.larridin.com/api/scout-api-v1-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.larridin.com/get-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.larridin.com/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://larridin.com/contact
- group: company
  title: ''
  type: Blog
  url: https://larridin.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://larridin.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/larridin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://larridin.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://larridin.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.larridin.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.larridin.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.larridin.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/larridin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/larridin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/larridin-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/larridin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/larridin-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/larridin-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/larridin-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/larridin-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/larridin-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/larridin-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/larridin-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/larridin-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/larridin-scout-overlay.yaml
created: '2026-07-17'
description: Larridin is an enterprise AI intelligence platform that measures whether an organization's investment in AI is actually paying off across both its human and agent workforce. Its Scout product instruments AI usage through a managed browser extension and desktop agent, then joins that telemetry with source control, coding-assistant, incident, and work-tracking systems to report on AI adoption, AI fluency (proficiency), AI governance and shadow-tool risk, token spend, workflow intelligence, and Developer Intelligence — covering AI code share, velocity, quality, CI/CD delivery, reliability, agent effectiveness, agent readiness, and developer sentiment. Larridin exposes this data through the read-only Scout API v1 and a beta Model Context Protocol server for agents.
image: https://larridin.com/assets/img/logo-header.webp
layout: provider
mcp_servers:
- description: 'Larridin publishes an official Model Context Protocol server that connects AI assistants and agents to Scout. It is enabled per organization: additional tools may be enabled for an organization and ac'
  name: Larridin MCP Server
  slug: larridin-mcp-server
modified: '2026-07-19'
name: Larridin
nav: Providers
network: true
overview: 'Larridin publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Adoption API, Proficiency API, Surveys API, and 2 more. Tagged areas include Company, Artificial Intelligence, AI Adoption, AI Governance, and Analytics.


  Larridin''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, authentication, and 24 more developer resources.'
random_paper: 13
scopes:
- name: Larridin Scopes
  scope_count: 4
  slug: larridin-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/larridin/refs/heads/main/screenshots/larridin-2026-07-25T224539.png
security:
- kind: authentication
  name: Larridin Authentication
  slug: larridin-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Larridin Domain Security
  slug: larridin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Larridin Vulnerability Disclosure
  slug: larridin-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Larridin Trust Center
  slug: larridin-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: larridin
tags:
- Company
- Artificial Intelligence
- AI Adoption
- AI Governance
- Analytics
- Developer Productivity
- Developer Intelligence
- Workflow Intelligence
- Enterprise Software
- Observability
website: https://larridin.com/
---
