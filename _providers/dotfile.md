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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Dotfile Agentic Access
  operation_count: 100
  slug: dotfile-agentic-access
  summary_line: 100 operations · 57 acting
api_count: 27
apis:
- description: The Activities API from Dotfile — 1 operation(s) for activities.
  name: Dotfile Activities API
  slug: dotfile-activities-api
- description: The AML check API from Dotfile — 5 operation(s) for aml check.
  name: Dotfile AML check API
  slug: dotfile-aml-check-api
- description: The Cases API from Dotfile — 10 operation(s) for cases.
  name: Dotfile Cases API
  slug: dotfile-cases-api
- description: The Checks API from Dotfile — 2 operation(s) for checks.
  name: Dotfile Checks API
  slug: dotfile-checks-api
- description: The Client portal API from Dotfile — 3 operation(s) for client portal.
  name: Dotfile Client portal API
  slug: dotfile-client-portal-api
- description: The Companies API from Dotfile — 4 operation(s) for companies.
  name: Dotfile Companies API
  slug: dotfile-companies-api
- description: The Company data API from Dotfile — 6 operation(s) for company data.
  name: Dotfile Company data API
  slug: dotfile-company-data-api
- description: The Company Monitoring check API from Dotfile — 1 operation(s) for company monitoring check.
  name: Dotfile Company Monitoring check API
  slug: dotfile-company-monitoring-check-api
- description: The Custom properties API from Dotfile — 2 operation(s) for custom properties.
  name: Dotfile Custom properties API
  slug: dotfile-custom-properties-api
- description: The Document check API from Dotfile — 6 operation(s) for document check.
  name: Dotfile Document check API
  slug: dotfile-document-check-api
- description: The eKYC check API from Dotfile — 3 operation(s) for ekyc check.
  name: Dotfile eKYC check API
  slug: dotfile-ekyc-check-api
- description: The Electronic Signature check API from Dotfile — 3 operation(s) for electronic signature check.
  name: Dotfile Electronic Signature check API
  slug: dotfile-electronic-signature-check-api
- description: The Files API from Dotfile — 2 operation(s) for files.
  name: Dotfile Files API
  slug: dotfile-files-api
- description: The Fraud database check API from Dotfile — 3 operation(s) for fraud database check.
  name: Dotfile Fraud database check API
  slug: dotfile-fraud-database-check-api
- description: The ID Document check API from Dotfile — 4 operation(s) for id document check.
  name: Dotfile ID Document check API
  slug: dotfile-id-document-check-api
- description: The ID Verification check API from Dotfile — 4 operation(s) for id verification check.
  name: Dotfile ID Verification check API
  slug: dotfile-id-verification-check-api
- description: The Individuals API from Dotfile — 3 operation(s) for individuals.
  name: Dotfile Individuals API
  slug: dotfile-individuals-api
- description: The Notes API from Dotfile — 2 operation(s) for notes.
  name: Dotfile Notes API
  slug: dotfile-notes-api
- description: The Online Reputation check API from Dotfile — 3 operation(s) for online reputation check.
  name: Dotfile Online Reputation check API
  slug: dotfile-online-reputation-check-api
- description: The Ping API from Dotfile — 1 operation(s) for ping.
  name: Dotfile Ping API
  slug: dotfile-ping-api
- description: The Routines API from Dotfile — 1 operation(s) for routines.
  name: Dotfile Routines API
  slug: dotfile-routines-api
- description: The Tables API from Dotfile — 2 operation(s) for tables.
  name: Dotfile Tables API
  slug: dotfile-tables-api
- description: The Tags API from Dotfile — 3 operation(s) for tags.
  name: Dotfile Tags API
  slug: dotfile-tags-api
- description: The Templates API from Dotfile — 3 operation(s) for templates.
  name: Dotfile Templates API
  slug: dotfile-templates-api
- description: The Users API from Dotfile — 2 operation(s) for users.
  name: Dotfile Users API
  slug: dotfile-users-api
- description: The Webhooks API from Dotfile — 3 operation(s) for webhooks.
  name: Dotfile Webhooks API
  slug: dotfile-webhooks-api
artifact_total: 33
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
overview: 'Dotfile publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Activities API, AML check API, Cases API, and 23 more. Tagged areas include KYB, KYC, AML, Business Verification, and Identity Verification.


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
  composite: 48.6
  coverage:
    artifact_dirs: 22
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 66.9
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 51.3
  previous_composite: 48.8
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
