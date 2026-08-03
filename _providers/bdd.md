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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Cucumber is the world's most popular BDD framework, supporting Java, JavaScript, Ruby, Python, and C#. It uses Gherkin syntax for writing human-readable test scenarios and provides integrations with a
  name: Cucumber
  slug: cucumber
- description: SpecFlow is a BDD framework for .NET developers, enabling teams to write behavior specifications in Gherkin and execute them in C# applications. SpecFlow+ Runner and SpecFlow+ LivingDoc provide enhanc
  name: SpecFlow
  slug: specflow
- description: Behave is a Python BDD framework inspired by Cucumber that enables teams to write behavior specifications in Gherkin syntax and execute them using Python. It integrates with Django, Flask, FastAPI, an
  name: Behave
  slug: behave
- description: Karate is a modern open-source BDD framework that unifies API testing, UI automation, performance testing, and mocking in a single framework. It uses a Gherkin-like DSL and is particularly powerful fo
  name: Karate
  slug: karate
- description: JBehave is a pioneering BDD framework for Java and JVM languages. It supports web, REST API, and microservices testing with integration for JUnit, Spring, Maven, and Gradle. JBehave Web extends the fr
  name: JBehave
  slug: jbehave
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bdd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cucumber.io/
- group: company
  title: ''
  type: Blog
  url: https://cucumber.io/blog/rss.xml
- group: docs
  title: ''
  type: Documentation
  url: https://cucumber.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cucumber
created: '2025-01-01'
description: Behavior-Driven Development (BDD) is a software development methodology that combines test-driven development with domain-driven design, encouraging collaboration between developers, QA, and business stakeholders through human-readable test scenarios. The BDD ecosystem includes frameworks, tools, and data providers that enable teams to write specifications in Gherkin syntax (Given-When-Then) and automate those scenarios as executable tests across APIs, UIs, and microservices.
features:
- description: Human-readable Given-When-Then scenario language for describing software behavior as executable specifications.
  name: Gherkin Syntax
- description: BDD frameworks available for Java, JavaScript, Python, Ruby, C#, Go, and most other programming languages.
  name: Multi-Language Support
- description: Frameworks like Karate and Cucumber enable BDD-style API testing for REST, GraphQL, and SOAP services.
  name: API Testing Integration
- description: BDD scenarios serve as living documentation that stays synchronized with the actual system behavior.
  name: Living Documentation
- description: All major BDD frameworks integrate with Jenkins, GitHub Actions, GitLab CI, CircleCI, and other CI/CD platforms.
  name: CI/CD Integration
finops:
- name: Bdd Finops
  service_category: API
  slug: bdd-finops
graphqls:
- description: ''
  name: BDD (Behavior-Driven Development) GraphQL API
  slug: bdd-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bdd.png
integrations:
- description: Java test runner integration for executing Cucumber and JBehave scenarios in Java projects.
  name: JUnit
- description: Browser automation integration for UI-level BDD testing with Cucumber or SpecFlow.
  name: Playwright
- description: Java DSL for REST API testing commonly used with Cucumber for BDD-style API test suites.
  name: REST Assured
- description: API testing platform that supports BDD-style test writing in the test scripts section.
  name: Postman
- description: Test reporting framework that integrates with Cucumber, SpecFlow, and other BDD frameworks for rich HTML reports.
  name: Allure
layout: provider
modified: '2026-04-19'
name: BDD (Behavior-Driven Development)
nav: Providers
network: true
overview: 'BDD (Behavior-Driven Development) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, BDD, Software Development, Testing, and Gherkin.


  BDD (Behavior-Driven Development)''s developer surface includes engineering blog, documentation, and 3 more developer resources.'
plans:
- name: Bdd Plans Pricing
  plan_count: 3
  slug: bdd-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Bdd Rate Limits
  slug: bdd-rate-limits
score:
  band: emerging
  composite: 21.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bdd/refs/heads/main/screenshots/bdd-2026-06-20T173104.png
security:
- kind: domain-security
  name: Bdd Domain Security
  slug: bdd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bdd
tags:
- Automation
- BDD
- Software Development
- Testing
- Gherkin
- Quality Assurance
use_cases:
- description: Use BDD frameworks to write executable API contract tests that verify request/response behavior from a business perspective.
  name: API Contract Testing
- description: Write acceptance tests in Gherkin that business stakeholders can read and validate before implementation begins.
  name: Acceptance Testing
- description: Build a regression test suite using BDD scenarios that can be run automatically on every code change.
  name: Regression Testing
- description: Test microservice integrations using BDD frameworks with HTTP clients and mock servers.
  name: Microservices Testing
website: https://cucumber.io/
---
