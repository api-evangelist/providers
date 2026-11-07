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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Runautomat Agentic Access
  operation_count: 1
  slug: runautomat-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://studio.runautomat.com
  baseurl_source: declared
  description: The extract API from Runautomat — 1 operation(s) for extract.
  name: Runautomat Extract API
  slug: runautomat-extract-api
artifact_total: 10
collections:
- collection_type: open
  name: extract API
  slug: open-runautomat-extract-api
common:
- group: commercial
  href: https://artifacts.apis.io/runautomat/plans/runautomat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/runautomat-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/runautomat/overlays/runautomat-extract-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/runautomat-extract-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://runautomat.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runautomat.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runautomat.com/guides/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runautomat.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runautomat.com/guides/getting-started/quickstart
- group: auth
  href: https://artifacts.apis.io/runautomat/authentication/runautomat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/runautomat-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.runautomat.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.runautomat.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://studio.runautomat.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://runautomat.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runautomat.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.runautomat.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runautomat.com/
- group: auth
  title: ''
  type: Compliance
  url: https://runautomat.com/enterprise
- group: agent
  href: https://artifacts.apis.io/runautomat/llms/runautomat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/runautomat-llms.txt
- group: agent
  href: https://artifacts.apis.io/runautomat/mcp/runautomat-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/runautomat-mcp.yml
- group: agent
  href: https://artifacts.apis.io/runautomat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/runautomat/errors/runautomat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/runautomat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/runautomat/conventions/runautomat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/runautomat-conventions.yml
- group: design
  href: https://artifacts.apis.io/runautomat/conformance/runautomat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/runautomat-conformance.yml
- group: design
  href: https://artifacts.apis.io/runautomat/lifecycle/runautomat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/runautomat-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/runautomat/data-model/runautomat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/runautomat-data-model.yml
- group: agent
  href: https://artifacts.apis.io/runautomat/agentic-access/runautomat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/runautomat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/runautomat/security/runautomat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runautomat-domain-security.yml
created: '2026-07-17'
description: Runautomat (dba Automat) builds AI agents that operate computers the way people do, replacing legacy RPA tools like UiPath, Automation Anywhere, and Blue Prism with self-healing managed automations. Founded in 2022 by ex-Google engineers Lucas Ochoa and Gautam Bose and backed by Felicis, Khosla Ventures, Initialized Capital, and Y Combinator. The platform spans UI-based AI agents (Computer Use RPA), AI document extraction (IDP), API-based automations (iPaaS), and a managed forward-deployed-engineer service. Its public developer surface is the Automat Document Extraction API, a single synchronous /api/extract operation that turns PDFs and images into structured JSON matching a configured extractor, authenticated with an organization API key.
finops:
- has_sources: true
  method: derived
  name: Runautomat Finops
  primary_unit: subscription
  service_category: ''
  slug: runautomat-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runautomat.png
layout: provider
modified: '2026-07-21'
name: Runautomat
nav: Providers
network: true
overview: 'Runautomat publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Extract API. Tagged areas include Company, Automation, RPA, Document Processing, and Artificial Intelligence.


  The Runautomat catalog on APIs.io includes 1 Spectral governance ruleset.


  Runautomat''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 19 more developer resources.'
plans:
- name: Runautomat Plans Pricing
  plan_count: 2
  slug: runautomat-plans-pricing
- name: Runautomat Price Estimates
  plan_count: 0
  slug: runautomat-price-estimates
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Runautomat API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: runautomat-rules
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 52.4
    developer_ergonomics: 55.4
    discoverability: 71.7
    operational_transparency: 7.9
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/runautomat/runautomat-2026-08-17T081652.png
security:
- kind: authentication
  name: Runautomat Authentication
  slug: runautomat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runautomat Domain Security
  slug: runautomat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: Extract structured data from a document
  slug: runautomat-extract-document
slug: runautomat
tags:
- Company
- Automation
- RPA
- Document Processing
- Artificial Intelligence
- Machine Learning
- Data Extraction
- iPaaS
- Agents
website: https://runautomat.com
---
