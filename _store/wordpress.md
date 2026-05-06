---
aid: wordpress
name: WordPress
description: WordPress is an open-source content management system (CMS) that powers a significant portion of websites on the internet. Its REST API enables applications to interact with WordPress sites by sending and receiving data as JSON, allowing developers to build decoupled frontends, mobile apps, and integrations in any language. The extensive plugin and theme ecosystem, block editor, and AI capabilities make it accessible for building everything from personal blogs to complex enterprise websites.
type: Index
url: https://developer.wordpress.org/rest-api/
tags:
  - CMS
  - Content Management
  - Open Source
  - WordPress
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wordpress:rest-api
    name: WordPress REST API
    description: The WordPress REST API provides endpoints for WordPress data types that allow developers to interact with sites remotely by sending and receiving JSON objects. The REST API is the backbone of the WordPress Block Editor (Gutenberg) and enables building decoupled applications, headless CMS setups, and third-party integrations.
    humanURL: https://developer.wordpress.org/rest-api/
    baseURL: https://{site}/wp-json
    tags:
      - CMS
      - Content
      - Posts
      - REST
      - WordPress
    properties:
      - type: Documentation
        url: https://developer.wordpress.org/rest-api/
      - type: APIReference
        url: https://developer.wordpress.org/rest-api/reference/
      - type: Authentication
        url: https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/
      - type: GettingStarted
        url: https://developer.wordpress.org/rest-api/using-the-rest-api/
      - type: OpenAPI
        url: openapi/wordpress-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/wordpress-post-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-page-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-media-item-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-comment-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-user-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-term-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-settings-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-theme-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-plugin-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-block-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-block-type-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-post-type-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-search-result-schema.json
      - type: JSONSchema
        url: json-schema/wordpress-rendered-content-schema.json
  - aid: wordpress:wp-cli
    name: WP-CLI
    description: WP-CLI is the command-line interface for WordPress. It provides commands for managing WordPress installations, plugins, themes, users, content, and more without using a web browser. WP-CLI is widely used for automation, deployment, and development workflows.
    humanURL: https://wp-cli.org/
    tags:
      - CLI
      - Command Line
      - DevOps
      - WordPress
    properties:
      - type: Documentation
        url: https://wp-cli.org/
      - type: APIReference
        url: https://developer.wordpress.org/cli/commands/
      - type: GitHubRepository
        url: https://github.com/wp-cli/wp-cli
      - type: CLI
        url: https://wp-cli.org/
  - aid: wordpress:block-editor-api
    name: WordPress Block Editor API
    description: The Block Editor API (Gutenberg) enables developers to create custom blocks, block patterns, block templates, and editor plugins for the WordPress Block Editor. It includes JavaScript and PHP APIs for registering block types, modifying editor behavior, and extending the editing experience.
    humanURL: https://developer.wordpress.org/block-editor/
    tags:
      - Block Editor
      - Gutenberg
      - JavaScript
      - WordPress
    properties:
      - type: Documentation
        url: https://developer.wordpress.org/block-editor/
      - type: APIReference
        url: https://developer.wordpress.org/block-editor/reference-guides/
      - type: GitHubRepository
        url: https://github.com/WordPress/gutenberg
      - type: GettingStarted
        url: https://developer.wordpress.org/block-editor/getting-started/
  - aid: wordpress:ai-api
    name: WordPress AI API
    description: WordPress AI API provides a provider-agnostic interface for integrating generative AI capabilities into WordPress plugins and themes. It supports multiple AI providers (OpenAI, Google, Anthropic) through a unified PHP client interface and includes an MCP adapter for bridging to the Model Context Protocol.
    humanURL: https://github.com/WordPress/wp-ai-client
    tags:
      - AI
      - Generative AI
      - MCP
      - WordPress
    properties:
      - type: Documentation
        url: https://github.com/WordPress/wp-ai-client
      - type: GitHubRepository
        url: https://github.com/WordPress/wp-ai-client
      - type: Tools
        url: https://github.com/WordPress/mcp-adapter
        title: MCP Adapter
