---
aid: wix
name: Wix
description: Wix is a cloud-based web development platform that allows users to create professional websites and online businesses. The Wix developer platform provides a comprehensive REST API, JavaScript SDK, and CLI for building custom apps, headless storefronts, and site extensions across eCommerce, CRM, bookings, blog, events, and more. Developers can customize Wix sites, build marketplace apps, and integrate Wix capabilities into any frontend.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS
  - eCommerce
  - Headless
  - Website Builder
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wix/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wix:rest-api
    name: Wix REST API
    description: The Wix REST API provides full programmatic access to all Wix platform capabilities via standard HTTP REST endpoints. The API covers eCommerce (stores, orders, catalog, payments, gift cards), bookings, CRM (contacts, members, forms), content (blog, events, restaurants, portfolio), business management (analytics, automations, calendar, notifications, payments), and account-level management (sites, domains, resellers). Authentication uses OAuth 2.0.
    humanURL: https://dev.wix.com/docs/rest
    tags:
      - CMS
      - CRM
      - eCommerce
      - REST
    properties:
      - type: Documentation
        url: https://dev.wix.com/docs/rest
      - type: Authentication
        url: https://dev.wix.com/docs/rest/articles/getting-started/api-authentication
  - aid: wix:javascript-sdk
    name: Wix JavaScript SDK
    description: The Wix JavaScript SDK provides modular npm packages for accessing Wix business solutions and site data from JavaScript code. It supports Wix Sites, Wix Apps, and Wix Headless projects. Modules cover eCommerce, bookings, CRM, blog, events, stores, payments, and more.
    humanURL: https://dev.wix.com/docs/sdk
    tags:
      - JavaScript
      - Node.js
      - SDK
    properties:
      - type: Documentation
        url: https://dev.wix.com/docs/sdk
      - type: SDK
        url: https://www.npmjs.com/org/wix
        title: Wix JavaScript SDK (npm)
  - aid: wix:headless
    name: Wix Headless
    description: Wix Headless enables developers to use Wix business solutions as a backend while building custom frontends with any framework. It provides managed commerce, CRM, and content APIs accessible from any tech stack.
    humanURL: https://dev.wix.com/docs/go-headless
    tags:
      - Headless
      - Commerce
      - Frontend
    properties:
      - type: Documentation
        url: https://dev.wix.com/docs/go-headless
common:
  - type: Website
    url: https://www.wix.com
  - type: DeveloperPortal
    url: https://dev.wix.com
  - type: Documentation
    url: https://dev.wix.com/docs
  - type: GettingStarted
    url: https://dev.wix.com/docs/rest/articles/getting-started/introduction
  - type: SignUp
    url: https://users.wix.com/signin
  - type: GitHub
    url: https://github.com/wix
  - type: Tools
    url: https://github.com/wix/wix-mcp
    title: Wix MCP Server
  - type: Blog
    url: https://dev.wix.com/blog
  - type: Support
    url: https://support.wix.com
  - type: Forum
    url: https://www.wix.com/forum/corvid-tips-questions-and-answers
  - type: GitHubOrganization
    url: https://github.com/wix
  - type: Features
    data:
      - name: eCommerce APIs
        description: Full store management including products, orders, payments, gift cards, and shipping via REST and SDK.
      - name: CRM APIs
        description: Manage site contacts, members, forms, automations, and loyalty programs.
      - name: Bookings APIs
        description: Service booking, staff scheduling, resources, and pricing plan management.
      - name: Headless Commerce
        description: Use Wix as a backend commerce engine with a custom frontend on any framework.
      - name: App Marketplace
        description: Build and publish apps to the Wix App Market using OAuth 2.0 and webhooks.
      - name: Wix MCP Server
        description: Model Context Protocol server that bridges AI clients to Wix APIs and documentation.
      - name: JavaScript SDK
        description: Modular npm packages for accessing Wix capabilities from JavaScript applications.
      - name: Velo by Wix
        description: Full-stack JavaScript development platform for adding custom functionality to Wix sites.
  - type: UseCases
    data:
      - name: Custom eCommerce Storefront
        description: Build a headless storefront with custom UI while using Wix for catalog, orders, and payments.
      - name: App Development
        description: Develop and publish apps to the Wix App Market that install on Wix sites.
      - name: CRM Integration
        description: Sync contacts, members, and orders with external CRM systems via REST API.
      - name: Booking System
        description: Build custom booking experiences for service businesses using Wix Bookings API.
      - name: AI-Powered Site Management
        description: Use the Wix MCP Server to manage Wix sites through AI assistants and agents.
  - type: Integrations
    data:
      - name: OAuth 2.0
        description: Authorization framework for Wix App authentication and user consent.
      - name: React
        description: Official SDK support for React-based headless applications.
      - name: Next.js
        description: Starter templates for headless Wix commerce with Next.js.
      - name: Webhooks
        description: Event-driven notifications for order, contact, and site events.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
