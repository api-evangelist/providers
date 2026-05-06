---
name: Templates
description: A cross-industry subject-matter collection covering API design templates, code templates, documentation templates, API specification templates, and templating engines used in API development and integration workflows. Covers OpenAPI templates, AsyncAPI templates, JSON Schema templates, Postman collection templates, and SDK code generation templates.
url: https://raw.githubusercontent.com/api-evangelist/templates/refs/heads/main/apis.yml
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Templates
  - API Design
  - Code Generation
  - Documentation
  - OpenAPI
  - AsyncAPI
apis:
  - name: Mustache Templates
    description: Mustache is a logic-less template syntax available for HTML, config files, source code, and more. Used widely for API client SDK generation, documentation generation, and configuration templating.
    humanURL: https://mustache.github.io/
    tags:
      - Templating
      - Code Generation
      - Developer Tools
    properties:
      - type: Documentation
        url: https://mustache.github.io/mustache.5.html
      - type: GitHub Repository
        url: https://github.com/mustache/mustache
  - name: Handlebars.js
    description: Handlebars provides the power necessary to let you build semantic templates effectively with no frustration. Widely used in API documentation generation, email templates, and API portal theming.
    humanURL: https://handlebarsjs.com/
    tags:
      - Templating
      - JavaScript
      - Documentation
    properties:
      - type: Documentation
        url: https://handlebarsjs.com/guide/
      - type: GitHub Repository
        url: https://github.com/handlebars-lang/handlebars.js
  - name: Jinja2
    description: Jinja is a fast, expressive, and extensible templating engine for Python. Used in API code generation (Cookiecutter templates), OpenAPI spec generation, Ansible playbooks, and infrastructure-as-code templates.
    humanURL: https://jinja.palletsprojects.com/
    tags:
      - Templating
      - Python
      - Code Generation
    properties:
      - type: Documentation
        url: https://jinja.palletsprojects.com/en/latest/
      - type: GitHub Repository
        url: https://github.com/pallets/jinja
  - name: OpenAPI Generator
    description: OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec. Supports 50+ languages and frameworks via configurable templates.
    humanURL: https://openapi-generator.tech/
    tags:
      - OpenAPI
      - Code Generation
      - SDK
      - Templates
    properties:
      - type: Documentation
        url: https://openapi-generator.tech/docs/
      - type: GitHub Repository
        url: https://github.com/OpenAPITools/openapi-generator
  - name: Cookiecutter
    description: A command-line utility that creates projects from project templates. Widely used for API project bootstrapping including FastAPI, Flask, Django REST, and microservice templates with standardized structure.
    humanURL: https://cookiecutter.readthedocs.io/
    tags:
      - Project Templates
      - Python
      - Scaffolding
      - Developer Tools
    properties:
      - type: Documentation
        url: https://cookiecutter.readthedocs.io/en/stable/
      - type: GitHub Repository
        url: https://github.com/cookiecutter/cookiecutter
  - name: Yeoman
    description: Yeoman is a scaffolding tool for modern webapps and APIs. Generators provide templates for REST APIs, Express apps, OpenAPI-first projects, and full-stack applications following community best practices.
    humanURL: https://yeoman.io/
    tags:
      - Scaffolding
      - JavaScript
      - Node.js
      - Developer Tools
    properties:
      - type: Documentation
        url: https://yeoman.io/learning/
      - type: GitHub Repository
        url: https://github.com/yeoman/yeoman
common:
  - type: Website
    url: https://mustache.github.io/
  - type: GitHub Repository
    url: https://github.com/mustache/mustache
  - type: JSON-LD
    url: json-ld/templates-context.jsonld
  - type: JSONSchema
    url: json-schema/templates-template-schema.json
  - type: Vocabulary
    url: vocabulary/templates-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
