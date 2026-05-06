---
aid: acceptance-criteria
url: https://raw.githubusercontent.com/api-evangelist/acceptance-criteria/refs/heads/main/apis.yml
name: Acceptance Criteria
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agile
  - Behavior Driven Development
  - Gherkin
  - Quality Assurance
  - Requirements
  - Testing
  - User Stories
description: Acceptance criteria are predefined conditions that a product, feature, or user story must meet to be considered complete and acceptable by stakeholders. These criteria establish clear, testable requirements that guide development, validate when work is done, and serve as the foundation for automated testing through frameworks like Cucumber, SpecFlow, and Behave. APIs in this space support requirements management, behavior-driven development (BDD), test execution tracking, and agile project management workflows.
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: acceptance-criteria:github-issues-api
    name: GitHub Issues API
    description: GitHub Issues API enables teams to create, manage, and track user stories and acceptance criteria as structured issue records with labels, milestones, and custom fields. Commonly used to attach acceptance criteria directly to issues using body text or checklists in Markdown.
    humanURL: https://docs.github.com/en/rest/issues
    baseURL: https://api.github.com
    tags:
      - Issues
      - User Stories
      - Requirements
      - Project Management
    properties:
      - url: https://docs.github.com/en/rest/issues
        type: Documentation
      - url: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
        type: Authentication
      - url: https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting
        type: RateLimits
  - aid: acceptance-criteria:jira-issues-api
    name: Jira Issues API
    description: Jira REST API provides access to issues, user stories, epics, and acceptance criteria stored in custom fields. Teams use Jira to define, link, and track acceptance criteria against development work items throughout the sprint lifecycle.
    humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/
    baseURL: https://your-domain.atlassian.net/rest/api/3
    tags:
      - Issues
      - User Stories
      - Sprint
      - Project Management
    properties:
      - url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/
        type: Documentation
      - url: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
        type: Authentication
      - url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
        type: RateLimits
  - aid: acceptance-criteria:azure-devops-work-items-api
    name: Azure DevOps Work Items API
    description: Azure DevOps Work Items REST API enables management of user stories, acceptance criteria, and test cases in Azure Boards. Acceptance criteria are stored as a rich text field on Product Backlog Items and User Story work item types, accessible and updatable via REST.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/wit
    tags:
      - Work Items
      - User Stories
      - Azure
      - Project Management
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/
        type: Authentication
  - aid: acceptance-criteria:linear-api
    name: Linear API
    description: Linear GraphQL API provides access to issues, projects, and cycles used by engineering teams to track features and acceptance criteria. Linear supports structured issue descriptions with Markdown, enabling teams to embed acceptance criteria checklists directly on issues.
    humanURL: https://developers.linear.app/docs/graphql/working-with-the-graphql-api
    baseURL: https://api.linear.app/graphql
    tags:
      - Issues
      - Project Management
      - GraphQL
      - Requirements
    properties:
      - url: https://developers.linear.app/docs/graphql/working-with-the-graphql-api
        type: Documentation
      - url: https://developers.linear.app/docs/graphql/working-with-the-graphql-api#authentication
        type: Authentication
  - aid: acceptance-criteria:testrail-api
    name: TestRail API
    description: TestRail REST API provides access to test cases, test runs, test plans, and results. Teams use TestRail to formally document acceptance criteria as test cases with preconditions, expected results, and step-by-step validation criteria that map directly to user stories.
    humanURL: https://support.testrail.com/hc/en-us/articles/7077792415124-Introduction-to-the-TestRail-API
    baseURL: https://your-instance.testrail.io/index.php?/api/v2
    tags:
      - Test Cases
      - Test Management
      - Quality Assurance
      - Requirements
    properties:
      - url: https://support.testrail.com/hc/en-us/articles/7077792415124-Introduction-to-the-TestRail-API
        type: Documentation
      - url: https://support.testrail.com/hc/en-us/articles/7077792415124-Introduction-to-the-TestRail-API#authentication
        type: Authentication
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://www.agilealliance.org/glossary/acceptance-criteria/
  - type: GettingStarted
    url: https://www.mountaingoatsoftware.com/blog/clarifying-the-relationship-between-definition-of-done-and-conditions-of-satisfaction
  - type: SpectralRules
    url: rules/acceptance-criteria-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/requirements-management.yaml
  - type: Vocabulary
    url: vocabulary/acceptance-criteria-vocabulary.yaml
  - url: openapi/acceptance-criteria-management.yaml
    type: OpenAPI
  - url: json-schema/acceptance-criteria-management-user-story-schema.json
    type: JSONSchema
  - url: json-schema/acceptance-criteria-management-acceptance-criterion-schema.json
    type: JSONSchema
  - url: json-schema/acceptance-criteria-management-scenario-schema.json
    type: JSONSchema
  - url: json-schema/acceptance-criteria-management-test-run-schema.json
    type: JSONSchema
  - url: json-structure/acceptance-criteria-management-user-story-structure.json
    type: JSONStructure
  - url: json-structure/acceptance-criteria-management-acceptance-criterion-structure.json
    type: JSONStructure
  - url: json-structure/acceptance-criteria-management-scenario-structure.json
    type: JSONStructure
  - url: json-structure/acceptance-criteria-management-test-run-structure.json
    type: JSONStructure
  - url: json-ld/acceptance-criteria-management-context.jsonld
    type: JSON-LD
  - url: examples/acceptance-criteria-management-user-story-example.json
    type: Example
  - url: examples/acceptance-criteria-management-acceptance-criterion-example.json
    type: Example
  - url: examples/acceptance-criteria-management-scenario-example.json
    type: Example
  - url: examples/acceptance-criteria-management-test-run-example.json
    type: Example
  - type: Features
    data:
      - name: Gherkin Syntax Support
        description: Structured Given/When/Then format for writing human-readable acceptance criteria that can be directly executed as automated tests
      - name: BDD Workflow Integration
        description: Behavior-driven development workflows connecting acceptance criteria to automated test suites via Cucumber, SpecFlow, or Behave
      - name: Acceptance Criteria Checklists
        description: Structured checklist format for breaking down complex acceptance criteria into discrete, verifiable conditions
      - name: Requirements Traceability
        description: Linking acceptance criteria to user stories, epics, test cases, and defects for end-to-end traceability
      - name: Automated Acceptance Testing
        description: Executing acceptance criteria as automated test suites that verify implementation correctness on each code change
      - name: Stakeholder Collaboration
        description: Shared definition of acceptance criteria between product owners, developers, and QA engineers using accessible, plain-language formats
      - name: Definition of Done Integration
        description: Incorporating acceptance criteria verification into team Definition of Done checklists and sprint completion gates
      - name: Test Coverage Reporting
        description: Tracking which acceptance criteria have passing automated tests and which remain untested or failing
  - type: UseCases
    data:
      - name: User Story Validation
        description: Define measurable, testable conditions that must be satisfied before a user story is accepted as complete
      - name: Automated BDD Testing
        description: Convert Gherkin-formatted acceptance criteria into executable test scenarios using Cucumber or SpecFlow
      - name: Sprint Review Preparation
        description: Use acceptance criteria as the basis for demonstrating completed work to stakeholders during sprint reviews
      - name: Regression Prevention
        description: Maintain automated acceptance test suites that run on every pull request to prevent regressions
      - name: API Contract Verification
        description: Use acceptance criteria to define and verify API behavior contracts between producers and consumers
      - name: Requirements Handoff
        description: Communicate precise feature requirements from product managers to engineers using structured acceptance criteria templates
      - name: Quality Gate Enforcement
        description: Block deployments or story completion when acceptance criteria tests are failing in CI/CD pipelines
  - type: Integrations
    data:
      - name: Cucumber
        description: Open-source BDD testing framework that executes Gherkin-formatted acceptance criteria as automated tests
      - name: SpecFlow
        description: BDD framework for .NET that maps Gherkin feature files to C# step definitions for automated acceptance testing
      - name: Behave
        description: Python BDD testing library that runs Gherkin acceptance criteria scenarios against Python application code
      - name: Jira
        description: Project management platform with dedicated Acceptance Criteria field on user story issue types
      - name: GitHub Issues
        description: Issue tracking with Markdown checklist support for embedding structured acceptance criteria on feature issues
      - name: Azure DevOps Boards
        description: Microsoft project management with Acceptance Criteria rich-text field on User Story and Product Backlog Item work items
      - name: TestRail
        description: Test management platform for formalizing acceptance criteria as structured test cases with expected outcomes
      - name: Linear
        description: Modern issue tracker supporting Markdown acceptance criteria on issues with checklist rendering
---