common:
  - type: Portal
    url: https://developer.wordpress.org/
  - type: GitHubOrganization
    url: https://github.com/WordPress
  - type: GitHubRepository
    url: https://github.com/WordPress/wordpress-develop
  - type: Documentation
    url: https://developer.wordpress.org/
  - type: GettingStarted
    url: https://developer.wordpress.org/rest-api/using-the-rest-api/
  - type: Blog
    url: https://developer.wordpress.org/news/
  - type: ChangeLog
    url: https://wordpress.org/documentation/article/wordpress-versions/
  - type: Support
    url: https://wordpress.org/support/
  - type: StatusPage
    url: https://www.incsub.com/status/
  - type: TermsOfService
    url: https://wordpress.org/about/license/
  - type: PrivacyPolicy
    url: https://automattic.com/privacy/
  - type: Security
    url: https://wordpress.org/about/security/
  - type: Training
    url: https://learn.wordpress.org/
  - type: Support
    url: https://wordpress.org/support/forums/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/wordpress
  - type: SDK
    url: https://github.com/WordPress/php-toolkit
    title: PHP Toolkit
  - type: NaftikoCapability
    url: capabilities/content-management.yaml
    title: Content Management
  - type: NaftikoCapability
    url: capabilities/shared/rest-api.yaml
    title: REST API (Shared)
  - type: SpectralRules
    url: rules/wordpress-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/wordpress-vocabulary.yml
  - type: JSONLD
    url: json-ld/wordpress-context.jsonld
  - type: Features
    data:
      - name: REST API
        description: JSON-based REST API for interacting with WordPress content including posts, pages, media, users, and custom post types
      - name: Block Editor
        description: Gutenberg block editor with JavaScript and PHP APIs for creating custom blocks and extending the editing experience
      - name: Application Passwords
        description: Built-in authentication mechanism for third-party applications using per-application passwords with granular scoping
      - name: WP-CLI
        description: Command-line interface for managing WordPress installations, automating tasks, and running deployments
      - name: Plugin API
        description: Hooks and filters system for extending WordPress functionality through plugins without modifying core code
      - name: Multisite
        description: WordPress Multisite enables running a network of sites from a single WordPress installation with shared users and plugins
      - name: WordPress Playground
        description: Run WordPress in the browser via WebAssembly PHP for development, testing, and demonstrations
      - name: AI Integration
        description: Provider-agnostic PHP AI client SDK and MCP adapter for integrating generative AI capabilities into WordPress
  - type: UseCases
    data:
      - name: Headless CMS
        description: Use WordPress as a headless CMS with the REST API to deliver content to any frontend framework like Next.js, Nuxt, or React
      - name: Mobile Applications
        description: Build iOS and Android apps that read and write WordPress content using the REST API
      - name: Content Automation
        description: Automate content creation, publishing, and management using WP-CLI in CI/CD pipelines
      - name: Custom Block Development
        description: Create custom Gutenberg blocks for unique editorial experiences and complex page layouts
      - name: Third-Party Integrations
        description: Connect WordPress to external services like CRMs, analytics platforms, and e-commerce systems via the REST API
      - name: AI-Powered Content
        description: Enhance WordPress with AI content generation, writing assistance, and intelligent recommendations
  - type: Integrations
    data:
      - name: WooCommerce
        description: E-commerce plugin with its own REST API that extends WordPress for online stores
      - name: Jetpack
        description: WordPress.com connectivity plugin providing security, performance, and marketing tools
      - name: Advanced Custom Fields
        description: Custom field framework for extending WordPress content models with structured data
      - name: Elementor
        description: Visual page builder with REST API extensions for custom integrations
      - name: OpenAI
        description: AI provider integration via WordPress AI API for content generation and assistance
      - name: Anthropic
        description: AI provider integration via WordPress AI API using Claude models
      - name: Google AI
        description: AI provider integration via WordPress AI API for Gemini models
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
