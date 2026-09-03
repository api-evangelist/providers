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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Acadia Agentic Access
  operation_count: 7
  slug: acadia-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 5
apis:
- baseURL: https://api.acadia-software.com/v1
  baseurl_source: declared
  description: Manage employee profiles and training records
  name: Acadia Employees API
  slug: acadia-employees-api
- baseURL: https://api.acadia-software.com/v1
  baseurl_source: declared
  description: Manage quizzes and assessments
  name: Acadia Quizzes API
  slug: acadia-quizzes-api
- baseURL: https://api.acadia-software.com/v1
  baseurl_source: declared
  description: Manage job roles and training requirements
  name: Acadia Roles API
  slug: acadia-roles-api
- baseURL: https://api.acadia-software.com/v1
  baseurl_source: declared
  description: Manage employee skills and skills matrices
  name: Acadia Skills API
  slug: acadia-skills-api
- baseURL: https://api.acadia-software.com/v1
  baseurl_source: declared
  description: Manage digital work instructions and task lists
  name: Acadia Work Instructions API
  slug: acadia-work-instructions-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acadia - Platform Employees API
  slug: open-acadia-employees-api
- collection_type: open
  name: Acadia - Platform Employees Quizzes API
  slug: open-acadia-quizzes-api
- collection_type: open
  name: Acadia - Platform Employees Roles API
  slug: open-acadia-roles-api
- collection_type: open
  name: Acadia - Platform Employees Skills API
  slug: open-acadia-skills-api
- collection_type: open
  name: Acadia - Platform Employees Work Instructions API
  slug: open-acadia-work-instructions-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/epicor/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acadia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acadia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.acadia-software.com/
- group: start
  title: ''
  type: Portal
  url: https://www.acadia-software.com/
- group: start
  title: ''
  type: Signup
  url: https://www.acadia-software.com/
- group: company
  title: ''
  type: Blog
  url: https://www.acadia-software.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.acadia-software.com/features/
- group: design
  title: ''
  type: SpectralRules
  url: rules/acadia-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/acadia-vocabulary.yaml
created: '2024-01-15'
description: Acadia is a Connected Worker Platform designed for employee productivity, acquired by Epicor. It delivers digital work instructions, knowledge management, skills matrices, quizzing, process evaluations, and team communications to frontline workers across manufacturing, transportation, healthcare, and retail banking. Acadia integrates with SSO, ERP, HRIS, LMS, IoT, and credentialing systems to enable enterprise-grade workforce development at scale.
examples:
- key_count: 6
  name: Acadia Employee Example
  slug: acadia-employee-example
- key_count: 4
  name: Acadia Employee List Example
  slug: acadia-employee-list-example
- key_count: 5
  name: Acadia Employee Skills Matrix Example
  slug: acadia-employee-skills-matrix-example
- key_count: 6
  name: Acadia Quiz Example
  slug: acadia-quiz-example
- key_count: 4
  name: Acadia Quiz List Example
  slug: acadia-quiz-list-example
- key_count: 5
  name: Acadia Role Example
  slug: acadia-role-example
- key_count: 4
  name: Acadia Role List Example
  slug: acadia-role-list-example
- key_count: 6
  name: Acadia Skill Record Example
  slug: acadia-skill-record-example
- key_count: 9
  name: Acadia Work Instruction Example
  slug: acadia-work-instruction-example
- key_count: 4
  name: Acadia Work Instruction List Example
  slug: acadia-work-instruction-list-example
- key_count: 3
  name: Acadia Work Instruction Step Example
  slug: acadia-work-instruction-step-example
features:
- description: Convert procedures to interactive task lists with videos, images, and dynamic content; assign via QR code, ERP integration, or manager distribution
  name: Digital Work Instructions
- description: Centralized document creation with automated translation, algorithmic search, and custom metadata filters
  name: Knowledge Management
- description: Track training and skill attainment, quantify individual and team performance, and identify capability gaps
  name: Skills Matrix
- description: Assess employee skill proficiency, measure comprehension, and perform objective skill evaluations during task execution
  name: Quizzing and Evaluations
- description: Auditable acknowledgements for process changes, group communications, and document change tracking
  name: Team Communications
- description: Secure single sign-on via Active Directory and LDAP with role-based access control
  name: SSO Integration
- description: Integration with ERP, HRIS, LMS, IoT, and credentialing systems for enterprise workforce management
  name: ERP and HRIS Integration
- description: Enterprise-grade security with multi-layer encryption, intrusion prevention, and GDPR compliance
  name: SOC 2 Type II Certified
