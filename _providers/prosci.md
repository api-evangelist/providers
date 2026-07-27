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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Prosci Agentic Access
  operation_count: 23
  slug: prosci-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 8
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
artifact_total: 19
collections:
- collection_type: open
  name: Prosci Change Management API
  slug: open-prosci-change-management
common:
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


  Prosci''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Prosci Plans Pricing
  plan_count: 3
  slug: prosci-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Prosci Rate Limits
  slug: prosci-rate-limits
rules:
- name: Prosci API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: prosci-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.9
  delta: 3.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.9
    developer_ergonomics: 13.0
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 50.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
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
