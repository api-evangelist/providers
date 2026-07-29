---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Aflac Agentic Access
  operation_count: 13
  slug: aflac-agentic-access
  summary_line: 13 operations · 5 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Aflac Claims API provides programmatic access to supplemental insurance claim submission, status retrieval, and benefit payment tracking. It enables policyholders and administrators to submit clai
  name: Aflac Claims API
  slug: claims-api
- description: Claims submission and status retrieval operations.
  name: aflac Claims API
  slug: aflac-claims-api
- description: Employee eligibility verification operations.
  name: aflac Eligibility API
  slug: aflac-eligibility-api
- description: Benefits enrollment operations for supplemental insurance products.
  name: aflac Enrollment API
  slug: aflac-enrollment-api
- description: Employer group management operations.
  name: aflac Groups API
  slug: aflac-groups-api
- description: Policy management and retrieval operations.
  name: aflac Policies API
  slug: aflac-policies-api
artifact_total: 71
collections:
- collection_type: open
  name: Aflac Enterprise Connect API
  slug: open-aflac-enterprise-connect
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aflac-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aflac-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aflac-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aflac-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aflac-SCM
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aflac
- group: start
  title: ''
  type: Portal
  url: https://docs.enterprise-connect.aflac.com
- group: company
  title: ''
  type: Website
  url: https://www.aflac.com
- group: start
  title: ''
  type: Signup
  url: https://www.aflac.com/business/default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aflac.com/about-aflac/legal/terms-and-conditions.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aflac.com/about-aflac/legal/privacy-policy.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.aflac.com/contact-aflac/default.aspx
- group: company
  title: ''
  type: Blog
  url: https://newsroom.aflac.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/aflac-enterprise-connect-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-claim-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-claim-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-claim-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-dependent-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-eligibility-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-eligibility-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-enrollment-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-enrollment-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-enrollment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-group-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-group-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-policy-list-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/enterprise-connect-policy-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-claim-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-claim-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-claim-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-dependent-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-eligibility-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-eligibility-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-enrollment-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-enrollment-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-enrollment-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-group-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-group-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-policy-list-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/enterprise-connect-policy-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aflac-enterprise-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-claim-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-claim-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-claim-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-dependent-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-eligibility-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-eligibility-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-enrollment-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-enrollment-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-enrollment-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-group-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-group-list-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-policy-example.json
- group: build
  title: ''
  type: Examples
  url: examples/enterprise-connect-policy-list-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/aflac-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aflac-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.enterprise-connect.aflac.com/llms.txt
description: Aflac is America's leading provider of supplemental insurance, offering products that pay benefits when a policyholder experiences an accident, illness, or injury. Aflac provides REST APIs through its Enterprise Connect (AEC) platform enabling benefits technology companies, HR platforms, and benefits administrators to integrate supplemental insurance enrollment, policy management, and claims capabilities into their workflows.
examples:
- key_count: 9
  name: Enterprise Connect Claim Example
  slug: enterprise-connect-claim-example
- key_count: 2
  name: Enterprise Connect Claim List Example
  slug: enterprise-connect-claim-list-example
- key_count: 4
  name: Enterprise Connect Claim Request Example
  slug: enterprise-connect-claim-request-example
- key_count: 4
  name: Enterprise Connect Dependent Example
  slug: enterprise-connect-dependent-example
- key_count: 3
  name: Enterprise Connect Eligibility Request Example
  slug: enterprise-connect-eligibility-request-example
- key_count: 5
  name: Enterprise Connect Eligibility Response Example
  slug: enterprise-connect-eligibility-response-example
- key_count: 12
  name: Enterprise Connect Enrollment Example
  slug: enterprise-connect-enrollment-example
- key_count: 4
  name: Enterprise Connect Enrollment List Example
  slug: enterprise-connect-enrollment-list-example
- key_count: 6
  name: Enterprise Connect Enrollment Request Example
  slug: enterprise-connect-enrollment-request-example
- key_count: 6
  name: Enterprise Connect Group Example
  slug: enterprise-connect-group-example
- key_count: 2
  name: Enterprise Connect Group List Example
  slug: enterprise-connect-group-list-example
- key_count: 9
  name: Enterprise Connect Policy Example
  slug: enterprise-connect-policy-example
- key_count: 2
  name: Enterprise Connect Policy List Example
  slug: enterprise-connect-policy-list-example
features:
- description: Replace EDI 834 file-based enrollment with real-time API-driven enrollment workflows for supplemental insurance products.
  name: Electronic Benefits Enrollment
- description: Manage group and individual supplemental insurance policies including enrollments, terminations, and coverage changes.
  name: Policy Administration
- description: Enable digital claim filing for supplemental insurance products including accident, critical illness, cancer, and disability coverage.
  name: Claims Submission
- description: Verify employee eligibility for Aflac supplemental insurance products in real time during enrollment.
  name: Eligibility Verification
- description: Connect benefits administration platforms with Aflac's enrollment and policy systems via standardized REST APIs.
  name: Benefits Administration Integration
- description: Receive immediate enrollment confirmation and policy numbers upon successful enrollment submission.
  name: Real-Time Enrollment Confirmation
finops:
- name: Aflac Finops
  service_category: Insurance / Supplemental Benefits
  slug: aflac-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aflac.png
integrations:
- description: Aflac connects with Employee Navigator benefits administration platform for automated enrollment data exchange.
  name: Employee Navigator
- description: Integration with Benefitfocus benefits marketplace for supplemental insurance enrollment.
  name: Benefitfocus
- description: Payroll and HR integration with ADP for Aflac premium deduction and enrollment synchronization.
  name: ADP
- description: Enterprise HR platform integration for benefits enrollment and Aflac policy administration.
  name: Workday
