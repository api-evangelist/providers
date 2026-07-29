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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Humaans Io Agentic Access
  operation_count: 63
  slug: humaans-io-agentic-access
  summary_line: 63 operations · 31 acting
api_count: 15
apis:
- description: Read-only audit trail
  name: Humaans Audit Events API
  slug: humaans-io-audit-events-api
- description: Employee bank account records
  name: Humaans Bank Accounts API
  slug: humaans-io-bank-accounts-api
- description: Tenant company record
  name: Humaans Companies API
  slug: humaans-io-companies-api
- description: Salary, bonus, and compensation history
  name: Humaans Compensations API
  slug: humaans-io-compensations-api
- description: Tenant-defined custom field definitions and values
  name: Humaans Custom Fields API
  slug: humaans-io-custom-fields-api
- description: Personal and company document storage
  name: Humaans Documents API
  slug: humaans-io-documents-api
- description: Equipment assigned to employees
  name: Humaans Equipment API
  slug: humaans-io-equipment-api
- description: Position and role definitions
  name: Humaans Job Roles API
  slug: humaans-io-job-roles-api
- description: Office and remote work locations
  name: Humaans Locations API
  slug: humaans-io-locations-api
- description: Employee records, the canonical resource of the HRIS
  name: Humaans People API
  slug: humaans-io-people-api
- description: Performance reviews, cycles, templates, and ratings
  name: Humaans Performance API
  slug: humaans-io-performance-api
- description: Time off, holidays, leave allocations, policies, and types
  name: Humaans Time Away API
  slug: humaans-io-time-away-api
- description: Timesheet entries and submissions
  name: Humaans Timesheet API
  slug: humaans-io-timesheet-api
- description: Outbound HMAC-signed event subscriptions
  name: Humaans Webhooks API
  slug: humaans-io-webhooks-api
- description: Work schedule patterns
  name: Humaans Working Patterns API
  slug: humaans-io-working-patterns-api
artifact_total: 41
collections:
- collection_type: open
  name: Humaans API
  slug: open-humaans-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humaans-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/humaans-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/humaans-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humaans-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/humaans-io-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://humaans.io
- group: company
  title: ''
  type: Website
  url: https://humaans.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humaans.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humaans.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.humaans.io/api/introduction
- group: start
  title: ''
  type: Login
  url: https://app.humaans.io
- group: start
  title: ''
  type: Signup
  url: https://humaans.io/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://humaans.io/pricing
- group: auth
  title: ''
  type: Security
  url: https://humaans.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humaans.io/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humaans.io/legal/terms-of-service
- group: docs
  title: ''
  type: Documentation
  url: https://humaans.io/legal/dpa
- group: docs
  title: ''
  type: Documentation
  url: https://humaans.io/legal/sub-processors
- group: company
  title: ''
  type: Blog
  url: https://humaans.io/blog
- group: other
  title: ''
  type: CaseStudies
  url: https://humaans.io/customers
- group: company
  title: ''
  type: About
  url: https://humaans.io/about
- group: company
  title: ''
  type: Careers
  url: https://humaans.io/careers
- group: operate
  title: ''
  type: Contact
  url: https://humaans.io/contact
- group: operate
  title: ''
  type: Support
  url: mailto:hi@humaans.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humaans
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/humaans_io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humaans
- group: build
  title: ''
  type: SDKs
  url: https://github.com/humaans/figbird
- group: build
  title: ''
  type: SDKs
  url: https://github.com/humaans/next-img
- group: build
  title: ''
  type: SDKs
  url: https://github.com/humaans/react-machine
- group: build
  title: ''
  type: SDKs
  url: https://github.com/humaans/react-space-router
- group: build
  title: ''
  type: Tools
  url: https://github.com/humaans/workalendar
- group: other
  title: ''
  type: Application
  url: https://apps.apple.com/app/humaans/id1610537316
- group: other
  title: ''
  type: Application
  url: https://play.google.com/store/apps/details?id=io.humaans
- group: other
  title: ''
  type: Review
  url: https://www.g2.com/products/humaans/reviews
