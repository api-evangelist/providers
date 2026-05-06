---
aid: apigen
url: https://raw.githubusercontent.com/api-evangelist/apigen/refs/heads/main/apis.yml
name: APIGen
description: ApiGen is an open source PHP API documentation generator that automatically produces smart and simple documentation from PHP source code. It supports PHP 7.1+ including all PHP 8.3 features like enums, union types, readonly classes, and intersection types. ApiGen is maintained by the ApiGen GitHub organization and can be installed via Docker, Phar binary, or Composer.
tags:
  - Code
  - Documentation
  - Generation
  - Open Source
  - PHP
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: apigen:apigen
    name: APIGen
    tags:
      - Documentation
      - Generation
      - PHP
    humanURL: https://github.com/ApiGen/ApiGen
    baseURL: https://api.apigen.com/v1
    properties:
      - url: https://github.com/ApiGen/ApiGen
        type: GitHubRepository
      - url: https://packagist.org/packages/apigen/apigen
        type: SDK
        title: Composer Package
      - url: openapi/apigen-apigen-openapi.yml
        type: OpenAPI
      - url: json-schema/apigen-project-schema.json
        type: JSONSchema
      - url: json-schema/apigen-api-schema.json
        type: JSONSchema
      - url: json-schema/apigen-endpoint-schema.json
        type: JSONSchema
      - url: json-schema/apigen-deployment-schema.json
        type: JSONSchema
      - url: json-ld/apigen-context.jsonld
        type: JSON-LD
    description: ApiGen is an easy to use and modern PHP API documentation generator that automatically builds API documentation from PHP source code with full support for PHP 7.1+ features including typed properties, enums, union types, readonly classes, and typed class constants.
common:
  - url: https://github.com/ApiGen/ApiGen
    type: GitHubOrganization
  - url: https://packagist.org/packages/apigen/apigen
    type: SDK
  - url: https://hub.docker.com/r/apigen/apigen
    type: Docker
  - type: Features
    data:
      - name: PHP Documentation Generation
        description: Automatically generates API documentation from PHP source code with phpDoc support.
      - name: Modern PHP Support
        description: Full support for PHP 7.1+ including typed properties, enums, union types, readonly classes, and PHP 8.3 features.
      - name: Advanced Type Systems
        description: Supports intersection types, disjunctive normal form types, constructor property promotion, and all PHPStan-supported types.
      - name: Flexible Installation
        description: Available via Docker, Phar binary, or Composer for flexible integration into any PHP project workflow.
      - name: Template-Based Output
        description: Uses Latte templating for customizable documentation output with built-in CommonMark support.
  - type: UseCases
    data:
      - name: PHP Library Documentation
        description: Generate comprehensive API reference documentation for PHP libraries and packages.
      - name: CI/CD Documentation Pipeline
        description: Automate API documentation generation as part of continuous integration workflows.
      - name: Open Source Project Docs
        description: Create and maintain documentation for open source PHP projects.
  - type: Integrations
    data:
      - name: Composer
        description: Available as a Composer package for easy installation in PHP projects.
      - name: Docker
        description: Official Docker image for containerized documentation generation.
      - name: GitHub Actions
        description: Can be integrated into GitHub Actions workflows for automated documentation.
      - name: PHPStan
        description: Built on phpstan/phpdoc-parser for comprehensive type system support.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
