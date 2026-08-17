---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Eruditus Executive Education Agentic Access
  operation_count: 4
  slug: eruditus-executive-education-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- description: Enrollment lead submission.
  name: Eruditus Leads API
  slug: eruditus-executive-education-leads-api
- description: Emeritus program catalog resources.
  name: Eruditus Programs API
  slug: eruditus-executive-education-programs-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Emeritus Leads API
  slug: open-eruditus-executive-education-leads-api
- collection_type: open
  name: Emeritus Programs API
  slug: open-eruditus-executive-education-programs-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/eruditus-executive-education-leads-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eruditus-executive-education-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://eruditus.com/
- group: company
  title: ''
  type: Website
  url: https://emeritus.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://emeritus-tech.github.io/emeritus-api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://emeritus-tech.github.io/emeritus-api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://emeritus-tech.github.io/emeritus-api-docs/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emeritus-tech
- group: company
  title: ''
  type: Blog
  url: https://emeritus.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://emeritus.org/connect-with-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emeritus.org/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emeritus.org/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emeritus.org/
- group: auth
  title: ''
  type: Security
  url: https://emeritus.org/reporting-a-vulnerabilities/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eruditus-executive-education-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eruditus-executive-education-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eruditus-executive-education-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eruditus-executive-education-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eruditus-executive-education-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eruditus-executive-education-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eruditus-executive-education-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eruditus-executive-education-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eruditus-executive-education-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/eruditus-executive-education-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eruditus-executive-education-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/eruditus-executive-education-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eruditus-executive-education-llms.txt
created: '2026-08-04'
description: 'Eruditus (Eruditus Group) is an online executive-education company founded in 2010 by Ashwin Damera and Chaitanya Kalipatnapu and headquartered in Singapore, operating consumer and enterprise learning under the Eruditus and Emeritus brands. It partners with more than 80 top-tier universities — including MIT, Harvard, Columbia, Wharton, Cambridge, INSEAD, IIM, NUS and HKUST — to deliver senior executive programs, professional certificates, short courses and degree programs to more than 350,000 learners across 80+ countries. Its public API surface is a small partner-facing REST estate documented at emeritus-tech.github.io/emeritus-api-docs: a Leads API for submitting B2C and B2B enrollment inquiries, and a Programs API exposing programs, partner schools and landing page templates. Both are token-authenticated with Emeritus-issued keys and offer separate staging and production environments.'
image: https://s44783.pcdn.co/wp-content/uploads/2020/12/emeritus-logo-1200-675.jpg.optimal.jpg
layout: provider
mcp_servers:
- description: ''
  name: eruditus-executive-education-mcp.yml
  slug: eruditus-executive-education-mcpyml
modified: '2026-08-04'
name: Eruditus
nav: Providers
network: true
overview: 'Eruditus publishes 2 APIs on the [APIs.io](https://apis.io/) network: Leads API and Programs API. Tagged areas include Company, Education, Online Learning, Executive Education, and EdTech.


  Eruditus'' developer surface includes documentation, getting-started guide, engineering blog, support, authentication, sandbox, and 22 more developer resources.'
random_paper: 78
score:
  band: developing
  composite: 44.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.7
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eruditus-executive-education/refs/heads/main/screenshots/eruditus-executive-education-2026-08-07T165004.png
security:
- kind: authentication
  name: Eruditus Executive Education Authentication
  slug: eruditus-executive-education-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Eruditus Executive Education Domain Security
  slug: eruditus-executive-education-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Eruditus Executive Education Vulnerability Disclosure
  slug: eruditus-executive-education-vulnerability-disclosure
  summary_line: contact published
slug: eruditus-executive-education
tags:
- Company
- Education
- Online Learning
- Executive Education
- EdTech
- Higher Education
- Leads
- Enrollment
- Programs
- Singapore
website: https://eruditus.com/
---
