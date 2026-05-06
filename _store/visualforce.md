---
aid: visualforce
name: Visualforce
description: Visualforce is a framework that enables developers to build sophisticated, custom user interfaces that can be hosted natively on the Salesforce platform. It uses a tag-based markup language similar to HTML and provides a component-based development model for building pages, email templates, and PDF documents within Salesforce.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/visualforce/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Salesforce
  - UI Framework
  - Web Development
apis:
  - aid: visualforce:visualforce-api
    name: Visualforce
    description: Visualforce is the Salesforce framework for building custom user interfaces using tag-based markup and Apex server-side controllers. Developers use it to create pages, email templates, and PDF documents within the Salesforce platform.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/
    tags:
      - MVC
      - Salesforce
      - UI Framework
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/
      - type: APIReference
        url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_compref.htm
      - type: GettingStarted
        url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_quick_start.htm
common:
  - type: Portal
    url: https://developer.salesforce.com
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/
  - type: GettingStarted
    url: https://trailhead.salesforce.com/en/content/learn/modules/visualforce_fundamentals
  - type: Blog
    url: https://developer.salesforce.com/blogs
  - type: Support
    url: https://developer.salesforce.com/support
  - type: TermsOfService
    url: https://www.salesforce.com/company/legal/agreements/
  - type: PrivacyPolicy
    url: https://www.salesforce.com/company/privacy/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/visualforce
  - type: GitHubOrganization
    url: https://github.com/salesforce
  - type: Training
    url: https://trailhead.salesforce.com/en/content/learn/modules/visualforce_fundamentals
  - type: Features
    data:
      - name: Tag-Based Markup Language
        description: HTML-like tag-based markup for building custom Salesforce pages without JavaScript frameworks.
      - name: Component-Based Architecture
        description: Reusable Visualforce components for consistent UI patterns across Salesforce applications.
      - name: Apex Controller Integration
        description: Server-side Apex controllers for business logic, data access, and page flow control.
      - name: Standard Controllers
        description: Built-in controllers for CRUD operations on standard and custom Salesforce objects.
      - name: PDF Generation
        description: Render Visualforce pages as PDF documents for invoices, reports, and printable content.
      - name: Email Templates
        description: Build dynamic HTML email templates with merge fields and conditional content.
  - type: UseCases
    data:
      - name: Custom Salesforce Pages
        description: Build custom UI pages that extend Salesforce functionality beyond standard page layouts.
      - name: PDF Document Generation
        description: Generate branded PDFs for invoices, quotes, contracts, and reports from Salesforce data.
      - name: Custom Email Templates
        description: Create rich HTML email templates with dynamic content from Salesforce records.
      - name: Embedded Dashboards
        description: Build custom analytics dashboards and data visualization pages within Salesforce.
      - name: Wizard-Style Forms
        description: Create multi-step form workflows for complex data entry processes.
  - type: Integrations
    data:
      - name: Salesforce Lightning
        description: Visualforce pages can be embedded in Lightning Experience as components and tabs.
      - name: Apex
        description: Server-side controller integration with Apex for database access and business logic.
      - name: JavaScript Remoting
        description: Asynchronous JavaScript calls to Apex methods for dynamic page interactions.
      - name: Salesforce REST API
        description: Client-side integration with Salesforce REST APIs for CRUD operations.
      - name: Force.com Canvas
        description: Embed external applications within Visualforce pages using Canvas framework.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
