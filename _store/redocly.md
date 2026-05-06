---
aid: redocly
url: https://raw.githubusercontent.com/api-evangelist/redocly/refs/heads/main/apis.yml
name: Redocly
description: Redocly is a company that specializes in API documentation and governance tools. Their platform helps organizations create, manage, and publish API documentation through Realm (their integrated lifecycle platform), Revel (developer portal), Reef (internal catalog and scorecard), and Redoc (open-source OpenAPI renderer). The Redocly CLI provides linting, bundling, splitting, decoration, and documentation generation for OpenAPI, AsyncAPI, and Arazzo specifications.
tags:
  - API Catalog
  - API Documentation
  - Developer Portal
  - Governance
  - Linting
  - OpenAPI
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-05'
modified: '2026-05-02'
position: Consumer
segments:
  - Documentation
specificationVersion: '0.19'
apis:
  - aid: redocly:redocly-realm
    name: Redocly Realm
    description: Redocly Realm is a comprehensive API lifecycle management platform that combines Redoc, Revel, and Reef into a single integrated product. Realm includes API documentation, mock servers, linting, catalog, scorecard, API functions, markdown docs, API Scout for discovering hidden or duplicate APIs, and dynamic client registration features.
    humanURL: https://redocly.com/realm
    tags:
      - API Catalog
      - Developer Portal
      - Documentation
    properties:
      - type: Documentation
        url: https://redocly.com/docs/realm
      - type: Changelog
        url: https://redocly.com/docs/realm/changelog
  - aid: redocly:redocly-reunite
    name: Redocly Reunite
    description: Redocly Reunite is a collaboration and deployment tool that prepares, deploys, and hosts documentation projects and mock servers in a Git-connected way. Provides Webview for uncommitted previews, Branch Previews for committed work-in-progress, and automated GitOps production releases. Integrates with GitHub, GitLab, and Azure DevOps.
    humanURL: https://redocly.com/docs/realm
    tags:
      - Collaboration
      - Deployment
      - Documentation
      - GitOps
    properties:
      - type: Documentation
        url: https://redocly.com/docs/realm
  - aid: redocly:redocly-revel
    name: Redocly Revel
    description: Redocly Revel is an external developer showcase that renders Markdown, Markdoc, and React pages with multi-product and localization capabilities, enabling organizations to create polished developer-facing portals and documentation experiences for external API consumers.
    humanURL: https://redocly.com/docs/realm
    tags:
      - Developer Portal
      - Documentation
      - Localization
    properties:
      - type: Documentation
        url: https://redocly.com/docs/realm
  - aid: redocly:redocly-reef
    name: Redocly Reef
    description: Redocly Reef is an internal service catalog and API governance platform that organizes, aids discovery, and monitors APIs throughout their lifecycle. Reef includes Catalog for organizing and searching APIs, Scorecard for running linting rules against APIs, API Scout for discovering hidden APIs, and developer onboarding with dynamic client registration.
    humanURL: https://redocly.com/reef
    tags:
      - API Catalog
      - Governance
      - Scorecard
    properties:
      - type: Documentation
        url: https://redocly.com/reef
      - type: Reference
        url: https://redocly.com/docs/realm/config/scorecard
  - aid: redocly:redocly-redoc
    name: Redocly Redoc
    description: Redoc is the open-source engine that renders API reference documentation from OpenAPI definitions with unmatched clarity and usability. Supports OpenAPI 3.2, 3.1, 3.0 and OpenAPI 2.0 (legacy Swagger). Available as a CLI tool, HTML tag, React component, and Docker image with over 23,000 GitHub stars.
    humanURL: https://redocly.com/redoc
    tags:
      - Documentation
      - OpenAPI
      - Reference
    properties:
      - type: Documentation
        url: https://redocly.com/docs/redoc
      - type: Reference
        url: https://redocly.com/redoc
      - type: GitHubOrg
        url: https://github.com/Redocly/redoc
  - aid: redocly:redocly-cli
    name: Redocly CLI
    description: Redocly CLI is an open-source command-line tool for working with OpenAPI descriptions, developer portals, and other API lifecycle operations. Supports linting, validation, bundling, splitting, and decorating OpenAPI files. Supports OpenAPI 3.2, 3.1, 3.0 and OpenAPI 2.0, AsyncAPI 3.0 and 2.6, and Arazzo 1.0. Provides built-in rulesets including spec, recommended, minimal, and recommended-strict.
    humanURL: https://redocly.com/redocly-cli
    tags:
      - CLI
      - Governance
      - Linting
      - OpenAPI
    properties:
      - type: Documentation
        url: https://redocly.com/docs/cli
      - type: Reference
        url: https://redocly.com/docs/cli/commands/lint
      - type: Changelog
        url: https://redocly.com/docs/cli/changelog
      - type: GitHubOrg
        url: https://github.com/Redocly/redocly-cli
      - type: JSONSchema
        url: json-schema/redocly-config-schema.json
      - type: JSONSchema
        url: json-schema/redocly-lint-result-schema.json
      - type: JSONStructure
        url: json-structure/redocly-config-structure.json
      - type: JSONStructure
        url: json-structure/redocly-lint-result-structure.json
      - type: JSONLd
        url: json-ld/redocly-context.jsonld
      - type: Vocabulary
        url: vocabulary/redocly-vocabulary.yml
