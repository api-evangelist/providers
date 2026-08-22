---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Fdc3 Agentic Access
  operation_count: 21
  slug: fdc3-agentic-access
  summary_line: 21 operations · 5 acting
api_count: 6
apis:
- description: The FDC3 Desktop Agent API is the primary interface for application interoperability on the financial desktop. It provides a JavaScript/TypeScript API that applications use to open other applications,
  name: FDC3 Desktop Agent API
  slug: desktop-agent-api
- description: The FDC3 App Directory (AppD) is a REST API standard for registering and discovering financial desktop applications. Desktop Agents query App Directories to resolve application definitions when launch
  name: FDC3 App Directory API
  slug: app-directory-api
- description: FDC3 Context Data defines a standard set of typed data structures used to carry information between financial applications when broadcasting or raising intents. Context types include instruments, posi
  name: FDC3 Context Data
  slug: context-data
- description: FDC3 Intents are standardized verbs that applications use to request functionality from other applications on the financial desktop. Standard intents include ViewChart, ViewQuote, ViewNews, ViewAnalys
  name: FDC3 Intents
  slug: intents
- description: 'FDC3 Desktop Agent Bridging (DAB) is a wire protocol that enables multiple Desktop Agent implementations to interoperate, allowing applications running under different Desktop Agents to share context '
  name: FDC3 Desktop Agent Bridging
  slug: desktop-agent-bridging
- description: The Application API from FDC3 — 5 operation(s) for application.
  name: FDC3 Application API
  slug: fdc3-application-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FDC3 Directory Application API
  slug: open-fdc3-application-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/finos/FDC3/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/finos/FDC3/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/finos/FDC3/blob/main/CODE_OF_CONDUCT.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fdc3-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fdc3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fdc3-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fdc3.finos.org
- group: docs
  title: ''
  type: Documentation
  url: https://fdc3.finos.org/docs/fdc3-intro
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/finos
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/finos/FDC3
- group: operate
  title: ''
  type: Slack
  url: https://finos-lf.slack.com/messages/fdc3
- group: other
  title: ''
  type: MailingList
  url: mailto:fdc3+subscribe@finos.org
- group: operate
  title: ''
  type: Community
  url: https://www.finos.org/community
- group: company
  title: ''
  type: Blog
  url: https://www.finos.org/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/finos/FDC3/blob/main/CHANGELOG.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/finos/FDC3/blob/main/LICENSE.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/finos/FDC3/blob/main/LICENSE.md
- group: other
  title: ''
  type: Contributing
  url: https://github.com/finos/FDC3/blob/main/CONTRIBUTING.md
- group: operate
  title: ''
  type: Status
  url: https://github.com/finos/FDC3/releases
created: '2026-06-13'
description: FDC3 (Financial Desktop Connectivity and Collaboration Consortium) is an open standard hosted by FINOS for interoperability between financial desktop applications. The standard defines how applications launch other apps, share typed context data, raise and resolve intents across the financial desktop, and register themselves in an App Directory. FDC3 eliminates the need for custom bilateral agreements between software vendors and enables plug-and-play integration workflows for financial services firms. Current version is 2.2, licensed under the Community Specification License 1.0 with code released under Apache 2.0.
examples:
- key_count: 17
  name: Fdc3 Workbench App
  slug: fdc3-workbench-app
finops:
- name: Fdc3 Finops
  service_category: Open Standard / Specification
  slug: fdc3-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fdc3.png
json_schemas:
- name: Appd.Schema
  property_count: 0
  slug: appd.schema
jsonld:
- class_count: 28
  name: Fdc3 Context
  property_count: 19
  slug: fdc3-context
layout: provider
modified: '2026-06-13'
name: FDC3
nav: Providers
network: true
overview: 'FDC3 publishes 2 APIs on the [APIs.io](https://apis.io/) network: App Directory API and Application API. Tagged areas include Financial Services, Fintech, Desktop Interoperability, Open Standard, and FINOS.


  The FDC3 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FDC3''s developer surface includes authentication, documentation, engineering blog, changelog, status page, and 14 more developer resources.'
plans:
- name: Fdc3 Plans Pricing
  plan_count: 5
  slug: fdc3-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Fdc3 Rate Limits
  slug: fdc3-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FDC3 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fdc3-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.8
  delta: -6.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 63.2
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fdc3/refs/heads/main/screenshots/fdc3-2026-06-20T181104.png
security:
- kind: authentication
  name: Fdc3 Authentication
  slug: fdc3-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fdc3 Domain Security
  slug: fdc3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fdc3
tags:
- Financial Services
- Fintech
- Desktop Interoperability
- Open Standard
- FINOS
- Context Sharing
- Intents
website: https://fdc3.finos.org
---
