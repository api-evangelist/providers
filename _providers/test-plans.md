---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: REST API for TestRail test management including test plans, test runs, milestones, and reporting, enabling structured test planning and execution tracking.
  name: TestRail API
  slug: testrail-api
- description: REST API for Jira Software project management, supporting test plan tracking via epics, sprints, issues, and custom fields integrated with testing workflows.
  name: Jira Software API
  slug: jira-software-api
- description: REST API for Azure DevOps Test Plans service supporting test plan creation, test suites, test case management, test execution, and results reporting.
  name: Azure DevOps Test Plans API
  slug: azure-devops-test-plans-api
- description: REST API for qTest test management platform by Tricentis, supporting test plan management, test cycle creation, defect linking, and release-level test planning.
  name: qTest API
  slug: qtest-api
- description: REST API for Micro Focus ALM Octane test planning and quality management, supporting test planning, defect management, and release quality tracking.
  name: ALM Octane API
  slug: alm-octane-api
artifact_total: 35
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-plans-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://en.wikipedia.org/wiki/Test_plan
- group: docs
  title: ''
  type: Documentation
  url: https://www.guru99.com/what-is-test-plan-how-to-write-it.html
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/test-plans-test-plan-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/test-plans-test-cycle-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/test-plans-milestone-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/test-plans-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/test-plans-vocabulary.yml
created: '2025'
description: Structured documentation outlining test objectives, scope, approach, resources, schedule, and deliverables for software testing activities. Test plans define the overall strategy for testing a system or feature, specifying what will be tested, how it will be tested, who will test it, and what constitutes a pass or fail. They are critical for coordinating testing efforts across teams and ensuring comprehensive coverage.
examples:
- key_count: 9
  name: Test Plans Milestone Example
  slug: test-plans-milestone-example
- key_count: 15
  name: Test Plans Test Cycle Example
  slug: test-plans-test-cycle-example
- key_count: 18
  name: Test Plans Test Plan Example
  slug: test-plans-test-plan-example
features:
- description: Define what features, modules, and components are in scope for the testing effort.
  name: Scope Definition
- description: Assign testers, environments, and tools needed to execute the test plan.
  name: Resource Allocation
- description: Identify testing risks and mitigation strategies for high-risk areas.
  name: Risk Assessment
- description: Define testing timelines, milestones, and entry and exit criteria for test phases.
  name: Schedule Management
- description: Map test cases to requirements ensuring complete coverage of all specifications.
  name: Coverage Mapping
- description: Link test failures to defect tracking systems for resolution workflow management.
  name: Defect Tracking Integration
finops:
- name: Test Plans Finops
  service_category: API
  slug: test-plans-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/test-plans.png
integrations:
- description: Link test plans to Jira epics and sprints for agile testing coordination.
  name: Jira
- description: Publish test plans to Confluence for team visibility and stakeholder review.
  name: Confluence
- description: Trigger automated test execution from test plans via Jenkins pipeline integration.
  name: Jenkins
- description: Send test plan status updates and milestone notifications to Slack channels.
  name: Slack
json_schemas:
- name: TestMilestone
  property_count: 9
  slug: test-plans-milestone
- name: TestCycle
  property_count: 15
  slug: test-plans-test-cycle
- name: TestPlan
  property_count: 18
  slug: test-plans-test-plan
json_structures:
- name: Test Plans Milestone Structure
  property_count: 9
  slug: test-plans-milestone-structure
- name: Test Plans Test Cycle Structure
  property_count: 15
  slug: test-plans-test-cycle-structure
- name: Test Plans Test Plan Structure
  property_count: 18
  slug: test-plans-test-plan-structure
jsonld:
- class_count: 3
  name: Test Plans Context
  property_count: 31
  slug: test-plans-context
layout: provider
modified: '2026-05-03'
name: Test Plans
nav: Providers
network: true
overview: 'Test Plans publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jira Software API and Azure DevOps Test Plans API. Tagged areas include Documentation, Quality Assurance, Software Development, Test Management, and Testing.


  The Test Plans catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Test Plans'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Test Plans Plans Pricing
  plan_count: 3
  slug: test-plans-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Test Plans Rate Limits
  slug: test-plans-rate-limits
rules:
- name: Test Plans API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: test-plans-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.8
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 47.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/test-plans/refs/heads/main/screenshots/test-plans-2026-06-20T195146.png
security:
- kind: domain-security
  name: Test Plans Domain Security
  slug: test-plans-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: test-plans
tags:
- Documentation
- Quality Assurance
- Software Development
- Test Management
- Testing
use_cases:
- description: Create a comprehensive test plan for each release cycle defining scope and success criteria.
  name: Release Test Planning
- description: Plan testing activities within agile sprints aligned to user stories and acceptance criteria.
  name: Sprint Test Planning
- description: Use test plans to document testing required for regulatory and compliance certifications.
  name: Regulatory Compliance Testing
- description: Plan load, stress, and performance test scenarios with target metrics and thresholds.
  name: Performance Test Planning
- description: Coordinate user acceptance testing with business stakeholders through structured test plans.
  name: UAT Coordination
website: https://en.wikipedia.org/wiki/Test_plan
---
