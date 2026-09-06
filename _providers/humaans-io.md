---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Humaans Io Agentic Access
  operation_count: 63
  slug: humaans-io-agentic-access
  summary_line: 63 operations · 31 acting
api_count: 1
apis:
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Read-only audit trail
  name: Humaans Audit Events API
  slug: humaans-io-audit-events-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Employee bank account records
  name: Humaans Bank Accounts API
  slug: humaans-io-bank-accounts-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Tenant company record
  name: Humaans Companies API
  slug: humaans-io-companies-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Salary, bonus, and compensation history
  name: Humaans Compensations API
  slug: humaans-io-compensations-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Tenant-defined custom field definitions and values
  name: Humaans Custom Fields API
  slug: humaans-io-custom-fields-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Personal and company document storage
  name: Humaans Documents API
  slug: humaans-io-documents-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Equipment assigned to employees
  name: Humaans Equipment API
  slug: humaans-io-equipment-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Position and role definitions
  name: Humaans Job Roles API
  slug: humaans-io-job-roles-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Office and remote work locations
  name: Humaans Locations API
  slug: humaans-io-locations-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Employee records, the canonical resource of the HRIS
  name: Humaans People API
  slug: humaans-io-people-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Performance reviews, cycles, templates, and ratings
  name: Humaans Performance API
  slug: humaans-io-performance-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Time off, holidays, leave allocations, policies, and types
  name: Humaans Time Away API
  slug: humaans-io-time-away-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Timesheet entries and submissions
  name: Humaans Timesheet API
  slug: humaans-io-timesheet-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Outbound HMAC-signed event subscriptions
  name: Humaans Webhooks API
  slug: humaans-io-webhooks-api
- baseURL: https://app.humaans.io/api
  baseurl_source: declared
  description: Work schedule patterns
  name: Humaans Working Patterns API
  slug: humaans-io-working-patterns-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Humaans API
  slug: open-humaans-api
- collection_type: open
  name: Humaans Audit Events API
  slug: open-humaans-io-audit-events-api
- collection_type: open
  name: Humaans Audit Events Bank Accounts API
  slug: open-humaans-io-bank-accounts-api
- collection_type: open
  name: Humaans Audit Events Companies API
  slug: open-humaans-io-companies-api
- collection_type: open
  name: Humaans Audit Events Compensations API
  slug: open-humaans-io-compensations-api
- collection_type: open
  name: Humaans Audit Events Custom Fields API
  slug: open-humaans-io-custom-fields-api
- collection_type: open
  name: Humaans Audit Events Documents API
  slug: open-humaans-io-documents-api
- collection_type: open
  name: Humaans Audit Events Equipment API
  slug: open-humaans-io-equipment-api
- collection_type: open
  name: Humaans Audit Events Job Roles API
  slug: open-humaans-io-job-roles-api
- collection_type: open
  name: Humaans Audit Events Locations API
  slug: open-humaans-io-locations-api
- collection_type: open
  name: Humaans Audit Events People API
  slug: open-humaans-io-people-api
- collection_type: open
  name: Humaans Audit Events Performance API
  slug: open-humaans-io-performance-api
- collection_type: open
  name: Humaans Audit Events Time Away API
  slug: open-humaans-io-time-away-api
- collection_type: open
  name: Humaans Audit Events Timesheet API
  slug: open-humaans-io-timesheet-api
- collection_type: open
  name: Humaans Audit Events Webhooks API
  slug: open-humaans-io-webhooks-api
- collection_type: open
  name: Humaans Audit Events Working Patterns API
  slug: open-humaans-io-working-patterns-api
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
random_paper: 2
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 66.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Workflow-Automation
- AI Companion
- Agentic AI
- UK
- London
website: https://humaans.io
---