- description: Benefits administration platform integration for Aflac group enrollment.
  name: bswift
json_schemas:
- name: ClaimList
  property_count: 2
  slug: enterprise-connect-claim-list
- name: ClaimRequest
  property_count: 4
  slug: enterprise-connect-claim-request
- name: Claim
  property_count: 9
  slug: enterprise-connect-claim
- name: Dependent
  property_count: 4
  slug: enterprise-connect-dependent
- name: EligibilityRequest
  property_count: 3
  slug: enterprise-connect-eligibility-request
- name: EligibilityResponse
  property_count: 5
  slug: enterprise-connect-eligibility-response
- name: EnrollmentList
  property_count: 4
  slug: enterprise-connect-enrollment-list
- name: EnrollmentRequest
  property_count: 6
  slug: enterprise-connect-enrollment-request
- name: Enrollment
  property_count: 12
  slug: enterprise-connect-enrollment
- name: GroupList
  property_count: 2
  slug: enterprise-connect-group-list
- name: Group
  property_count: 6
  slug: enterprise-connect-group
- name: PolicyList
  property_count: 2
  slug: enterprise-connect-policy-list
- name: Policy
  property_count: 9
  slug: enterprise-connect-policy
json_structures:
- name: Enterprise Connect Claim List Structure
  property_count: 2
  slug: enterprise-connect-claim-list-structure
- name: Enterprise Connect Claim Request Structure
  property_count: 4
  slug: enterprise-connect-claim-request-structure
- name: Enterprise Connect Claim Structure
  property_count: 9
  slug: enterprise-connect-claim-structure
- name: Enterprise Connect Dependent Structure
  property_count: 4
  slug: enterprise-connect-dependent-structure
- name: Enterprise Connect Eligibility Request Structure
  property_count: 3
  slug: enterprise-connect-eligibility-request-structure
- name: Enterprise Connect Eligibility Response Structure
  property_count: 5
  slug: enterprise-connect-eligibility-response-structure
- name: Enterprise Connect Enrollment List Structure
  property_count: 4
  slug: enterprise-connect-enrollment-list-structure
- name: Enterprise Connect Enrollment Request Structure
  property_count: 6
  slug: enterprise-connect-enrollment-request-structure
- name: Enterprise Connect Enrollment Structure
  property_count: 12
  slug: enterprise-connect-enrollment-structure
- name: Enterprise Connect Group List Structure
  property_count: 2
  slug: enterprise-connect-group-list-structure
- name: Enterprise Connect Group Structure
  property_count: 6
  slug: enterprise-connect-group-structure
- name: Enterprise Connect Policy List Structure
  property_count: 2
  slug: enterprise-connect-policy-list-structure
- name: Enterprise Connect Policy Structure
  property_count: 9
  slug: enterprise-connect-policy-structure
jsonld:
- class_count: 17
  name: Aflac Enterprise Context
  property_count: 30
  slug: aflac-enterprise-context
layout: provider
modified: '2026-04-19'
name: aflac
nav: Providers
network: true
overview: 'aflac publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Eligibility API, Enrollment API, and 2 more. Tagged areas include Fortune 500.


  The aflac catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  aflac''s developer surface includes authentication, developer portal, signup flow, support, engineering blog, code examples, and 51 more developer resources.'
plans:
- name: Aflac Plans Pricing
  plan_count: 2
  slug: aflac-plans-pricing
press:
- date: '2026-05-25'
  title: Aflac Incorporated Discloses Cybersecurity Incident
  url: https://www.prnewswire.com/news-releases/aflac-incorporated-discloses-cybersecurity-incident-302487036.html
- date: '2026-05-25'
  title: Aflac Breach Highlights Need for Proactive Cybersecurity ...
  url: https://www.linkedin.com/posts/dcass001_aflac-data-breach-affects-2265-million-activity-7416841698208555008-obqx
- date: '2026-05-25'
  title: Artificial Intelligence at Aflac - Two Use Cases
  url: https://emerj.com/artificial-intelligence-at-aflac/
- date: '2026-05-25'
  title: Privacy Policy
  url: https://www.aflac.com/about-aflac/privacy-policy.aspx
- date: '2026-05-25'
  title: Why Aflac isn't rushing generative AI adoption
  url: https://www.ciodive.com/news/Aflac-CIO-Shelia-Anderson-generative-ai-cloud-strategy/742503/
random_paper: 23
rate_limits:
- limit_count: 1
  name: Aflac Rate Limits
  slug: aflac-rate-limits
rules:
- name: aflac API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aflac-jsonschema-spectral-rules
- name: aflac API Rules
  rule_count: 30
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 16
  slug: aflac-spectral-rules
scopes:
- name: Aflac Scopes
  scope_count: 6
  slug: aflac-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: developing
  composite: 48.4
  delta: -7.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/aflac/refs/heads/main/screenshots/aflac-2026-06-20T165702.png
security:
- kind: authentication
  name: Aflac Authentication
  slug: aflac-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Aflac Domain Security
  slug: aflac-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aflac
tags:
- Fortune 500
use_cases:
- description: HR and benefits administration platforms integrate with Aflac's API to offer supplemental insurance enrollment within their existing benefits workflows.
  name: HR Platform Integration
- description: Employers manage supplemental insurance enrollments for employees during open enrollment periods via connected benefits platforms.
  name: Employer Self-Service Enrollment
- description: Employees and HR teams track the status of Aflac supplemental insurance claims submitted after a qualifying health event.
  name: Claims Tracking
- description: Benefits brokers manage group policy setup, employee enrollment, and plan changes for employer clients through integrated tools.
  name: Benefits Broker Workflow
website: https://www.aflac.com
---
