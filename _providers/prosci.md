---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Prosci Agentic Access
  operation_count: 23
  slug: prosci-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 1
apis:
- description: Assess individual and group change readiness using Prosci's ADKAR Model
  name: Prosci ADKAR Assessments API
  slug: prosci-adkar-assessments-api
- description: Create and manage change plans including communications, sponsorship, coaching, training, and resistance management
  name: Prosci Change Plans API
  slug: prosci-change-plans-api
- description: Organization-level change management maturity
  name: Prosci Organizations API
  slug: prosci-organizations-api
- description: Evaluate change initiative health using the Prosci Change Triangle
  name: Prosci PCT Assessments API
  slug: prosci-pct-assessments-api
- description: Manage change management projects
  name: Prosci Projects API
  slug: prosci-projects-api
- description: Assess and manage change risk
  name: Prosci Risk Assessment API
  slug: prosci-risk-assessment-api
- description: Manage stakeholders and impacted groups
  name: Prosci Stakeholders API
  slug: prosci-stakeholders-api
- description: Training programs and enrollment management
  name: Prosci Training API
  slug: prosci-training-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prosci Change Management ADKAR Assessments API
  slug: open-prosci-adkar-assessments-api
- collection_type: open
  name: Prosci Change Management API
  slug: open-prosci-change-management
- collection_type: open
  name: Prosci Change Management ADKAR Assessments Change Plans API
  slug: open-prosci-change-plans-api
- collection_type: open
  name: Prosci Change Management ADKAR Assessments Organizations API
  slug: open-prosci-organizations-api
- collection_type: open
  name: Prosci Change Management ADKAR Assessments PCT Assessments API
  slug: open-prosci-pct-assessments-api
- collection_type: open
  name: Prosci Change Management ADKAR Assessments Projects API
  slug: open-prosci-projects-api
- collection_type: open
  name: Prosci Change Management ADKAR Assessments Risk Assessment API
  slug: open-prosci-risk-assessment-api
- collection_type: open
  name: Prosci Change Management ADKAR Assessments Stakeholders API
  slug: open-prosci-stakeholders-api
- collection_type: open
  name: Prosci Change Management ADKAR Assessments Training API
  slug: open-prosci-training-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/prosci-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prosci-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prosci-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prosci-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prosci
- group: company
  title: ''
  type: Blog
  url: https://www.prosci.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prosci.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prosci.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.prosci.com
created: '2024-01-20'
description: Prosci is a global leader in change management research, methodology, and solutions. They provide change management training, certification, tools, and consulting services to help organizations successfully implement change initiatives.
finops:
- name: Prosci Finops
  service_category: API
  slug: prosci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prosci.png
json_schemas:
- name: Prosci ADKAR Assessment
  property_count: 17
  slug: prosci-adkar-assessment
- name: Prosci Change Project
  property_count: 22
  slug: prosci-change-project
jsonld:
- class_count: 22
  name: Prosci Context
  property_count: 46
  slug: prosci-context
layout: provider
modified: '2026-05-19'
name: Prosci
nav: Providers
network: true
overview: 'Prosci publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ADKAR Assessments API, Change Plans API, Organizations API, and 5 more. Tagged areas include Change Management, Methodology, and Training.


  The Prosci catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Prosci''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Prosci Plans Pricing
  plan_count: 3
  slug: prosci-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Prosci Rate Limits
  slug: prosci-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Prosci API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: prosci-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 65.9
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prosci/refs/heads/main/screenshots/prosci-2026-08-17T124907.png
security:
- kind: authentication
  name: Prosci Authentication
  slug: prosci-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Prosci Domain Security
  slug: prosci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prosci
tags:
- Change Management
- Methodology
- Training
website: https://www.prosci.com
---
