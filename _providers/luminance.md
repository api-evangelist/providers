---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: 'The current Luminance REST API (documented as version 1.5, "Public API v2"), deployed by standard to Luminance product versions 1.43.0 onward. 62 paths / 94 operations across System, Users, Projects, '
  name: Luminance Public API v2
  slug: luminance-public-api-v2
- description: Luminance REST API version 1.4.0, deployed by standard to earlier Luminance product versions. 53 paths / 74 operations across Accounts, Users, Projects, Tasks, Reviews, Folders, Documents, Annotations
  name: Luminance API v1.4.0
  slug: luminance-api-v140
- description: Luminance REST API version 1.3.0, deployed by standard to Luminance product versions 1.37.0 to 1.42.0 inclusive. 49 paths / 67 operations across Root, Accounts, Users, Projects, Tasks, Reviews, Folder
  name: Luminance API v1.3.0
  slug: luminance-api-v130
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/luminance-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.luminance.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.luminance.com/swagger-docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.luminance.com/swagger-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.luminance.com/swagger-docsv150
- group: operate
  title: ''
  type: Support
  url: https://help.luminance.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.luminance.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.luminance.com/resources/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.luminance.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.luminance.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.luminance.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.luminance.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/luminance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/luminance-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/luminance-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/luminance-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/luminance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/luminance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/luminance-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/luminance-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/luminance-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/luminance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luminance-domain-security.yml
created: '2026-08-04'
description: 'Luminance Technologies Ltd. is a UK-headquartered legal-AI company, founded in 2015 out of Cambridge mathematics research, that builds what it markets as Legal-Grade AI for the full contract lifecycle — drafting, negotiation, analysis, compliance, investigation and collaboration. The platform is delivered as a per-customer instance (an "instance moniker" subdomain) and exposes a documented RESTful HTTP/JSON API that lets external software read and act on projects, folders, documents, matters, matter versions, tasks, reviews, annotations, workflows and document templates, plus machine-learning surfaces such as Traffic Light Analysis and annotation-driven contract intelligence. Three OpenAPI 3.0 versions are published from Luminance''s own API host: v1.3.0 and v1.4.0 (OAuth2 client-credentials) and the newer "Public API v2" v1.5, which is deployed by standard to Luminance product versions 1.43.0 onward. Authentication is OAuth2 client credentials against the customer instance
  token endpoint, and API traffic is rate limited to 100 requests every 10 minutes.'
image: https://api.luminance.com/img/general_resources/luminance_logos/Luminance-logo.png
layout: provider
modified: '2026-08-04'
name: Luminance
nav: Providers
network: true
overview: 'Luminance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Public API v2, API v1.4.0, and API v1.3.0. Tagged areas include Company, Legal, Artificial Intelligence, Contracts, and Contract Lifecycle Management.


  Luminance''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 52
rate_limits:
- limit_count: 1
  name: Luminance Rate Limits
  slug: luminance-rate-limits
scopes:
- name: Luminance Scopes
  scope_count: 0
  slug: luminance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 43.9
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 44.1
  provenance:
    conformance: first-party
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Luminance Authentication
  slug: luminance-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Luminance Domain Security
  slug: luminance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Luminance Trust Center
  slug: luminance-trust-center
  summary_line: SOC 2, ISO 27001
slug: luminance
tags:
- Company
- Legal
- Artificial Intelligence
- Contracts
- Contract Lifecycle Management
- Document Intelligence
- Compliance
- Legal Technology
- Enterprise Software
- Automation
website: https://www.luminance.com/
---