- description: Display advancement requirements and skill gap identification for employee career development
  name: Career Path Visibility
finops:
- name: Acadia Finops
  service_category: Connected Worker / Workforce Enablement SaaS
  slug: acadia-finops
image: /assets/icons/acadia.png
integrations:
- description: Integration with SAP ERP for work order-triggered digital work instruction assignment
  name: SAP
- description: Single sign-on via Microsoft Active Directory for enterprise identity management
  name: Active Directory
- description: LDAP-based SSO for enterprise authentication systems
  name: LDAP
- description: Integration with third-party LMS platforms for training record synchronization
  name: Learning Management Systems
- description: Integration with HR information systems for employee data synchronization
  name: HRIS Systems
- description: Integration with IoT systems for operational data correlation with training and task execution
  name: IoT Platforms
json_schemas:
- name: EmployeeList
  property_count: 4
  slug: acadia-employee-list
- name: Employee
  property_count: 6
  slug: acadia-employee
- name: EmployeeSkillsMatrix
  property_count: 5
  slug: acadia-employee-skills-matrix
- name: QuizList
  property_count: 4
  slug: acadia-quiz-list
- name: Quiz
  property_count: 6
  slug: acadia-quiz
- name: RoleList
  property_count: 4
  slug: acadia-role-list
- name: Role
  property_count: 5
  slug: acadia-role
- name: SkillRecord
  property_count: 6
  slug: acadia-skill-record
- name: WorkInstructionList
  property_count: 4
  slug: acadia-work-instruction-list
- name: WorkInstruction
  property_count: 9
  slug: acadia-work-instruction
- name: WorkInstructionStep
  property_count: 3
  slug: acadia-work-instruction-step
json_structures:
- name: Acadia Employee List Structure
  property_count: 4
  slug: acadia-employee-list-structure
- name: Acadia Employee Skills Matrix Structure
  property_count: 5
  slug: acadia-employee-skills-matrix-structure
- name: Acadia Employee Structure
  property_count: 6
  slug: acadia-employee-structure
- name: Acadia Quiz List Structure
  property_count: 4
  slug: acadia-quiz-list-structure
- name: Acadia Quiz Structure
  property_count: 6
  slug: acadia-quiz-structure
- name: Acadia Role List Structure
  property_count: 4
  slug: acadia-role-list-structure
- name: Acadia Role Structure
  property_count: 5
  slug: acadia-role-structure
- name: Acadia Skill Record Structure
  property_count: 6
  slug: acadia-skill-record-structure
- name: Acadia Work Instruction List Structure
  property_count: 4
  slug: acadia-work-instruction-list-structure
- name: Acadia Work Instruction Step Structure
  property_count: 3
  slug: acadia-work-instruction-step-structure
- name: Acadia Work Instruction Structure
  property_count: 9
  slug: acadia-work-instruction-structure
jsonld:
- class_count: 10
  name: Acadia Platform Context
  property_count: 25
  slug: acadia-platform-context
layout: provider
modified: '2026-05-19'
name: Acadia
nav: Providers
network: true
overview: 'Acadia publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Employees API, Quizzes API, Roles API, and 2 more. Tagged areas include Connected Worker, Knowledge-Management, Manufacturing, Skills Management, and Training.


  The Acadia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Acadia''s developer surface includes authentication, developer portal, signup flow, engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Acadia Plans Pricing
  plan_count: 1
  slug: acadia-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Acadia Rate Limits
  slug: acadia-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acadia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: acadia-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Acadia API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 14
  slug: acadia-spectral-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 28.5
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 0.0
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/screenshots/acadia-2026-06-20T163529.png
security:
- kind: authentication
  name: Acadia Authentication
  slug: acadia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acadia Domain Security
  slug: acadia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acadia
tags:
- Connected Worker
- Knowledge-Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
use_cases:
- description: Use digital work instructions to onboard new manufacturing employees quickly and ensure procedure compliance
  name: Manufacturing Workforce Onboarding
- description: Assign and track completion of compliance-critical training and policy acknowledgements with full auditability
  name: Compliance Training
- description: Use the skills matrix to identify capability gaps in frontline teams and prioritize training investments
  name: Frontline Skill Gap Analysis
- description: Capture structured employee feedback on task-specific procedures to improve standard work over time
  name: Process Improvement Feedback
- description: Automatically assign work instructions based on ERP work orders for synchronized production operations
  name: ERP-Triggered Work Instructions
- description: Deploy synchronized multi-language training content to global workforces without manual translation delays
  name: Multi-Language Training Deployment
website: https://www.acadia-software.com/
---
