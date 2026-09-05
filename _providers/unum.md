---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Unum Agentic Access
  operation_count: 18
  slug: unum-agentic-access
  summary_line: 18 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Unum Benefits Enrollment API allows benefits administration platforms and HR systems to submit, update, and manage employee benefit enrollments in real time. The API enables seamless data synchron
  name: Unum Benefits Enrollment API
  slug: benefits-enrollment
- description: The Unum Leave and Absence Management API integrates Unum's leave solutions directly with HCM platforms, automating leave request intake, status tracking, return-to-work coordination, and FMLA/state l
  name: Unum Leave and Absence Management API
  slug: leave-absence
- baseURL: https://api.unum.com
  baseurl_source: declared
  description: OAuth 2.0 token management
  name: Unum Authentication API
  slug: unum-authentication-api
- baseURL: https://api.unum.com
  baseurl_source: declared
  description: Premium billing and payment management
  name: Unum Billing API
  slug: unum-billing-api
- baseURL: https://api.unum.com
  baseurl_source: declared
  description: Member eligibility management and verification
  name: Unum Eligibility API
  slug: unum-eligibility-api
- baseURL: https://api.unum.com
  baseurl_source: declared
  description: Benefits enrollment and lifecycle management
  name: Unum Enrollment API
  slug: unum-enrollment-api
- baseURL: https://api.unum.com
  baseurl_source: declared
  description: EOI submission and status tracking
  name: Unum Evidence of Insurability API
  slug: unum-evidence-of-insurability-api
- baseURL: https://api.unum.com
  baseurl_source: declared
  description: Leave and absence request management
  name: Unum Leave Management API
  slug: unum-leave-management-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unum HR Connect Authentication API
  slug: open-unum-authentication-api
- collection_type: open
  name: Unum HR Connect Authentication Billing API
  slug: open-unum-billing-api
- collection_type: open
  name: Unum HR Connect Authentication Eligibility API
  slug: open-unum-eligibility-api
- collection_type: open
  name: Unum HR Connect Authentication Enrollment API
  slug: open-unum-enrollment-api
- collection_type: open
  name: Unum HR Connect Authentication Evidence of Insurability API
  slug: open-unum-evidence-of-insurability-api
- collection_type: open
  name: Unum HR Connect API
  slug: open-unum-hr-connect
- collection_type: open
  name: Unum HR Connect Authentication Leave Management API
  slug: open-unum-leave-management-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unum-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unum-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unum
- group: company
  title: ''
  type: Website
  url: https://www.unum.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.unum.com/s/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.unum.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.unum.com/employers/hr-trends
- group: other
  title: ''
  type: Case Studies
  url: https://www.broadcom.com/case-studies/automation/unum-better-leverages-apis-to-deepen-customer-relationships-and-improve-customer-loyalty
created: '2026-05-03'
description: Unum Group is a leading provider of financial protection benefits including disability insurance, life insurance, dental insurance, vision insurance, and critical illness coverage. Unum's developer platform offers APIs for HR system integration, eligibility management, leave and absence management, enrollment, and evidence of insurability processing.
examples:
- key_count: 2
  name: Unum List Eligible Members Example
  slug: unum-list-eligible-members-example
- key_count: 2
  name: Unum Submit Eoi Example
  slug: unum-submit-eoi-example
- key_count: 2
  name: Unum Submit Leave Request Example
  slug: unum-submit-leave-request-example
finops:
- name: Unum Finops
  service_category: Insurance
  slug: unum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unum.png
json_schemas:
- name: Unum Leave Request
  property_count: 13
  slug: unum-leave-request
- name: Unum Member
  property_count: 13
  slug: unum-member
json_structures:
- name: Unum Member Structure
  property_count: 0
  slug: unum-member-structure
jsonld:
- class_count: 5
  name: Unum Context
  property_count: 30
  slug: unum-context
layout: provider
modified: '2026-05-19'
name: Unum
nav: Providers
network: true
overview: 'Unum publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Billing API, Eligibility API, and 3 more. Tagged areas include Insurance, Benefits Administration, HR Integration, Disability Insurance, and Life Insurance.


  The Unum catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Unum''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Unum Plans Pricing
  plan_count: 1
  slug: unum-plans-pricing
press:
- date: '2026-05-25'
  title: Unum Group secures patent for safer generative AI
  url: https://www.linkedin.com/posts/sheliaanderson_teamunum-innovation-ai-activity-7386390648087592961-PN5O
- date: '2026-05-25'
  title: Digital Transformation
  url: https://careers.unum.com/global/en/digital-transformation
- date: '2026-05-25'
  title: Unum Group builds custom AI application to search 1.3 ...
  url: https://www.microsoft.com/en/customers/story/1772120481217819586-unumgroup-azure-insurance-en-united-states
- date: '2026-05-25'
  title: New Unum Total Leave ™ will help employers and ...
  url: https://investors.unum.com/news-events/news/news-details/2021/New-Unum-Total-Leave--will-help-employers-and-employees-better-manage-complex-leave-process-04-27-2021/default.aspx
- date: '2026-05-25'
  title: Financials - Quarterly Results - Unum Group - Investor Relations
  url: https://investors.unum.com/financials/quarterly-results/default.aspx
random_paper: 12
rate_limits:
- limit_count: 1
  name: Unum Rate Limits
  slug: unum-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Unum API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unum-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Unum API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 10
  slug: unum-rules
scopes:
- name: Unum Scopes
  scope_count: 9
  slug: unum-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.5
    catalog_earned_first_party: 0.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 66.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unum/refs/heads/main/screenshots/unum-2026-06-20T200424.png
security:
- kind: authentication
  name: Unum Authentication
  slug: unum-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Unum Domain Security
  slug: unum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unum
tags:
- Insurance
- Benefits Administration
- HR Integration
- Disability Insurance
- Life Insurance
- Fortune 500
website: https://www.unum.com
---