common:
  - name: About Redocly Documentation
    url: https://redocly.com/docs
    type: Documentation
  - name: Customers
    url: https://redocly.com/customers
    type: Customers
  - name: Pricing
    url: https://redocly.com/pricing
    type: Pricing
  - name: Redocly Blog
    url: https://redocly.com/blog
    type: Blog
  - name: Webinars
    url: https://redocly.com/webinars
    type: Webinars
  - name: Security at Redocly
    url: https://redocly.com/security
    type: Security
  - name: Redocly Status Page
    url: https://status.redocly.com/
    type: Status
  - name: Service Level Agreement
    url: https://redocly.com/sla
    type: ServiceLevelAgreement
  - name: Redocly CLI
    url: https://redocly.com/redocly-cli
    type: CLI
  - name: About Redocly
    url: https://redocly.com/about
    type: About
  - name: Contact Redocly
    url: https://redocly.com/contact-us
    type: Support
  - name: Redocly Products
    url: https://redocly.com/products
    type: Products
  - name: Redocly Login
    url: https://auth.cloud.redocly.com/login
    type: Login
  - name: Redocly Sign Up
    url: https://redocly.com/billing/signup
    type: SignUp
  - name: Redocly Privacy Notice
    url: https://redocly.com/privacy-notice
    type: PrivacyPolicy
  - name: Redocly Subscription Agreement
    url: https://redocly.com/subscription-agreement
    type: TermsOfService
  - name: Redocly Careers
    url: https://redocly.com/careers
    type: Careers
  - name: Redocly on GitHub
    url: https://github.com/Redocly
    type: GitHubOrg
  - name: Redocly on X
    url: https://twitter.com/Redocly
    type: X
  - name: Redocly on LinkedIn
    url: https://www.linkedin.com/company/redocly
    type: LinkedIn
  - name: Redocly API Governance
    url: https://redocly.com/api-governance
    type: Governance
  - name: Redocly Changelog
    url: https://redocly.com/docs/realm/changelog
    type: Changelog
  - name: Redocly Vulnerability Disclosure Policy
    url: https://redocly.com/vulnerability-disclosure-policy
    type: VulnerabilityDisclosure
  - name: Redocly Data Processing Addendum
    url: https://redocly.com/dpa
    type: DataProcessingAddendum
  - name: Redocly Startup Discount
    url: https://redocly.com/startup-discount
    type: Pricing
  - name: Redocly OpenAPI Reference Docs
    url: https://redocly.com/reference
    type: Reference
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