created: '2026-05-25T00:00:00.000Z'
description: Humaans is a London-headquartered modern HRIS (Human Resources Information System) for fast-growing, distributed teams. The platform combines a best-in-class system of record — employee directory, documents, time off, timesheets, compensation, equipment, locations, custom fields and tables, performance reviews, and onboarding/offboarding workflows — with the Athena agentic AI platform and an AI Companion that automate administrative HR work. Humaans exposes a comprehensive REST API at app.humaans.io/api with Bearer token authentication, OAuth-style scopes, $limit/$skip pagination, rich filter operators, and HMAC SHA-256 signed webhooks. The API spans 70+ documented resource categories including People, Companies, Compensations, Bank Accounts, Documents, Time Away (entries, allocations, policies, types), Equipment, Job Roles, Locations, Custom Fields and Values, Performance, Timesheet entries and submissions, Webhooks, Audit Events, and Working Patterns. Humaans ships pre-built
  integrations across payroll, identity, compliance, finance, ATS, performance, benefits, learning, and automation, plus a Zapier connector and an Apideck HRIS unified-API binding. Trusted by global teams across 300+ locations and rated 4.8/5 on G2.
features:
- REST HRIS API with consistent resource-oriented URLs, JSON in / JSON out, and standard HTTP verbs and status codes
- Bearer token authentication with OAuth-style scopes (public:read, private:read, private:write, compensations:read/write, documents:read/write, webhooks:manage)
- Role-based access control (Owner, Admin, Finance, Tech, Manager, User) reflected in API access
- Pagination via $limit (default 100, max 250) and $skip
- Rich filtering operators ($in, $nin, $gt, $gte, $lt, $lte, $or) on most collections
- 70+ documented resource categories — People, Companies, Compensations, Bank Accounts, Documents, Document Folders, Document Types, Identity Documents
- Time Away — entries, allocations, types, policies, and accruals
- Equipment, Job Roles, Locations, Custom Fields, Custom Values, Working Patterns
- Performance — reviews, cycles, templates, ratings (mostly read)
- Timesheet entries and submissions with full CRUD
- HMAC SHA-256 signed webhooks with exponential backoff retry and auto-disable after 5 days of failures
- Read-only Audit Events stream for compliance and SIEM integration
- Pre-built integrations across Payroll (Remote, Oyster, Papaya Global, Symmetrical, Payap, PayCaptain, Salary), Identity (Okta, JumpCloud, Microsoft Entra ID, Google SSO, SAML), Compliance (Vanta, Drata, Secureframe), Finance (Carta, Pulley, Pleo, Spendesk, Moss, Ramp, Pave, Ravio, Figures, Ledgy, Mesh Payments, Cledara), ATS (Greenhouse, Lever, Workable, Ashby, Teamtailor, Gem, Pinpoint, Manatal), Performance (Lattice, CultureAmp, Leapsome, Workvivo, Eletive, Officevibe, Frankli, Appraisd), Calendar/Comms (Google Calendar, Slack), eSignature (Docusign, Contractbook), Benefits (Ben, Assembly, Bonusly, Goody, Kota, Happl, CakeDrop), Learning (Sana Labs, WorkRamp, Ethena), Automation (Zapier), People Analytics (ChartHop, Insightful)
- Native Apideck HRIS unified-API connector for Humaans
- Athena agentic AI platform plus AI Companion add-on for natural-language HR queries
- Workflow automation, onboarding/offboarding sequences, and dynamic databases (custom data tables)
- 300+ global locations supported with country-specific localisation
- iOS and Android mobile apps
- SOC 2, ISO 27001, and GDPR-aligned controls; Vanta/Drata/Secureframe automation integrations
- 99.9% uptime SLA on the Enterprise plan
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/humaans-io.png
layout: provider
modified: '2026-05-25'
name: Humaans
nav: Providers
network: true
overview: 'Humaans publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Audit Events API, Bank Accounts API, Companies API, and 12 more. Tagged areas include HR, HRIS, Human Resources, People Operations, and People Analytics.


  Humaans'' developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 28 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 45.5
  delta: -2.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 53.4
    developer_ergonomics: 60.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humaans-io/refs/heads/main/screenshots/humaans-io-2026-06-20T182927.png
security:
- kind: authentication
  name: Humaans Io Authentication
  slug: humaans-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Humaans Io Domain Security
  slug: humaans-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Humaans Io Vulnerability Disclosure
  slug: humaans-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Humaans Io Trust Center
  slug: humaans-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: humaans-io
tags:
- HR
- HRIS
- Human Resources
- People Operations
- People Analytics
- Onboarding
- Offboarding
- Performance Management
- Time Off
- Compensation
- Workflow Automation
- AI Companion
- Agentic AI
- UK
- London
website: https://humaans.io
---
