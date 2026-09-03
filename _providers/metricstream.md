---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
  scored_at: '2026-09-02'
api_count: 8
apis:
- description: Business REST APIs over the GRC Foundation object model — Area of Compliance, Asset, Asset Class, Control, Evidence, Exception, Financial Accounts, Function, Framework/Model Reference, Objectives, Pro
  name: MetricStream GRC Foundation APIs
  slug: metricstream-grc-foundation
- description: 'Business REST APIs for the Issues module — reporting issues and viewing issue details, so first-line users and upstream systems can flag weaknesses, gaps in internal controls and process deficiencies '
  name: MetricStream Issues APIs
  slug: metricstream-issues
- description: Business REST APIs for operational loss data — internal and external loss events, impacts, approval (loss) rules, default currency configuration and risk/regulatory event type mapping. 36 documented o
  name: MetricStream Loss Event Management APIs
  slug: metricstream-loss-event-management
- description: Business REST APIs for KRI/KPI metric definitions and metric data entry — create and maintain metric definitions and post metric data points into the GRC platform.
  name: MetricStream Metrics APIs
  slug: metricstream-metrics
- description: Business REST APIs for risk assessment tasks and the setup of risk aggregation weights used when rolling assessment scores up a risk hierarchy.
  name: MetricStream Risk Assessments APIs
  slug: metricstream-risk-assessments
- description: Business REST APIs for the Regulatory Engagement module — engagements with regulators and the tasks raised under them.
  name: MetricStream Regulatory Engagements APIs
  slug: metricstream-regulatory-engagements
- description: Business REST APIs for the Survey/Questionnaire module — creating questionnaires and initiating survey, scorecard and certification campaigns.
  name: MetricStream Surveys APIs
  slug: metricstream-surveys
- description: Business REST APIs for the Compliance module's test and self-assessment plans — creating and maintaining the plans that drive control testing cycles.
  name: MetricStream Self Assessment & Testing APIs
  slug: metricstream-self-assessment-testing
artifact_total: 14
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/metricstream-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.metricstream.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.metricstream.com/developer-portal.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.metricstream.com/api-developer-portal.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.metricstream.com/platform/apis.htm
- group: company
  title: ''
  type: Blog
  url: https://www.metricstream.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MetricStream
- group: operate
  title: ''
  type: Support
  url: https://www.metricstream.com/about-us/lets-talk.html
- group: start
  title: ''
  type: SignUp
  url: https://www.metricstream.com/about-us/get-started.htm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metricstream.com/customer-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metricstream.com/about-us/privacy-policy.htm
- group: auth
  title: ''
  type: Compliance
  url: conformance/metricstream-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metricstream-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/metricstream-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metricstream-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metricstream-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metricstream-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metricstream-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metricstream-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metricstream-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metricstream-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/metricstream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metricstream-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/metricstream-changelog.yml
created: '2026-08-25'
description: MetricStream is a San Jose, California based enterprise software company and a market leader in integrated Governance, Risk, and Compliance (GRC) management, serving large regulated organizations across banking and financial services, insurance, healthcare, life sciences, energy, utilities, telecom, technology and manufacturing. Its AI-first Connected GRC platform unifies enterprise and operational risk, regulatory and corporate compliance, policy and document management, internal audit and SOX, IT and cyber risk, third-party and vendor risk, operational resilience and business continuity, ESG, and case and incident management on one data core. MetricStream publishes a public API developer portal describing its Business REST APIs — a family of OpenAPI-derived REST modules covering GRC Foundation objects, Issues, Loss Event Management, Metrics, Risk Assessments, Regulatory Engagements, Surveys and Self Assessment & Testing — that customers, partners and internal developers use
  to move GRC data in and out of a MetricStream instance over HTTPS.
image: https://www.metricstream.com/sites/default/files/2025-05/metricstream-logo.png
layout: provider
modified: '2026-08-25'
name: MetricStream
nav: Providers
network: true
overview: 'MetricStream publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Governance, Risk, Compliance, and GRC.


  MetricStream''s developer surface includes API reference, documentation, engineering blog, support, signup flow, authentication, changelog, and 18 more developer resources.'
plans:
- name: Metricstream Plans Pricing
  plan_count: 0
  slug: metricstream-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Metricstream Rate Limits
  slug: metricstream-rate-limits
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 29.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metricstream/refs/heads/main/screenshots/metricstream-2026-09-02T150529.png
security:
- kind: authentication
  name: Metricstream Authentication
  slug: metricstream-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Metricstream Domain Security
  slug: metricstream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Metricstream Vulnerability Disclosure
  slug: metricstream-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Metricstream Trust Center
  slug: metricstream-trust-center
  summary_line: ISO 27001, SOC 2 Type II, HIPAA
slug: metricstream
tags:
- Company
- Governance
- Risk
- Compliance
- GRC
- Audit
- Enterprise Software
- Regulatory Technology
- Cyber Risk
- Third-Party Risk
- Operational Resilience
- ESG
website: https://www.metricstream.com/
---
