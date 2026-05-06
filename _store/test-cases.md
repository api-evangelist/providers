---
name: Test Cases
description: Structured scenarios that verify software functionality by defining inputs, execution conditions, and expected results to ensure quality and correctness. Test cases are the fundamental units of software testing that document what needs to be tested, the conditions under which the test runs, and the expected outcomes. They are widely used across manual testing, automated testing, and API testing workflows.
url: https://en.wikipedia.org/wiki/Test_case
tags:
  - API Testing
  - Automation
  - Quality Assurance
  - Software Development
  - Software Testing
  - Testing
created: '2025'
modified: '2026-05-03'
apis:
  - name: Postman API
    description: API for managing Postman collections, environments, monitors, mock servers, and test runs programmatically. Supports creating and executing test cases via Newman and Postman scripts.
    humanURL: https://www.postman.com/postman/workspace/postman-public-workspace/collection/12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a
    baseURL: https://api.getpostman.com
    tags:
      - API Testing
      - Collections
      - Environments
      - Test Automation
    properties:
      - type: Documentation
        url: https://www.postman.com/postman/workspace/postman-public-workspace/documentation/12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a
  - name: TestRail API
    description: REST API for TestRail test case management system, enabling programmatic creation, update, and retrieval of test cases, test runs, test plans, and results.
    humanURL: https://www.testrail.com/api
    baseURL: https://yourproject.testrail.io/index.php?/api/v2
    tags:
      - Test Case Management
      - Test Management
      - Test Runs
      - Testing
    properties:
      - type: Documentation
        url: https://support.testrail.com/hc/en-us/articles/7077990413588-Introduction-to-the-API
      - type: APIReference
        url: https://support.testrail.com/hc/en-us/categories/7076832415124-API-Reference
  - name: Zephyr Scale API
    description: REST API for Zephyr Scale test management in Jira Cloud, supporting test case creation, test cycles, test execution, and reporting within Jira.
    humanURL: https://support.smartbear.com/zephyr-scale-cloud/api-docs/
    baseURL: https://api.zephyrscale.smartbear.com/v2
    tags:
      - Jira
      - Test Case Management
      - Test Management
      - Testing
    properties:
      - type: Documentation
        url: https://support.smartbear.com/zephyr-scale-cloud/api-docs/
  - name: Xray Test Management API
    description: REST API for Xray test management in Jira, supporting test case management, test execution, test coverage, and CI/CD integration for structured test case workflows.
    humanURL: https://docs.getxray.app/display/XRAYCLOUD/REST+API
    baseURL: https://xray.cloud.getxray.app/api/v2
    tags:
      - Behavior-Driven Development
      - Jira
      - Test Case Management
      - Test Execution
    properties:
      - type: Documentation
        url: https://docs.getxray.app/display/XRAYCLOUD/REST+API
  - name: PractiTest API
    description: REST API for PractiTest test management platform supporting test case libraries, test runs, requirements, defects, and full quality management workflows.
    humanURL: https://developers.practitest.com
    baseURL: https://api.practitest.com/api/v2
    tags:
      - Quality Management
      - Requirements
      - Test Case Management
      - Testing
    properties:
      - type: Documentation
        url: https://developers.practitest.com
      - type: APIReference
        url: https://developers.practitest.com/docs/api-reference
  - name: Katalon TestOps API
    description: API for Katalon TestOps test automation platform, providing endpoints for test case management, test execution, reports, and integration with CI/CD pipelines.
    humanURL: https://katalon.com
    baseURL: https://testops.katalon.io/api/v1
    tags:
      - CI/CD Integration
      - Test Automation
      - Test Case Management
      - Testing
    properties:
      - type: Documentation
        url: https://docs.katalon.com/docs/katalon-testops/remote-execution/katalon-testops-api
common:
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Test_case
  - type: Features
    data:
      - name: Test Case Design
        description: Define structured test scenarios with preconditions, inputs, execution steps, and expected results.
      - name: Test Case Management
        description: Organize, version, and prioritize test cases within test suites and test plans.
      - name: Parameterized Testing
        description: Run test cases with multiple input datasets using data-driven testing approaches.
      - name: Reusability
        description: Share and reuse test cases across different test suites and projects.
      - name: Traceability
        description: Link test cases to requirements, user stories, and defects for full traceability.
      - name: Automated Execution
        description: Execute test cases programmatically via APIs or CI/CD integrations.
  - type: UseCases
    data:
      - name: Regression Testing
        description: Verify that existing functionality has not been broken by recent code changes.
      - name: Acceptance Testing
        description: Confirm that software meets business requirements and user expectations.
      - name: API Contract Testing
        description: Validate API request and response payloads against defined contracts and schemas.
      - name: Smoke Testing
        description: Quickly verify that the most critical application functions work after a new build.
      - name: Integration Testing
        description: Validate that different modules and services interact correctly with each other.
  - type: Integrations
    data:
      - name: Jira
        description: Link test cases to Jira issues and track test coverage for requirements.
      - name: Jenkins
        description: Trigger test case execution as part of Jenkins CI/CD pipelines.
      - name: GitHub Actions
        description: Run test cases automatically on pull requests and push events.
      - name: Slack
        description: Receive test run notifications and results in Slack channels.
  - type: JSONSchema
    url: json-schema/test-cases-test-case-schema.json
  - type: JSONSchema
    url: json-schema/test-cases-test-step-schema.json
  - type: JSONSchema
    url: json-schema/test-cases-test-result-schema.json
  - type: JSONSchema
    url: json-schema/test-cases-test-suite-schema.json
  - type: JSONLD
    url: json-ld/test-cases-context.jsonld
  - type: Vocabulary
    url: vocabulary/test-cases-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
