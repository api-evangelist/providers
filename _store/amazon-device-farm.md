---
name: Amazon Device Farm
description: AWS Device Farm is an application testing service that lets you improve the quality of your web and mobile apps by testing them across an extensive range of desktop browsers and real mobile devices without having to provision and manage any testing infrastructure.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/device-farm/
created: '2026-03-16'
modified: '2026-04-19'
apis:
  - name: AWS Device Farm API
    description: The AWS Device Farm API enables programmatic access to create and manage test runs, device pools, projects, and jobs for testing mobile and web applications across real devices and browsers. Supports 77 operations covering projects, runs, devices, uploads, remote access sessions, Selenium test grid, network profiles, instance profiles, VPC endpoint configurations, and resource tagging.
    humanURL: https://aws.amazon.com/device-farm/
    baseURL: https://devicefarm.amazonaws.com
    tags:
      - Application Testing
      - Device Management
      - Mobile Testing
      - Quality Assurance
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-device-farm-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/device-farm/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/device-farm/pricing/
      - type: FAQ
        url: https://aws.amazon.com/device-farm/faqs/
      - type: JSONSchema
        url: json-schema/amazon-device-farm-project-schema.json
      - type: JSONSchema
        url: json-schema/amazon-device-farm-run-schema.json
      - type: JSONSchema
        url: json-schema/amazon-device-farm-device-schema.json
      - type: JSONSchema
        url: json-schema/amazon-device-farm-upload-schema.json
      - type: JSONSchema
        url: json-schema/amazon-device-farm-device-pool-schema.json
      - type: JSONStructure
        url: json-structure/amazon-device-farm-project-structure.json
      - type: JSONStructure
        url: json-structure/amazon-device-farm-run-structure.json
      - type: JSONStructure
        url: json-structure/amazon-device-farm-device-structure.json
      - type: JSON-LD
        url: json-ld/amazon-device-farm-context.jsonld
      - type: Example
        url: examples/amazon-device-farm-project-example.json
      - type: Example
        url: examples/amazon-device-farm-run-example.json
      - type: Example
        url: examples/amazon-device-farm-device-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/device-farm/
  - type: Website
    url: https://aws.amazon.com/device-farm/
  - type: Documentation
    url: https://docs.aws.amazon.com/devicefarm/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mobile/category/mobile-services/aws-device-farm/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/devicefarm/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-device-farm-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-device-farm-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/mobile-browser-testing.yaml
  - type: Features
    data:
      - name: Real Device Testing
        description: Test mobile apps on thousands of real physical Android and iOS devices without managing any device infrastructure.
      - name: Desktop Browser Testing
        description: Test web applications on desktop browsers using Selenium RemoteWebDriver through Device Farm's test grid.
      - name: Automated Test Frameworks
        description: Supports popular test frameworks including Appium, XCTest, Espresso, Calabash, and built-in fuzz testing.
      - name: Remote Access Sessions
        description: Interactively access real devices via remote desktop to manually test and debug your app.
      - name: Network Condition Simulation
        description: Simulate different network conditions including bandwidth, latency, and packet loss using network profiles.
      - name: Private Device Fleet
        description: Provision and manage private dedicated devices for exclusive use in testing your applications.
      - name: VPC Integration
        description: Test apps hosted in private VPCs using VPC endpoint configurations without exposing them publicly.
      - name: Parallel Test Execution
        description: Run tests in parallel across multiple devices simultaneously to reduce overall testing time.
  - type: UseCases
    data:
      - name: Mobile App Quality Assurance
        description: Validate mobile app functionality, performance, and compatibility across a wide range of real Android and iOS devices.
      - name: Cross-Device Compatibility Testing
        description: Ensure your app behaves correctly on different device manufacturers, screen sizes, OS versions, and hardware configurations.
      - name: Web Application Browser Testing
        description: Run Selenium-based browser tests against your web application across multiple desktop browser environments.
      - name: CI/CD Test Integration
        description: Integrate device testing into your continuous integration and deployment pipelines for automated quality gates.
      - name: App Performance Benchmarking
        description: Measure app performance metrics including CPU usage, memory consumption, and network activity across different devices.
  - type: Integrations
    data:
      - name: AWS CodePipeline
        description: Integrate Device Farm tests as a stage in your CodePipeline CI/CD pipelines for automated testing.
      - name: AWS CodeBuild
        description: Trigger Device Farm test runs from CodeBuild projects as part of build and deploy workflows.
      - name: Jenkins
        description: Run Device Farm tests from Jenkins CI using the AWS Device Farm plugin for Jenkins.
      - name: Appium
        description: Supports Appium test scripts for both Android and iOS cross-platform mobile testing.
      - name: Selenium
        description: Integrates with Selenium RemoteWebDriver for automated desktop browser testing.
      - name: GitHub Actions
        description: Trigger Device Farm test runs using the AWS Device Farm GitHub Action in your workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Application Testing
  - AWS
  - Device Testing
  - Mobile Testing
  - Quality Assurance
---
