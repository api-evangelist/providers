---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Wordpress Agentic Access
  operation_count: 24
  slug: wordpress-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 17
apis:
- description: WP-CLI is the command-line interface for WordPress. It provides commands for managing WordPress installations, plugins, themes, users, content, and more without using a web browser. WP-CLI is widely u
  name: WP-CLI
  slug: wp-cli
- description: The Block Editor API (Gutenberg) enables developers to create custom blocks, block patterns, block templates, and editor plugins for the WordPress Block Editor. It includes JavaScript and PHP APIs for
  name: WordPress Block Editor API
  slug: block-editor-api
- description: WordPress AI API provides a provider-agnostic interface for integrating generative AI capabilities into WordPress plugins and themes. It supports multiple AI providers (OpenAI, Google, Anthropic) thro
  name: WordPress AI API
  slug: ai-api
- description: Query registered block types
  name: WordPress Block Types API
  slug: wordpress-block-types-api
- description: Manage reusable blocks
  name: WordPress Blocks API
  slug: wordpress-blocks-api
- description: Manage post categories
  name: WordPress Categories API
  slug: wordpress-categories-api
- description: Manage WordPress comments
  name: WordPress Comments API
  slug: wordpress-comments-api
- description: Manage WordPress media library
  name: WordPress Media API
  slug: wordpress-media-api
- description: Manage WordPress pages
  name: WordPress Pages API
  slug: wordpress-pages-api
- description: Manage WordPress plugins
  name: WordPress Plugins API
  slug: wordpress-plugins-api
- description: Query registered post types
  name: WordPress Post Types API
  slug: wordpress-post-types-api
- description: Manage WordPress posts
  name: WordPress Posts API
  slug: wordpress-posts-api
- description: Search across WordPress content
  name: WordPress Search API
  slug: wordpress-search-api
- description: Manage site settings
  name: WordPress Settings API
  slug: wordpress-settings-api
- description: Manage post tags
  name: WordPress Tags API
  slug: wordpress-tags-api
- description: Manage WordPress themes
  name: WordPress Themes API
  slug: wordpress-themes-api
- description: Manage WordPress users
  name: WordPress Users API
  slug: wordpress-users-api
arazzos:
- description: Resolve a user by role, confirm them, and publish a post under their byline.
  name: WordPress Assign Post to Author
  slug: wordpress-assign-post-to-author-workflow
- description: Find an image in the media library and publish a post that features it.
  name: WordPress Attach Featured Media to Post
  slug: wordpress-attach-featured-media-to-post-workflow
- description: Create a category, publish a post into it, then read the post back.
  name: WordPress Categorize and Publish Post
  slug: wordpress-categorize-and-publish-post-workflow
- description: Search for a post, post a comment on it, then list comments to confirm.
  name: WordPress Comment on Found Post
  slug: wordpress-comment-on-found-post-workflow
- description: Find a parent page by title and create a child page nested beneath it.
  name: WordPress Create Subpage Under Parent
  slug: wordpress-create-subpage-under-parent-workflow
- description: Create a draft post, revise it, then flip it to published.
  name: WordPress Draft Then Publish Post
  slug: wordpress-draft-then-publish-post-workflow
- description: Find a tag by name and apply it to an existing post.
  name: WordPress Tag an Existing Post
  slug: wordpress-tag-an-existing-post-workflow
- description: Find a published post by search and revert it to draft.
  name: WordPress Unpublish Post to Draft
  slug: wordpress-unpublish-post-to-draft-workflow
artifact_total: 146
collections:
- collection_type: postman
  name: WordPress REST API
  slug: postman-wordpress-rest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WordPress REST Block Types API
  slug: open-wordpress-block-types-api
- collection_type: open
  name: WordPress REST Block Types Blocks API
  slug: open-wordpress-blocks-api
- collection_type: open
  name: WordPress REST Block Types Categories API
  slug: open-wordpress-categories-api
- collection_type: open
  name: WordPress REST Block Types Comments API
  slug: open-wordpress-comments-api
- collection_type: open
  name: WordPress REST Block Types Media API
  slug: open-wordpress-media-api
- collection_type: open
  name: WordPress REST Block Types Pages API
  slug: open-wordpress-pages-api
