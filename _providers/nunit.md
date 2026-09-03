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
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: The core NUnit testing framework programming API for writing and executing unit tests in .NET applications. Provides assertions, attributes, and lifecycle hooks consumed via the NUnit NuGet package.
  name: NUnit Framework API
  slug: nunit-framework-api
- description: Console runner for executing NUnit tests from the command line, enabling automation in build pipelines and CI/CD systems.
  name: NUnit Console Runner
  slug: nunit-console-runner
- description: Test adapter for running NUnit tests in Visual Studio, dotnet test, and other VSTest-compatible test runners.
  name: NUnit3 Test Adapter
  slug: nunit3-test-adapter
- description: Roslyn-based analyzers for NUnit that detect common test authoring mistakes and suggest fixes at compile time.
  name: NUnit Analyzers
  slug: nunit-analyzers
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nunit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nunit.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nunit.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nunit
- group: company
  title: ''
  type: Blog
  url: https://nunit.org/news/
- group: operate
  title: ''
  type: Community
  url: https://nunit.org/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nunit.org/articles/nunit/release-notes/
- group: commercial
  title: ''
  type: License
  url: https://docs.nunit.org/articles/nunit/license.html
created: '2024-01-01'
description: NUnit is a unit-testing framework for all .NET languages. Initially ported from JUnit, the current production release has been completely rewritten with many new features and support for a wide range of .NET platforms. NUnit is a software testing framework, not a remote HTTP API service.
finops:
- name: Nunit Finops
  service_category: API
  slug: nunit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nunit.png
layout: provider
modified: '2026-04-28'
name: NUnit
nav: Providers
network: true
overview: 'NUnit publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, C#, Framework, Open-Source, and TDD.


  NUnit''s developer surface includes documentation, engineering blog, changelog, and 5 more developer resources.'
plans:
- name: Nunit Plans Pricing
  plan_count: 3
  slug: nunit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Nunit Rate Limits
  slug: nunit-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nunit/refs/heads/main/screenshots/nunit-2026-06-20T190523.png
security:
- kind: domain-security
  name: Nunit Domain Security
  slug: nunit-domain-security
  summary_line: TLSv1.3
slug: nunit
tags:
- .NET
- C#
- Framework
- Open-Source
- TDD
- Testing
- Unit Testing
website: https://nunit.org
---
