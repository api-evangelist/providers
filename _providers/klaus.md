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
  - '{''url'': ''https://www.klausapp.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.zendesk.com/service/quality-assurance/ — a different registrable domain (klausapp.com -> zendesk.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://yoursubdomain.zendesk.com/qa
  baseurl_source: declared
  description: The PubImportApi API from Klaus — 3 operation(s) for pubimportapi.
  name: Klaus PubImportApi API
  slug: klaus-pubimportapi-api
- baseURL: https://yoursubdomain.zendesk.com/qa
  baseurl_source: declared
  description: The PublicExportApi API from Klaus — 18 operation(s) for publicexportapi.
  name: Klaus PublicExportApi API
  slug: klaus-publicexportapi-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public Export PubImportApi API
  slug: open-klaus-pubimportapi-api
- collection_type: open
  name: Public Export PubImportApi PublicExportApi API
  slug: open-klaus-publicexportapi-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/zendesk/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/klaus-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/klaus-public-export-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.klausapp.com/
- group: other
  title: ''
  type: ProductPage
  url: https://www.zendesk.com/service/quality-assurance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zendesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.zendesk.com/hc/en-us/sections/6999625340058-Using-Zendesk-QA
- group: docs
  title: ''
  type: APIReference
  url: https://pub.klausapp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.zendesk.com/hc/en-us/articles/10093676975898-Getting-started-with-Zendesk-QA-Admin-guide
- group: operate
  title: ''
  type: Support
  url: https://support.zendesk.com/hc/en-us/articles/4408843597850-Contacting-Zendesk-customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.zendesk.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klausapp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zendesk.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.zendesk.com/register/
- group: start
  title: ''
  type: Login
  url: https://www.zendesk.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zendesk.com/company/agreements-and-terms/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zendesk.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://support.zendesk.com/hc/en-us/articles/10049464191258-Announcing-the-removal-of-Klaus-surveys-and-the-Zendesk-QA-conversations-Insights-view
- group: auth
  title: ''
  type: Security
  url: https://www.zendesk.com/company/policies-and-guidelines/responsible-disclosure-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.zendesk.com/trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.zendesk.com/trust-center/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/klaus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klaus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klaus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klaus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/klaus-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/klaus-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klaus-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klaus-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/klaus-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klaus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/klaus-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/klaus-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klaus-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klaus-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Klaus is an AI-powered conversation review and quality assurance (QA) platform for customer support teams, founded in Tallinn, Estonia in 2019 and acquired by Zendesk in 2023, where it now ships as Zendesk QA. The product samples support conversations from connected help desks, scores them against configurable scorecards and rating categories, runs AutoQA checks, tracks disputes and calibration sessions, measures CSAT, and delivers coaching, quizzes and agent-performance dashboards. Klaus exposes two public REST APIs — a Public Import API for pushing conversations and users into QA from a custom help desk, and a Public Export API for pulling reviews, AutoQA ratings, CSAT, disputes, calibration sessions, scorecards, quizzes and users back out for external analysis. Both are documented as Swagger 2.0 specifications at pub.klausapp.com and authenticated with a bearer API token issued from a Zendesk QA custom integration.
image: https://d1eipm3vz40hy0.cloudfront.net/images/logos/favicons/zendesk-image.png
layout: provider
modified: '2026-07-19'
name: Klaus
nav: Providers
network: true
overview: 'Klaus publishes 2 APIs on the [APIs.io](https://apis.io/) network: PubImportApi API and PublicExportApi API. Tagged areas include Company, Quality Assurance, Customer-Support, Customer Experience, and Conversation Analytics.


  Klaus'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 4
  name: Klaus Rate Limits
  slug: klaus-rate-limits
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 44.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 53.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klaus/refs/heads/main/screenshots/klaus-2026-07-25T223939.png
security:
- kind: authentication
  name: Klaus Authentication
  slug: klaus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Klaus Domain Security
  slug: klaus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Klaus Vulnerability Disclosure
  slug: klaus-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Klaus Trust Center
  slug: klaus-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, ISO 27017:2015, ISO 27018:2019, ISO 27701:2019, ISO 42001, FedRAMP LI-SaaS, CSA STAR AI Levels 1 & 2, HIPAA (BAA available), HDS
slug: klaus
tags:
- Company
- Quality Assurance
- Customer-Support
- Customer Experience
- Conversation Analytics
- Contact Center
- Coaching
- Artificial Intelligence
- Software-as-a-Service
website: https://www.klausapp.com/
---
