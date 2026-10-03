---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 35
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering plugin, extension, and add-on architectures with public APIs and marketplaces. This collection spans editor and IDE plugin ecosystems (VS Code Marketplace, JetBrains Marketplace, Chrome Web Store, Firefox Add-ons), SaaS platform extension marketplaces (Atlassian Marketplace and Forge, Salesforce AppExchange, Shopify App Store, WordPress Plugins, Slack Apps, Discord Apps, Microsoft AppSource, Google Workspace Marketplace, Notion, Postman, Figma, Sketch, Webflow Apps, HubSpot Marketplace, Zapier App Directory), API gateway plugin frameworks (Kong Plugin Hub, Tyk Plugins, Gravitee Plugins), identity extensibility (Auth0 Actions and Extensions), and AI plugin and tool ecosystems (Open WebUI Functions, ChatGPT Plugins and GPTs, Claude Code plugins, OpenAI tools). It tracks the manifests, listing schemas, install and entitlement flows, extension points, and review and distribution APIs that power modern plugin and extension marketplaces.
examples:
- key_count: 13
  name: Plugin Manifest Example
  slug: plugin-manifest-example
- key_count: 18
  name: Plugin Marketplace Listing Example
  slug: plugin-marketplace-listing-example
features:
- description: Marketplaces and runtimes use declarative manifests (manifest.json for Chrome and VS Code, plugin.xml for JetBrains, app manifests for Slack and Atlassian Connect) to describe identity, permissions, entry points, and capabilities of a plugin.
  name: Plugin Manifests
- description: Public APIs and search endpoints expose listings, categories, ratings, and download counts so developers and users can discover plugins across VS Code Marketplace, Chrome Web Store, JetBrains Marketplace, Shopify App Store, and Atlassian Marketplace.
  name: Marketplace Listing and Discovery APIs
- description: Host platforms expose well-defined extension points, events, and lifecycle hooks (Forge modules, Shopify Functions, Auth0 Actions, Kong plugin phases, WordPress hooks) that plugins implement to integrate with the host.
  name: Extension Points and Hooks
- description: Marketplaces standardize installation, OAuth grant, license check, and entitlement validation flows for individual users, organizations, and tenants, including paid plugin billing and trials.
  name: Install, Update, and Entitlement Flows
- description: Plugin runtimes enforce permission scopes, sandboxed execution (Atlassian Forge, Chrome MV3 service workers, Slack Bolt scopes, Salesforce managed packages) and review processes to protect host platforms and end users.
  name: Sandboxing and Permissions
- description: AI platforms expose plugin and tool surfaces (ChatGPT GPTs and plugins, Open WebUI Functions, Claude Code plugins, OpenAI tools) that let third-party developers extend LLM behavior with custom actions, retrieval, and integrations.
  name: AI Tooling and Agent Plugins
- description: API gateways such as Kong, Tyk, and Gravitee define plugin frameworks where authentication, transformation, rate limiting, and observability behavior is implemented and distributed as installable plugins.
  name: API Gateway Plugin Frameworks
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Microsoft's marketplace for Visual Studio Code and Visual Studio extensions, with a Gallery API for search, download, and metadata.
  name: VS Code Marketplace
- description: Official plugin and theme distribution platform for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with a public plugins API.
  name: JetBrains Marketplace
- description: Google's distribution channel for Chrome and Edge browser extensions and themes, governed by Manifest V3 and the Chrome Web Store API.
  name: Chrome Web Store
- description: Marketplace for apps that extend Jira, Confluence, and Bitbucket, including Atlassian Connect and Forge apps with a public Marketplace REST API.
  name: Atlassian Marketplace
- description: Enterprise marketplace for managed packages and Lightning components extending Salesforce CRM, with package install APIs and security review.
  name: Salesforce AppExchange
- description: Marketplace for apps extending Shopify Admin, Storefront, and Checkout via Shopify Apps, Functions, and Theme App Extensions.
  name: Shopify App Store
- description: Open directory of free WordPress plugins powering a large share of the web, distributed through wordpress.org with a public plugins.org API.
  name: WordPress Plugin Directory
- description: Directory of Slack apps and integrations built on the Slack platform, manifested through app config and the Apps API.
  name: Slack App Directory
- description: Microsoft's marketplace for business apps and Office 365 add-ins, Teams apps, and Power Platform connectors.
  name: Microsoft AppSource
- description: Distribution platform for Google Workspace add-ons and Apps Script-based extensions to Gmail, Drive, Docs, Sheets, and Calendar.
  name: Google Workspace Marketplace
- description: Marketplace for HubSpot apps, themes, and templates extending the HubSpot CRM and CMS via OAuth apps and serverless functions.
  name: HubSpot Marketplace
- description: Directory of integrations and triggers/actions that Zapier exposes to its automation builder via the Zapier Platform CLI and Public APIs.
  name: Zapier App Directory
- description: Catalog of first-party and community plugins for Kong Gateway and Konnect, written in Lua, Go, or JavaScript and distributed through the Plugin Hub.
  name: Kong Plugin Hub
- description: Pluggable functions, tools, and pipelines that extend the Open WebUI LLM chat interface with custom integrations and behavior.
  name: Open WebUI Functions
json_schemas:
- name: PluginManifest
  property_count: 13
  slug: plugin-manifest
- name: MarketplaceListing
  property_count: 18
  slug: plugin-marketplace-listing
json_structures:
- name: Plugin Manifest Structure
  property_count: 13
  slug: plugin-manifest-structure
- name: Plugin Marketplace Listing Structure
  property_count: 18
  slug: plugin-marketplace-listing-structure
jsonld:
- class_count: 9
  name: Plugin Context
  property_count: 21
  slug: plugin-context
layout: provider
modified: '2026-05-19'
name: Plugin
nav: Providers
network: true
overview: 'Plugin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Plugins, Extension, Marketplace, App Directory, and Addon.


  The Plugin catalog on APIs.io includes 1 JSON-LD context.


  Plugin''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: plugin
tags:
- Plugins
- Extension
- Marketplace
- App Directory
- Addon
use_cases:
- description: Developers ship language support, linters, debuggers, and AI assistants as plugins through VS Code Marketplace and JetBrains Marketplace, reaching millions of editor installations through manifest-driven distribution.
  name: Editor and IDE Extensibility
- description: ISVs build and list apps on Salesforce AppExchange, Shopify App Store, Atlassian Marketplace, HubSpot Marketplace, and Slack App Directory to extend SaaS platforms and reach enterprise customers.
  name: SaaS Platform App Marketplaces
- description: Developers package and distribute browser extensions for content blocking, productivity, password management, and accessibility through Chrome Web Store, Firefox Add-ons, and Microsoft Edge Add-ons.
  name: Browser Extension Distribution
- description: Platform teams extend Kong, Tyk, and Gravitee with custom plugins for authentication, request transformation, AI prompt firewalls, and policy enforcement, often shared through plugin hubs.
  name: API Gateway Customization
- description: WordPress plugin directory and Shopify App Store let merchants and publishers extend CMS and commerce platforms with payment processors, shipping integrations, page builders, and analytics.
  name: CMS and Commerce Extensibility
- description: Builders publish ChatGPT GPTs and plugins, Open WebUI Functions, and Claude Code plugins to give AI agents domain-specific tools, retrieval sources, and connectors to external systems.
  name: AI Agent Tooling
- description: Auth0 Actions, Extensions, and the Auth0 Marketplace let teams add custom rules, MFA providers, and SSO integrations to identity flows without forking the platform.
  name: Identity and Access Extensions
website: https://apievangelist.com
---
