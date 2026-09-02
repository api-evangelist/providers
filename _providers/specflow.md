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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: SpecFlow is a BDD framework for .NET that bridges the communication gap between domain experts and developers by enabling natural language specifications (Gherkin) to be executed as automated tests. I
  name: SpecFlow
  slug: specflow
- description: Reqnroll is the open-source community continuation and fork of SpecFlow, maintaining full backward compatibility while supporting .NET 8.0 and .NET 9.0. Created in 2024 after Tricentis announced SpecF
  name: Reqnroll
  slug: reqnroll
artifact_total: 26
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/tricentis/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/specflow-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/specflow
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/SpecFlowOSS/SpecFlow
- group: docs
  title: ''
  type: Documentation
  url: https://docs.specflow.org
- group: other
  title: ''
  type: NuGet
  url: https://www.nuget.org/packages/SpecFlow/
- group: other
  title: ''
  type: Successor
  url: https://reqnroll.net/
- group: company
  title: ''
  type: Blog
  url: https://reqnroll.net/news/2025/01/specflow-end-of-life-has-been-announced/
created: '2024-01-01'
description: SpecFlow was an open-source BDD (Behavior-Driven Development) testing framework for .NET that allowed teams to write executable specifications in natural language using the Gherkin syntax. Originally developed by TechTalk, it was acquired by Tricentis in 2020 and reached end-of-life on December 31, 2024. The community continuation is Reqnroll, a fork maintaining full backward compatibility.
examples:
- key_count: 5
  name: Specflow Feature Example
  slug: specflow-feature-example
features:
- name: Gherkin Syntax
- name: BDD Scenarios
- name: .NET Integration
- name: NUnit Support
- name: xUnit Support
- name: MSTest Support
- name: Visual Studio Integration
- name: Step Definitions
- name: Scenario Outlines
- name: Data Tables
- name: Hooks
- name: Context Injection
- name: Parallel Execution
- name: Living Documentation
finops:
- name: Specflow Finops
  service_category: API
  slug: specflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/specflow.png
json_schemas:
- name: SpecFlow Feature
  property_count: 6
  slug: specflow-feature
- name: SpecFlow Scenario
  property_count: 7
  slug: specflow-scenario
json_structures:
- name: Specflow Feature Structure
  property_count: 0
  slug: specflow-feature-structure
jsonld:
- class_count: 4
  name: Specflow Context
  property_count: 14
  slug: specflow-context
layout: provider
modified: '2026-05-02'
name: SpecFlow
nav: Providers
network: true
overview: 'SpecFlow publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, BDD, Cucumber, Gherkin, and Testing.


  The SpecFlow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SpecFlow''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Specflow Plans Pricing
  plan_count: 3
  slug: specflow-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Specflow Rate Limits
  slug: specflow-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SpecFlow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: specflow-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 17.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/specflow/refs/heads/main/screenshots/specflow-2026-06-20T194251.png
security:
- kind: domain-security
  name: Specflow Domain Security
  slug: specflow-domain-security
  summary_line: TLSv1.3
slug: specflow
tags:
- .NET
- BDD
- Cucumber
- Gherkin
- Testing
---
