---
access_model:
  confidence: high
  label: Sales-assisted, with published list pricing
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans/pardot-plans-pricing.yml
  - https://www.salesforce.com/marketing/b2b-automation/pricing/
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pardot Agentic Access
  operation_count: 35
  slug: pardot-agentic-access
  summary_line: 35 operations · 11 acting
api_count: 1
apis:
- description: Version 5 REST API for managing prospects, accounts, campaigns, emails, forms, lists, and engagement programs in Marketing Cloud Account Engagement. Authentication uses Salesforce OAuth 2.0 with the p
  name: Account Engagement API v5
  slug: account-engagement-api-v5
- description: Legacy v3/v4 REST API endpoints for Pardot resources. Still supported for many objects not yet migrated to v5; uses the same Salesforce OAuth 2.0 authentication scheme.
  name: Account Engagement API v3/v4 (Legacy)
  slug: account-engagement-api-v4
- description: The Objects API from Salesforce Marketing Cloud Account Engagement (Pardot) — 24 operation(s) for objects.
  name: Salesforce Marketing Cloud Account Engagement (Pardot) Objects API
  slug: pardot-objects-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Account Engagement (Pardot) API v5 Objects API
  slug: open-pardot-objects-api
- collection_type: open
  name: Salesforce Account Engagement (Pardot) API v5
  slug: open-pardot
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pardot-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pardot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pardot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pardot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pardot-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pardot
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/marketing/b2b-automation/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/marketing/b2b-automation/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.salesforce.com/form/signup/freetrial-b2bma/
- group: auth
  title: ''
  type: Security
  url: security/pardot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pardot-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pardot-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pardot-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pardot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pardot-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pardot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.salesforce.com/docs/marketing/pardot/guide/transitioning-v5.html
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pardot-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pardot-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pardot-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/pardot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pardot-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pardot-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/pardot-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pardot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pardot-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pardot-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: XMLSchema
  url: schemas/pardot-schemas.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/pardot/postman-pardot-apis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.salesforce.com/docs/marketing/pardot/guide/version5overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/marketing/pardot/guide/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/s/articleView?id=sf.bundle_pardot_parent.htm&type=5
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pardot/api-schemas
created: '2026-05-11'
description: Salesforce Marketing Cloud Account Engagement, formerly known as Pardot, is a B2B marketing automation platform tightly integrated with Salesforce CRM for lead generation, lead nurturing, email marketing, and marketing ROI reporting. The platform provides campaigns, forms, landing pages, dynamic content, lead scoring/grading, and Engagement Studio for multi-step nurture programs. Version 5 of the Account Engagement REST API uses Salesforce OAuth 2.0 authentication and requires a Business Unit ID header, with hosts at pi.pardot.com (production) and pi.demo.pardot.com (sandbox).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pardot.png
layout: provider
mcp_servers:
- description: ''
  name: Salesforce Marketing Cloud Account Engagement (Pardot) MCP Server
  slug: salesforce-marketing-cloud-account-engagement-pardot-mcp-server
modified: '2026-08-21'
name: Salesforce Marketing Cloud Account Engagement (Pardot)
nav: Providers
network: true
overview: 'Salesforce Marketing Cloud Account Engagement (Pardot) publishes 1 API on the [APIs.io](https://apis.io/) network: Objects API. Tagged areas include Marketing Automation, B2B Marketing, Lead Generation, Email Marketing, and Salesforce.


  Salesforce Marketing Cloud Account Engagement (Pardot)''s developer surface includes authentication, documentation, pricing, signup flow, sandbox, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Pardot Plans Pricing
  plan_count: 4
  slug: pardot-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Pardot Rate Limits
  slug: pardot-rate-limits
scopes:
- name: Pardot Scopes
  scope_count: 1
  slug: pardot-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 15.3
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pardot/refs/heads/main/screenshots/pardot-2026-06-20T191406.png
security:
- kind: authentication
  name: Pardot Authentication
  slug: pardot-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pardot Domain Security
  slug: pardot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pardot Vulnerability Disclosure
  slug: pardot-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Pardot Trust Center
  slug: pardot-trust-center
  summary_line: C5 (ISAE 3000), CCCS Assessment - Protected B, CJIS, CSA STAR, DoD IL2, DoD IL4, DoD IL5, EU Cloud Code of Conduct, FedRAMP High, FedRAMP Moderate, GDPR, HIPAA, HITRUST, IRAP, ISMAP, ISO 22301, ISO 27001, ISO 27017, ISO 27018, ISO 42001, ISO 9001, NEN 7510, NIST SP 800-171, PCI DSS, PrivacyMark, SOC 1, SOC 2, SOC 3, Salesforce BCRs, TISAX, TX-RAMP, U.S. Data Privacy Framework (DPF), WCAG 2.2 AA
slug: pardot
tags:
- Marketing Automation
- B2B Marketing
- Lead Generation
- Email Marketing
- Salesforce
- Account Engagement
website: https://www.salesforce.com/marketing/b2b-automation/
---