- collection_type: open
  name: WordPress REST Block Types Plugins API
  slug: open-wordpress-plugins-api
- collection_type: open
  name: WordPress REST Block Types Post Types API
  slug: open-wordpress-post-types-api
- collection_type: open
  name: WordPress REST Block Types Posts API
  slug: open-wordpress-posts-api
- collection_type: open
  name: WordPress REST API
  slug: open-wordpress-rest-api
- collection_type: open
  name: WordPress REST Block Types Search API
  slug: open-wordpress-search-api
- collection_type: open
  name: WordPress REST Block Types Settings API
  slug: open-wordpress-settings-api
- collection_type: open
  name: WordPress REST Block Types Tags API
  slug: open-wordpress-tags-api
- collection_type: open
  name: WordPress REST Block Types Themes API
  slug: open-wordpress-themes-api
- collection_type: open
  name: WordPress REST Block Types Users API
  slug: open-wordpress-users-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/wp-cli/wp-cli/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wordpress-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wordpress-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wordpress-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wordpress-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wordpress/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-assign-post-to-author-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-attach-featured-media-to-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-categorize-and-publish-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-comment-on-found-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-create-subpage-under-parent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-draft-then-publish-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-tag-an-existing-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wordpress-unpublish-post-to-draft-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.wordpress.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WordPress
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/WordPress/wordpress-develop
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wordpress.org/rest-api/using-the-rest-api/
- group: company
  title: ''
  type: Blog
  url: https://developer.wordpress.org/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://wordpress.org/documentation/article/wordpress-versions/
- group: operate
  title: ''
  type: Support
  url: https://wordpress.org/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.incsub.com/status/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wordpress.org/about/license/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://automattic.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://wordpress.org/about/security/
- group: learn
  title: ''
  type: Training
  url: https://learn.wordpress.org/
- group: operate
  title: ''
  type: Support
  url: https://wordpress.org/support/forums/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/wordpress
- group: build
  title: PHP Toolkit
  type: SDKs
  url: https://github.com/WordPress/php-toolkit
- group: design
  title: ''
  type: SpectralRules
  url: rules/wordpress-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wordpress-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wordpress-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/WordPress/mcp-adapter
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/WordPress/agent-skills
created: '2025'
description: WordPress is an open-source content management system (CMS) that powers a significant portion of websites on the internet. Its REST API enables applications to interact with WordPress sites by sending and receiving data as JSON, allowing developers to build decoupled frontends, mobile apps, and integrations in any language. The extensive plugin and theme ecosystem, block editor, and AI capabilities make it accessible for building everything from personal blogs to complex enterprise websites.
examples:
- key_count: 5
  name: Wordpress Block Example
  slug: wordpress-block-example
- key_count: 6
  name: Wordpress Block Type Example
  slug: wordpress-block-type-example
- key_count: 10
  name: Wordpress Comment Example
  slug: wordpress-comment-example
- key_count: 5
  name: Wordpress Comment Input Example
  slug: wordpress-comment-input-example
- key_count: 10
  name: Wordpress Media Item Example
  slug: wordpress-media-item-example
- key_count: 12
  name: Wordpress Page Example
  slug: wordpress-page-example
- key_count: 5
  name: Wordpress Page Input Example
  slug: wordpress-page-input-example
- key_count: 8
  name: Wordpress Plugin Example
  slug: wordpress-plugin-example
- key_count: 20
  name: Wordpress Post Example
  slug: wordpress-post-example
- key_count: 8
  name: Wordpress Post Input Example
  slug: wordpress-post-input-example
- key_count: 7
  name: Wordpress Post Type Example
  slug: wordpress-post-type-example
- key_count: 2
  name: Wordpress Rendered Content Example
  slug: wordpress-rendered-content-example
- key_count: 5
  name: Wordpress Search Result Example
  slug: wordpress-search-result-example
- key_count: 12
  name: Wordpress Settings Example
  slug: wordpress-settings-example
- key_count: 8
  name: Wordpress Term Example
  slug: wordpress-term-example
- key_count: 4
  name: Wordpress Term Input Example
  slug: wordpress-term-input-example
