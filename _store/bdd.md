---
aid: bdd
name: BDD (Behavior-Driven Development)
description: Behavior-Driven Development (BDD) is a software development methodology that combines test-driven development with domain-driven design, encouraging collaboration between developers, QA, and business stakeholders through human-readable test scenarios. The BDD ecosystem includes frameworks, tools, and data providers that enable teams to write specifications in Gherkin syntax (Given-When-Then) and automate those scenarios as executable tests across APIs, UIs, and microservices.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - BDD
  - Software Development
  - Testing
  - Gherkin
  - Quality Assurance
url: https://raw.githubusercontent.com/api-evangelist/bdd/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: bdd:cucumber
    name: Cucumber
    description: Cucumber is the world's most popular BDD framework, supporting Java, JavaScript, Ruby, Python, and C#. It uses Gherkin syntax for writing human-readable test scenarios and provides integrations with all major test runners, CI/CD platforms, and API testing tools. Cucumber School offers learning resources and the Cucumber Open platform provides team-based BDD tooling.
    humanURL: https://cucumber.io/
    tags:
      - BDD
      - Testing
      - Gherkin
      - Java
      - JavaScript
    properties:
      - type: Documentation
        url: https://cucumber.io/docs/cucumber/
      - type: GettingStarted
        url: https://cucumber.io/docs/guides/10-minute-tutorial/
      - type: GitHubRepository
        url: https://github.com/cucumber/cucumber-jvm
  - aid: bdd:specflow
    name: SpecFlow
    description: SpecFlow is a BDD framework for .NET developers, enabling teams to write behavior specifications in Gherkin and execute them in C# applications. SpecFlow+ Runner and SpecFlow+ LivingDoc provide enhanced test execution and living documentation capabilities.
    humanURL: https://specflow.org/
    tags:
      - BDD
      - Testing
      - Gherkin
      - .NET
      - C#
    properties:
      - type: Documentation
        url: https://docs.specflow.org/
      - type: GettingStarted
        url: https://docs.specflow.org/projects/specflow/en/latest/Getting-Started/
  - aid: bdd:behave
    name: Behave
    description: Behave is a Python BDD framework inspired by Cucumber that enables teams to write behavior specifications in Gherkin syntax and execute them using Python. It integrates with Django, Flask, FastAPI, and REST API testing tools.
    humanURL: https://behave.readthedocs.io/
    tags:
      - BDD
      - Testing
      - Gherkin
      - Python
    properties:
      - type: Documentation
        url: https://behave.readthedocs.io/en/stable/
      - type: GitHubRepository
        url: https://github.com/behave/behave
  - aid: bdd:karate
    name: Karate
    description: Karate is a modern open-source BDD framework that unifies API testing, UI automation, performance testing, and mocking in a single framework. It uses a Gherkin-like DSL and is particularly powerful for REST and GraphQL API testing with JSON/XML validation, JavaScript scripting, and parallel execution.
    humanURL: https://karatelabs.github.io/karate/
    tags:
      - BDD
      - API Testing
      - REST Testing
      - Performance Testing
    properties:
      - type: Documentation
        url: https://karatelabs.github.io/karate/
      - type: GitHubRepository
        url: https://github.com/karatelabs/karate
  - aid: bdd:jbehave
    name: JBehave
    description: JBehave is a pioneering BDD framework for Java and JVM languages. It supports web, REST API, and microservices testing with integration for JUnit, Spring, Maven, and Gradle. JBehave Web extends the framework for browser-based BDD testing.
    humanURL: https://jbehave.org/
    tags:
      - BDD
      - Testing
      - Java
      - JVM
    properties:
      - type: Documentation
        url: https://jbehave.org/reference/latest/
      - type: GitHubRepository
        url: https://github.com/jbehave/jbehave-core
common:
  - type: Website
    url: https://cucumber.io/
  - type: Documentation
    url: https://cucumber.io/docs/
  - type: GitHubOrganization
    url: https://github.com/cucumber
  - type: Features
    data:
      - name: Gherkin Syntax
        description: Human-readable Given-When-Then scenario language for describing software behavior as executable specifications.
      - name: Multi-Language Support
        description: BDD frameworks available for Java, JavaScript, Python, Ruby, C#, Go, and most other programming languages.
      - name: API Testing Integration
        description: Frameworks like Karate and Cucumber enable BDD-style API testing for REST, GraphQL, and SOAP services.
      - name: Living Documentation
        description: BDD scenarios serve as living documentation that stays synchronized with the actual system behavior.
      - name: CI/CD Integration
        description: All major BDD frameworks integrate with Jenkins, GitHub Actions, GitLab CI, CircleCI, and other CI/CD platforms.
  - type: UseCases
    data:
      - name: API Contract Testing
        description: Use BDD frameworks to write executable API contract tests that verify request/response behavior from a business perspective.
      - name: Acceptance Testing
        description: Write acceptance tests in Gherkin that business stakeholders can read and validate before implementation begins.
      - name: Regression Testing
        description: Build a regression test suite using BDD scenarios that can be run automatically on every code change.
      - name: Microservices Testing
        description: Test microservice integrations using BDD frameworks with HTTP clients and mock servers.
  - type: Integrations
    data:
      - name: JUnit
        description: Java test runner integration for executing Cucumber and JBehave scenarios in Java projects.
      - name: Playwright
        description: Browser automation integration for UI-level BDD testing with Cucumber or SpecFlow.
      - name: REST Assured
        description: Java DSL for REST API testing commonly used with Cucumber for BDD-style API test suites.
      - name: Postman
        description: API testing platform that supports BDD-style test writing in the test scripts section.
      - name: Allure
        description: Test reporting framework that integrates with Cucumber, SpecFlow, and other BDD frameworks for rich HTML reports.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
