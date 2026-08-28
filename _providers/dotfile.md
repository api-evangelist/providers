---
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Dotfile Agentic Access
  operation_count: 100
  slug: dotfile-agentic-access
  summary_line: 100 operations · 57 acting
api_count: 1
apis:
- description: 'REST API covering the full business-verification lifecycle: create a case with its companies, individuals and relations, launch checks by template or one at a time, read results, record a review verdi'
  name: Dotfile API
  slug: dotfile-api
artifact_total: 8
asyncapis:
- description: ''
  name: Dotfile Webhooks
  slug: dotfile-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.dotfile.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dotfile.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dotfile.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dotfile.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dotfile.com/docs/quick-start
- group: operate
  title: ''
  type: Support
  url: https://docs.dotfile.com/reference/getting-help
- group: company
  title: ''
  type: Blog
  url: https://www.dotfile.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DotfileTech
- group: start
  title: ''
  type: Login
  url: https://app.dotfile.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dotfile.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dotfile.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dotfile-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dotfile-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/dotfile-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/dotfile-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dotfile-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dotfile-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dotfile-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dotfile-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dotfile.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dotfile.com/reference/api-release-changes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dotfile-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dotfile-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dotfile-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dotfile-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dotfile.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dotfile-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotfile-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dotfile-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dotfile-api-overlay.yaml
- group: design
  title: ''
  type: Components
  url: components/dotfile-components.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dotfile-agentic-access.yml
created: '2026-08-17'
description: 'Dotfile is a French (Paris-based) end-to-end business verification platform that automates KYB, KYC and AML compliance for regulated and high-growth companies. A single REST API and a case-management console act on the same data: a case holds the companies and individuals under verification, the checks run on them, and the decision that closes it. Nine check types are exposed — document, id_document, id_verification, ekyc, aml, company_monitoring, electronic_signature, fraud_database and online_reputation — alongside company-data search and fetch against official registries, document ordering, risk scoring, periodic review, templates, tables, custom properties, white-label client portals, tags, activities and an autonomous "Autonomy" agent routine trigger. The API is 100 operations over 82 paths, keyed with an X-DOTFILE-API-KEY header, and reports check outcomes asynchronously through 46 subscribable webhook events.'
image: https://cdn.sanity.io/images/cfd7mhkz/production/be810f412f56503cdfcd6aa0e33debc99b73f00b-14528x7688.png?rect=0,31,14528,7627&w=1200&h=630
layout: provider
modified: '2026-08-17'
name: Dotfile
nav: Providers
network: true
overview: 'Dotfile publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include KYB, KYC, AML, Business Verification, and Identity Verification.


  The Dotfile catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dotfile''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 26 more developer resources.'
plans:
- name: Dotfile Plans Pricing
  plan_count: 0
  slug: dotfile-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Dotfile Rate Limits
  slug: dotfile-rate-limits
score:
  band: developing
  composite: 50.9
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 16.7
    contract_quality: 68.3
    developer_ergonomics: 47.0
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 51.3
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Dotfile Authentication
  slug: dotfile-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dotfile Domain Security
  slug: dotfile-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Dotfile Trust Center
  slug: dotfile-trust-center
  summary_line: SOC 2, GDPR
slug: dotfile
tags:
- KYB
- KYC
- AML
- Business Verification
- Identity Verification
- Compliance
- RegTech
- Onboarding
- Sanctions Screening
- Document Verification
- Fraud Detection
- Company Data
- Beneficial Ownership
- Case Management
- Electronic Signature
- Webhook
website: https://www.dotfile.com/
---
