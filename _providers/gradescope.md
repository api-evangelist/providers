---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Gradescope's primary supported integration surface. Implements the 1EdTech LTI 1.3 / LTI Advantage standard, including Names and Role Provisioning Services (NRPS) for roster sync, Assignment and Grade
  name: Gradescope LTI Integration
  slug: gradescope-lti-api
- description: 'Course and roster data. Gradescope does not expose a generally available public REST endpoint for listing or managing courses; course roster provisioning happens through LTI 1.3 NRPS during LMS sync. '
  name: Gradescope Courses API
  slug: gradescope-courses-api
- description: Assignment configuration and the autograder framework for code assignments. The documented programmatic contract is a Docker-based autograder that reads student submissions and emits a results.json fi
  name: Gradescope Assignments API
  slug: gradescope-assignments-api
- description: Submission handling. Code submissions are processed inside the autograder container, where the submission is mounted and graded according to the autograder specification. Gradescope does not publish a
  name: Gradescope Submissions API
  slug: gradescope-submissions-api
- description: Grade data and gradebook sync. Grades are pushed to an LMS gradebook through LTI 1.3 Assignment and Grade Services (AGS) rather than a first-party public REST API. Programmatic export/import of grades
  name: Gradescope Grades API
  slug: gradescope-grades-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gradescope API
  slug: open-gradescope
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gradescope-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gradescope
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/turnitin-gradescope/
- group: company
  title: ''
  type: Website
  url: https://www.gradescope.com
- group: docs
  title: ''
  type: Documentation
  url: https://guides.gradescope.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/gradescope-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gradescope-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gradescope-finops.yml
created: '2026-06-21'
description: Gradescope, a Turnitin company, is an assessment and grading platform for paper-based, digital, and code assignments used across higher education and K-12. It does not publish a generally available public REST API; programmatic integration is delivered through LTI 1.3 / LTI Advantage (roster and grade sync with Canvas, Blackboard, Brightspace/D2L, Moodle, and Sakai) and a documented autograder framework for code assignments. A first-party public API for courses, assignments, submissions, and grades is a published feature request but is not yet generally available.
finops:
- name: Gradescope Finops
  service_category: Education and Assessment
  slug: gradescope-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gradescope.png
layout: provider
modified: '2026-06-21'
name: Gradescope
nav: Providers
network: true
overview: 'Gradescope publishes 5 APIs on the [APIs.io](https://apis.io/) network, including LTI Integration, Courses API, Assignments API, and 2 more. Tagged areas include Education, EdTech, Grading, Assessment, and LTI.


  Gradescope''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Gradescope Plans Pricing
  plan_count: 2
  slug: gradescope-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Gradescope Rate Limits
  slug: gradescope-rate-limits
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 23.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gradescope/refs/heads/main/screenshots/gradescope-2026-07-25T220156.png
security:
- kind: domain-security
  name: Gradescope Domain Security
  slug: gradescope-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: gradescope
tags:
- Education
- EdTech
- Grading
- Assessment
- LTI
website: https://www.gradescope.com
---
