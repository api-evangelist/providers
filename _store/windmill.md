---
aid: windmill
name: Windmill
segments:
  - ProCode API Composition
  - Workflows
description: Windmill is an open-source developer platform and workflow engine for turning scripts into webhooks, workflows, and internal apps. It supports TypeScript, Python, Go, PHP, Bash, C#, SQL, and Rust, and serves as an open-source alternative to Retool, Airflow, and Temporal for building comprehensive internal tools including endpoints, workflows, and UIs.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Internal Tools
  - Open Source
  - ProCode API Composition
  - Scripts
  - Webhooks
  - Workflow Engine
  - Workflows
created: '2026-03-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/windmill/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: windmill:windmill-api
    name: Windmill API
    description: The Windmill API provides programmatic access to the Windmill developer platform, enabling management of scripts, flows, apps, resources, variables, schedules, jobs, users, workspaces, and webhooks. It follows the OpenAPI 3.0.3 specification and powers all interactions with the Windmill platform.
    humanURL: https://www.windmill.dev/docs/intro
    baseURL: https://app.windmill.dev/api
    tags:
      - Automation
      - Internal Tools
      - ProCode_API_Composition
      - Scripts
      - Webhooks
      - Workflows
    properties:
      - type: Documentation
        url: https://www.windmill.dev/docs/intro
      - type: OpenAPI
        url: https://raw.githubusercontent.com/windmill-labs/windmill/main/backend/windmill-api/openapi.yaml
      - type: APIReferenceDocumentation
        url: https://app.windmill.dev/openapi.html
      - type: GettingStarted
        url: https://www.windmill.dev/docs/getting_started/how_to_use_windmill
      - type: Authentication
        url: https://www.windmill.dev/docs/core_concepts/authentification
      - type: HTTPRoutes
        url: https://www.windmill.dev/docs/core_concepts/http_routing
      - type: CLI
        url: https://www.windmill.dev/docs/advanced/cli
      - type: SelfHosting
        url: https://www.windmill.dev/docs/advanced/self_host
      - type: TypeScriptSDK
        url: https://www.windmill.dev/docs/advanced/clients/ts_client
      - type: PythonSDK
        url: https://www.windmill.dev/docs/advanced/clients/python_client
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/windmill/refs/heads/main/openapi/windmill-api-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/windmill/refs/heads/main/rules/windmill-api-rules.yml
common:
  - type: Portal
    url: https://www.windmill.dev
  - type: Documentation
    url: https://www.windmill.dev/docs/intro
  - type: GettingStarted
    url: https://www.windmill.dev/docs/getting_started/how_to_use_windmill
  - type: Pricing
    url: https://www.windmill.dev/pricing
  - type: Plans
    url: https://www.windmill.dev/docs/misc/plans_details
  - type: Blog
    url: https://www.windmill.dev/blog
  - type: Changelog
    url: https://www.windmill.dev/changelog
  - type: Roadmap
    url: https://www.windmill.dev/roadmap
  - type: Login
    url: https://app.windmill.dev/user/login
  - type: GitHubOrg
    url: https://github.com/windmill-labs
  - type: GitHubRepo
    url: https://github.com/windmill-labs/windmill
  - type: IntegrationHub
    url: https://hub.windmill.dev
  - type: StatusPage
    url: https://windmill.betteruptime.com/
  - type: Discord
    url: https://discord.com/invite/V7PM2YHsPB
  - type: CommunityForum
    url: https://questions.windmill.dev/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/windmill-labs/windmill/main/backend/windmill-api/openapi.yaml
  - type: TermsOfService
    url: https://www.windmill.dev/terms_of_service
  - type: PrivacyPolicy
    url: https://www.windmill.dev/privacy_policy
  - type: LicenseTerms
    url: https://www.windmill.dev/terms
  - type: TrustCenter
    url: https://trust.windmill.dev
  - type: Careers
    url: https://www.windmill.dev/careers
  - type: Partners
    url: https://www.windmill.dev/partners
  - type: CaseStudies
    url: https://www.windmill.dev/case-studies
  - type: Brand
    url: https://www.windmill.dev/brand
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/windmill/refs/heads/main/json-ld/windmill-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/windmill/refs/heads/main/vocabulary/windmill-vocabulary.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/windmill/refs/heads/main/capabilities/workflow-automation.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
