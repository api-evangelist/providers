---
aid: cucumber
url: https://raw.githubusercontent.com/api-evangelist/cucumber/refs/heads/main/apis.yml
x-type: opensource
name: Cucumber
description: Cucumber is an open-source Behavior Driven Development (BDD) tool for running automated tests written in plain language using the Gherkin syntax. It enables collaboration between technical and non-technical team members by expressing executable specifications as Given/When/Then scenarios. Cucumber has implementations for many languages (JVM, JavaScript, Ruby, .NET, Python, Go, Rust) and a shared message protocol that connects parsers, runners, and reporters.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - BDD
  - Behavior Driven Development
  - Gherkin
  - Open Source
  - Quality Assurance
  - Test Framework
  - Testing
type: Index
specificationVersion: '0.19'
created: '2024-01-01'
modified: '2026-04-28'
apis:
  - aid: cucumber:cucumber-jvm
    name: Cucumber JVM
    description: Java/JVM implementation of Cucumber supporting Java, Kotlin, Scala, and other JVM languages. Distributed via Maven Central under the io.cucumber group.
    humanURL: https://github.com/cucumber/cucumber-jvm
    baseURL: https://github.com/cucumber/cucumber-jvm
    tags:
      - BDD
      - Java
      - JVM
      - Kotlin
      - Scala
      - Testing
    properties:
      - type: GitHubRepository
        url: https://github.com/cucumber/cucumber-jvm
      - type: Documentation
        url: https://cucumber.io/docs/cucumber/
      - type: PackageIndex
        url: https://search.maven.org/search?q=g:io.cucumber
  - aid: cucumber:cucumber-js
    name: Cucumber.js
    description: JavaScript/Node.js implementation of Cucumber for running BDD tests in Node and the browser. Distributed as @cucumber/cucumber on npm.
    humanURL: https://github.com/cucumber/cucumber-js
    baseURL: https://github.com/cucumber/cucumber-js
    tags:
      - BDD
      - JavaScript
      - Node.js
      - Testing
    properties:
      - type: GitHubRepository
        url: https://github.com/cucumber/cucumber-js
      - type: Documentation
        url: https://github.com/cucumber/cucumber-js/blob/main/docs/
      - type: PackageIndex
        url: https://www.npmjs.com/package/@cucumber/cucumber
  - aid: cucumber:cucumber-ruby
    name: Cucumber Ruby
    description: Ruby implementation of Cucumber, the original Cucumber project. Distributed as the cucumber gem on RubyGems.
    humanURL: https://github.com/cucumber/cucumber-ruby
    baseURL: https://github.com/cucumber/cucumber-ruby
    tags:
      - BDD
      - Ruby
      - Testing
    properties:
      - type: GitHubRepository
        url: https://github.com/cucumber/cucumber-ruby
      - type: Documentation
        url: https://cucumber.io/docs/cucumber/
      - type: PackageIndex
        url: https://rubygems.org/gems/cucumber
  - aid: cucumber:gherkin
    name: Gherkin
    description: Gherkin is the language used to write Cucumber feature files. Parsers are published per language and emit Cucumber Messages that downstream tools consume.
    humanURL: https://github.com/cucumber/gherkin
    tags:
      - DSL
      - Gherkin
      - Parser
    properties:
      - type: GitHubRepository
        url: https://github.com/cucumber/gherkin
      - type: Reference
        url: https://cucumber.io/docs/gherkin/reference/
  - aid: cucumber:cucumber-messages
    name: Cucumber Messages
    description: Protocol-buffer / JSON Schema specification of the messages exchanged between Cucumber components (parsers, runners, formatters). Implemented across all language ports for consistent reporting.
    humanURL: https://github.com/cucumber/messages
    tags:
      - Protocol
      - JSON Schema
      - Messages
    properties:
      - type: GitHubRepository
        url: https://github.com/cucumber/messages
      - type: JSONSchema
        url: json-schema/cucumber-message-schema.json
features:
  - name: Plain-Language Specifications
    description: Tests written in Gherkin (Given/When/Then) readable by non-engineers.
  - name: Multi-Language Implementations
    description: First-class implementations for JVM, JavaScript, Ruby, .NET, Python, Go, and Rust.
  - name: Step Definitions and Cucumber Expressions
    description: Pattern-matched code bindings for Gherkin steps via regex or Cucumber Expressions.
  - name: Hooks and Tags
    description: Before/After hooks plus tag-driven scenario selection and configuration.
  - name: Cucumber Messages Protocol
    description: Shared message format for parsers, runners, and formatters across implementations.
  - name: Pluggable Formatters
    description: Built-in pretty, JSON, JUnit, and HTML reporters; third-party formatters supported.
  - name: Parallel Execution
    description: Implementations support parallel scenario execution.
  - name: CI Integration
    description: Reports plug into CI systems (GitHub Actions, Jenkins, GitLab) via JUnit/HTML output.
useCases:
  - name: Acceptance Testing
    description: Product, QA, and engineering collaborate on acceptance tests written in Gherkin.
  - name: Living Documentation
    description: Feature files double as up-to-date documentation of system behavior.
  - name: API Contract Testing
    description: BDD scenarios verify external API contracts and integrations.
  - name: Regression Suites
    description: Tagged scenarios provide selectable regression suites for CI.
  - name: Cross-Team Communication
    description: Bridges product, QA, and engineering with a shared specification language.
common:
  - type: Website
    url: https://cucumber.io
  - type: Documentation
    url: https://cucumber.io/docs
  - type: Reference
    url: https://cucumber.io/docs/gherkin/reference/
  - type: School
    url: https://school.cucumber.io
  - type: Tools
    url: https://cucumber.io/tools
  - type: GitHubOrganization
    url: https://github.com/cucumber
  - type: X
    url: https://twitter.com/cucumberbdd
  - type: Slack
    url: https://cucumber.io/community#slack
  - type: YouTube
    url: https://www.youtube.com/channel/UCVhQ7ulinkFAkUx3eNvzoEg
  - type: JSONSchema
    url: json-schema/cucumber-message-schema.json
  - type: JSONLDContext
    url: json-ld/cucumber-context.jsonld
  - type: Vocabulary
    url: vocabulary/cucumber-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
