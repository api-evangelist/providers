---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: GraphQL API for MSPs covering clients, tickets, assets, users, invoices, knowledge base, and service catalog. US and EU data centers.
  name: SuperOps MSP GraphQL API
  slug: superops-msp-graphql-api
- description: GraphQL API for internal IT teams covering assets, tickets, users, knowledge base, service catalog, and IT documentation. US and EU data centers.
  name: SuperOps IT GraphQL API
  slug: superops-it-graphql-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://superops.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.superops.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.superops.com/en/collections/3666305-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://support.superops.com/en/articles/6632215-how-to-integrate-applications-using-superops-ai-graphql-apis
- group: operate
  title: ''
  type: Support
  url: https://support.superops.com
- group: company
  title: ''
  type: Blog
  url: https://superops.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://superops.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://superops.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superops.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superops.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superops.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superopsai
- group: auth
  title: ''
  type: Authentication
  url: authentication/superops-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superops-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superops-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/superops-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superops-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superops-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://superops.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/superops-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/superops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://superops.com/security/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superops-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/superops-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/superops-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superops-llms.txt
created: '2026-07-17'
description: SuperOps is a unified PSA (Professional Services Automation) and RMM (Remote Monitoring and Management) platform for managed service providers (MSPs) and internal IT teams, spanning service desk and ticketing, endpoint monitoring, patch management, asset and IT documentation, project management, billing and invoicing, and AI-assisted operations. SuperOps exposes a public GraphQL API with separate MSP and IT surfaces across US and EU data centers, giving programmatic access to clients, tickets, assets, users, invoices, knowledge base, and service catalog data. Requests authenticate with a bearer API token plus a CustomerSubDomain header and are limited to 800 requests per minute.
image: https://us-west-2.graphassets.com/AsRMKMrtKTFW6TGbr4KgUz/cmo8lbrrc1xga07n3l58jhure
layout: provider
modified: '2026-07-21'
name: SuperOps
nav: Providers
network: true
overview: 'SuperOps publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, It Management Software, PSA, RMM, and MSP.


  SuperOps'' developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 2
  name: Superops Rate Limits
  slug: superops-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 40.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superops/refs/heads/main/screenshots/superops-2026-09-02T161249.png
security:
- kind: authentication
  name: Superops Authentication
  slug: superops-authentication
  summary_line: http-bearer/apiKey · 2 schemes
- kind: domain-security
  name: Superops Domain Security
  slug: superops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Superops Vulnerability Disclosure
  slug: superops-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Superops Trust Center
  slug: superops-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, HIPAA, GDPR
slug: superops
tags:
- Company
- It Management Software
- PSA
- RMM
- MSP
- Service Desk
- Endpoint Management
- IT Documentation
- GraphQL
website: https://superops.com
---