- key_count: 9
  name: Wordpress Theme Example
  slug: wordpress-theme-example
- key_count: 7
  name: Wordpress User Example
  slug: wordpress-user-example
features:
- description: JSON-based REST API for interacting with WordPress content including posts, pages, media, users, and custom post types
  name: REST API
- description: Gutenberg block editor with JavaScript and PHP APIs for creating custom blocks and extending the editing experience
  name: Block Editor
- description: Built-in authentication mechanism for third-party applications using per-application passwords with granular scoping
  name: Application Passwords
- description: Command-line interface for managing WordPress installations, automating tasks, and running deployments
  name: WP-CLI
- description: Hooks and filters system for extending WordPress functionality through plugins without modifying core code
  name: Plugin API
- description: WordPress Multisite enables running a network of sites from a single WordPress installation with shared users and plugins
  name: Multisite
- description: Run WordPress in the browser via WebAssembly PHP for development, testing, and demonstrations
  name: WordPress Playground
- description: Provider-agnostic PHP AI client SDK and MCP adapter for integrating generative AI capabilities into WordPress
  name: AI Integration
finops:
- name: Wordpress Finops
  service_category: API
  slug: wordpress-finops
graphqls:
- description: WordPress supports a full-featured GraphQL API through the [WPGraphQL plugin](https://www.wpgraphql.com/), an open-source WordPress plugin that provides an extendable GraphQL schema and API for any Wo
  name: WordPress GraphQL API
  slug: wordpress-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wordpress.png
integrations:
- description: E-commerce plugin with its own REST API that extends WordPress for online stores
  name: WooCommerce
- description: WordPress.com connectivity plugin providing security, performance, and marketing tools
  name: Jetpack
- description: Custom field framework for extending WordPress content models with structured data
  name: Advanced Custom Fields
- description: Visual page builder with REST API extensions for custom integrations
  name: Elementor
- description: AI provider integration via WordPress AI API for content generation and assistance
  name: OpenAI
- description: AI provider integration via WordPress AI API using Claude models
  name: Anthropic
- description: AI provider integration via WordPress AI API for Gemini models
  name: Google AI
json_schemas:
- name: Block
  property_count: 5
  slug: wordpress-block
- name: BlockType
  property_count: 6
  slug: wordpress-block-type
- name: CommentInput
  property_count: 5
  slug: wordpress-comment-input
- name: Comment
  property_count: 10
  slug: wordpress-comment
- name: MediaItem
  property_count: 10
  slug: wordpress-media-item
- name: PageInput
  property_count: 5
  slug: wordpress-page-input
- name: Page
  property_count: 12
  slug: wordpress-page
- name: Plugin
  property_count: 8
  slug: wordpress-plugin
- name: PostInput
  property_count: 8
  slug: wordpress-post-input
- name: Post
  property_count: 20
  slug: wordpress-post
- name: PostType
  property_count: 7
  slug: wordpress-post-type
- name: RenderedContent
  property_count: 2
  slug: wordpress-rendered-content
- name: SearchResult
  property_count: 5
  slug: wordpress-search-result
- name: Settings
  property_count: 12
  slug: wordpress-settings
- name: TermInput
  property_count: 4
  slug: wordpress-term-input
- name: Term
  property_count: 8
  slug: wordpress-term
- name: Theme
  property_count: 9
  slug: wordpress-theme
- name: User
  property_count: 7
  slug: wordpress-user
json_structures:
- name: Wordpress Block Structure
  property_count: 5
  slug: wordpress-block-structure
- name: Wordpress Block Type Structure
  property_count: 6
  slug: wordpress-block-type-structure
- name: Wordpress Comment Input Structure
  property_count: 5
  slug: wordpress-comment-input-structure
- name: Wordpress Comment Structure
  property_count: 10
  slug: wordpress-comment-structure
- name: Wordpress Media Item Structure
  property_count: 10
  slug: wordpress-media-item-structure
- name: Wordpress Page Input Structure
  property_count: 5
  slug: wordpress-page-input-structure
- name: Wordpress Page Structure
  property_count: 12
  slug: wordpress-page-structure
- name: Wordpress Plugin Structure
  property_count: 8
  slug: wordpress-plugin-structure
- name: Wordpress Post Input Structure
  property_count: 8
  slug: wordpress-post-input-structure
- name: Wordpress Post Structure
  property_count: 20
  slug: wordpress-post-structure
- name: Wordpress Post Type Structure
  property_count: 7
  slug: wordpress-post-type-structure
- name: Wordpress Rendered Content Structure
  property_count: 2
  slug: wordpress-rendered-content-structure
- name: Wordpress Search Result Structure
  property_count: 5
  slug: wordpress-search-result-structure
- name: Wordpress Settings Structure
  property_count: 12
  slug: wordpress-settings-structure
- name: Wordpress Term Input Structure
  property_count: 4
  slug: wordpress-term-input-structure
- name: Wordpress Term Structure
  property_count: 8
  slug: wordpress-term-structure
- name: Wordpress Theme Structure
  property_count: 9
  slug: wordpress-theme-structure
- name: Wordpress User Structure
  property_count: 7
  slug: wordpress-user-structure
jsonld:
- class_count: 18
  name: Wordpress Context
  property_count: 62
  slug: wordpress-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: WordPress
nav: Providers
network: true
overview: 'WordPress publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Block Types API, Blocks API, Categories API, and 11 more. Tagged areas include CMS, Content Management, Open Source, and WordPress.


  The WordPress catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WordPress'' developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 28 more developer resources.'
plans:
- name: Wordpress Plans Pricing
  plan_count: 3
  slug: wordpress-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 5
  name: Wordpress Rate Limits
  slug: wordpress-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WordPress API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wordpress-jsonschema-spectral-rules
- effective_rule_count: 87
  extends:
  - spectral:oas
  name: WordPress API Rules
  rule_count: 46
  severity_counts:
    error: 10
    hint: 0
    info: 13
    warn: 23
  slug: wordpress-spectral-rules
score:
  band: developing
  composite: 44.5
  delta: -8.2
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 25.0
    contract_quality: 39.4
    developer_ergonomics: 69.0
    discoverability: 57.4
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wordpress/refs/heads/main/screenshots/wordpress-2026-06-20T201546.png
security:
- kind: authentication
  name: Wordpress Authentication
  slug: wordpress-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wordpress Domain Security
  slug: wordpress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wordpress Vulnerability Disclosure
  slug: wordpress-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 17
skills:
- name: blueprint
  slug: blueprint
- name: wordpress-router
  slug: wordpress-router
- name: wp-abilities-api
  slug: wp-abilities-api
- name: wp-abilities-audit
  slug: wp-abilities-audit
- name: wp-abilities-verify
  slug: wp-abilities-verify
- name: wp-block-development
  slug: wp-block-development
- name: wp-block-themes
  slug: wp-block-themes
- name: wp-interactivity-api
  slug: wp-interactivity-api
- name: wp-performance
  slug: wp-performance
- name: wp-phpstan
  slug: wp-phpstan
- name: wp-playground
  slug: wp-playground
- name: wp-plugin-development
  slug: wp-plugin-development
- name: wp-plugin-directory-guidelines
  slug: wp-plugin-directory-guidelines
- name: wp-project-triage
  slug: wp-project-triage
- name: wp-rest-api
  slug: wp-rest-api
- name: wp-wpcli-and-ops
  slug: wp-wpcli-and-ops
- name: wpds
  slug: wpds
slug: wordpress
tags:
- CMS
- Content Management
- Open Source
- WordPress
use_cases:
- description: Use WordPress as a headless CMS with the REST API to deliver content to any frontend framework like Next.js, Nuxt, or React
  name: Headless CMS
- description: Build iOS and Android apps that read and write WordPress content using the REST API
  name: Mobile Applications
- description: Automate content creation, publishing, and management using WP-CLI in CI/CD pipelines
  name: Content Automation
- description: Create custom Gutenberg blocks for unique editorial experiences and complex page layouts
  name: Custom Block Development
- description: Connect WordPress to external services like CRMs, analytics platforms, and e-commerce systems via the REST API
  name: Third-Party Integrations
- description: Enhance WordPress with AI content generation, writing assistance, and intelligent recommendations
  name: AI-Powered Content
website: https://developer.wordpress.org/
---
