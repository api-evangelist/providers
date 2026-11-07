---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://integrations.predictiveindex.com
  baseurl_source: declared
  description: The Behavioral Assessments API from The Predictive Index — 1 operation(s) for behavioral assessments.
  name: The Predictive Index Behavioral Assessments API
  slug: the-predictive-index-behavioral-assessments-api
- baseURL: https://integrations.predictiveindex.com
  baseurl_source: declared
  description: The Candidates API from The Predictive Index — 3 operation(s) for candidates.
  name: The Predictive Index Candidates API
  slug: the-predictive-index-candidates-api
- baseURL: https://integrations.predictiveindex.com
  baseurl_source: declared
  description: The Employees API from The Predictive Index — 2 operation(s) for employees.
  name: The Predictive Index Employees API
  slug: the-predictive-index-employees-api
- baseURL: https://integrations.predictiveindex.com
  baseurl_source: declared
  description: The Jobs API from The Predictive Index — 1 operation(s) for jobs.
  name: The Predictive Index Jobs API
  slug: the-predictive-index-jobs-api
artifact_total: 17
asyncapis:
- description: ''
  name: The Predictive Index Webhooks
  slug: the-predictive-index-webhooks
collections:
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments API
  slug: open-the-predictive-index-behavioral-assessments-api
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments Candidates API
  slug: open-the-predictive-index-candidates-api
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments Employees API
  slug: open-the-predictive-index-employees-api
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments Jobs API
  slug: open-the-predictive-index-jobs-api
common:
- group: commercial
  href: https://artifacts.apis.io/the-predictive-index/plans/the-predictive-index-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-predictive-index-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.predictiveindex.com/blog/feed/
- group: other
  href: https://artifacts.apis.io/the-predictive-index/capabilities/the-predictive-index-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/the-predictive-index-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.predictiveindex.com/
- group: agent
  href: https://artifacts.apis.io/the-predictive-index/mcp/the-predictive-index-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/the-predictive-index-mcp.yml
- group: auth
  href: https://artifacts.apis.io/the-predictive-index/security/the-predictive-index-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-predictive-index-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.predictiveindex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.predictiveindex.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.predictiveindex.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.predictiveindex.com/getting-started
- group: auth
  href: https://artifacts.apis.io/the-predictive-index/authentication/the-predictive-index-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-predictive-index-authentication.yml
- group: design
  href: https://artifacts.apis.io/the-predictive-index/conventions/the-predictive-index-conventions.yml
  title: ''
  type: Conventions
  url: conventions/the-predictive-index-conventions.yml
- group: design
  href: https://artifacts.apis.io/the-predictive-index/asyncapi/the-predictive-index-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/the-predictive-index-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/the-predictive-index/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.predictiveindex.com
- group: auth
  title: ''
  type: Security
  url: https://www.predictiveindex.com/security/responsible-disclosure/
- group: auth
  href: https://artifacts.apis.io/the-predictive-index/security/the-predictive-index-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-predictive-index-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/the-predictive-index/well-known/the-predictive-index-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/the-predictive-index-security.txt
- group: agent
  href: https://artifacts.apis.io/the-predictive-index/well-known/the-predictive-index-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-predictive-index-well-known.yml
- group: agent
  href: https://artifacts.apis.io/the-predictive-index/llms/the-predictive-index-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-predictive-index-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/predictiveindex
- group: company
  title: ''
  type: Blog
  url: https://www.predictiveindex.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.predictiveindex.com/company/contact-us/#support-case
- group: commercial
  title: ''
  type: Pricing
  url: https://www.predictiveindex.com/plans/
- group: start
  title: ''
  type: SignUp
  url: https://app.predictiveindex.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.predictiveindex.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.predictiveindex.com/privacy/
created: '2026-07-17'
description: The Predictive Index (PI) is a talent optimization platform that pairs 70+ years of behavioral science with software to help organizations hire, engage, and develop teams — behavioral and cognitive assessments, hiring and candidate screening, leadership development, employee engagement, and performance management. PI publishes a RESTful Integration API (on Azure API Management) that lets external systems such as ATS/HRIS platforms programmatically create candidates, send behavioral and cognitive assessments, retrieve jobs and results, and generate insight and coaching-guide reports — the same data that appears in the PI Portal software. Status-change notification webhooks push assessment completion events to listening systems. Backed by a $50M investment from General Catalyst.
finops:
- has_sources: true
  method: derived
  name: The Predictive Index Finops
  primary_unit: annual subscription priced by headcount
  service_category: ''
  slug: the-predictive-index-finops
  template: false
image: https://media.predictiveindex.com/wp-content/uploads/2025/02/25165442/ThePredictiveIndex_Thumbnail-1.jpg
layout: provider
modified: '2026-10-06'
name: The Predictive Index
nav: Providers
network: true
overview: 'The Predictive Index publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Behavioral Assessments API, Candidates API, Employees API, and 1 more. Tagged areas include Company, Talent Optimization, Human Resources, Assessment, and Behavioral Science.


  The The Predictive Index catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  The Predictive Index''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 20 more developer resources.'
plans:
- name: The Predictive Index Plans Pricing
  plan_count: 1
  slug: the-predictive-index-plans-pricing
- name: The Predictive Index Price Estimates
  plan_count: 0
  slug: the-predictive-index-price-estimates
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: The Predictive Index API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: the-predictive-index-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 57.4
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 51.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/the-predictive-index/the-predictive-index-2026-08-17T082339.png
security:
- kind: authentication
  name: The Predictive Index Authentication
  slug: the-predictive-index-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Predictive Index Domain Security
  slug: the-predictive-index-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: The Predictive Index Vulnerability Disclosure
  slug: the-predictive-index-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: Send a PI assessment to a candidate
  slug: the-predictive-index-send-assessment
slug: the-predictive-index
tags:
- Company
- Talent Optimization
- Human Resources
- Assessment
- Behavioral Science
- Hiring
- Recruiting
- Employee Engagement
website: https://www.predictiveindex.com/
---
