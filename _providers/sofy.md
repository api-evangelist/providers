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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://public.sofy.ai
  baseurl_source: declared
  description: Upload and manage application builds under test.
  name: SOFY Applications API
  slug: sofy-applications-api
- baseURL: https://public.sofy.ai
  baseurl_source: declared
  description: Trigger, monitor, and abort scheduled test runs.
  name: SOFY Scheduled Runs API
  slug: sofy-scheduled-runs-api
artifact_total: 8
asyncapis:
- description: ''
  name: Sofy Webhooks
  slug: sofy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SOFY Public Applications API
  slug: open-sofy-applications-api
- collection_type: open
  name: SOFY Public Applications Scheduled Runs API
  slug: open-sofy-scheduled-runs-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sofy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sofy.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sofy.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sofy.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sofy.ai/schedule-runs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sofy.ai/getting-started
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sofy-public-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sofy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sofy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sofy-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sofy-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sofy-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sofy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sofy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sofy-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sofy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sofy-upload-and-run-tests.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sofy-monitor-and-abort-run.md
- group: other
  title: ''
  type: Overlay
  url: overlays/sofy-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sofy-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://sofy.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://sofy.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sofy.ai/Pricing/
- group: start
  title: ''
  type: SignUp
  url: https://web.sofy.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sofy.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sofy.ai/privacy-policy/
created: '2026-07-17'
description: 'SOFY is an AI-powered software testing platform that autonomously writes, executes, and maintains no-code tests across mobile, web, API, and enterprise applications. Testers describe intent in natural language and SOFY''s AI agents generate and self-heal the automation as the app changes, running against 2,000+ real devices in the cloud plus web and ERP surfaces (SAP, Dynamics 365). SOFY exposes a public REST API at https://public.sofy.ai for CI/CD automation (GitHub Actions, GitLab, Jenkins, Azure DevOps): upload application builds, trigger scheduled test runs, poll status, and abort runs, with outbound webhooks on run completion. SOFY is a portfolio company of 500 Global.'
image: https://web.sofy.ai/assets/icons/sofy-icon.svg
layout: provider
modified: '2026-07-21'
name: SOFY
nav: Providers
network: true
overview: 'SOFY publishes 2 APIs on the [APIs.io](https://apis.io/) network: Applications API and Scheduled Runs API. Tagged areas include Company, AI Testing, Test Automation, Mobile Testing, and QA.


  The SOFY catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SOFY''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 19 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 65.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sofy/refs/heads/main/screenshots/sofy-2026-08-17T081948.png
security:
- kind: authentication
  name: Sofy Authentication
  slug: sofy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sofy Domain Security
  slug: sofy-domain-security
  summary_line: TLSv1.3
slug: sofy
tags:
- Company
- AI Testing
- Test Automation
- Mobile Testing
- QA
- No-Code
- Continuous Testing
- DevOps
website: https://sofy.ai
---
